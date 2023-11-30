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


class JuiceFSFuseSpec(object):
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
        'clean_policy': 'str',
        'env': 'list[V1EnvVar]',
        '_global': 'bool',
        'image': 'str',
        'image_pull_policy': 'str',
        'image_tag': 'str',
        'network_mode': 'str',
        'node_selector': 'dict(str, str)',
        'options': 'dict(str, str)',
        'pod_metadata': 'PodMetadata',
        'resources': 'V1ResourceRequirements',
        'volume_mounts': 'list[V1VolumeMount]'
    }

    attribute_map = {
        'clean_policy': 'cleanPolicy',
        'env': 'env',
        '_global': 'global',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag',
        'network_mode': 'networkMode',
        'node_selector': 'nodeSelector',
        'options': 'options',
        'pod_metadata': 'podMetadata',
        'resources': 'resources',
        'volume_mounts': 'volumeMounts'
    }

    def __init__(self, clean_policy=None, env=None, _global=None, image=None, image_pull_policy=None, image_tag=None, network_mode=None, node_selector=None, options=None, pod_metadata=None, resources=None, volume_mounts=None, local_vars_configuration=None):  # noqa: E501
        """JuiceFSFuseSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._clean_policy = None
        self._env = None
        self.__global = None
        self._image = None
        self._image_pull_policy = None
        self._image_tag = None
        self._network_mode = None
        self._node_selector = None
        self._options = None
        self._pod_metadata = None
        self._resources = None
        self._volume_mounts = None
        self.discriminator = None

        if clean_policy is not None:
            self.clean_policy = clean_policy
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
        if network_mode is not None:
            self.network_mode = network_mode
        if node_selector is not None:
            self.node_selector = node_selector
        if options is not None:
            self.options = options
        if pod_metadata is not None:
            self.pod_metadata = pod_metadata
        if resources is not None:
            self.resources = resources
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts

    @property
    def clean_policy(self):
        """Gets the clean_policy of this JuiceFSFuseSpec.  # noqa: E501

        CleanPolicy decides when to clean Juicefs Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnDemand  # noqa: E501

        :return: The clean_policy of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._clean_policy

    @clean_policy.setter
    def clean_policy(self, clean_policy):
        """Sets the clean_policy of this JuiceFSFuseSpec.

        CleanPolicy decides when to clean Juicefs Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnDemand  # noqa: E501

        :param clean_policy: The clean_policy of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._clean_policy = clean_policy

    @property
    def env(self):
        """Gets the env of this JuiceFSFuseSpec.  # noqa: E501

        Environment variables that will be used by JuiceFS Fuse  # noqa: E501

        :return: The env of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this JuiceFSFuseSpec.

        Environment variables that will be used by JuiceFS Fuse  # noqa: E501

        :param env: The env of this JuiceFSFuseSpec.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def _global(self):
        """Gets the _global of this JuiceFSFuseSpec.  # noqa: E501

        If the fuse client should be deployed in global mode, otherwise the affinity should be considered  # noqa: E501

        :return: The _global of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this JuiceFSFuseSpec.

        If the fuse client should be deployed in global mode, otherwise the affinity should be considered  # noqa: E501

        :param _global: The _global of this JuiceFSFuseSpec.  # noqa: E501
        :type: bool
        """

        self.__global = _global

    @property
    def image(self):
        """Gets the image of this JuiceFSFuseSpec.  # noqa: E501

        Image for JuiceFS fuse  # noqa: E501

        :return: The image of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this JuiceFSFuseSpec.

        Image for JuiceFS fuse  # noqa: E501

        :param image: The image of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this JuiceFSFuseSpec.  # noqa: E501

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :return: The image_pull_policy of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this JuiceFSFuseSpec.

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        """Gets the image_tag of this JuiceFSFuseSpec.  # noqa: E501

        Image for JuiceFS fuse  # noqa: E501

        :return: The image_tag of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this JuiceFSFuseSpec.

        Image for JuiceFS fuse  # noqa: E501

        :param image_tag: The image_tag of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def network_mode(self):
        """Gets the network_mode of this JuiceFSFuseSpec.  # noqa: E501

        Whether to use hostnetwork or not  # noqa: E501

        :return: The network_mode of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        """Sets the network_mode of this JuiceFSFuseSpec.

        Whether to use hostnetwork or not  # noqa: E501

        :param network_mode: The network_mode of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._network_mode = network_mode

    @property
    def node_selector(self):
        """Gets the node_selector of this JuiceFSFuseSpec.  # noqa: E501

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :return: The node_selector of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this JuiceFSFuseSpec.

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :param node_selector: The node_selector of this JuiceFSFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def options(self):
        """Gets the options of this JuiceFSFuseSpec.  # noqa: E501

        Options mount options that fuse pod will use  # noqa: E501

        :return: The options of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this JuiceFSFuseSpec.

        Options mount options that fuse pod will use  # noqa: E501

        :param options: The options of this JuiceFSFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def pod_metadata(self):
        """Gets the pod_metadata of this JuiceFSFuseSpec.  # noqa: E501


        :return: The pod_metadata of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: PodMetadata
        """
        return self._pod_metadata

    @pod_metadata.setter
    def pod_metadata(self, pod_metadata):
        """Sets the pod_metadata of this JuiceFSFuseSpec.


        :param pod_metadata: The pod_metadata of this JuiceFSFuseSpec.  # noqa: E501
        :type: PodMetadata
        """

        self._pod_metadata = pod_metadata

    @property
    def resources(self):
        """Gets the resources of this JuiceFSFuseSpec.  # noqa: E501


        :return: The resources of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this JuiceFSFuseSpec.


        :param resources: The resources of this JuiceFSFuseSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this JuiceFSFuseSpec.  # noqa: E501

        VolumeMounts specifies the volumes listed in \".spec.volumes\" to mount into runtime component's filesystem.  # noqa: E501

        :return: The volume_mounts of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: list[V1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this JuiceFSFuseSpec.

        VolumeMounts specifies the volumes listed in \".spec.volumes\" to mount into runtime component's filesystem.  # noqa: E501

        :param volume_mounts: The volume_mounts of this JuiceFSFuseSpec.  # noqa: E501
        :type: list[V1VolumeMount]
        """

        self._volume_mounts = volume_mounts

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
        if not isinstance(other, JuiceFSFuseSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JuiceFSFuseSpec):
            return True

        return self.to_dict() != other.to_dict()
