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
Unit tests for Kylin.
"""

import unittest
# from unittest import mock

import kylin
from kylin import exceptions


VALID_FRAME = """ADCO 524563565245 /
OPTARIF HC.. <
ISOUSC 20 8
HCHC 001065963 _
HCHP 001521211 '
PTEC HC.. S
IINST 001 I
IMAX 008 2
PMAX 06030 3
PAPP 01250 +
HHPHC E 0
MOTDETAT 000000 B
PPOT 00 #
ADCO 524563565245 /
OPTARIF HC.. <
ISOUSC 20 8
"""


class KylinTestCase(unittest.TestCase):
    """Main object for unit tests."""

    def test_invalid_serial_port(self):
        with self.assertRaises(exceptions.KylinNotFoundError):
            kylin.Kylin("/dev/ttyFoo00")

    # def test_valid_usb_port(self):
    #     self.assertTrue(kylin.Kylin("/dev/ttyS0"))

    def test_extract_teleinfo(self):
        pass  # Try to mock serial here
