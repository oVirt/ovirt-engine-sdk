
#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


########################################
############ GENERATED CODE ############
########################################

'''Generated at: 2014-08-12 09:31:39.000729'''

import types
import urlparse

from ovirtsdk.infrastructure.errors import UnsecuredConnectionAttemptError
from ovirtsdk.infrastructure.connectionspool import ConnectionsPool
from ovirtsdk.infrastructure.errors import DisconnectedError
from ovirtsdk.infrastructure.errors import ImmutableError
from ovirtsdk.infrastructure.context import context
from ovirtsdk.infrastructure.proxy import Proxy
from ovirtsdk.infrastructure.cache import Mode

from ovirtsdk.infrastructure.brokers import Bookmarks
from ovirtsdk.infrastructure.brokers import Capabilities
from ovirtsdk.infrastructure.brokers import Clusters
from ovirtsdk.infrastructure.brokers import DataCenters
from ovirtsdk.infrastructure.brokers import Disks
from ovirtsdk.infrastructure.brokers import Domains
from ovirtsdk.infrastructure.brokers import Events
from ovirtsdk.infrastructure.brokers import Groups
from ovirtsdk.infrastructure.brokers import Hosts
from ovirtsdk.infrastructure.brokers import InstanceTypes
from ovirtsdk.infrastructure.brokers import Jobs
from ovirtsdk.infrastructure.brokers import Networks
from ovirtsdk.infrastructure.brokers import Permissions
from ovirtsdk.infrastructure.brokers import Roles
from ovirtsdk.infrastructure.brokers import SchedulingPolicies
from ovirtsdk.infrastructure.brokers import SchedulingPolicyUnits
from ovirtsdk.infrastructure.brokers import StorageConnections
from ovirtsdk.infrastructure.brokers import StorageDomains
from ovirtsdk.infrastructure.brokers import Tags
from ovirtsdk.infrastructure.brokers import Templates
from ovirtsdk.infrastructure.brokers import Users
from ovirtsdk.infrastructure.brokers import VMs
from ovirtsdk.infrastructure.brokers import VmPools
from ovirtsdk.infrastructure.brokers import VnicProfiles


class API(object):
    def __init__(self, url, username, password, key_file=None, cert_file=None,
                 ca_file=None, port=None, timeout=None, session_timeout=None, persistent_auth=True,
                 renew_session=False, insecure=False, validate_cert_chain=True, filter=False, debug=False):  # @ReservedAssignment

        '''
        @param url: server url (format "http/s://server[:port]/ovirt-engine/api")
        @param username: user (format user@domain)
        @param password: password
        [@param key_file: client PEM key_file for ssl enabled connection]
        [@param cert_file: client PEM cert_file for ssl enabled connection]
        [@param ca_file: server ca_file for ssl enabled connection]
        [@param port: port to use (if not specified in url)]
        [@param timeout: request timeout]
        [@param session_timeout: authentication session timeout in minutes (if persistent_auth is enabled)]
        [@param persistent_auth: use persistent authentication (default is True)]
        [@param renew_session: automatically renew expired authentication session (default is False)]
        [@param insecure: signals to not demand site trustworthiness for ssl enabled connection (default is False)]
        [@param validate_cert_chain: validate the server's CA certificate (default is True)]
        [@param filter: enables user-api filtering (default is False)]
        [@param debug: debug (format True|False)]

        @raise NoCertificatesError: raised when CA certificate is not provided for SSL site (can be disabled using 'insecure=True' argument).
        @raise UnsecuredConnectionAttemptError: raised when HTTP protocol is used in url against server running HTTPS.
        @raise ImmutableError: raised on sdk < 3.2 when sdk initiation attempt occurred while sdk instance already exist under the same domain.
        @raise DisconnectedError: raised when sdk usage attempt occurred after it was explicitly disconnected.
        @raise MissingParametersError: raised when get() method invoked without id or name been specified.
        @raise ConnectionError: raised when any kind of communication error occurred.
        @raise RequestError: raised when any kind of oVirt server error occurred.
        @raise FormatError: raised when server replies in non-XML format.
        '''

        # The instance id
        self.__id = id(self)

        # Implicitly disconnect and perform cleanup
        # when detected instance of the SDK proxy with
        # ref-count == 0
        if context.manager.has_key(self.__id):
            try:
                self.disconnect()
            except DisconnectedError:
                pass

        # Remove trailing slashes from the URL:
        url = url.rstrip('/')

        # For backwards compatibility we need to support URLs that don't
        # contain a path, and in that case the path should be the old /api:
        prefix = urlparse.urlparse(url).path
        if prefix == '':
            prefix = '/api'
            url = url + prefix

        # Create the connection pool:
        pool = ConnectionsPool(
            url=url,
            username=username,
            password=password,
            context=self.id,
            key_file=key_file,
            cert_file=cert_file,
            ca_file=ca_file,
            port=port,
            strict=False,
            timeout=timeout,
            insecure=insecure,
            validate_cert_chain=validate_cert_chain,
            debug=debug
        )

        # Create the proxy:
        proxy = Proxy(
            pool,
            persistent_auth,
            prefix
        )

        # Store filter to the context:
        self.set_filter(filter)

        # We need to remember if renew_session is enabled:
        self.set_renew_session(renew_session)

        # Store session_timeout to the context:
        self.__set_session_timeout(session_timeout)

        # Get entry point
        entry_point = proxy.request(
            method='GET',
            url=''
        )

        # If server returns no response for the root resource, this is sign
        # that used http protocol against SSL secured site
        if type(entry_point) == types.StringType and entry_point == '':
            raise UnsecuredConnectionAttemptError

        # Store entry point to the context
        context.manager[self.id].add(
            'entry_point',
            entry_point,
            Mode.R
        )

        # Store proxy to the context:
        context.manager[self.id].add(
            'proxy',
            proxy,
            Mode.R
        )

        # We need to remember if persistent auth is enabled:
        context.manager[self.id].add(
            'persistent_auth',
             persistent_auth,
             Mode.R,
             typ=types.BooleanType
        )

        self.bookmarks = Bookmarks(self.id)
        self.capabilities = Capabilities(self.id)
        self.clusters = Clusters(self.id)
        self.datacenters = DataCenters(self.id)
        self.disks = Disks(self.id)
        self.domains = Domains(self.id)
        self.events = Events(self.id)
        self.groups = Groups(self.id)
        self.hosts = Hosts(self.id)
        self.instancetypes = InstanceTypes(self.id)
        self.jobs = Jobs(self.id)
        self.networks = Networks(self.id)
        self.permissions = Permissions(self.id)
        self.roles = Roles(self.id)
        self.schedulingpolicies = SchedulingPolicies(self.id)
        self.schedulingpolicyunits = SchedulingPolicyUnits(self.id)
        self.storageconnections = StorageConnections(self.id)
        self.storagedomains = StorageDomains(self.id)
        self.tags = Tags(self.id)
        self.templates = Templates(self.id)
        self.users = Users(self.id)
        self.vms = VMs(self.id)
        self.vmpools = VmPools(self.id)
        self.vnicprofiles = VnicProfiles(self.id)


    @property
    def id(self):
        return self.__id

    def __setattr__(self, name, value):
        if name in ['__id', 'id']:
            raise ImmutableError(name)
        else:
            super(API, self).__setattr__(name, value)

    def disconnect(self):
        ''' terminates server connection/s '''

        proxy = context.manager[self.id].get('proxy')
        persistent_auth = context.manager[self.id].get('persistent_auth')

        # If persistent authentication is enabled then we need to
        # send a last request as a hint to the server to close the
        # session:
        if proxy:
            if persistent_auth:
                try:
                    proxy.request(
                        method='GET',
                        url='',
                        last=True
                    )
                except Exception:
                    pass
        else:
            raise DisconnectedError

        # Clear context
        context.manager.drop(self.id)

    def test(self, throw_exception=False):
        ''' test server connectivity '''

        proxy = context.manager[self.id].get('proxy')
        if proxy:
            try :
                proxy.request(
                    method='GET',
                    url=''
                )
            except Exception, e:
                if throw_exception: raise e
                return False
            return True
        raise DisconnectedError

    def set_filter(self, filter):  # @ReservedAssignment
        ''' enables user permission based filtering '''
        if filter != None:
            context.manager[self.id].add(
                             'filter',
                             filter,
                             typ=types.BooleanType
            )

    def set_renew_session(self, renew_session):
        ''' automatically renew expired authentication session '''
        if renew_session != None:
            context.manager[self.id].add(
                'renew_session',
                 renew_session,
                 Mode.RW,
                 typ=types.BooleanType
            )

    def __set_session_timeout(self, session_timeout):
        ''' set authentication session timeout '''
        if session_timeout != None:
            context.manager[self.id].add(
                             'session_timeout',
                             session_timeout,
                             typ=types.IntType
            )

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):  # @ReservedAssignment
        self.disconnect()


    def get_comment(self):
        entry_point = context.manager[self.id].get('entry_point')
        if entry_point:
            return entry_point.comment
        raise DisconnectedError


    def get_special_objects(self):
        entry_point = context.manager[self.id].get('entry_point')
        if entry_point:
            return entry_point.special_objects
        raise DisconnectedError

    def get_summary(self):
        proxy = context.manager[self.id].get('proxy')
        if proxy:
            return proxy.request(
                method='GET',
                url=''
            ).summary

        raise DisconnectedError

    def get_time(self):
        proxy = context.manager[self.id].get('proxy')
        if proxy:
            return proxy.request(
                method='GET',
                url=''
            ).time

        raise DisconnectedError


    def get_product_info(self):
        entry_point = context.manager[self.id].get('entry_point')
        if entry_point:
            return entry_point.product_info
        raise DisconnectedError

