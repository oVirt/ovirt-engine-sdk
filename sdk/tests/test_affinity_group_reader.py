# -*- coding: utf-8 -*-

#
# Copyright (c) 2017 Red Hat, Inc.
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
    assert_true,
)
from ovirtsdk4.readers import AffinityGroupReader
from ovirtsdk4.xml import XmlReader


def make_buffer(str):
    """
    Creates an IO object to be used for writing.
    """
    return BytesIO(str.encode('utf-8'))


def test_affinity_group_reader_with_assigned_vms():
    """
    Test that reading of `vms` attribute of affinity group reads the `href`
    of the link as well as content of the `vms` element.
    """
    reader = XmlReader(make_buffer(
        '<affinity_group>'
        '<link href="/ovirt-engine/api/clusters/123/affinitygroups/456/vms" rel="vms"/>'
        '<vms><vm id="123"/></vms>'
        '</affinity_group>'
    ))
    result = AffinityGroupReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.AffinityGroup))
    assert_true(len(result.vms) > 0)
    assert_equals(
        result.vms.href,
        '/ovirt-engine/api/clusters/123/affinitygroups/456/vms'
    )
    assert_equals(result.vms[0].id, '123')


def test_affinity_group_reader_with_assigned_vms_no_order():
    """
    Test that reading of `vms` attribute of affinity group reads the `href`
    of the link as well as content of the `vms` element. Test it's
    correctly processed when link is provided after 'vms' element.
    """
    reader = XmlReader(make_buffer(
        '<affinity_group>'
        '<vms><vm id="123"/></vms>'
        '<link href="/ovirt-engine/api/clusters/123/affinitygroups/456/vms" rel="vms"/>'
        '</affinity_group>'
    ))
    result = AffinityGroupReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.AffinityGroup))
    assert_true(len(result.vms) > 0)
    assert_equals(
        result.vms.href,
        '/ovirt-engine/api/clusters/123/affinitygroups/456/vms'
    )
    assert_equals(result.vms[0].id, '123')
