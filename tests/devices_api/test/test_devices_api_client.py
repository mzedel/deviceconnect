# Copyright 2021 Northern.tech AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# coding: utf-8

"""
    Device Connect

    Device facing API for managing persistent device connections.   # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@mender.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import devices_api
from devices_api.api.devices_api_client import DevicesAPIClient  # noqa: E501
from devices_api.rest import ApiException


class TestDevicesAPIClient(unittest.TestCase):
    """DevicesAPIClient unit test stubs"""

    def setUp(self):
        self.api = devices_api.api.devices_api_client.DevicesAPIClient()  # noqa: E501

    def tearDown(self):
        pass

    def test_connect(self):
        """Test case for connect

        Connect the device and make it available to the server.   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
