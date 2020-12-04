# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class SandboxProcessorTokenCreateRequestOptions(object):
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
        'override_username': 'str',
        'override_password': 'str'
    }

    attribute_map = {
        'override_username': 'override_username',
        'override_password': 'override_password'
    }

    def __init__(self, override_username='user_good', override_password='pass_good', local_vars_configuration=None):  # noqa: E501
        """SandboxProcessorTokenCreateRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._override_username = None
        self._override_password = None
        self.discriminator = None

        if override_username is not None:
            self.override_username = override_username
        if override_password is not None:
            self.override_password = override_password

    @property
    def override_username(self):
        """Gets the override_username of this SandboxProcessorTokenCreateRequestOptions.  # noqa: E501

        Test username to use for the creation of the Sandbox Item. Default value is `user_good`.  # noqa: E501

        :return: The override_username of this SandboxProcessorTokenCreateRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._override_username

    @override_username.setter
    def override_username(self, override_username):
        """Sets the override_username of this SandboxProcessorTokenCreateRequestOptions.

        Test username to use for the creation of the Sandbox Item. Default value is `user_good`.  # noqa: E501

        :param override_username: The override_username of this SandboxProcessorTokenCreateRequestOptions.  # noqa: E501
        :type override_username: str
        """

        self._override_username = override_username

    @property
    def override_password(self):
        """Gets the override_password of this SandboxProcessorTokenCreateRequestOptions.  # noqa: E501

        Test password to use for the creation of the Sandbox Item. Default value is `pass_good`.  # noqa: E501

        :return: The override_password of this SandboxProcessorTokenCreateRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._override_password

    @override_password.setter
    def override_password(self, override_password):
        """Sets the override_password of this SandboxProcessorTokenCreateRequestOptions.

        Test password to use for the creation of the Sandbox Item. Default value is `pass_good`.  # noqa: E501

        :param override_password: The override_password of this SandboxProcessorTokenCreateRequestOptions.  # noqa: E501
        :type override_password: str
        """

        self._override_password = override_password

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
        if not isinstance(other, SandboxProcessorTokenCreateRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxProcessorTokenCreateRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
