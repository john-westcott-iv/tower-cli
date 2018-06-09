# Copyright 2018, Ansible, Inc.
# John Westcott <john.westcott.iv@redhat.com>
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

import base64
import re


def base64_encode(password):
    # If the password is already encrypted just return it
    if re.match("^b64\(.*\)$", password):
        return password

    encoded_bytes = base64.b64encode(bytearray(password, 'utf-8'))
    return "b64({})".format(encoded_bytes.decode("utf-8"))


def base64_decode(encrypted_string):
    # If the password is
    m = re.match("^b64\((.*)\)$", encrypted_string)
    if not m:
        return encrypted_string

    unencoded_bytes = base64.b64decode(m.group(1))
    return unencoded_bytes.decode("utf-8")
