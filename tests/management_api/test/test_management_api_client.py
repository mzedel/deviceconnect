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

    API for managing persistent device connections. Intended for use by the web GUI   # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@mender.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import management_api
from management_api.api.management_api_client import ManagementAPIClient  # noqa: E501
from management_api.rest import ApiException


class TestManagementAPIClient(unittest.TestCase):
    """ManagementAPIClient unit test stubs"""

    def setUp(self):
        self.api = management_api.api.management_api_client.ManagementAPIClient()  # noqa: E501

    def tearDown(self):
        pass

    def test_connect(self):
        """Test case for connect

        Establish permanent connection with device  # noqa: E501
        """
        pass

    def test_get_device(self):
        """Test case for get_device

        Fetch the state of a device.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
