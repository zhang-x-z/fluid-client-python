# coding: utf-8

"""
    fluid

    client for fluid  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fluid.configuration import Configuration


class JindoFuseSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'args': 'list[str]',
        'clean_policy': 'str',
        'disabled': 'bool',
        'env': 'dict(str, str)',
        '_global': 'bool',
        'image': 'str',
        'image_pull_policy': 'str',
        'image_tag': 'str',
        'labels': 'dict(str, str)',
        'log_config': 'dict(str, str)',
        'node_selector': 'dict(str, str)',
        'pod_metadata': 'PodMetadata',
        'properties': 'dict(str, str)',
        'resources': 'V1ResourceRequirements',
        'tolerations': 'list[V1Toleration]'
    }

    attribute_map = {
        'args': 'args',
        'clean_policy': 'cleanPolicy',
        'disabled': 'disabled',
        'env': 'env',
        '_global': 'global',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag',
        'labels': 'labels',
        'log_config': 'logConfig',
        'node_selector': 'nodeSelector',
        'pod_metadata': 'podMetadata',
        'properties': 'properties',
        'resources': 'resources',
        'tolerations': 'tolerations'
    }

    def __init__(self, args=None, clean_policy=None, disabled=None, env=None, _global=None, image=None, image_pull_policy=None, image_tag=None, labels=None, log_config=None, node_selector=None, pod_metadata=None, properties=None, resources=None, tolerations=None, local_vars_configuration=None):  # noqa: E501
        """JindoFuseSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._clean_policy = None
        self._disabled = None
        self._env = None
        self.__global = None
        self._image = None
        self._image_pull_policy = None
        self._image_tag = None
        self._labels = None
        self._log_config = None
        self._node_selector = None
        self._pod_metadata = None
        self._properties = None
        self._resources = None
        self._tolerations = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if clean_policy is not None:
            self.clean_policy = clean_policy
        if disabled is not None:
            self.disabled = disabled
        if env is not None:
            self.env = env
        if _global is not None:
            self._global = _global
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_tag is not None:
            self.image_tag = image_tag
        if labels is not None:
            self.labels = labels
        if log_config is not None:
            self.log_config = log_config
        if node_selector is not None:
            self.node_selector = node_selector
        if pod_metadata is not None:
            self.pod_metadata = pod_metadata
        if properties is not None:
            self.properties = properties
        if resources is not None:
            self.resources = resources
        if tolerations is not None:
            self.tolerations = tolerations

    @property
    def args(self):
        """Gets the args of this JindoFuseSpec.  # noqa: E501

        Arguments that will be passed to Jindo Fuse  # noqa: E501

        :return: The args of this JindoFuseSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this JindoFuseSpec.

        Arguments that will be passed to Jindo Fuse  # noqa: E501

        :param args: The args of this JindoFuseSpec.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def clean_policy(self):
        """Gets the clean_policy of this JindoFuseSpec.  # noqa: E501

        CleanPolicy decides when to clean JindoFS Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnRuntimeDeleted  # noqa: E501

        :return: The clean_policy of this JindoFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._clean_policy

    @clean_policy.setter
    def clean_policy(self, clean_policy):
        """Sets the clean_policy of this JindoFuseSpec.

        CleanPolicy decides when to clean JindoFS Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnRuntimeDeleted  # noqa: E501

        :param clean_policy: The clean_policy of this JindoFuseSpec.  # noqa: E501
        :type: str
        """

        self._clean_policy = clean_policy

    @property
    def disabled(self):
        """Gets the disabled of this JindoFuseSpec.  # noqa: E501

        If disable JindoFS fuse  # noqa: E501

        :return: The disabled of this JindoFuseSpec.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this JindoFuseSpec.

        If disable JindoFS fuse  # noqa: E501

        :param disabled: The disabled of this JindoFuseSpec.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def env(self):
        """Gets the env of this JindoFuseSpec.  # noqa: E501

        Environment variables that will be used by Jindo Fuse  # noqa: E501

        :return: The env of this JindoFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this JindoFuseSpec.

        Environment variables that will be used by Jindo Fuse  # noqa: E501

        :param env: The env of this JindoFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._env = env

    @property
    def _global(self):
        """Gets the _global of this JindoFuseSpec.  # noqa: E501

        If the fuse client should be deployed in global mode, otherwise the affinity should be considered  # noqa: E501

        :return: The _global of this JindoFuseSpec.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this JindoFuseSpec.

        If the fuse client should be deployed in global mode, otherwise the affinity should be considered  # noqa: E501

        :param _global: The _global of this JindoFuseSpec.  # noqa: E501
        :type: bool
        """

        self.__global = _global

    @property
    def image(self):
        """Gets the image of this JindoFuseSpec.  # noqa: E501

        Image for Jindo Fuse(e.g. jindo/jindo-fuse)  # noqa: E501

        :return: The image of this JindoFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this JindoFuseSpec.

        Image for Jindo Fuse(e.g. jindo/jindo-fuse)  # noqa: E501

        :param image: The image of this JindoFuseSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this JindoFuseSpec.  # noqa: E501

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :return: The image_pull_policy of this JindoFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this JindoFuseSpec.

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this JindoFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        """Gets the image_tag of this JindoFuseSpec.  # noqa: E501

        Image Tag for Jindo Fuse(e.g. 2.3.0-SNAPSHOT)  # noqa: E501

        :return: The image_tag of this JindoFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this JindoFuseSpec.

        Image Tag for Jindo Fuse(e.g. 2.3.0-SNAPSHOT)  # noqa: E501

        :param image_tag: The image_tag of this JindoFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def labels(self):
        """Gets the labels of this JindoFuseSpec.  # noqa: E501

        Labels will be added on all the JindoFS pods. DEPRECATED: this is a deprecated field. Please use PodMetadata.Labels instead. Note: this field is set to be exclusive with PodMetadata.Labels  # noqa: E501

        :return: The labels of this JindoFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this JindoFuseSpec.

        Labels will be added on all the JindoFS pods. DEPRECATED: this is a deprecated field. Please use PodMetadata.Labels instead. Note: this field is set to be exclusive with PodMetadata.Labels  # noqa: E501

        :param labels: The labels of this JindoFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def log_config(self):
        """Gets the log_config of this JindoFuseSpec.  # noqa: E501


        :return: The log_config of this JindoFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        """Sets the log_config of this JindoFuseSpec.


        :param log_config: The log_config of this JindoFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._log_config = log_config

    @property
    def node_selector(self):
        """Gets the node_selector of this JindoFuseSpec.  # noqa: E501

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :return: The node_selector of this JindoFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this JindoFuseSpec.

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :param node_selector: The node_selector of this JindoFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def pod_metadata(self):
        """Gets the pod_metadata of this JindoFuseSpec.  # noqa: E501


        :return: The pod_metadata of this JindoFuseSpec.  # noqa: E501
        :rtype: PodMetadata
        """
        return self._pod_metadata

    @pod_metadata.setter
    def pod_metadata(self, pod_metadata):
        """Sets the pod_metadata of this JindoFuseSpec.


        :param pod_metadata: The pod_metadata of this JindoFuseSpec.  # noqa: E501
        :type: PodMetadata
        """

        self._pod_metadata = pod_metadata

    @property
    def properties(self):
        """Gets the properties of this JindoFuseSpec.  # noqa: E501

        Configurable properties for Jindo System. <br>  # noqa: E501

        :return: The properties of this JindoFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this JindoFuseSpec.

        Configurable properties for Jindo System. <br>  # noqa: E501

        :param properties: The properties of this JindoFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def resources(self):
        """Gets the resources of this JindoFuseSpec.  # noqa: E501


        :return: The resources of this JindoFuseSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this JindoFuseSpec.


        :param resources: The resources of this JindoFuseSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def tolerations(self):
        """Gets the tolerations of this JindoFuseSpec.  # noqa: E501

        If specified, the pod's tolerations.  # noqa: E501

        :return: The tolerations of this JindoFuseSpec.  # noqa: E501
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this JindoFuseSpec.

        If specified, the pod's tolerations.  # noqa: E501

        :param tolerations: The tolerations of this JindoFuseSpec.  # noqa: E501
        :type: list[V1Toleration]
        """

        self._tolerations = tolerations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JindoFuseSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JindoFuseSpec):
            return True

        return self.to_dict() != other.to_dict()