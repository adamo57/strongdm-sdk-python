# Copyright 2020 StrongDM Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This file was generated by protogen. DO NOT EDIT.


class RPCError(Exception):
    """A generic RPC error"""
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code


# AlreadyExistsError is used when an entity already exists in the system
class AlreadyExistsError(RPCError):
    """Used when an entity already exists in the system"""
    def __init__(self, msg):
        super().__init__(msg, 6)


# NotFoundError is used when an entity does not exist in the system
class NotFoundError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 5)


# BadRequestError identifies a bad request sent by the client
class BadRequestError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 3)


# AuthenticationError is used to specify an authentication failure condition
class AuthenticationError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 16)


# PermissionError is used to specify a permissions violation
class PermissionError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 7)


# InternalError is used to specify an internal system error
class InternalError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 13)


# RateLimitError is used for rate limit excess condition
class RateLimitError(RPCError):
    def __init__(self, msg, rate_limit):
        super().__init__(msg, 8)
        self.rate_limit = rate_limit


class TimeoutError(RPCError):
    def __init__(self):
        super().__init__('deadline exceeded', 4)
