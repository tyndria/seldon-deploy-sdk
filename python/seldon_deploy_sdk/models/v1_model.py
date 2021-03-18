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


class V1Model(object):
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
        'uri': 'str',
        'name': 'str',
        'version': 'str',
        'implementation': 'str',
        'task_type': 'str',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'uri': 'URI',
        'name': 'name',
        'version': 'version',
        'implementation': 'implementation',
        'task_type': 'taskType',
        'tags': 'tags'
    }

    def __init__(self, uri=None, name=None, version='"v0.0.1"', implementation=None, task_type=None, tags=None):  # noqa: E501
        """V1Model - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._version = None
        self._implementation = None
        self._task_type = None
        self._tags = None
        self.discriminator = None

        self.uri = uri
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if implementation is not None:
            self.implementation = implementation
        if task_type is not None:
            self.task_type = task_type
        if tags is not None:
            self.tags = tags

    @property
    def uri(self):
        """Gets the uri of this V1Model.  # noqa: E501

        The URI for the storage bucket containing the model, or the URI to the docker image for custom models.  # noqa: E501

        :return: The uri of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this V1Model.

        The URI for the storage bucket containing the model, or the URI to the docker image for custom models.  # noqa: E501

        :param uri: The uri of this V1Model.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this V1Model.  # noqa: E501

        The name of the model.  # noqa: E501

        :return: The name of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1Model.

        The name of the model.  # noqa: E501

        :param name: The name of this V1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this V1Model.  # noqa: E501

        The version of the model.  # noqa: E501

        :return: The version of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1Model.

        The version of the model.  # noqa: E501

        :param version: The version of this V1Model.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def implementation(self):
        """Gets the implementation of this V1Model.  # noqa: E501

        The implementation used for serving the model.  # noqa: E501

        :return: The implementation of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._implementation

    @implementation.setter
    def implementation(self, implementation):
        """Sets the implementation of this V1Model.

        The implementation used for serving the model.  # noqa: E501

        :param implementation: The implementation of this V1Model.  # noqa: E501
        :type: str
        """

        self._implementation = implementation

    @property
    def task_type(self):
        """Gets the task_type of this V1Model.  # noqa: E501

        The task type of the model.  # noqa: E501

        :return: The task_type of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this V1Model.

        The task type of the model.  # noqa: E501

        :param task_type: The task_type of this V1Model.  # noqa: E501
        :type: str
        """

        self._task_type = task_type

    @property
    def tags(self):
        """Gets the tags of this V1Model.  # noqa: E501

        Key-value pairs of arbitrary metadata associated with the model  # noqa: E501

        :return: The tags of this V1Model.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1Model.

        Key-value pairs of arbitrary metadata associated with the model  # noqa: E501

        :param tags: The tags of this V1Model.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

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
        if issubclass(V1Model, dict):
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
        if not isinstance(other, V1Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other