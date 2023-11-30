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
from fluid.models.clean_cache_policy import CleanCachePolicy  # noqa: E501
from fluid.rest import ApiException

class TestCleanCachePolicy(unittest.TestCase):
    """CleanCachePolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CleanCachePolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.clean_cache_policy.CleanCachePolicy()  # noqa: E501
        if include_optional :
            return CleanCachePolicy(
                grace_period_seconds = 56, 
                max_retry_attempts = 56
            )
        else :
            return CleanCachePolicy(
        )

    def testCleanCachePolicy(self):
        """Test CleanCachePolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
