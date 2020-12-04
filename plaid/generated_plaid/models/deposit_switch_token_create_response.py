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


class DepositSwitchTokenCreateResponse(object):
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
        'deposit_switch_token': 'str',
        'deposit_switch_token_expiration_time': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'deposit_switch_token': 'deposit_switch_token',
        'deposit_switch_token_expiration_time': 'deposit_switch_token_expiration_time',
        'request_id': 'request_id'
    }

    def __init__(self, deposit_switch_token=None, deposit_switch_token_expiration_time=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """DepositSwitchTokenCreateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deposit_switch_token = None
        self._deposit_switch_token_expiration_time = None
        self._request_id = None
        self.discriminator = None

        if deposit_switch_token is not None:
            self.deposit_switch_token = deposit_switch_token
        if deposit_switch_token_expiration_time is not None:
            self.deposit_switch_token_expiration_time = deposit_switch_token_expiration_time
        if request_id is not None:
            self.request_id = request_id

    @property
    def deposit_switch_token(self):
        """Gets the deposit_switch_token of this DepositSwitchTokenCreateResponse.  # noqa: E501

        Deposit Switch token, used to initialize Link for the Deposit Switch product  # noqa: E501

        :return: The deposit_switch_token of this DepositSwitchTokenCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._deposit_switch_token

    @deposit_switch_token.setter
    def deposit_switch_token(self, deposit_switch_token):
        """Sets the deposit_switch_token of this DepositSwitchTokenCreateResponse.

        Deposit Switch token, used to initialize Link for the Deposit Switch product  # noqa: E501

        :param deposit_switch_token: The deposit_switch_token of this DepositSwitchTokenCreateResponse.  # noqa: E501
        :type deposit_switch_token: str
        """

        self._deposit_switch_token = deposit_switch_token

    @property
    def deposit_switch_token_expiration_time(self):
        """Gets the deposit_switch_token_expiration_time of this DepositSwitchTokenCreateResponse.  # noqa: E501

        Expiration time of the token, in ISO8601 format  # noqa: E501

        :return: The deposit_switch_token_expiration_time of this DepositSwitchTokenCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._deposit_switch_token_expiration_time

    @deposit_switch_token_expiration_time.setter
    def deposit_switch_token_expiration_time(self, deposit_switch_token_expiration_time):
        """Sets the deposit_switch_token_expiration_time of this DepositSwitchTokenCreateResponse.

        Expiration time of the token, in ISO8601 format  # noqa: E501

        :param deposit_switch_token_expiration_time: The deposit_switch_token_expiration_time of this DepositSwitchTokenCreateResponse.  # noqa: E501
        :type deposit_switch_token_expiration_time: str
        """

        self._deposit_switch_token_expiration_time = deposit_switch_token_expiration_time

    @property
    def request_id(self):
        """Gets the request_id of this DepositSwitchTokenCreateResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this DepositSwitchTokenCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DepositSwitchTokenCreateResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this DepositSwitchTokenCreateResponse.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

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
        if not isinstance(other, DepositSwitchTokenCreateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DepositSwitchTokenCreateResponse):
            return True

        return self.to_dict() != other.to_dict()
