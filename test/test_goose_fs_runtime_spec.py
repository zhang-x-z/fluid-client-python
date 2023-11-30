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
from fluid.models.goose_fs_runtime_spec import GooseFSRuntimeSpec  # noqa: E501
from fluid.rest import ApiException

class TestGooseFSRuntimeSpec(unittest.TestCase):
    """GooseFSRuntimeSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GooseFSRuntimeSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.goose_fs_runtime_spec.GooseFSRuntimeSpec()  # noqa: E501
        if include_optional :
            return GooseFSRuntimeSpec(
                api_gateway = fluid.models./goose_fs_comp_template_spec..GooseFSCompTemplateSpec(
                    annotations = {
                        'key' : '0'
                        }, 
                    enabled = True, 
                    env = {
                        'key' : '0'
                        }, 
                    jvm_options = [
                        '0'
                        ], 
                    node_selector = {
                        'key' : '0'
                        }, 
                    ports = {
                        'key' : 56
                        }, 
                    properties = {
                        'key' : '0'
                        }, 
                    replicas = 56, 
                    resources = None, ), 
                clean_cache_policy = fluid.models./clean_cache_policy..CleanCachePolicy(
                    grace_period_seconds = 56, 
                    max_retry_attempts = 56, ), 
                data = fluid.models./data..Data(
                    pin = True, 
                    replicas = 56, ), 
                disable_prometheus = True, 
                fuse = fluid.models./goose_fs_fuse_spec..GooseFSFuseSpec(
                    annotations = {
                        'key' : '0'
                        }, 
                    args = [
                        '0'
                        ], 
                    clean_policy = '0', 
                    env = {
                        'key' : '0'
                        }, 
                    global = True, 
                    image = '0', 
                    image_pull_policy = '0', 
                    image_tag = '0', 
                    jvm_options = [
                        '0'
                        ], 
                    node_selector = {
                        'key' : '0'
                        }, 
                    properties = {
                        'key' : '0'
                        }, 
                    resources = None, ), 
                goosefs_version = fluid.models./version_spec..VersionSpec(
                    image = '0', 
                    image_pull_policy = '0', 
                    image_tag = '0', ), 
                hadoop_config = '0', 
                init_users = fluid.models./init_users_spec..InitUsersSpec(
                    env = {
                        'key' : '0'
                        }, 
                    image = '0', 
                    image_pull_policy = '0', 
                    image_tag = '0', 
                    resources = None, ), 
                job_master = fluid.models./goose_fs_comp_template_spec..GooseFSCompTemplateSpec(
                    annotations = {
                        'key' : '0'
                        }, 
                    enabled = True, 
                    env = {
                        'key' : '0'
                        }, 
                    jvm_options = [
                        '0'
                        ], 
                    node_selector = {
                        'key' : '0'
                        }, 
                    ports = {
                        'key' : 56
                        }, 
                    properties = {
                        'key' : '0'
                        }, 
                    replicas = 56, 
                    resources = None, ), 
                job_worker = fluid.models./goose_fs_comp_template_spec..GooseFSCompTemplateSpec(
                    annotations = {
                        'key' : '0'
                        }, 
                    enabled = True, 
                    env = {
                        'key' : '0'
                        }, 
                    jvm_options = [
                        '0'
                        ], 
                    node_selector = {
                        'key' : '0'
                        }, 
                    ports = {
                        'key' : 56
                        }, 
                    properties = {
                        'key' : '0'
                        }, 
                    replicas = 56, 
                    resources = None, ), 
                jvm_options = [
                    '0'
                    ], 
                master = fluid.models./goose_fs_comp_template_spec..GooseFSCompTemplateSpec(
                    annotations = {
                        'key' : '0'
                        }, 
                    enabled = True, 
                    env = {
                        'key' : '0'
                        }, 
                    jvm_options = [
                        '0'
                        ], 
                    node_selector = {
                        'key' : '0'
                        }, 
                    ports = {
                        'key' : 56
                        }, 
                    properties = {
                        'key' : '0'
                        }, 
                    replicas = 56, 
                    resources = None, ), 
                properties = {
                    'key' : '0'
                    }, 
                replicas = 56, 
                run_as = fluid.models./user..User(
                    gid = 56, 
                    group = '0', 
                    uid = 56, 
                    user = '0', ), 
                tieredstore = fluid.models./tiered_store..TieredStore(
                    levels = [
                        fluid.models./level..Level(
                            high = '0', 
                            low = '0', 
                            mediumtype = '0', 
                            path = '0', 
                            quota = None, 
                            quota_list = '0', 
                            volume_source = fluid.models./volume_source..VolumeSource(
                                aws_elastic_block_store = None, 
                                azure_disk = None, 
                                azure_file = None, 
                                cephfs = None, 
                                cinder = None, 
                                config_map = None, 
                                csi = None, 
                                downward_api = None, 
                                empty_dir = None, 
                                ephemeral = None, 
                                fc = None, 
                                flex_volume = None, 
                                flocker = None, 
                                gce_persistent_disk = None, 
                                git_repo = None, 
                                glusterfs = None, 
                                host_path = None, 
                                iscsi = None, 
                                nfs = None, 
                                persistent_volume_claim = None, 
                                photon_persistent_disk = None, 
                                portworx_volume = None, 
                                projected = None, 
                                quobyte = None, 
                                rbd = None, 
                                scale_io = None, 
                                secret = None, 
                                storageos = None, 
                                vsphere_volume = None, ), 
                            volume_type = '0', )
                        ], ), 
                worker = fluid.models./goose_fs_comp_template_spec..GooseFSCompTemplateSpec(
                    annotations = {
                        'key' : '0'
                        }, 
                    enabled = True, 
                    env = {
                        'key' : '0'
                        }, 
                    jvm_options = [
                        '0'
                        ], 
                    node_selector = {
                        'key' : '0'
                        }, 
                    ports = {
                        'key' : 56
                        }, 
                    properties = {
                        'key' : '0'
                        }, 
                    replicas = 56, 
                    resources = None, )
            )
        else :
            return GooseFSRuntimeSpec(
        )

    def testGooseFSRuntimeSpec(self):
        """Test GooseFSRuntimeSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()