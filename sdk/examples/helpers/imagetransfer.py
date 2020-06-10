#
# Copyright (c) 2020 Red Hat, Inc.
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
"""
Image transfer helpers
"""

import logging

log = logging.getLogger("helpers")


def find_host(connection, sd_name):
    """
    Check if we can preform a transfer using the local host and return a host
    instance. Return None if we cannot use this host.

    Using the local host for an image transfer allows optimizing the connection
    using unix socket. This speeds up the transfer significantly and minimizes
    the network bandwidth.

    However using the local host is possible only if:
    - The local host is a oVirt host
    - The host is Up
    - The host is in the same DC of the storage domain

    Consider this setup:

        laptop1

        dc1
            host1 (down)
            host2 (up)
            sd1
                disk1

        dc2
            host3 (up)
            sd2
                disk2

    - If we run on laptop1 we cannot use the local host for any transfer.
    - If we run on host1, we cannot use the local host for any transfer.
    - If we run on host2, we can use use host2 for transferring disk1.
    - If we run on host3, we can use host3 for transferring disk2.

    Args:
        connection (ovirtsdk4.Connection): Connection instance
        sd_name (str): Storage domain name

    Returns:
        ovirtsdk4.types.Host
    """

    # Try to read this host hardware id.

    try:
        with open("/etc/vdsm/vdsm.id") as f:
            vdsm_id = f.readline().strip()
    except FileNotFoundError:
        log.debug("Not running on oVirt host, using any host")
        return None
    except OSError as e:
        # Unexpected error when running on ovirt host. Since choosing a host is
        # an optimization, log and continue.
        log.warning("Cannot read /etc/vdsm/vdsm.id, using any host: %s", e)
        return None

    log.debug("Found host hardware id: %s", vdsm_id)

    # Find the data center by storage domain name.

    system_service = connection.system_service()
    data_centers = system_service.data_centers_service().list(
        search='storage.name=%s' % sd_name,
        case_sensitive=True,
    )
    if len(data_centers) == 0:
        raise RuntimeError(
            "Storage domain {} is not attached to a DC"
            .format(sd_name))

    data_center = data_centers[0]
    log.debug("Found data center: %s", data_center.name)

    # Validate that this host is up and in data center.

    hosts_service = system_service.hosts_service()
    hosts = hosts_service.list(
        search="hw_id={} and datacenter={} and status=Up".format(
            vdsm_id, data_center.name),
        case_sensitive=True,
    )
    if len(hosts) == 0:
        log.debug(
            "Cannot use host with hardware id %s, host is not up, or does "
            "not belong to data center %s",
            vdsm_id, data_center.name)
        return None

    host = hosts[0]
    log.debug("Using host id %s", host.id)

    return host
