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
from fluid.models.init_fuse_spec import InitFuseSpec  # noqa: E501
from fluid.rest import ApiException

class TestInitFuseSpec(unittest.TestCase):
    """InitFuseSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InitFuseSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.init_fuse_spec.InitFuseSpec()  # noqa: E501
        if include_optional :
            return InitFuseSpec(
                version = fluid.models./version_spec..VersionSpec(
                    image = '0', 
                    image_pull_policy = '0', 
                    image_tag = '0', )
            )
        else :
            return InitFuseSpec(
        )

    def testInitFuseSpec(self):
        """Test InitFuseSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
