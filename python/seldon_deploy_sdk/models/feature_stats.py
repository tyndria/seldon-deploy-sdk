# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FeatureStats(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'avg': 'float',
        'buckets': 'list[FeatureStatsBucket]',
        'count': 'int',
        'max': 'float',
        'min': 'float',
        'most_frequent_category': 'str',
        'most_frequent_category_count': 'float'
    }

    attribute_map = {
        'avg': 'avg',
        'buckets': 'buckets',
        'count': 'count',
        'max': 'max',
        'min': 'min',
        'most_frequent_category': 'most_frequent_category',
        'most_frequent_category_count': 'most_frequent_category_count'
    }

    def __init__(self, avg=None, buckets=None, count=None, max=None, min=None, most_frequent_category=None, most_frequent_category_count=None):  # noqa: E501
        """FeatureStats - a model defined in Swagger"""  # noqa: E501

        self._avg = None
        self._buckets = None
        self._count = None
        self._max = None
        self._min = None
        self._most_frequent_category = None
        self._most_frequent_category_count = None
        self.discriminator = None

        if avg is not None:
            self.avg = avg
        if buckets is not None:
            self.buckets = buckets
        if count is not None:
            self.count = count
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if most_frequent_category is not None:
            self.most_frequent_category = most_frequent_category
        if most_frequent_category_count is not None:
            self.most_frequent_category_count = most_frequent_category_count

    @property
    def avg(self):
        """Gets the avg of this FeatureStats.  # noqa: E501

        Statistical Average of a feature value (relevant to REAL features)  # noqa: E501

        :return: The avg of this FeatureStats.  # noqa: E501
        :rtype: float
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        """Sets the avg of this FeatureStats.

        Statistical Average of a feature value (relevant to REAL features)  # noqa: E501

        :param avg: The avg of this FeatureStats.  # noqa: E501
        :type: float
        """

        self._avg = avg

    @property
    def buckets(self):
        """Gets the buckets of this FeatureStats.  # noqa: E501

        Buckets in a feature statistics  # noqa: E501

        :return: The buckets of this FeatureStats.  # noqa: E501
        :rtype: list[FeatureStatsBucket]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this FeatureStats.

        Buckets in a feature statistics  # noqa: E501

        :param buckets: The buckets of this FeatureStats.  # noqa: E501
        :type: list[FeatureStatsBucket]
        """

        self._buckets = buckets

    @property
    def count(self):
        """Gets the count of this FeatureStats.  # noqa: E501

        Statistical Count of a feature value (relevant to REAL features)  # noqa: E501

        :return: The count of this FeatureStats.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this FeatureStats.

        Statistical Count of a feature value (relevant to REAL features)  # noqa: E501

        :param count: The count of this FeatureStats.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def max(self):
        """Gets the max of this FeatureStats.  # noqa: E501

        Statistical Maximum of a feature value (relevant to REAL features)  # noqa: E501

        :return: The max of this FeatureStats.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this FeatureStats.

        Statistical Maximum of a feature value (relevant to REAL features)  # noqa: E501

        :param max: The max of this FeatureStats.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this FeatureStats.  # noqa: E501

        Statistical Minimum of a feature value (relevant to REAL features)  # noqa: E501

        :return: The min of this FeatureStats.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this FeatureStats.

        Statistical Minimum of a feature value (relevant to REAL features)  # noqa: E501

        :param min: The min of this FeatureStats.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def most_frequent_category(self):
        """Gets the most_frequent_category of this FeatureStats.  # noqa: E501

        Statistical Most Frequent Category Name of a feature value (relevant to CATEGORICAL, PROBA and ONE_HOT features)  # noqa: E501

        :return: The most_frequent_category of this FeatureStats.  # noqa: E501
        :rtype: str
        """
        return self._most_frequent_category

    @most_frequent_category.setter
    def most_frequent_category(self, most_frequent_category):
        """Sets the most_frequent_category of this FeatureStats.

        Statistical Most Frequent Category Name of a feature value (relevant to CATEGORICAL, PROBA and ONE_HOT features)  # noqa: E501

        :param most_frequent_category: The most_frequent_category of this FeatureStats.  # noqa: E501
        :type: str
        """

        self._most_frequent_category = most_frequent_category

    @property
    def most_frequent_category_count(self):
        """Gets the most_frequent_category_count of this FeatureStats.  # noqa: E501

        Statistical Most Frequent Category Count of a feature value (relevant to CATEGORICAL, PROBA and ONE_HOT features)  # noqa: E501

        :return: The most_frequent_category_count of this FeatureStats.  # noqa: E501
        :rtype: float
        """
        return self._most_frequent_category_count

    @most_frequent_category_count.setter
    def most_frequent_category_count(self, most_frequent_category_count):
        """Sets the most_frequent_category_count of this FeatureStats.

        Statistical Most Frequent Category Count of a feature value (relevant to CATEGORICAL, PROBA and ONE_HOT features)  # noqa: E501

        :param most_frequent_category_count: The most_frequent_category_count of this FeatureStats.  # noqa: E501
        :type: float
        """

        self._most_frequent_category_count = most_frequent_category_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(FeatureStats, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeatureStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
