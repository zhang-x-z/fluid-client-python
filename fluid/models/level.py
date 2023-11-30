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


class Level(object):
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
        'high': 'str',
        'low': 'str',
        'mediumtype': 'str',
        'path': 'str',
        'quota': 'K8sIoApimachineryPkgApiResourceQuantity',
        'quota_list': 'str',
        'volume_source': 'VolumeSource',
        'volume_type': 'str'
    }

    attribute_map = {
        'high': 'high',
        'low': 'low',
        'mediumtype': 'mediumtype',
        'path': 'path',
        'quota': 'quota',
        'quota_list': 'quotaList',
        'volume_source': 'volumeSource',
        'volume_type': 'volumeType'
    }

    def __init__(self, high=None, low=None, mediumtype='', path=None, quota=None, quota_list=None, volume_source=None, volume_type='', local_vars_configuration=None):  # noqa: E501
        """Level - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._high = None
        self._low = None
        self._mediumtype = None
        self._path = None
        self._quota = None
        self._quota_list = None
        self._volume_source = None
        self._volume_type = None
        self.discriminator = None

        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        self.mediumtype = mediumtype
        if path is not None:
            self.path = path
        if quota is not None:
            self.quota = quota
        if quota_list is not None:
            self.quota_list = quota_list
        if volume_source is not None:
            self.volume_source = volume_source
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def high(self):
        """Gets the high of this Level.  # noqa: E501

        Ratio of high watermark of the tier (e.g. 0.9)  # noqa: E501

        :return: The high of this Level.  # noqa: E501
        :rtype: str
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this Level.

        Ratio of high watermark of the tier (e.g. 0.9)  # noqa: E501

        :param high: The high of this Level.  # noqa: E501
        :type: str
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this Level.  # noqa: E501

        Ratio of low watermark of the tier (e.g. 0.7)  # noqa: E501

        :return: The low of this Level.  # noqa: E501
        :rtype: str
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this Level.

        Ratio of low watermark of the tier (e.g. 0.7)  # noqa: E501

        :param low: The low of this Level.  # noqa: E501
        :type: str
        """

        self._low = low

    @property
    def mediumtype(self):
        """Gets the mediumtype of this Level.  # noqa: E501

        Medium Type of the tier. One of the three types: `MEM`, `SSD`, `HDD`  # noqa: E501

        :return: The mediumtype of this Level.  # noqa: E501
        :rtype: str
        """
        return self._mediumtype

    @mediumtype.setter
    def mediumtype(self, mediumtype):
        """Sets the mediumtype of this Level.

        Medium Type of the tier. One of the three types: `MEM`, `SSD`, `HDD`  # noqa: E501

        :param mediumtype: The mediumtype of this Level.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mediumtype is None:  # noqa: E501
            raise ValueError("Invalid value for `mediumtype`, must not be `None`")  # noqa: E501

        self._mediumtype = mediumtype

    @property
    def path(self):
        """Gets the path of this Level.  # noqa: E501

        File paths to be used for the tier. Multiple paths are supported. Multiple paths should be separated with comma. For example: \"/mnt/cache1,/mnt/cache2\".  # noqa: E501

        :return: The path of this Level.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Level.

        File paths to be used for the tier. Multiple paths are supported. Multiple paths should be separated with comma. For example: \"/mnt/cache1,/mnt/cache2\".  # noqa: E501

        :param path: The path of this Level.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def quota(self):
        """Gets the quota of this Level.  # noqa: E501


        :return: The quota of this Level.  # noqa: E501
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this Level.


        :param quota: The quota of this Level.  # noqa: E501
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """

        self._quota = quota

    @property
    def quota_list(self):
        """Gets the quota_list of this Level.  # noqa: E501

        QuotaList are quotas used to set quota on multiple paths. Quotas should be separated with comma. Quotas in this list will be set to paths with the same order in Path. For example, with Path defined with \"/mnt/cache1,/mnt/cache2\" and QuotaList set to \"100Gi, 50Gi\", then we get 100GiB cache storage under \"/mnt/cache1\" and 50GiB under \"/mnt/cache2\". Also note that num of quotas must be consistent with the num of paths defined in Path.  # noqa: E501

        :return: The quota_list of this Level.  # noqa: E501
        :rtype: str
        """
        return self._quota_list

    @quota_list.setter
    def quota_list(self, quota_list):
        """Sets the quota_list of this Level.

        QuotaList are quotas used to set quota on multiple paths. Quotas should be separated with comma. Quotas in this list will be set to paths with the same order in Path. For example, with Path defined with \"/mnt/cache1,/mnt/cache2\" and QuotaList set to \"100Gi, 50Gi\", then we get 100GiB cache storage under \"/mnt/cache1\" and 50GiB under \"/mnt/cache2\". Also note that num of quotas must be consistent with the num of paths defined in Path.  # noqa: E501

        :param quota_list: The quota_list of this Level.  # noqa: E501
        :type: str
        """

        self._quota_list = quota_list

    @property
    def volume_source(self):
        """Gets the volume_source of this Level.  # noqa: E501


        :return: The volume_source of this Level.  # noqa: E501
        :rtype: VolumeSource
        """
        return self._volume_source

    @volume_source.setter
    def volume_source(self, volume_source):
        """Sets the volume_source of this Level.


        :param volume_source: The volume_source of this Level.  # noqa: E501
        :type: VolumeSource
        """

        self._volume_source = volume_source

    @property
    def volume_type(self):
        """Gets the volume_type of this Level.  # noqa: E501

        VolumeType is the volume type of the tier. Should be one of the three types: `hostPath`, `emptyDir` and `volumeTemplate`. If not set, defaults to hostPath.  # noqa: E501

        :return: The volume_type of this Level.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this Level.

        VolumeType is the volume type of the tier. Should be one of the three types: `hostPath`, `emptyDir` and `volumeTemplate`. If not set, defaults to hostPath.  # noqa: E501

        :param volume_type: The volume_type of this Level.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

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
        if not isinstance(other, Level):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Level):
            return True

        return self.to_dict() != other.to_dict()
