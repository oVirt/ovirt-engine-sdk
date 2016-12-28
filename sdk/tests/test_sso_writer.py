# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import ovirtsdk4.types as types

from io import BytesIO
from nose.tools import (
    assert_equals,
)
from ovirtsdk4.writers import SsoWriter
from ovirtsdk4.xml import XmlWriter


def make_buffer():
    """
    Creates an IO object to be used for writing.
    """
    return BytesIO()


def decode_buffer(io_buffer):
    """
    Extracts the text stored in the given bytes buffer and generates an
    Unicode string.
    """
    return io_buffer.getvalue().decode('utf-8')


def test_sso_method_id_is_attribute():
    """
    Test that writing an SSL object with one method writes the method
    identifier as the 'id' attribute.
    """
    sso = types.Sso(
        methods=[
            types.Method(
                id=types.SsoMethod.GUEST_AGENT
            )
        ]
    )
    buf = make_buffer()
    writer = XmlWriter(buf, indent=True)
    SsoWriter.write_one(sso, writer)
    writer.flush()
    assert_equals(
        decode_buffer(buf),
        '<sso>\n' +
        '  <methods>\n' +
        '    <method id="guest_agent"/>\n' +
        '  </methods>\n' +
        '</sso>\n'
    )
