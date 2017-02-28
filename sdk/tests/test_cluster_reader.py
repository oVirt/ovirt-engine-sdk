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
    assert_is_none,
    assert_true,
)
from ovirtsdk4.readers import ClusterReader
from ovirtsdk4.xml import XmlReader


def make_buffer(str):
    """
    Creates an IO object to be used for writing.
    """
    return BytesIO(str.encode('utf-8'))


def test_cluster_with_no_rng_sources_and_switch_type():
    """
    Test that reading the 'switch_type' enum when it appears after an
    empty list works correctly.
    """
    reader = XmlReader(make_buffer(
      '<cluster>'
        '<required_rng_sources/>'
        '<switch_type>legacy</switch_type>'
      '</cluster>'
    ))
    result = ClusterReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.Cluster))
    assert_equals(result.required_rng_sources, [])
    assert_equals(result.switch_type, types.SwitchType.LEGACY)



def test_unsupported_switch_type_dont_raise_exception():
    """
    Test when given switch type is unsupported, it don't raise exception.
    """
    reader = XmlReader(make_buffer(
        '<cluster>'
        '<switch_type>ugly</switch_type>'
        '</cluster>'
    ))
    result = ClusterReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.Cluster))
    assert_is_none(result.switch_type)
