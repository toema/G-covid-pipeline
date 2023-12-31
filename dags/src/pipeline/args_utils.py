# Copyright 2020 Google LLC.
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

import argparse
import os

import path_utils


class _AbsPathAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, os.path.abspath(values))


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--allowlist', '-w', dest='allowlist', action='store_true',
                        help='Filter configs against allowlist.yaml.')
    parser.add_argument('--no-allowlist', dest='allowlist', action='store_false',
                        help='Disable filtering of configs against allowlist.yaml.')

    parser.add_argument('--source', nargs=1, help='Specify a single source.')
    parser.add_argument('--date', nargs=1, help='Specify a single date in YYYY-MM-DD format.')
    parser.add_argument(
        '--publish_dir', default=path_utils.root_dir, action=_AbsPathAction,
        help='Base directory where outputs are written. Default value writes to the current directory tree.')
    parser.set_defaults(allowlist=True)

    return parser
