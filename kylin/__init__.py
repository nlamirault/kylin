# Copyright (C) 2017-2018 Nicolas Lamirault <nicolas.lamirault@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Kylin library.

Read Teleinfo data.


For more information read Enedis document "Enedis-NOI-CPT_54E"
"""

import logging
import os
import serial  # pylint: disable=import-error
from serial.tools import list_ports  # pylint: disable=import-error
import datetime

from kylin import exceptions
DEFAULT_SERIAL_PORT = '/dev/ttyS0'

DEFAULT_TIMEOUT = 1

LOGGER = logging.getLogger(__name__)


class Kylin():
    FRAME_START = '\x02'
    FRAME_END = '\x03'
    """Represents a Teleinfo board. """

    def __init__(self, port=DEFAULT_SERIAL_PORT, timeout=DEFAULT_TIMEOUT,
                 verbose=False):
        if not serial_is_available(port):
            raise exceptions.KylinNotFoundError(port)
        self._port = port
        self._timeout = timeout
        self._teleinfo = None
        self._verbose = verbose
        level = logging.INFO
        if verbose:
            level = logging.DEBUG
        LOGGER.setLevel(level)

    def open(self):
        """Open the serial port."""
        try:
            LOGGER.info("Open serial port: %s with timeout %d",
                        self._port, self._timeout)
            self._teleinfo = serial.Serial(
                port=self._port,
                baudrate=self.BAUDRATE,
                bytesize=serial.SEVENBITS,
                parity=serial.PARITY_EVEN,
                stopbits=serial.STOPBITS_ONE,
                rtscts=1,
                timeout=self._timeout)

        except serial.SerialException as err:
            raise exceptions.KylinSerialError(
                "Unable to open or read serial connection", err)

    def close(self):
        """Close the serial connection. """
        if self._teleinfo is None:
            return
        try:
            if self._teleinfo.isOpen():
                self._teleinfo.close()
        except serial.SerialException as err:
            raise exceptions.KylinSerialError(
                "Unable to close serial connection", err)

    def _readline(self):
        data = self._teleinfo.readline()
        line = data.decode('ascii')
        return line.replace('\r', '').replace('\n', '')


    def readframe(self):
        """Read a frame from serial port. """
        is_over = False
        line = self._readline()
        LOGGER.info("Line: %s", line)
        frame = []
        while not is_over:
            # We're waiting for a new frame
            while self.FRAME_START not in line:
                line = self._readline()
                LOGGER.debug("Waiting ....")

            line = ''
            while self.FRAME_START not in line:
                LOGGER.info(u"New frame")
                line = self._readline()
                LOGGER.info("Line: %s", line)
                name, ts, value, checksum = self.split_line(line)

                if self.frame_is_valid(line, checksum):
                    frame.append({
                        "name": name,
                        "value": value,
                        "checksum": checksum,
                        "timestamp": ts,
                    })
                    is_over = True
                else:
                    LOGGER.warning("Frame corrupted. Waiting for a new one.")
                    break

                line = self._readline()
                LOGGER.info("Line: %s", line)

        LOGGER.info("Frame: %s", frame)
        return frame


class TICStandard(Kylin):
    BAUDRATE = 9600

    @staticmethod
    def split_line(line):
        ''' Splits a standard line. Can either be N\tV\tC or
        N\tV\tV..\tV\tC'''
        s = line.split('\t')
        if len(s) == 3:
            name = s[0]
            values = s[1]
            checksum = s[2]
            ts = None
        elif len(s) == 4:
            name = s[0]
            values = s[2]
            checksum = s[3]

            raw_ts = s[1][1:1+2*5]
            ts = datetime.datetime.strptime(raw_ts, "%y%m%d%H%S")
        else:
            raise Exception(f'Unknown format for {line}')

        return (name, ts, values, checksum)

    @staticmethod
    def frame_is_valid(frame, checksum):
        """ Check if a frame is valid

            @param frame : the full frame
            @param checksum : the frame checksum
        """
        LOGGER.debug("Check checksum : f = %s, chk = %s", frame, checksum)
        datas = '\t'.join(frame.split('\t')[0:-1]) + '\t' #  All except CRC

        my_sum = 0
        for cks in datas:
            my_sum = my_sum + ord(cks)

        computed_checksum = (my_sum & 0x3F) + 0x20
        if chr(computed_checksum) == checksum:
            return True

        LOGGER.warning(u"Invalid checksum for %s : %s. Waiting %s",
                    frame, computed_checksum, checksum)
        return False


class TICHistorique(Kylin):
    BAUDRATE = 1200

    @staticmethod
    def split_line(line):
        ''' Splits a "historique" line '''

        # Don't use strip() here because the checksum can be ' '
        splitted_line = line.split()
        if len(splitted_line) == 2:
            # The checksum char is ' '
            name, value = line.replace('\r', '').replace(
                '\n', '').split()
            checksum = ' '
        elif len(splitted_line) == 3:
            name, value, checksum = line.split()
        else:
            raise Exception('Wrong line')

        # There is no timestamp in historique frames
        ts = None
        return name, ts, value, checksum


    @staticmethod
    def frame_is_valid(frame, checksum):
        """ Check if a frame is valid

            @param frame : the full frame
            @param checksum : the frame checksum
        """
        LOGGER.debug("Check checksum : f = %s, chk = %s", frame, checksum)
        datas = ' '.join(frame.split()[0:2])
        my_sum = 0
        for cks in datas:
            my_sum = my_sum + ord(cks)
        computed_checksum = (my_sum & int("111111", 2)) + 0x20
        if chr(computed_checksum) == checksum:
            return True

        LOGGER.warning(u"Invalid checksum for %s : %s. Waiting %s",
                    frame, computed_checksum, checksum)
        return False


def serial_is_available(name):
    """ Check if a serial port is available. """

    if os.path.islink(name):
        # Follow the symlink
        name = os.path.realpath(name)

    ports = list_ports.comports()
    for port in ports:
        LOGGER.info("Port: %s", port)
        if port.device == name:
            return True
    return False

