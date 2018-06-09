# -*- coding: utf-8 -*-
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


from tower_cli.utils.password import base64_encode, base64_decode

from tests.compat import unittest


class PasswordTests(unittest.TestCase):
    """A set of tests to establish that the encode/decode methods work
    """

    def test_encoding_unencoded(self):
        """Test encoding an unencoded string"""
        self.assertEqual(base64_encode('test'), 'b64(dGVzdA==)')

    def test_decoding_encoded(self):
        "Test decoding an encoded string"""
        self.assertEqual(base64_decode('b64(dGVzdA==)'), 'test')

    def test_encoding_encoded(self):
        """Test encoding an encoded string"""
        self.assertEqual(base64_encode('b64(dGVzdA==)'), 'b64(dGVzdA==)')

    def test_decoding_unencoded(self):
        "Test decoding an unencoded string"""
        self.assertEqual(base64_decode('test'), 'test')
