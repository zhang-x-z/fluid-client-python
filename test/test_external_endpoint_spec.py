# coding: utf-8

"""
    fluid

    client for fluid  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import fluid
from fluid.models.external_endpoint_spec import ExternalEndpointSpec  # noqa: E501
from fluid.rest import ApiException

class TestExternalEndpointSpec(unittest.TestCase):
    """ExternalEndpointSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExternalEndpointSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.external_endpoint_spec.ExternalEndpointSpec()  # noqa: E501
        if include_optional :
            return ExternalEndpointSpec(
                encrypt_options = [
                    fluid.models./encrypt_option..EncryptOption(
                        name = '0', 
                        value_from = fluid.models./encrypt_option_source..EncryptOptionSource(
                            secret_key_ref = fluid.models./secret_key_selector..SecretKeySelector(
                                key = '0', 
                                name = '0', ), ), )
                    ], 
                options = {
                    'key' : '0'
                    }, 
                uri = '0'
            )
        else :
            return ExternalEndpointSpec(
        )

    def testExternalEndpointSpec(self):
        """Test ExternalEndpointSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
