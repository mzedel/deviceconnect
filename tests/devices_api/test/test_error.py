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
import datetime

import devices_api
from devices_api.models.error import Error  # noqa: E501
from devices_api.rest import ApiException

class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Error
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = devices_api.models.error.Error()  # noqa: E501
        if include_optional :
            return Error(
                error = '0', 
                request_id = '0'
            )
        else :
            return Error(
        )

    def testError(self):
        """Test Error"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
