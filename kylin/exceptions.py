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
Exceptions raised by Kylin.

"""


class KylinError(Exception):
    """Base exception for errors raised by Kylin"""
    pass


class KylinSerialError(KylinError):
    """Base class for serial port exceptions. """

    def __init__(self, msg, error):
        super(KylinSerialError, self).__init__(msg + (": %s" % error))
        self.error = error


class KylinNotFoundError(KylinError):
    """Base class when no serial port exists. """

    def __init__(self, name):
        super(KylinNotFoundError, self).__init__(
            "Serial port not available: %s", name)
