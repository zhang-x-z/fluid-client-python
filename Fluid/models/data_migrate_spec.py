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


class DataMigrateSpec(object):
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
        'affinity': 'V1Affinity',
        'block': 'bool',
        '_from': 'DataToMigrate',
        'image': 'str',
        'image_pull_policy': 'str',
        'image_tag': 'str',
        'node_selector': 'dict(str, str)',
        'options': 'dict(str, str)',
        'pod_metadata': 'PodMetadata',
        'policy': 'str',
        'resources': 'V1ResourceRequirements',
        'run_after': 'OperationRef',
        'runtime_type': 'str',
        'schedule': 'str',
        'scheduler_name': 'str',
        'to': 'DataToMigrate',
        'tolerations': 'list[V1Toleration]',
        'ttl_seconds_after_finished': 'int'
    }

    attribute_map = {
        'affinity': 'affinity',
        'block': 'block',
        '_from': 'from',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag',
        'node_selector': 'nodeSelector',
        'options': 'options',
        'pod_metadata': 'podMetadata',
        'policy': 'policy',
        'resources': 'resources',
        'run_after': 'runAfter',
        'runtime_type': 'runtimeType',
        'schedule': 'schedule',
        'scheduler_name': 'schedulerName',
        'to': 'to',
        'tolerations': 'tolerations',
        'ttl_seconds_after_finished': 'ttlSecondsAfterFinished'
    }

    def __init__(self, affinity=None, block=None, _from=None, image=None, image_pull_policy=None, image_tag=None, node_selector=None, options=None, pod_metadata=None, policy=None, resources=None, run_after=None, runtime_type=None, schedule=None, scheduler_name=None, to=None, tolerations=None, ttl_seconds_after_finished=None, local_vars_configuration=None):  # noqa: E501
        """DataMigrateSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affinity = None
        self._block = None
        self.__from = None
        self._image = None
        self._image_pull_policy = None
        self._image_tag = None
        self._node_selector = None
        self._options = None
        self._pod_metadata = None
        self._policy = None
        self._resources = None
        self._run_after = None
        self._runtime_type = None
        self._schedule = None
        self._scheduler_name = None
        self._to = None
        self._tolerations = None
        self._ttl_seconds_after_finished = None
        self.discriminator = None

        if affinity is not None:
            self.affinity = affinity
        if block is not None:
            self.block = block
        self._from = _from
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_tag is not None:
            self.image_tag = image_tag
        if node_selector is not None:
            self.node_selector = node_selector
        if options is not None:
            self.options = options
        if pod_metadata is not None:
            self.pod_metadata = pod_metadata
        if policy is not None:
            self.policy = policy
        if resources is not None:
            self.resources = resources
        if run_after is not None:
            self.run_after = run_after
        if runtime_type is not None:
            self.runtime_type = runtime_type
        if schedule is not None:
            self.schedule = schedule
        if scheduler_name is not None:
            self.scheduler_name = scheduler_name
        self.to = to
        if tolerations is not None:
            self.tolerations = tolerations
        if ttl_seconds_after_finished is not None:
            self.ttl_seconds_after_finished = ttl_seconds_after_finished

    @property
    def affinity(self):
        """Gets the affinity of this DataMigrateSpec.  # noqa: E501


        :return: The affinity of this DataMigrateSpec.  # noqa: E501
        :rtype: V1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this DataMigrateSpec.


        :param affinity: The affinity of this DataMigrateSpec.  # noqa: E501
        :type: V1Affinity
        """

        self._affinity = affinity

    @property
    def block(self):
        """Gets the block of this DataMigrateSpec.  # noqa: E501

        if dataMigrate blocked dataset usage, default is false  # noqa: E501

        :return: The block of this DataMigrateSpec.  # noqa: E501
        :rtype: bool
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this DataMigrateSpec.

        if dataMigrate blocked dataset usage, default is false  # noqa: E501

        :param block: The block of this DataMigrateSpec.  # noqa: E501
        :type: bool
        """

        self._block = block

    @property
    def _from(self):
        """Gets the _from of this DataMigrateSpec.  # noqa: E501


        :return: The _from of this DataMigrateSpec.  # noqa: E501
        :rtype: DataToMigrate
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DataMigrateSpec.


        :param _from: The _from of this DataMigrateSpec.  # noqa: E501
        :type: DataToMigrate
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def image(self):
        """Gets the image of this DataMigrateSpec.  # noqa: E501

        Image (e.g. alluxio/alluxio)  # noqa: E501

        :return: The image of this DataMigrateSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DataMigrateSpec.

        Image (e.g. alluxio/alluxio)  # noqa: E501

        :param image: The image of this DataMigrateSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this DataMigrateSpec.  # noqa: E501

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :return: The image_pull_policy of this DataMigrateSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this DataMigrateSpec.

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this DataMigrateSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        """Gets the image_tag of this DataMigrateSpec.  # noqa: E501

        Image tag (e.g. 2.3.0-SNAPSHOT)  # noqa: E501

        :return: The image_tag of this DataMigrateSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this DataMigrateSpec.

        Image tag (e.g. 2.3.0-SNAPSHOT)  # noqa: E501

        :param image_tag: The image_tag of this DataMigrateSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def node_selector(self):
        """Gets the node_selector of this DataMigrateSpec.  # noqa: E501

        NodeSelector defiens node selector for DataLoad pod  # noqa: E501

        :return: The node_selector of this DataMigrateSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this DataMigrateSpec.

        NodeSelector defiens node selector for DataLoad pod  # noqa: E501

        :param node_selector: The node_selector of this DataMigrateSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def options(self):
        """Gets the options of this DataMigrateSpec.  # noqa: E501

        options for migrate, different for each runtime  # noqa: E501

        :return: The options of this DataMigrateSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DataMigrateSpec.

        options for migrate, different for each runtime  # noqa: E501

        :param options: The options of this DataMigrateSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def pod_metadata(self):
        """Gets the pod_metadata of this DataMigrateSpec.  # noqa: E501


        :return: The pod_metadata of this DataMigrateSpec.  # noqa: E501
        :rtype: PodMetadata
        """
        return self._pod_metadata

    @pod_metadata.setter
    def pod_metadata(self, pod_metadata):
        """Sets the pod_metadata of this DataMigrateSpec.


        :param pod_metadata: The pod_metadata of this DataMigrateSpec.  # noqa: E501
        :type: PodMetadata
        """

        self._pod_metadata = pod_metadata

    @property
    def policy(self):
        """Gets the policy of this DataMigrateSpec.  # noqa: E501

        policy for migrate, including Once, Cron, OnEvent  # noqa: E501

        :return: The policy of this DataMigrateSpec.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this DataMigrateSpec.

        policy for migrate, including Once, Cron, OnEvent  # noqa: E501

        :param policy: The policy of this DataMigrateSpec.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def resources(self):
        """Gets the resources of this DataMigrateSpec.  # noqa: E501


        :return: The resources of this DataMigrateSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this DataMigrateSpec.


        :param resources: The resources of this DataMigrateSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def run_after(self):
        """Gets the run_after of this DataMigrateSpec.  # noqa: E501


        :return: The run_after of this DataMigrateSpec.  # noqa: E501
        :rtype: OperationRef
        """
        return self._run_after

    @run_after.setter
    def run_after(self, run_after):
        """Sets the run_after of this DataMigrateSpec.


        :param run_after: The run_after of this DataMigrateSpec.  # noqa: E501
        :type: OperationRef
        """

        self._run_after = run_after

    @property
    def runtime_type(self):
        """Gets the runtime_type of this DataMigrateSpec.  # noqa: E501

        using which runtime to migrate data; if none, take dataset runtime as default  # noqa: E501

        :return: The runtime_type of this DataMigrateSpec.  # noqa: E501
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        """Sets the runtime_type of this DataMigrateSpec.

        using which runtime to migrate data; if none, take dataset runtime as default  # noqa: E501

        :param runtime_type: The runtime_type of this DataMigrateSpec.  # noqa: E501
        :type: str
        """

        self._runtime_type = runtime_type

    @property
    def schedule(self):
        """Gets the schedule of this DataMigrateSpec.  # noqa: E501

        The schedule in Cron format, only set when policy is cron, see https://en.wikipedia.org/wiki/Cron.  # noqa: E501

        :return: The schedule of this DataMigrateSpec.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this DataMigrateSpec.

        The schedule in Cron format, only set when policy is cron, see https://en.wikipedia.org/wiki/Cron.  # noqa: E501

        :param schedule: The schedule of this DataMigrateSpec.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def scheduler_name(self):
        """Gets the scheduler_name of this DataMigrateSpec.  # noqa: E501

        SchedulerName sets the scheduler to be used for DataLoad pod  # noqa: E501

        :return: The scheduler_name of this DataMigrateSpec.  # noqa: E501
        :rtype: str
        """
        return self._scheduler_name

    @scheduler_name.setter
    def scheduler_name(self, scheduler_name):
        """Sets the scheduler_name of this DataMigrateSpec.

        SchedulerName sets the scheduler to be used for DataLoad pod  # noqa: E501

        :param scheduler_name: The scheduler_name of this DataMigrateSpec.  # noqa: E501
        :type: str
        """

        self._scheduler_name = scheduler_name

    @property
    def to(self):
        """Gets the to of this DataMigrateSpec.  # noqa: E501


        :return: The to of this DataMigrateSpec.  # noqa: E501
        :rtype: DataToMigrate
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this DataMigrateSpec.


        :param to: The to of this DataMigrateSpec.  # noqa: E501
        :type: DataToMigrate
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def tolerations(self):
        """Gets the tolerations of this DataMigrateSpec.  # noqa: E501

        Tolerations defines tolerations for DataLoad pod  # noqa: E501

        :return: The tolerations of this DataMigrateSpec.  # noqa: E501
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this DataMigrateSpec.

        Tolerations defines tolerations for DataLoad pod  # noqa: E501

        :param tolerations: The tolerations of this DataMigrateSpec.  # noqa: E501
        :type: list[V1Toleration]
        """

        self._tolerations = tolerations

    @property
    def ttl_seconds_after_finished(self):
        """Gets the ttl_seconds_after_finished of this DataMigrateSpec.  # noqa: E501

        TTLSecondsAfterFinished is the time second to clean up data operations after finished or failed  # noqa: E501

        :return: The ttl_seconds_after_finished of this DataMigrateSpec.  # noqa: E501
        :rtype: int
        """
        return self._ttl_seconds_after_finished

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished):
        """Sets the ttl_seconds_after_finished of this DataMigrateSpec.

        TTLSecondsAfterFinished is the time second to clean up data operations after finished or failed  # noqa: E501

        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this DataMigrateSpec.  # noqa: E501
        :type: int
        """

        self._ttl_seconds_after_finished = ttl_seconds_after_finished

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
        if not isinstance(other, DataMigrateSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataMigrateSpec):
            return True

        return self.to_dict() != other.to_dict()
