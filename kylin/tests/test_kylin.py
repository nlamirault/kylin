# Copyright (C) 2017 Nicolas Lamirault <nicolas.lamirault@gmail.com>

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

import unittest

import kylin
from kylin import exceptions


class KylinTestCase(unittest.TestCase):

    def test_invalid_serial_port(self):
        with self.assertRaises(exceptions.KylinNotFoundError):
            kylin.Kylin("/dev/ttyFoo00")

    def test_valid_usb_port(self):
        self.assertTrue(kylin.Kylin("/dev/ttyACM0"))