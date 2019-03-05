# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from paddle_hub.tools.arg_helper import add_argument, print_arguments
from paddle_hub.tools.logger import logger
import argparse


class BaseCommand:
    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        assert not hasattr(
            self.__class__,
            '_instance'), 'Please use `instance()` to get Command object!'
        self.parser = argparse.ArgumentParser(description=__doc__)
        self.args = None

    def add_arg(self, argument, type="str", default=None, help=None):
        add_argument(
            argument=argument,
            type=type,
            default=default,
            help=help,
            argparser=self.parser)

    def print_args(self):
        print_arguments(self.args)

    def exec(self, argv):
        raise NotImplementedError("Base Command should not be execute!")
