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


from ovirtsdk4 import List
from ovirtsdk4 import types
from ovirtsdk4.reader import Reader


class ActionReader(Reader):

    def __init__(self):
        super(ActionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Action()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'activate':
                obj.activate = Reader.read_boolean(reader)
            elif tag == 'allow_partial_import':
                obj.allow_partial_import = Reader.read_boolean(reader)
            elif tag == 'async':
                obj.async_ = Reader.read_boolean(reader)
            elif tag == 'attachment':
                obj.attachment = DiskAttachmentReader.read_one(reader)
            elif tag == 'authorized_key':
                obj.authorized_key = AuthorizedKeyReader.read_one(reader)
            elif tag == 'auto_pinning_policy':
                obj.auto_pinning_policy = Reader.read_enum(types.AutoPinningPolicy, reader)
            elif tag == 'bricks':
                obj.bricks = GlusterBrickReader.read_many(reader)
            elif tag == 'certificates':
                obj.certificates = CertificateReader.read_many(reader)
            elif tag == 'check_connectivity':
                obj.check_connectivity = Reader.read_boolean(reader)
            elif tag == 'clone':
                obj.clone = Reader.read_boolean(reader)
            elif tag == 'clone_permissions':
                obj.clone_permissions = Reader.read_boolean(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'collapse_snapshots':
                obj.collapse_snapshots = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'commit_on_success':
                obj.commit_on_success = Reader.read_boolean(reader)
            elif tag == 'connection':
                obj.connection = StorageConnectionReader.read_one(reader)
            elif tag == 'connectivity_timeout':
                obj.connectivity_timeout = Reader.read_integer(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'deploy_hosted_engine':
                obj.deploy_hosted_engine = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'details':
                obj.details = GlusterVolumeProfileDetailsReader.read_one(reader)
            elif tag == 'directory':
                obj.directory = Reader.read_string(reader)
            elif tag == 'discard_snapshots':
                obj.discard_snapshots = Reader.read_boolean(reader)
            elif tag == 'discovered_targets':
                obj.discovered_targets = IscsiDetailsReader.read_many(reader)
            elif tag == 'disk':
                obj.disk = DiskReader.read_one(reader)
            elif tag == 'disk_profile':
                obj.disk_profile = DiskProfileReader.read_one(reader)
            elif tag == 'disks':
                obj.disks = DiskReader.read_many(reader)
            elif tag == 'exclusive':
                obj.exclusive = Reader.read_boolean(reader)
            elif tag == 'fault':
                obj.fault = FaultReader.read_one(reader)
            elif tag == 'fence_type':
                obj.fence_type = Reader.read_string(reader)
            elif tag == 'filename':
                obj.filename = Reader.read_string(reader)
            elif tag == 'filter':
                obj.filter = Reader.read_boolean(reader)
            elif tag == 'fix_layout':
                obj.fix_layout = Reader.read_boolean(reader)
            elif tag == 'force':
                obj.force = Reader.read_boolean(reader)
            elif tag == 'grace_period':
                obj.grace_period = GracePeriodReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'image':
                obj.image = Reader.read_string(reader)
            elif tag == 'image_transfer':
                obj.image_transfer = ImageTransferReader.read_one(reader)
            elif tag == 'import_as_template':
                obj.import_as_template = Reader.read_boolean(reader)
            elif tag == 'is_attached':
                obj.is_attached = Reader.read_boolean(reader)
            elif tag == 'iscsi':
                obj.iscsi = IscsiDetailsReader.read_one(reader)
            elif tag == 'iscsi_targets':
                obj.iscsi_targets = Reader.read_strings(reader)
            elif tag == 'job':
                obj.job = JobReader.read_one(reader)
            elif tag == 'lease':
                obj.lease = StorageDomainLeaseReader.read_one(reader)
            elif tag == 'logical_units':
                obj.logical_units = LogicalUnitReader.read_many(reader)
            elif tag == 'maintenance_after_restart':
                obj.maintenance_after_restart = Reader.read_boolean(reader)
            elif tag == 'maintenance_enabled':
                obj.maintenance_enabled = Reader.read_boolean(reader)
            elif tag == 'migrate_vms_in_affinity_closure':
                obj.migrate_vms_in_affinity_closure = Reader.read_boolean(reader)
            elif tag == 'modified_bonds':
                obj.modified_bonds = HostNicReader.read_many(reader)
            elif tag == 'modified_labels':
                obj.modified_labels = NetworkLabelReader.read_many(reader)
            elif tag == 'modified_network_attachments':
                obj.modified_network_attachments = NetworkAttachmentReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'optimize_cpu_settings':
                obj.optimize_cpu_settings = Reader.read_boolean(reader)
            elif tag == 'option':
                obj.option = OptionReader.read_one(reader)
            elif tag == 'pause':
                obj.pause = Reader.read_boolean(reader)
            elif tag == 'permission':
                obj.permission = PermissionReader.read_one(reader)
            elif tag == 'power_management':
                obj.power_management = PowerManagementReader.read_one(reader)
            elif tag == 'proxy_ticket':
                obj.proxy_ticket = ProxyTicketReader.read_one(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'reason':
                obj.reason = Reader.read_string(reader)
            elif tag == 'reassign_bad_macs':
                obj.reassign_bad_macs = Reader.read_boolean(reader)
            elif tag == 'reboot':
                obj.reboot = Reader.read_boolean(reader)
            elif tag == 'registration_configuration':
                obj.registration_configuration = RegistrationConfigurationReader.read_one(reader)
            elif tag == 'remote_viewer_connection_file':
                obj.remote_viewer_connection_file = Reader.read_string(reader)
            elif tag == 'removed_bonds':
                obj.removed_bonds = HostNicReader.read_many(reader)
            elif tag == 'removed_labels':
                obj.removed_labels = NetworkLabelReader.read_many(reader)
            elif tag == 'removed_network_attachments':
                obj.removed_network_attachments = NetworkAttachmentReader.read_many(reader)
            elif tag == 'resolution_type':
                obj.resolution_type = Reader.read_string(reader)
            elif tag == 'restore_memory':
                obj.restore_memory = Reader.read_boolean(reader)
            elif tag == 'root_password':
                obj.root_password = Reader.read_string(reader)
            elif tag == 'seal':
                obj.seal = Reader.read_boolean(reader)
            elif tag == 'snapshot':
                obj.snapshot = SnapshotReader.read_one(reader)
            elif tag == 'source_host':
                obj.source_host = HostReader.read_one(reader)
            elif tag == 'ssh':
                obj.ssh = SshReader.read_one(reader)
            elif tag == 'status':
                obj.status = Reader.read_string(reader)
            elif tag == 'stop_gluster_service':
                obj.stop_gluster_service = Reader.read_boolean(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'storage_domains':
                obj.storage_domains = StorageDomainReader.read_many(reader)
            elif tag == 'succeeded':
                obj.succeeded = Reader.read_boolean(reader)
            elif tag == 'synchronized_network_attachments':
                obj.synchronized_network_attachments = NetworkAttachmentReader.read_many(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'ticket':
                obj.ticket = TicketReader.read_one(reader)
            elif tag == 'timeout':
                obj.timeout = Reader.read_integer(reader)
            elif tag == 'undeploy_hosted_engine':
                obj.undeploy_hosted_engine = Reader.read_boolean(reader)
            elif tag == 'upgrade_action':
                obj.upgrade_action = Reader.read_enum(types.ClusterUpgradeAction, reader)
            elif tag == 'use_cloud_init':
                obj.use_cloud_init = Reader.read_boolean(reader)
            elif tag == 'use_ignition':
                obj.use_ignition = Reader.read_boolean(reader)
            elif tag == 'use_initialization':
                obj.use_initialization = Reader.read_boolean(reader)
            elif tag == 'use_sysprep':
                obj.use_sysprep = Reader.read_boolean(reader)
            elif tag == 'virtual_functions_configuration':
                obj.virtual_functions_configuration = HostNicVirtualFunctionsConfigurationReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vnic_profile_mappings':
                obj.vnic_profile_mappings = VnicProfileMappingReader.read_many(reader)
            elif tag == 'volatile':
                obj.volatile = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            ActionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ActionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class AffinityGroupReader(Reader):

    def __init__(self):
        super(AffinityGroupReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.AffinityGroup()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'broken':
                obj.broken = Reader.read_boolean(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'enforcing':
                obj.enforcing = Reader.read_boolean(reader)
            elif tag == 'host_labels':
                obj.host_labels = AffinityLabelReader.read_many(reader)
            elif tag == 'hosts':
                obj.hosts = HostReader.read_many(reader)
            elif tag == 'hosts_rule':
                obj.hosts_rule = AffinityRuleReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'positive':
                obj.positive = Reader.read_boolean(reader)
            elif tag == 'priority':
                obj.priority = Reader.read_decimal(reader)
            elif tag == 'vm_labels':
                obj.vm_labels = AffinityLabelReader.read_many(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'vms_rule':
                obj.vms_rule = AffinityRuleReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            AffinityGroupReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(AffinityGroupReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "hostlabels":
                if obj.host_labels is not None:
                    obj.host_labels.href = href
                else:
                    obj.host_labels = List(href)
            elif rel == "hosts":
                if obj.hosts is not None:
                    obj.hosts.href = href
                else:
                    obj.hosts = List(href)
            elif rel == "vmlabels":
                if obj.vm_labels is not None:
                    obj.vm_labels.href = href
                else:
                    obj.vm_labels = List(href)
            elif rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class AffinityLabelReader(Reader):

    def __init__(self):
        super(AffinityLabelReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.AffinityLabel()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'has_implicit_affinity_group':
                obj.has_implicit_affinity_group = Reader.read_boolean(reader)
            elif tag == 'hosts':
                obj.hosts = HostReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'read_only':
                obj.read_only = Reader.read_boolean(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            AffinityLabelReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(AffinityLabelReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "hosts":
                if obj.hosts is not None:
                    obj.hosts.href = href
                else:
                    obj.hosts = List(href)
            elif rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class AffinityRuleReader(Reader):

    def __init__(self):
        super(AffinityRuleReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.AffinityRule()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            elif tag == 'enforcing':
                obj.enforcing = Reader.read_boolean(reader)
            elif tag == 'positive':
                obj.positive = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            AffinityRuleReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(AffinityRuleReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class AgentReader(Reader):

    def __init__(self):
        super(AgentReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Agent()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'concurrent':
                obj.concurrent = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'encrypt_options':
                obj.encrypt_options = Reader.read_boolean(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'options':
                obj.options = OptionReader.read_many(reader)
            elif tag == 'order':
                obj.order = Reader.read_integer(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'type':
                obj.type = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            AgentReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(AgentReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class AgentConfigurationReader(Reader):

    def __init__(self):
        super(AgentConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.AgentConfiguration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'broker_type':
                obj.broker_type = Reader.read_enum(types.MessageBrokerType, reader)
            elif tag == 'network_mappings':
                obj.network_mappings = Reader.read_string(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            AgentConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(AgentConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ApiReader(Reader):

    def __init__(self):
        super(ApiReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Api()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'authenticated_user':
                obj.authenticated_user = UserReader.read_one(reader)
            elif tag == 'effective_user':
                obj.effective_user = UserReader.read_one(reader)
            elif tag == 'product_info':
                obj.product_info = ProductInfoReader.read_one(reader)
            elif tag == 'special_objects':
                obj.special_objects = SpecialObjectsReader.read_one(reader)
            elif tag == 'summary':
                obj.summary = ApiSummaryReader.read_one(reader)
            elif tag == 'time':
                obj.time = Reader.read_date(reader)
            else:
                reader.next_element()
        for link in links:
            ApiReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ApiReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ApiSummaryReader(Reader):

    def __init__(self):
        super(ApiSummaryReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ApiSummary()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'hosts':
                obj.hosts = ApiSummaryItemReader.read_one(reader)
            elif tag == 'storage_domains':
                obj.storage_domains = ApiSummaryItemReader.read_one(reader)
            elif tag == 'users':
                obj.users = ApiSummaryItemReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = ApiSummaryItemReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            ApiSummaryReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ApiSummaryReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ApiSummaryItemReader(Reader):

    def __init__(self):
        super(ApiSummaryItemReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ApiSummaryItem()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active':
                obj.active = Reader.read_integer(reader)
            elif tag == 'total':
                obj.total = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            ApiSummaryItemReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ApiSummaryItemReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ApplicationReader(Reader):

    def __init__(self):
        super(ApplicationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Application()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            ApplicationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ApplicationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class AuthorizedKeyReader(Reader):

    def __init__(self):
        super(AuthorizedKeyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.AuthorizedKey()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'key':
                obj.key = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            AuthorizedKeyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(AuthorizedKeyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class BackupReader(Reader):

    def __init__(self):
        super(BackupReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Backup()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'creation_date':
                obj.creation_date = Reader.read_date(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disks':
                obj.disks = DiskReader.read_many(reader)
            elif tag == 'from_checkpoint_id':
                obj.from_checkpoint_id = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'modification_date':
                obj.modification_date = Reader.read_date(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'phase':
                obj.phase = Reader.read_enum(types.BackupPhase, reader)
            elif tag == 'to_checkpoint_id':
                obj.to_checkpoint_id = Reader.read_string(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            BackupReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BackupReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "disks":
                if obj.disks is not None:
                    obj.disks.href = href
                else:
                    obj.disks = List(href)


class BalanceReader(Reader):

    def __init__(self):
        super(BalanceReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Balance()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'scheduling_policy':
                obj.scheduling_policy = SchedulingPolicyReader.read_one(reader)
            elif tag == 'scheduling_policy_unit':
                obj.scheduling_policy_unit = SchedulingPolicyUnitReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            BalanceReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BalanceReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class BiosReader(Reader):

    def __init__(self):
        super(BiosReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Bios()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'boot_menu':
                obj.boot_menu = BootMenuReader.read_one(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.BiosType, reader)
            else:
                reader.next_element()
        for link in links:
            BiosReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BiosReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class BlockStatisticReader(Reader):

    def __init__(self):
        super(BlockStatisticReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.BlockStatistic()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            BlockStatisticReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BlockStatisticReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class BondingReader(Reader):

    def __init__(self):
        super(BondingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Bonding()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active_slave':
                obj.active_slave = HostNicReader.read_one(reader)
            elif tag == 'ad_partner_mac':
                obj.ad_partner_mac = MacReader.read_one(reader)
            elif tag == 'options':
                obj.options = OptionReader.read_many(reader)
            elif tag == 'slaves':
                obj.slaves = HostNicReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            BondingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BondingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class BookmarkReader(Reader):

    def __init__(self):
        super(BookmarkReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Bookmark()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            BookmarkReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BookmarkReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class BootReader(Reader):

    def __init__(self):
        super(BootReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Boot()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'devices':
                obj.devices = Reader.read_enums(types.BootDevice, reader)
            else:
                reader.next_element()
        for link in links:
            BootReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BootReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class BootMenuReader(Reader):

    def __init__(self):
        super(BootMenuReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.BootMenu()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            BootMenuReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BootMenuReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class BrickProfileDetailReader(Reader):

    def __init__(self):
        super(BrickProfileDetailReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.BrickProfileDetail()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'brick':
                obj.brick = GlusterBrickReader.read_one(reader)
            elif tag == 'profile_details':
                obj.profile_details = ProfileDetailReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            BrickProfileDetailReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(BrickProfileDetailReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class CdromReader(Reader):

    def __init__(self):
        super(CdromReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Cdrom()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'file':
                obj.file = FileReader.read_one(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            CdromReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CdromReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class CertificateReader(Reader):

    def __init__(self):
        super(CertificateReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Certificate()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'content':
                obj.content = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'organization':
                obj.organization = Reader.read_string(reader)
            elif tag == 'subject':
                obj.subject = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            CertificateReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CertificateReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class CheckpointReader(Reader):

    def __init__(self):
        super(CheckpointReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Checkpoint()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'creation_date':
                obj.creation_date = Reader.read_date(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disks':
                obj.disks = DiskReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'parent_id':
                obj.parent_id = Reader.read_string(reader)
            elif tag == 'state':
                obj.state = Reader.read_enum(types.CheckpointState, reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            CheckpointReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CheckpointReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "disks":
                if obj.disks is not None:
                    obj.disks.href = href
                else:
                    obj.disks = List(href)


class CloudInitReader(Reader):

    def __init__(self):
        super(CloudInitReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.CloudInit()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'authorized_keys':
                obj.authorized_keys = AuthorizedKeyReader.read_many(reader)
            elif tag == 'files':
                obj.files = FileReader.read_many(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'network_configuration':
                obj.network_configuration = NetworkConfigurationReader.read_one(reader)
            elif tag == 'regenerate_ssh_keys':
                obj.regenerate_ssh_keys = Reader.read_boolean(reader)
            elif tag == 'timezone':
                obj.timezone = Reader.read_string(reader)
            elif tag == 'users':
                obj.users = UserReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            CloudInitReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CloudInitReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ClusterReader(Reader):

    def __init__(self):
        super(ClusterReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Cluster()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'affinity_groups':
                obj.affinity_groups = AffinityGroupReader.read_many(reader)
            elif tag == 'ballooning_enabled':
                obj.ballooning_enabled = Reader.read_boolean(reader)
            elif tag == 'bios_type':
                obj.bios_type = Reader.read_enum(types.BiosType, reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'cpu_profiles':
                obj.cpu_profiles = CpuProfileReader.read_many(reader)
            elif tag == 'custom_scheduling_policy_properties':
                obj.custom_scheduling_policy_properties = PropertyReader.read_many(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'display':
                obj.display = DisplayReader.read_one(reader)
            elif tag == 'enabled_features':
                obj.enabled_features = ClusterFeatureReader.read_many(reader)
            elif tag == 'error_handling':
                obj.error_handling = ErrorHandlingReader.read_one(reader)
            elif tag == 'external_network_providers':
                obj.external_network_providers = ExternalProviderReader.read_many(reader)
            elif tag == 'fencing_policy':
                obj.fencing_policy = FencingPolicyReader.read_one(reader)
            elif tag == 'fips_mode':
                obj.fips_mode = Reader.read_enum(types.FipsMode, reader)
            elif tag == 'firewall_type':
                obj.firewall_type = Reader.read_enum(types.FirewallType, reader)
            elif tag == 'gluster_hooks':
                obj.gluster_hooks = GlusterHookReader.read_many(reader)
            elif tag == 'gluster_service':
                obj.gluster_service = Reader.read_boolean(reader)
            elif tag == 'gluster_tuned_profile':
                obj.gluster_tuned_profile = Reader.read_string(reader)
            elif tag == 'gluster_volumes':
                obj.gluster_volumes = GlusterVolumeReader.read_many(reader)
            elif tag == 'ha_reservation':
                obj.ha_reservation = Reader.read_boolean(reader)
            elif tag == 'ksm':
                obj.ksm = KsmReader.read_one(reader)
            elif tag == 'log_max_memory_used_threshold':
                obj.log_max_memory_used_threshold = Reader.read_integer(reader)
            elif tag == 'log_max_memory_used_threshold_type':
                obj.log_max_memory_used_threshold_type = Reader.read_enum(types.LogMaxMemoryUsedThresholdType, reader)
            elif tag == 'mac_pool':
                obj.mac_pool = MacPoolReader.read_one(reader)
            elif tag == 'maintenance_reason_required':
                obj.maintenance_reason_required = Reader.read_boolean(reader)
            elif tag == 'management_network':
                obj.management_network = NetworkReader.read_one(reader)
            elif tag == 'memory_policy':
                obj.memory_policy = MemoryPolicyReader.read_one(reader)
            elif tag == 'migration':
                obj.migration = MigrationOptionsReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'network_filters':
                obj.network_filters = NetworkFilterReader.read_many(reader)
            elif tag == 'networks':
                obj.networks = NetworkReader.read_many(reader)
            elif tag == 'optional_reason':
                obj.optional_reason = Reader.read_boolean(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'required_rng_sources':
                obj.required_rng_sources = Reader.read_enums(types.RngSource, reader)
            elif tag == 'scheduling_policy':
                obj.scheduling_policy = SchedulingPolicyReader.read_one(reader)
            elif tag == 'serial_number':
                obj.serial_number = SerialNumberReader.read_one(reader)
            elif tag == 'supported_versions':
                obj.supported_versions = VersionReader.read_many(reader)
            elif tag == 'switch_type':
                obj.switch_type = Reader.read_enum(types.SwitchType, reader)
            elif tag == 'threads_as_cores':
                obj.threads_as_cores = Reader.read_boolean(reader)
            elif tag == 'trusted_service':
                obj.trusted_service = Reader.read_boolean(reader)
            elif tag == 'tunnel_migration':
                obj.tunnel_migration = Reader.read_boolean(reader)
            elif tag == 'version':
                obj.version = VersionReader.read_one(reader)
            elif tag == 'virt_service':
                obj.virt_service = Reader.read_boolean(reader)
            elif tag == 'vnc_encryption':
                obj.vnc_encryption = Reader.read_boolean(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            ClusterReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ClusterReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "affinitygroups":
                if obj.affinity_groups is not None:
                    obj.affinity_groups.href = href
                else:
                    obj.affinity_groups = List(href)
            elif rel == "cpuprofiles":
                if obj.cpu_profiles is not None:
                    obj.cpu_profiles.href = href
                else:
                    obj.cpu_profiles = List(href)
            elif rel == "enabledfeatures":
                if obj.enabled_features is not None:
                    obj.enabled_features.href = href
                else:
                    obj.enabled_features = List(href)
            elif rel == "externalnetworkproviders":
                if obj.external_network_providers is not None:
                    obj.external_network_providers.href = href
                else:
                    obj.external_network_providers = List(href)
            elif rel == "glusterhooks":
                if obj.gluster_hooks is not None:
                    obj.gluster_hooks.href = href
                else:
                    obj.gluster_hooks = List(href)
            elif rel == "glustervolumes":
                if obj.gluster_volumes is not None:
                    obj.gluster_volumes.href = href
                else:
                    obj.gluster_volumes = List(href)
            elif rel == "networkfilters":
                if obj.network_filters is not None:
                    obj.network_filters.href = href
                else:
                    obj.network_filters = List(href)
            elif rel == "networks":
                if obj.networks is not None:
                    obj.networks.href = href
                else:
                    obj.networks = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)


class ClusterFeatureReader(Reader):

    def __init__(self):
        super(ClusterFeatureReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ClusterFeature()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster_level':
                obj.cluster_level = ClusterLevelReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ClusterFeatureReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ClusterFeatureReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ClusterLevelReader(Reader):

    def __init__(self):
        super(ClusterLevelReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ClusterLevel()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster_features':
                obj.cluster_features = ClusterFeatureReader.read_many(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'cpu_types':
                obj.cpu_types = CpuTypeReader.read_many(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'permits':
                obj.permits = PermitReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            ClusterLevelReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ClusterLevelReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "clusterfeatures":
                if obj.cluster_features is not None:
                    obj.cluster_features.href = href
                else:
                    obj.cluster_features = List(href)


class ConfigurationReader(Reader):

    def __init__(self):
        super(ConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Configuration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'data':
                obj.data = Reader.read_string(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.ConfigurationType, reader)
            else:
                reader.next_element()
        for link in links:
            ConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ConsoleReader(Reader):

    def __init__(self):
        super(ConsoleReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Console()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            ConsoleReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ConsoleReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class CoreReader(Reader):

    def __init__(self):
        super(CoreReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Core()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'index':
                obj.index = Reader.read_integer(reader)
            elif tag == 'socket':
                obj.socket = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            CoreReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CoreReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class CpuReader(Reader):

    def __init__(self):
        super(CpuReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Cpu()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'architecture':
                obj.architecture = Reader.read_enum(types.Architecture, reader)
            elif tag == 'cores':
                obj.cores = CoreReader.read_many(reader)
            elif tag == 'cpu_tune':
                obj.cpu_tune = CpuTuneReader.read_one(reader)
            elif tag == 'level':
                obj.level = Reader.read_integer(reader)
            elif tag == 'mode':
                obj.mode = Reader.read_enum(types.CpuMode, reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'speed':
                obj.speed = Reader.read_decimal(reader)
            elif tag == 'topology':
                obj.topology = CpuTopologyReader.read_one(reader)
            elif tag == 'type':
                obj.type = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            CpuReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CpuReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class CpuProfileReader(Reader):

    def __init__(self):
        super(CpuProfileReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.CpuProfile()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'qos':
                obj.qos = QosReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            CpuProfileReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CpuProfileReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)


class CpuTopologyReader(Reader):

    def __init__(self):
        super(CpuTopologyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.CpuTopology()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cores':
                obj.cores = Reader.read_integer(reader)
            elif tag == 'sockets':
                obj.sockets = Reader.read_integer(reader)
            elif tag == 'threads':
                obj.threads = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            CpuTopologyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CpuTopologyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class CpuTuneReader(Reader):

    def __init__(self):
        super(CpuTuneReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.CpuTune()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'vcpu_pins':
                obj.vcpu_pins = VcpuPinReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            CpuTuneReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CpuTuneReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class CpuTypeReader(Reader):

    def __init__(self):
        super(CpuTypeReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.CpuType()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'architecture':
                obj.architecture = Reader.read_enum(types.Architecture, reader)
            elif tag == 'level':
                obj.level = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            CpuTypeReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CpuTypeReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class CustomPropertyReader(Reader):

    def __init__(self):
        super(CustomPropertyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.CustomProperty()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'regexp':
                obj.regexp = Reader.read_string(reader)
            elif tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            CustomPropertyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(CustomPropertyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class DataCenterReader(Reader):

    def __init__(self):
        super(DataCenterReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.DataCenter()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'clusters':
                obj.clusters = ClusterReader.read_many(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'iscsi_bonds':
                obj.iscsi_bonds = IscsiBondReader.read_many(reader)
            elif tag == 'local':
                obj.local = Reader.read_boolean(reader)
            elif tag == 'mac_pool':
                obj.mac_pool = MacPoolReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'networks':
                obj.networks = NetworkReader.read_many(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'qoss':
                obj.qoss = QosReader.read_many(reader)
            elif tag == 'quota_mode':
                obj.quota_mode = Reader.read_enum(types.QuotaModeType, reader)
            elif tag == 'quotas':
                obj.quotas = QuotaReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.DataCenterStatus, reader)
            elif tag == 'storage_domains':
                obj.storage_domains = StorageDomainReader.read_many(reader)
            elif tag == 'storage_format':
                obj.storage_format = Reader.read_enum(types.StorageFormat, reader)
            elif tag == 'supported_versions':
                obj.supported_versions = VersionReader.read_many(reader)
            elif tag == 'version':
                obj.version = VersionReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            DataCenterReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DataCenterReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "clusters":
                if obj.clusters is not None:
                    obj.clusters.href = href
                else:
                    obj.clusters = List(href)
            elif rel == "iscsibonds":
                if obj.iscsi_bonds is not None:
                    obj.iscsi_bonds.href = href
                else:
                    obj.iscsi_bonds = List(href)
            elif rel == "networks":
                if obj.networks is not None:
                    obj.networks.href = href
                else:
                    obj.networks = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "qoss":
                if obj.qoss is not None:
                    obj.qoss.href = href
                else:
                    obj.qoss = List(href)
            elif rel == "quotas":
                if obj.quotas is not None:
                    obj.quotas.href = href
                else:
                    obj.quotas = List(href)
            elif rel == "storagedomains":
                if obj.storage_domains is not None:
                    obj.storage_domains.href = href
                else:
                    obj.storage_domains = List(href)


class DeviceReader(Reader):

    def __init__(self):
        super(DeviceReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Device()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            DeviceReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DeviceReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class DiskReader(Reader):

    def __init__(self):
        super(DiskReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Disk()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active':
                obj.active = Reader.read_boolean(reader)
            elif tag == 'actual_size':
                obj.actual_size = Reader.read_integer(reader)
            elif tag == 'alias':
                obj.alias = Reader.read_string(reader)
            elif tag == 'backup':
                obj.backup = Reader.read_enum(types.DiskBackup, reader)
            elif tag == 'backup_mode':
                obj.backup_mode = Reader.read_enum(types.DiskBackupMode, reader)
            elif tag == 'bootable':
                obj.bootable = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'content_type':
                obj.content_type = Reader.read_enum(types.DiskContentType, reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk_profile':
                obj.disk_profile = DiskProfileReader.read_one(reader)
            elif tag == 'disk_snapshots':
                obj.disk_snapshots = DiskSnapshotReader.read_many(reader)
            elif tag == 'external_disk':
                obj.external_disk = Reader.read_string(reader)
            elif tag == 'format':
                obj.format = Reader.read_enum(types.DiskFormat, reader)
            elif tag == 'image_id':
                obj.image_id = Reader.read_string(reader)
            elif tag == 'initial_size':
                obj.initial_size = Reader.read_integer(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'interface':
                obj.interface = Reader.read_enum(types.DiskInterface, reader)
            elif tag == 'logical_name':
                obj.logical_name = Reader.read_string(reader)
            elif tag == 'lun_storage':
                obj.lun_storage = HostStorageReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'openstack_volume_type':
                obj.openstack_volume_type = OpenStackVolumeTypeReader.read_one(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'propagate_errors':
                obj.propagate_errors = Reader.read_boolean(reader)
            elif tag == 'provisioned_size':
                obj.provisioned_size = Reader.read_integer(reader)
            elif tag == 'qcow_version':
                obj.qcow_version = Reader.read_enum(types.QcowVersion, reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'read_only':
                obj.read_only = Reader.read_boolean(reader)
            elif tag == 'sgio':
                obj.sgio = Reader.read_enum(types.ScsiGenericIO, reader)
            elif tag == 'shareable':
                obj.shareable = Reader.read_boolean(reader)
            elif tag == 'snapshot':
                obj.snapshot = SnapshotReader.read_one(reader)
            elif tag == 'sparse':
                obj.sparse = Reader.read_boolean(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.DiskStatus, reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'storage_domains':
                obj.storage_domains = StorageDomainReader.read_many(reader)
            elif tag == 'storage_type':
                obj.storage_type = Reader.read_enum(types.DiskStorageType, reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'total_size':
                obj.total_size = Reader.read_integer(reader)
            elif tag == 'uses_scsi_reservation':
                obj.uses_scsi_reservation = Reader.read_boolean(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'wipe_after_delete':
                obj.wipe_after_delete = Reader.read_boolean(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            DiskReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DiskReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "disksnapshots":
                if obj.disk_snapshots is not None:
                    obj.disk_snapshots.href = href
                else:
                    obj.disk_snapshots = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)
            elif rel == "storagedomains":
                if obj.storage_domains is not None:
                    obj.storage_domains.href = href
                else:
                    obj.storage_domains = List(href)
            elif rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class DiskAttachmentReader(Reader):

    def __init__(self):
        super(DiskAttachmentReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.DiskAttachment()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active':
                obj.active = Reader.read_boolean(reader)
            elif tag == 'bootable':
                obj.bootable = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk':
                obj.disk = DiskReader.read_one(reader)
            elif tag == 'interface':
                obj.interface = Reader.read_enum(types.DiskInterface, reader)
            elif tag == 'logical_name':
                obj.logical_name = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'pass_discard':
                obj.pass_discard = Reader.read_boolean(reader)
            elif tag == 'read_only':
                obj.read_only = Reader.read_boolean(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'uses_scsi_reservation':
                obj.uses_scsi_reservation = Reader.read_boolean(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            DiskAttachmentReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DiskAttachmentReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class DiskProfileReader(Reader):

    def __init__(self):
        super(DiskProfileReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.DiskProfile()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'qos':
                obj.qos = QosReader.read_one(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            DiskProfileReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DiskProfileReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)


class DiskSnapshotReader(Reader):

    def __init__(self):
        super(DiskSnapshotReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.DiskSnapshot()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active':
                obj.active = Reader.read_boolean(reader)
            elif tag == 'actual_size':
                obj.actual_size = Reader.read_integer(reader)
            elif tag == 'alias':
                obj.alias = Reader.read_string(reader)
            elif tag == 'backup':
                obj.backup = Reader.read_enum(types.DiskBackup, reader)
            elif tag == 'backup_mode':
                obj.backup_mode = Reader.read_enum(types.DiskBackupMode, reader)
            elif tag == 'bootable':
                obj.bootable = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'content_type':
                obj.content_type = Reader.read_enum(types.DiskContentType, reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk':
                obj.disk = DiskReader.read_one(reader)
            elif tag == 'disk_profile':
                obj.disk_profile = DiskProfileReader.read_one(reader)
            elif tag == 'disk_snapshots':
                obj.disk_snapshots = DiskSnapshotReader.read_many(reader)
            elif tag == 'external_disk':
                obj.external_disk = Reader.read_string(reader)
            elif tag == 'format':
                obj.format = Reader.read_enum(types.DiskFormat, reader)
            elif tag == 'image_id':
                obj.image_id = Reader.read_string(reader)
            elif tag == 'initial_size':
                obj.initial_size = Reader.read_integer(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'interface':
                obj.interface = Reader.read_enum(types.DiskInterface, reader)
            elif tag == 'logical_name':
                obj.logical_name = Reader.read_string(reader)
            elif tag == 'lun_storage':
                obj.lun_storage = HostStorageReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'openstack_volume_type':
                obj.openstack_volume_type = OpenStackVolumeTypeReader.read_one(reader)
            elif tag == 'parent':
                obj.parent = DiskSnapshotReader.read_one(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'propagate_errors':
                obj.propagate_errors = Reader.read_boolean(reader)
            elif tag == 'provisioned_size':
                obj.provisioned_size = Reader.read_integer(reader)
            elif tag == 'qcow_version':
                obj.qcow_version = Reader.read_enum(types.QcowVersion, reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'read_only':
                obj.read_only = Reader.read_boolean(reader)
            elif tag == 'sgio':
                obj.sgio = Reader.read_enum(types.ScsiGenericIO, reader)
            elif tag == 'shareable':
                obj.shareable = Reader.read_boolean(reader)
            elif tag == 'snapshot':
                obj.snapshot = SnapshotReader.read_one(reader)
            elif tag == 'sparse':
                obj.sparse = Reader.read_boolean(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.DiskStatus, reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'storage_domains':
                obj.storage_domains = StorageDomainReader.read_many(reader)
            elif tag == 'storage_type':
                obj.storage_type = Reader.read_enum(types.DiskStorageType, reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'total_size':
                obj.total_size = Reader.read_integer(reader)
            elif tag == 'uses_scsi_reservation':
                obj.uses_scsi_reservation = Reader.read_boolean(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'wipe_after_delete':
                obj.wipe_after_delete = Reader.read_boolean(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            DiskSnapshotReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DiskSnapshotReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "disksnapshots":
                if obj.disk_snapshots is not None:
                    obj.disk_snapshots.href = href
                else:
                    obj.disk_snapshots = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)
            elif rel == "storagedomains":
                if obj.storage_domains is not None:
                    obj.storage_domains.href = href
                else:
                    obj.storage_domains = List(href)
            elif rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class DisplayReader(Reader):

    def __init__(self):
        super(DisplayReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Display()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'allow_override':
                obj.allow_override = Reader.read_boolean(reader)
            elif tag == 'certificate':
                obj.certificate = CertificateReader.read_one(reader)
            elif tag == 'copy_paste_enabled':
                obj.copy_paste_enabled = Reader.read_boolean(reader)
            elif tag == 'disconnect_action':
                obj.disconnect_action = Reader.read_string(reader)
            elif tag == 'file_transfer_enabled':
                obj.file_transfer_enabled = Reader.read_boolean(reader)
            elif tag == 'keyboard_layout':
                obj.keyboard_layout = Reader.read_string(reader)
            elif tag == 'monitors':
                obj.monitors = Reader.read_integer(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'proxy':
                obj.proxy = Reader.read_string(reader)
            elif tag == 'secure_port':
                obj.secure_port = Reader.read_integer(reader)
            elif tag == 'single_qxl_pci':
                obj.single_qxl_pci = Reader.read_boolean(reader)
            elif tag == 'smartcard_enabled':
                obj.smartcard_enabled = Reader.read_boolean(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.DisplayType, reader)
            else:
                reader.next_element()
        for link in links:
            DisplayReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DisplayReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class DnsReader(Reader):

    def __init__(self):
        super(DnsReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Dns()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'search_domains':
                obj.search_domains = HostReader.read_many(reader)
            elif tag == 'servers':
                obj.servers = HostReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            DnsReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DnsReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class DnsResolverConfigurationReader(Reader):

    def __init__(self):
        super(DnsResolverConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.DnsResolverConfiguration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'name_servers':
                obj.name_servers = Reader.read_strings(reader)
            else:
                reader.next_element()
        for link in links:
            DnsResolverConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DnsResolverConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class DomainReader(Reader):

    def __init__(self):
        super(DomainReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Domain()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'groups':
                obj.groups = GroupReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            elif tag == 'users':
                obj.users = UserReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            DomainReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(DomainReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "groups":
                if obj.groups is not None:
                    obj.groups.href = href
                else:
                    obj.groups = List(href)
            elif rel == "users":
                if obj.users is not None:
                    obj.users.href = href
                else:
                    obj.users = List(href)


class EntityProfileDetailReader(Reader):

    def __init__(self):
        super(EntityProfileDetailReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.EntityProfileDetail()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'profile_details':
                obj.profile_details = ProfileDetailReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            EntityProfileDetailReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(EntityProfileDetailReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ErrorHandlingReader(Reader):

    def __init__(self):
        super(ErrorHandlingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ErrorHandling()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'on_error':
                obj.on_error = Reader.read_enum(types.MigrateOnError, reader)
            else:
                reader.next_element()
        for link in links:
            ErrorHandlingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ErrorHandlingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class EventReader(Reader):

    def __init__(self):
        super(EventReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Event()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'code':
                obj.code = Reader.read_integer(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'correlation_id':
                obj.correlation_id = Reader.read_string(reader)
            elif tag == 'custom_data':
                obj.custom_data = Reader.read_string(reader)
            elif tag == 'custom_id':
                obj.custom_id = Reader.read_integer(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'flood_rate':
                obj.flood_rate = Reader.read_integer(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'index':
                obj.index = Reader.read_integer(reader)
            elif tag == 'log_on_host':
                obj.log_on_host = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'origin':
                obj.origin = Reader.read_string(reader)
            elif tag == 'severity':
                obj.severity = Reader.read_enum(types.LogSeverity, reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'time':
                obj.time = Reader.read_date(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            EventReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(EventReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class EventSubscriptionReader(Reader):

    def __init__(self):
        super(EventSubscriptionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.EventSubscription()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'event':
                obj.event = Reader.read_enum(types.NotifiableEvent, reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'notification_method':
                obj.notification_method = Reader.read_enum(types.NotificationMethod, reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            EventSubscriptionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(EventSubscriptionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ExternalComputeResourceReader(Reader):

    def __init__(self):
        super(ExternalComputeResourceReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalComputeResource()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'external_host_provider':
                obj.external_host_provider = ExternalHostProviderReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'provider':
                obj.provider = Reader.read_string(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            elif tag == 'user':
                obj.user = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ExternalComputeResourceReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalComputeResourceReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ExternalDiscoveredHostReader(Reader):

    def __init__(self):
        super(ExternalDiscoveredHostReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalDiscoveredHost()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'external_host_provider':
                obj.external_host_provider = ExternalHostProviderReader.read_one(reader)
            elif tag == 'ip':
                obj.ip = Reader.read_string(reader)
            elif tag == 'last_report':
                obj.last_report = Reader.read_string(reader)
            elif tag == 'mac':
                obj.mac = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'subnet_name':
                obj.subnet_name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ExternalDiscoveredHostReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalDiscoveredHostReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ExternalHostReader(Reader):

    def __init__(self):
        super(ExternalHostReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalHost()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'external_host_provider':
                obj.external_host_provider = ExternalHostProviderReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ExternalHostReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalHostReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ExternalHostGroupReader(Reader):

    def __init__(self):
        super(ExternalHostGroupReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalHostGroup()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'architecture_name':
                obj.architecture_name = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'domain_name':
                obj.domain_name = Reader.read_string(reader)
            elif tag == 'external_host_provider':
                obj.external_host_provider = ExternalHostProviderReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'operating_system_name':
                obj.operating_system_name = Reader.read_string(reader)
            elif tag == 'subnet_name':
                obj.subnet_name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ExternalHostGroupReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalHostGroupReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ExternalHostProviderReader(Reader):

    def __init__(self):
        super(ExternalHostProviderReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalHostProvider()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'authentication_url':
                obj.authentication_url = Reader.read_string(reader)
            elif tag == 'certificates':
                obj.certificates = CertificateReader.read_many(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'compute_resources':
                obj.compute_resources = ExternalComputeResourceReader.read_many(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'discovered_hosts':
                obj.discovered_hosts = ExternalDiscoveredHostReader.read_many(reader)
            elif tag == 'host_groups':
                obj.host_groups = ExternalHostGroupReader.read_many(reader)
            elif tag == 'hosts':
                obj.hosts = HostReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'requires_authentication':
                obj.requires_authentication = Reader.read_boolean(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            ExternalHostProviderReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalHostProviderReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "certificates":
                if obj.certificates is not None:
                    obj.certificates.href = href
                else:
                    obj.certificates = List(href)
            elif rel == "computeresources":
                if obj.compute_resources is not None:
                    obj.compute_resources.href = href
                else:
                    obj.compute_resources = List(href)
            elif rel == "discoveredhosts":
                if obj.discovered_hosts is not None:
                    obj.discovered_hosts.href = href
                else:
                    obj.discovered_hosts = List(href)
            elif rel == "hostgroups":
                if obj.host_groups is not None:
                    obj.host_groups.href = href
                else:
                    obj.host_groups = List(href)
            elif rel == "hosts":
                if obj.hosts is not None:
                    obj.hosts.href = href
                else:
                    obj.hosts = List(href)


class ExternalNetworkProviderConfigurationReader(Reader):

    def __init__(self):
        super(ExternalNetworkProviderConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalNetworkProviderConfiguration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'external_network_provider':
                obj.external_network_provider = ExternalProviderReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ExternalNetworkProviderConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalNetworkProviderConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ExternalProviderReader(Reader):

    def __init__(self):
        super(ExternalProviderReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalProvider()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'authentication_url':
                obj.authentication_url = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'requires_authentication':
                obj.requires_authentication = Reader.read_boolean(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ExternalProviderReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalProviderReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ExternalTemplateImportReader(Reader):

    def __init__(self):
        super(ExternalTemplateImportReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalTemplateImport()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'clone':
                obj.clone = Reader.read_boolean(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'cpu_profile':
                obj.cpu_profile = CpuProfileReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ExternalTemplateImportReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalTemplateImportReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ExternalVmImportReader(Reader):

    def __init__(self):
        super(ExternalVmImportReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ExternalVmImport()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'cpu_profile':
                obj.cpu_profile = CpuProfileReader.read_one(reader)
            elif tag == 'drivers_iso':
                obj.drivers_iso = FileReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'provider':
                obj.provider = Reader.read_enum(types.ExternalVmProviderType, reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'sparse':
                obj.sparse = Reader.read_boolean(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            ExternalVmImportReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ExternalVmImportReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class FaultReader(Reader):

    def __init__(self):
        super(FaultReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Fault()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'detail':
                obj.detail = Reader.read_string(reader)
            elif tag == 'reason':
                obj.reason = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            FaultReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(FaultReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class FencingPolicyReader(Reader):

    def __init__(self):
        super(FencingPolicyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.FencingPolicy()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            elif tag == 'skip_if_connectivity_broken':
                obj.skip_if_connectivity_broken = SkipIfConnectivityBrokenReader.read_one(reader)
            elif tag == 'skip_if_gluster_bricks_up':
                obj.skip_if_gluster_bricks_up = Reader.read_boolean(reader)
            elif tag == 'skip_if_gluster_quorum_not_met':
                obj.skip_if_gluster_quorum_not_met = Reader.read_boolean(reader)
            elif tag == 'skip_if_sd_active':
                obj.skip_if_sd_active = SkipIfSdActiveReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            FencingPolicyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(FencingPolicyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class FileReader(Reader):

    def __init__(self):
        super(FileReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.File()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'content':
                obj.content = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'type':
                obj.type = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            FileReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(FileReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class FilterReader(Reader):

    def __init__(self):
        super(FilterReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Filter()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'position':
                obj.position = Reader.read_integer(reader)
            elif tag == 'scheduling_policy_unit':
                obj.scheduling_policy_unit = SchedulingPolicyUnitReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            FilterReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(FilterReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class FloppyReader(Reader):

    def __init__(self):
        super(FloppyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Floppy()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'file':
                obj.file = FileReader.read_one(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            FloppyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(FloppyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class FopStatisticReader(Reader):

    def __init__(self):
        super(FopStatisticReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.FopStatistic()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            FopStatisticReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(FopStatisticReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class GlusterBrickReader(Reader):

    def __init__(self):
        super(GlusterBrickReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterBrick()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'brick_dir':
                obj.brick_dir = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'device':
                obj.device = Reader.read_string(reader)
            elif tag == 'fs_name':
                obj.fs_name = Reader.read_string(reader)
            elif tag == 'gluster_clients':
                obj.gluster_clients = GlusterClientReader.read_many(reader)
            elif tag == 'gluster_volume':
                obj.gluster_volume = GlusterVolumeReader.read_one(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'memory_pools':
                obj.memory_pools = GlusterMemoryPoolReader.read_many(reader)
            elif tag == 'mnt_options':
                obj.mnt_options = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'pid':
                obj.pid = Reader.read_integer(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'server_id':
                obj.server_id = Reader.read_string(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.GlusterBrickStatus, reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            GlusterBrickReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterBrickReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)
            elif rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class GlusterBrickAdvancedDetailsReader(Reader):

    def __init__(self):
        super(GlusterBrickAdvancedDetailsReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterBrickAdvancedDetails()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'device':
                obj.device = Reader.read_string(reader)
            elif tag == 'fs_name':
                obj.fs_name = Reader.read_string(reader)
            elif tag == 'gluster_clients':
                obj.gluster_clients = GlusterClientReader.read_many(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'memory_pools':
                obj.memory_pools = GlusterMemoryPoolReader.read_many(reader)
            elif tag == 'mnt_options':
                obj.mnt_options = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'pid':
                obj.pid = Reader.read_integer(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            GlusterBrickAdvancedDetailsReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterBrickAdvancedDetailsReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class GlusterBrickMemoryInfoReader(Reader):

    def __init__(self):
        super(GlusterBrickMemoryInfoReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterBrickMemoryInfo()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'memory_pools':
                obj.memory_pools = GlusterMemoryPoolReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            GlusterBrickMemoryInfoReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterBrickMemoryInfoReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class GlusterClientReader(Reader):

    def __init__(self):
        super(GlusterClientReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterClient()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'bytes_read':
                obj.bytes_read = Reader.read_integer(reader)
            elif tag == 'bytes_written':
                obj.bytes_written = Reader.read_integer(reader)
            elif tag == 'client_port':
                obj.client_port = Reader.read_integer(reader)
            elif tag == 'host_name':
                obj.host_name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            GlusterClientReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterClientReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class GlusterHookReader(Reader):

    def __init__(self):
        super(GlusterHookReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterHook()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'checksum':
                obj.checksum = Reader.read_string(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'conflict_status':
                obj.conflict_status = Reader.read_integer(reader)
            elif tag == 'conflicts':
                obj.conflicts = Reader.read_string(reader)
            elif tag == 'content':
                obj.content = Reader.read_string(reader)
            elif tag == 'content_type':
                obj.content_type = Reader.read_enum(types.HookContentType, reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'gluster_command':
                obj.gluster_command = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'server_hooks':
                obj.server_hooks = GlusterServerHookReader.read_many(reader)
            elif tag == 'stage':
                obj.stage = Reader.read_enum(types.HookStage, reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.GlusterHookStatus, reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            GlusterHookReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterHookReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "serverhooks":
                if obj.server_hooks is not None:
                    obj.server_hooks.href = href
                else:
                    obj.server_hooks = List(href)


class GlusterMemoryPoolReader(Reader):

    def __init__(self):
        super(GlusterMemoryPoolReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterMemoryPool()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'alloc_count':
                obj.alloc_count = Reader.read_integer(reader)
            elif tag == 'cold_count':
                obj.cold_count = Reader.read_integer(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'hot_count':
                obj.hot_count = Reader.read_integer(reader)
            elif tag == 'max_alloc':
                obj.max_alloc = Reader.read_integer(reader)
            elif tag == 'max_stdalloc':
                obj.max_stdalloc = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'padded_size':
                obj.padded_size = Reader.read_integer(reader)
            elif tag == 'pool_misses':
                obj.pool_misses = Reader.read_integer(reader)
            elif tag == 'type':
                obj.type = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            GlusterMemoryPoolReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterMemoryPoolReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class GlusterServerHookReader(Reader):

    def __init__(self):
        super(GlusterServerHookReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterServerHook()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'checksum':
                obj.checksum = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'content_type':
                obj.content_type = Reader.read_enum(types.HookContentType, reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.GlusterHookStatus, reader)
            else:
                reader.next_element()
        for link in links:
            GlusterServerHookReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterServerHookReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class GlusterVolumeReader(Reader):

    def __init__(self):
        super(GlusterVolumeReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterVolume()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'bricks':
                obj.bricks = GlusterBrickReader.read_many(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disperse_count':
                obj.disperse_count = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'options':
                obj.options = OptionReader.read_many(reader)
            elif tag == 'redundancy_count':
                obj.redundancy_count = Reader.read_integer(reader)
            elif tag == 'replica_count':
                obj.replica_count = Reader.read_integer(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.GlusterVolumeStatus, reader)
            elif tag == 'stripe_count':
                obj.stripe_count = Reader.read_integer(reader)
            elif tag == 'transport_types':
                obj.transport_types = Reader.read_enums(types.TransportType, reader)
            elif tag == 'volume_type':
                obj.volume_type = Reader.read_enum(types.GlusterVolumeType, reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            GlusterVolumeReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterVolumeReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "bricks":
                if obj.bricks is not None:
                    obj.bricks.href = href
                else:
                    obj.bricks = List(href)
            elif rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)


class GlusterVolumeProfileDetailsReader(Reader):

    def __init__(self):
        super(GlusterVolumeProfileDetailsReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GlusterVolumeProfileDetails()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'brick_profile_details':
                obj.brick_profile_details = BrickProfileDetailReader.read_many(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'nfs_profile_details':
                obj.nfs_profile_details = NfsProfileDetailReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            GlusterVolumeProfileDetailsReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GlusterVolumeProfileDetailsReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class GracePeriodReader(Reader):

    def __init__(self):
        super(GracePeriodReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GracePeriod()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'expiry':
                obj.expiry = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            GracePeriodReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GracePeriodReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class GraphicsConsoleReader(Reader):

    def __init__(self):
        super(GraphicsConsoleReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GraphicsConsole()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'protocol':
                obj.protocol = Reader.read_enum(types.GraphicsType, reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'tls_port':
                obj.tls_port = Reader.read_integer(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            GraphicsConsoleReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GraphicsConsoleReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class GroupReader(Reader):

    def __init__(self):
        super(GroupReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Group()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'domain':
                obj.domain = DomainReader.read_one(reader)
            elif tag == 'domain_entry_id':
                obj.domain_entry_id = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'namespace':
                obj.namespace = Reader.read_string(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'roles':
                obj.roles = RoleReader.read_many(reader)
            elif tag == 'tags':
                obj.tags = TagReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            GroupReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GroupReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "roles":
                if obj.roles is not None:
                    obj.roles.href = href
                else:
                    obj.roles = List(href)
            elif rel == "tags":
                if obj.tags is not None:
                    obj.tags.href = href
                else:
                    obj.tags = List(href)


class GuestOperatingSystemReader(Reader):

    def __init__(self):
        super(GuestOperatingSystemReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.GuestOperatingSystem()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'architecture':
                obj.architecture = Reader.read_string(reader)
            elif tag == 'codename':
                obj.codename = Reader.read_string(reader)
            elif tag == 'distribution':
                obj.distribution = Reader.read_string(reader)
            elif tag == 'family':
                obj.family = Reader.read_string(reader)
            elif tag == 'kernel':
                obj.kernel = KernelReader.read_one(reader)
            elif tag == 'version':
                obj.version = VersionReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            GuestOperatingSystemReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(GuestOperatingSystemReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class HardwareInformationReader(Reader):

    def __init__(self):
        super(HardwareInformationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.HardwareInformation()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'family':
                obj.family = Reader.read_string(reader)
            elif tag == 'manufacturer':
                obj.manufacturer = Reader.read_string(reader)
            elif tag == 'product_name':
                obj.product_name = Reader.read_string(reader)
            elif tag == 'serial_number':
                obj.serial_number = Reader.read_string(reader)
            elif tag == 'supported_rng_sources':
                obj.supported_rng_sources = Reader.read_enums(types.RngSource, reader)
            elif tag == 'uuid':
                obj.uuid = Reader.read_string(reader)
            elif tag == 'version':
                obj.version = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            HardwareInformationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HardwareInformationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class HighAvailabilityReader(Reader):

    def __init__(self):
        super(HighAvailabilityReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.HighAvailability()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            elif tag == 'priority':
                obj.priority = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            HighAvailabilityReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HighAvailabilityReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class HookReader(Reader):

    def __init__(self):
        super(HookReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Hook()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'event_name':
                obj.event_name = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'md5':
                obj.md5 = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            HookReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HookReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class HostReader(Reader):

    def __init__(self):
        super(HostReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Host()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'affinity_labels':
                obj.affinity_labels = AffinityLabelReader.read_many(reader)
            elif tag == 'agents':
                obj.agents = AgentReader.read_many(reader)
            elif tag == 'auto_numa_status':
                obj.auto_numa_status = Reader.read_enum(types.AutoNumaStatus, reader)
            elif tag == 'certificate':
                obj.certificate = CertificateReader.read_one(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'device_passthrough':
                obj.device_passthrough = HostDevicePassthroughReader.read_one(reader)
            elif tag == 'devices':
                obj.devices = HostDeviceReader.read_many(reader)
            elif tag == 'display':
                obj.display = DisplayReader.read_one(reader)
            elif tag == 'external_host_provider':
                obj.external_host_provider = ExternalHostProviderReader.read_one(reader)
            elif tag == 'external_network_provider_configurations':
                obj.external_network_provider_configurations = ExternalNetworkProviderConfigurationReader.read_many(reader)
            elif tag == 'external_status':
                obj.external_status = Reader.read_enum(types.ExternalStatus, reader)
            elif tag == 'hardware_information':
                obj.hardware_information = HardwareInformationReader.read_one(reader)
            elif tag == 'hooks':
                obj.hooks = HookReader.read_many(reader)
            elif tag == 'hosted_engine':
                obj.hosted_engine = HostedEngineReader.read_one(reader)
            elif tag == 'iscsi':
                obj.iscsi = IscsiDetailsReader.read_one(reader)
            elif tag == 'katello_errata':
                obj.katello_errata = KatelloErratumReader.read_many(reader)
            elif tag == 'kdump_status':
                obj.kdump_status = Reader.read_enum(types.KdumpStatus, reader)
            elif tag == 'ksm':
                obj.ksm = KsmReader.read_one(reader)
            elif tag == 'libvirt_version':
                obj.libvirt_version = VersionReader.read_one(reader)
            elif tag == 'max_scheduling_memory':
                obj.max_scheduling_memory = Reader.read_integer(reader)
            elif tag == 'memory':
                obj.memory = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'network_attachments':
                obj.network_attachments = NetworkAttachmentReader.read_many(reader)
            elif tag == 'network_operation_in_progress':
                obj.network_operation_in_progress = Reader.read_boolean(reader)
            elif tag == 'nics':
                obj.nics = HostNicReader.read_many(reader)
            elif tag == 'host_numa_nodes':
                obj.numa_nodes = NumaNodeReader.read_many(reader)
            elif tag == 'numa_supported':
                obj.numa_supported = Reader.read_boolean(reader)
            elif tag == 'os':
                obj.os = OperatingSystemReader.read_one(reader)
            elif tag == 'override_iptables':
                obj.override_iptables = Reader.read_boolean(reader)
            elif tag == 'ovn_configured':
                obj.ovn_configured = Reader.read_boolean(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'power_management':
                obj.power_management = PowerManagementReader.read_one(reader)
            elif tag == 'protocol':
                obj.protocol = Reader.read_enum(types.HostProtocol, reader)
            elif tag == 'reinstallation_required':
                obj.reinstallation_required = Reader.read_boolean(reader)
            elif tag == 'root_password':
                obj.root_password = Reader.read_string(reader)
            elif tag == 'se_linux':
                obj.se_linux = SeLinuxReader.read_one(reader)
            elif tag == 'spm':
                obj.spm = SpmReader.read_one(reader)
            elif tag == 'ssh':
                obj.ssh = SshReader.read_one(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.HostStatus, reader)
            elif tag == 'status_detail':
                obj.status_detail = Reader.read_string(reader)
            elif tag == 'storage_connection_extensions':
                obj.storage_connection_extensions = StorageConnectionExtensionReader.read_many(reader)
            elif tag == 'storages':
                obj.storages = HostStorageReader.read_many(reader)
            elif tag == 'summary':
                obj.summary = VmSummaryReader.read_one(reader)
            elif tag == 'tags':
                obj.tags = TagReader.read_many(reader)
            elif tag == 'transparent_hugepages':
                obj.transparent_huge_pages = TransparentHugePagesReader.read_one(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.HostType, reader)
            elif tag == 'unmanaged_networks':
                obj.unmanaged_networks = UnmanagedNetworkReader.read_many(reader)
            elif tag == 'update_available':
                obj.update_available = Reader.read_boolean(reader)
            elif tag == 'version':
                obj.version = VersionReader.read_one(reader)
            elif tag == 'vgpu_placement':
                obj.vgpu_placement = Reader.read_enum(types.VgpuPlacement, reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            HostReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HostReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "affinitylabels":
                if obj.affinity_labels is not None:
                    obj.affinity_labels.href = href
                else:
                    obj.affinity_labels = List(href)
            elif rel == "agents":
                if obj.agents is not None:
                    obj.agents.href = href
                else:
                    obj.agents = List(href)
            elif rel == "devices":
                if obj.devices is not None:
                    obj.devices.href = href
                else:
                    obj.devices = List(href)
            elif rel == "externalnetworkproviderconfigurations":
                if obj.external_network_provider_configurations is not None:
                    obj.external_network_provider_configurations.href = href
                else:
                    obj.external_network_provider_configurations = List(href)
            elif rel == "hooks":
                if obj.hooks is not None:
                    obj.hooks.href = href
                else:
                    obj.hooks = List(href)
            elif rel == "katelloerrata":
                if obj.katello_errata is not None:
                    obj.katello_errata.href = href
                else:
                    obj.katello_errata = List(href)
            elif rel == "networkattachments":
                if obj.network_attachments is not None:
                    obj.network_attachments.href = href
                else:
                    obj.network_attachments = List(href)
            elif rel == "nics":
                if obj.nics is not None:
                    obj.nics.href = href
                else:
                    obj.nics = List(href)
            elif rel == "numanodes":
                if obj.numa_nodes is not None:
                    obj.numa_nodes.href = href
                else:
                    obj.numa_nodes = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)
            elif rel == "storageconnectionextensions":
                if obj.storage_connection_extensions is not None:
                    obj.storage_connection_extensions.href = href
                else:
                    obj.storage_connection_extensions = List(href)
            elif rel == "storages":
                if obj.storages is not None:
                    obj.storages.href = href
                else:
                    obj.storages = List(href)
            elif rel == "tags":
                if obj.tags is not None:
                    obj.tags.href = href
                else:
                    obj.tags = List(href)
            elif rel == "unmanagednetworks":
                if obj.unmanaged_networks is not None:
                    obj.unmanaged_networks.href = href
                else:
                    obj.unmanaged_networks = List(href)


class HostDeviceReader(Reader):

    def __init__(self):
        super(HostDeviceReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.HostDevice()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'capability':
                obj.capability = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'driver':
                obj.driver = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'iommu_group':
                obj.iommu_group = Reader.read_integer(reader)
            elif tag == 'm_dev_types':
                obj.m_dev_types = MDevTypeReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'parent_device':
                obj.parent_device = HostDeviceReader.read_one(reader)
            elif tag == 'physical_function':
                obj.physical_function = HostDeviceReader.read_one(reader)
            elif tag == 'placeholder':
                obj.placeholder = Reader.read_boolean(reader)
            elif tag == 'product':
                obj.product = ProductReader.read_one(reader)
            elif tag == 'vendor':
                obj.vendor = VendorReader.read_one(reader)
            elif tag == 'virtual_functions':
                obj.virtual_functions = Reader.read_integer(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            HostDeviceReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HostDeviceReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class HostDevicePassthroughReader(Reader):

    def __init__(self):
        super(HostDevicePassthroughReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.HostDevicePassthrough()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            HostDevicePassthroughReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HostDevicePassthroughReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class HostNicReader(Reader):

    def __init__(self):
        super(HostNicReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.HostNic()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'ad_aggregator_id':
                obj.ad_aggregator_id = Reader.read_integer(reader)
            elif tag == 'base_interface':
                obj.base_interface = Reader.read_string(reader)
            elif tag == 'bonding':
                obj.bonding = BondingReader.read_one(reader)
            elif tag == 'boot_protocol':
                obj.boot_protocol = Reader.read_enum(types.BootProtocol, reader)
            elif tag == 'bridged':
                obj.bridged = Reader.read_boolean(reader)
            elif tag == 'check_connectivity':
                obj.check_connectivity = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'custom_configuration':
                obj.custom_configuration = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'ip':
                obj.ip = IpReader.read_one(reader)
            elif tag == 'ipv6':
                obj.ipv6 = IpReader.read_one(reader)
            elif tag == 'ipv6_boot_protocol':
                obj.ipv6_boot_protocol = Reader.read_enum(types.BootProtocol, reader)
            elif tag == 'mac':
                obj.mac = MacReader.read_one(reader)
            elif tag == 'mtu':
                obj.mtu = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'network':
                obj.network = NetworkReader.read_one(reader)
            elif tag == 'network_labels':
                obj.network_labels = NetworkLabelReader.read_many(reader)
            elif tag == 'override_configuration':
                obj.override_configuration = Reader.read_boolean(reader)
            elif tag == 'physical_function':
                obj.physical_function = HostNicReader.read_one(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'qos':
                obj.qos = QosReader.read_one(reader)
            elif tag == 'speed':
                obj.speed = Reader.read_integer(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.NicStatus, reader)
            elif tag == 'virtual_functions_configuration':
                obj.virtual_functions_configuration = HostNicVirtualFunctionsConfigurationReader.read_one(reader)
            elif tag == 'vlan':
                obj.vlan = VlanReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            HostNicReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HostNicReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "networklabels":
                if obj.network_labels is not None:
                    obj.network_labels.href = href
                else:
                    obj.network_labels = List(href)
            elif rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)


class HostNicVirtualFunctionsConfigurationReader(Reader):

    def __init__(self):
        super(HostNicVirtualFunctionsConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.HostNicVirtualFunctionsConfiguration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'all_networks_allowed':
                obj.all_networks_allowed = Reader.read_boolean(reader)
            elif tag == 'max_number_of_virtual_functions':
                obj.max_number_of_virtual_functions = Reader.read_integer(reader)
            elif tag == 'number_of_virtual_functions':
                obj.number_of_virtual_functions = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            HostNicVirtualFunctionsConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HostNicVirtualFunctionsConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class HostStorageReader(Reader):

    def __init__(self):
        super(HostStorageReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.HostStorage()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'driver_options':
                obj.driver_options = PropertyReader.read_many(reader)
            elif tag == 'driver_sensitive_options':
                obj.driver_sensitive_options = PropertyReader.read_many(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'logical_units':
                obj.logical_units = LogicalUnitReader.read_many(reader)
            elif tag == 'mount_options':
                obj.mount_options = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'nfs_retrans':
                obj.nfs_retrans = Reader.read_integer(reader)
            elif tag == 'nfs_timeo':
                obj.nfs_timeo = Reader.read_integer(reader)
            elif tag == 'nfs_version':
                obj.nfs_version = Reader.read_enum(types.NfsVersion, reader)
            elif tag == 'override_luns':
                obj.override_luns = Reader.read_boolean(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'path':
                obj.path = Reader.read_string(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'portal':
                obj.portal = Reader.read_string(reader)
            elif tag == 'target':
                obj.target = Reader.read_string(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.StorageType, reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'vfs_type':
                obj.vfs_type = Reader.read_string(reader)
            elif tag == 'volume_group':
                obj.volume_group = VolumeGroupReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            HostStorageReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HostStorageReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class HostedEngineReader(Reader):

    def __init__(self):
        super(HostedEngineReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.HostedEngine()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active':
                obj.active = Reader.read_boolean(reader)
            elif tag == 'configured':
                obj.configured = Reader.read_boolean(reader)
            elif tag == 'global_maintenance':
                obj.global_maintenance = Reader.read_boolean(reader)
            elif tag == 'local_maintenance':
                obj.local_maintenance = Reader.read_boolean(reader)
            elif tag == 'score':
                obj.score = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            HostedEngineReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(HostedEngineReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class IconReader(Reader):

    def __init__(self):
        super(IconReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Icon()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'data':
                obj.data = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'media_type':
                obj.media_type = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            IconReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(IconReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class IdentifiedReader(Reader):

    def __init__(self):
        super(IdentifiedReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Identified()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            IdentifiedReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(IdentifiedReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ImageReader(Reader):

    def __init__(self):
        super(ImageReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Image()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'size':
                obj.size = Reader.read_integer(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.ImageFileType, reader)
            else:
                reader.next_element()
        for link in links:
            ImageReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ImageReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ImageTransferReader(Reader):

    def __init__(self):
        super(ImageTransferReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ImageTransfer()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active':
                obj.active = Reader.read_boolean(reader)
            elif tag == 'backup':
                obj.backup = BackupReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'direction':
                obj.direction = Reader.read_enum(types.ImageTransferDirection, reader)
            elif tag == 'disk':
                obj.disk = DiskReader.read_one(reader)
            elif tag == 'format':
                obj.format = Reader.read_enum(types.DiskFormat, reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'image':
                obj.image = ImageReader.read_one(reader)
            elif tag == 'inactivity_timeout':
                obj.inactivity_timeout = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'phase':
                obj.phase = Reader.read_enum(types.ImageTransferPhase, reader)
            elif tag == 'proxy_url':
                obj.proxy_url = Reader.read_string(reader)
            elif tag == 'shallow':
                obj.shallow = Reader.read_boolean(reader)
            elif tag == 'snapshot':
                obj.snapshot = DiskSnapshotReader.read_one(reader)
            elif tag == 'timeout_policy':
                obj.timeout_policy = Reader.read_enum(types.ImageTransferTimeoutPolicy, reader)
            elif tag == 'transfer_url':
                obj.transfer_url = Reader.read_string(reader)
            elif tag == 'transferred':
                obj.transferred = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            ImageTransferReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ImageTransferReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class InitializationReader(Reader):

    def __init__(self):
        super(InitializationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Initialization()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active_directory_ou':
                obj.active_directory_ou = Reader.read_string(reader)
            elif tag == 'authorized_ssh_keys':
                obj.authorized_ssh_keys = Reader.read_string(reader)
            elif tag == 'cloud_init':
                obj.cloud_init = CloudInitReader.read_one(reader)
            elif tag == 'cloud_init_network_protocol':
                obj.cloud_init_network_protocol = Reader.read_enum(types.CloudInitNetworkProtocol, reader)
            elif tag == 'configuration':
                obj.configuration = ConfigurationReader.read_one(reader)
            elif tag == 'custom_script':
                obj.custom_script = Reader.read_string(reader)
            elif tag == 'dns_search':
                obj.dns_search = Reader.read_string(reader)
            elif tag == 'dns_servers':
                obj.dns_servers = Reader.read_string(reader)
            elif tag == 'domain':
                obj.domain = Reader.read_string(reader)
            elif tag == 'host_name':
                obj.host_name = Reader.read_string(reader)
            elif tag == 'input_locale':
                obj.input_locale = Reader.read_string(reader)
            elif tag == 'nic_configurations':
                obj.nic_configurations = NicConfigurationReader.read_many(reader)
            elif tag == 'org_name':
                obj.org_name = Reader.read_string(reader)
            elif tag == 'regenerate_ids':
                obj.regenerate_ids = Reader.read_boolean(reader)
            elif tag == 'regenerate_ssh_keys':
                obj.regenerate_ssh_keys = Reader.read_boolean(reader)
            elif tag == 'root_password':
                obj.root_password = Reader.read_string(reader)
            elif tag == 'system_locale':
                obj.system_locale = Reader.read_string(reader)
            elif tag == 'timezone':
                obj.timezone = Reader.read_string(reader)
            elif tag == 'ui_language':
                obj.ui_language = Reader.read_string(reader)
            elif tag == 'user_locale':
                obj.user_locale = Reader.read_string(reader)
            elif tag == 'user_name':
                obj.user_name = Reader.read_string(reader)
            elif tag == 'windows_license_key':
                obj.windows_license_key = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            InitializationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(InitializationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class InstanceTypeReader(Reader):

    def __init__(self):
        super(InstanceTypeReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.InstanceType()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'auto_pinning_policy':
                obj.auto_pinning_policy = Reader.read_enum(types.AutoPinningPolicy, reader)
            elif tag == 'bios':
                obj.bios = BiosReader.read_one(reader)
            elif tag == 'cdroms':
                obj.cdroms = CdromReader.read_many(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'console':
                obj.console = ConsoleReader.read_one(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'cpu_profile':
                obj.cpu_profile = CpuProfileReader.read_one(reader)
            elif tag == 'cpu_shares':
                obj.cpu_shares = Reader.read_integer(reader)
            elif tag == 'creation_time':
                obj.creation_time = Reader.read_date(reader)
            elif tag == 'custom_compatibility_version':
                obj.custom_compatibility_version = VersionReader.read_one(reader)
            elif tag == 'custom_cpu_model':
                obj.custom_cpu_model = Reader.read_string(reader)
            elif tag == 'custom_emulated_machine':
                obj.custom_emulated_machine = Reader.read_string(reader)
            elif tag == 'custom_properties':
                obj.custom_properties = CustomPropertyReader.read_many(reader)
            elif tag == 'delete_protected':
                obj.delete_protected = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk_attachments':
                obj.disk_attachments = DiskAttachmentReader.read_many(reader)
            elif tag == 'display':
                obj.display = DisplayReader.read_one(reader)
            elif tag == 'domain':
                obj.domain = DomainReader.read_one(reader)
            elif tag == 'graphics_consoles':
                obj.graphics_consoles = GraphicsConsoleReader.read_many(reader)
            elif tag == 'high_availability':
                obj.high_availability = HighAvailabilityReader.read_one(reader)
            elif tag == 'initialization':
                obj.initialization = InitializationReader.read_one(reader)
            elif tag == 'io':
                obj.io = IoReader.read_one(reader)
            elif tag == 'large_icon':
                obj.large_icon = IconReader.read_one(reader)
            elif tag == 'lease':
                obj.lease = StorageDomainLeaseReader.read_one(reader)
            elif tag == 'memory':
                obj.memory = Reader.read_integer(reader)
            elif tag == 'memory_policy':
                obj.memory_policy = MemoryPolicyReader.read_one(reader)
            elif tag == 'migration':
                obj.migration = MigrationOptionsReader.read_one(reader)
            elif tag == 'migration_downtime':
                obj.migration_downtime = Reader.read_integer(reader)
            elif tag == 'multi_queues_enabled':
                obj.multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'nics':
                obj.nics = NicReader.read_many(reader)
            elif tag == 'origin':
                obj.origin = Reader.read_string(reader)
            elif tag == 'os':
                obj.os = OperatingSystemReader.read_one(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'placement_policy':
                obj.placement_policy = VmPlacementPolicyReader.read_one(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'rng_device':
                obj.rng_device = RngDeviceReader.read_one(reader)
            elif tag == 'serial_number':
                obj.serial_number = SerialNumberReader.read_one(reader)
            elif tag == 'small_icon':
                obj.small_icon = IconReader.read_one(reader)
            elif tag == 'soundcard_enabled':
                obj.soundcard_enabled = Reader.read_boolean(reader)
            elif tag == 'sso':
                obj.sso = SsoReader.read_one(reader)
            elif tag == 'start_paused':
                obj.start_paused = Reader.read_boolean(reader)
            elif tag == 'stateless':
                obj.stateless = Reader.read_boolean(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.TemplateStatus, reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'storage_error_resume_behaviour':
                obj.storage_error_resume_behaviour = Reader.read_enum(types.VmStorageErrorResumeBehaviour, reader)
            elif tag == 'tags':
                obj.tags = TagReader.read_many(reader)
            elif tag == 'time_zone':
                obj.time_zone = TimeZoneReader.read_one(reader)
            elif tag == 'tpm_enabled':
                obj.tpm_enabled = Reader.read_boolean(reader)
            elif tag == 'tunnel_migration':
                obj.tunnel_migration = Reader.read_boolean(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.VmType, reader)
            elif tag == 'usb':
                obj.usb = UsbReader.read_one(reader)
            elif tag == 'version':
                obj.version = TemplateVersionReader.read_one(reader)
            elif tag == 'virtio_scsi':
                obj.virtio_scsi = VirtioScsiReader.read_one(reader)
            elif tag == 'virtio_scsi_multi_queues':
                obj.virtio_scsi_multi_queues = Reader.read_integer(reader)
            elif tag == 'virtio_scsi_multi_queues_enabled':
                obj.virtio_scsi_multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'watchdogs':
                obj.watchdogs = WatchdogReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            InstanceTypeReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(InstanceTypeReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "cdroms":
                if obj.cdroms is not None:
                    obj.cdroms.href = href
                else:
                    obj.cdroms = List(href)
            elif rel == "diskattachments":
                if obj.disk_attachments is not None:
                    obj.disk_attachments.href = href
                else:
                    obj.disk_attachments = List(href)
            elif rel == "graphicsconsoles":
                if obj.graphics_consoles is not None:
                    obj.graphics_consoles.href = href
                else:
                    obj.graphics_consoles = List(href)
            elif rel == "nics":
                if obj.nics is not None:
                    obj.nics.href = href
                else:
                    obj.nics = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "tags":
                if obj.tags is not None:
                    obj.tags.href = href
                else:
                    obj.tags = List(href)
            elif rel == "watchdogs":
                if obj.watchdogs is not None:
                    obj.watchdogs.href = href
                else:
                    obj.watchdogs = List(href)


class IoReader(Reader):

    def __init__(self):
        super(IoReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Io()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'threads':
                obj.threads = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            IoReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(IoReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class IpReader(Reader):

    def __init__(self):
        super(IpReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Ip()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'gateway':
                obj.gateway = Reader.read_string(reader)
            elif tag == 'netmask':
                obj.netmask = Reader.read_string(reader)
            elif tag == 'version':
                obj.version = Reader.read_enum(types.IpVersion, reader)
            else:
                reader.next_element()
        for link in links:
            IpReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(IpReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class IpAddressAssignmentReader(Reader):

    def __init__(self):
        super(IpAddressAssignmentReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.IpAddressAssignment()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'assignment_method':
                obj.assignment_method = Reader.read_enum(types.BootProtocol, reader)
            elif tag == 'ip':
                obj.ip = IpReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            IpAddressAssignmentReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(IpAddressAssignmentReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class IscsiBondReader(Reader):

    def __init__(self):
        super(IscsiBondReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.IscsiBond()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'networks':
                obj.networks = NetworkReader.read_many(reader)
            elif tag == 'storage_connections':
                obj.storage_connections = StorageConnectionReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            IscsiBondReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(IscsiBondReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "networks":
                if obj.networks is not None:
                    obj.networks.href = href
                else:
                    obj.networks = List(href)
            elif rel == "storageconnections":
                if obj.storage_connections is not None:
                    obj.storage_connections.href = href
                else:
                    obj.storage_connections = List(href)


class IscsiDetailsReader(Reader):

    def __init__(self):
        super(IscsiDetailsReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.IscsiDetails()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'disk_id':
                obj.disk_id = Reader.read_string(reader)
            elif tag == 'initiator':
                obj.initiator = Reader.read_string(reader)
            elif tag == 'lun_mapping':
                obj.lun_mapping = Reader.read_integer(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'paths':
                obj.paths = Reader.read_integer(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'portal':
                obj.portal = Reader.read_string(reader)
            elif tag == 'product_id':
                obj.product_id = Reader.read_string(reader)
            elif tag == 'serial':
                obj.serial = Reader.read_string(reader)
            elif tag == 'size':
                obj.size = Reader.read_integer(reader)
            elif tag == 'status':
                obj.status = Reader.read_string(reader)
            elif tag == 'storage_domain_id':
                obj.storage_domain_id = Reader.read_string(reader)
            elif tag == 'target':
                obj.target = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'vendor_id':
                obj.vendor_id = Reader.read_string(reader)
            elif tag == 'volume_group_id':
                obj.volume_group_id = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            IscsiDetailsReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(IscsiDetailsReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class JobReader(Reader):

    def __init__(self):
        super(JobReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Job()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'auto_cleared':
                obj.auto_cleared = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'end_time':
                obj.end_time = Reader.read_date(reader)
            elif tag == 'external':
                obj.external = Reader.read_boolean(reader)
            elif tag == 'last_updated':
                obj.last_updated = Reader.read_date(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'owner':
                obj.owner = UserReader.read_one(reader)
            elif tag == 'start_time':
                obj.start_time = Reader.read_date(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.JobStatus, reader)
            elif tag == 'steps':
                obj.steps = StepReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            JobReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(JobReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "steps":
                if obj.steps is not None:
                    obj.steps.href = href
                else:
                    obj.steps = List(href)


class KatelloErratumReader(Reader):

    def __init__(self):
        super(KatelloErratumReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.KatelloErratum()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'issued':
                obj.issued = Reader.read_date(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'packages':
                obj.packages = PackageReader.read_many(reader)
            elif tag == 'severity':
                obj.severity = Reader.read_string(reader)
            elif tag == 'solution':
                obj.solution = Reader.read_string(reader)
            elif tag == 'summary':
                obj.summary = Reader.read_string(reader)
            elif tag == 'title':
                obj.title = Reader.read_string(reader)
            elif tag == 'type':
                obj.type = Reader.read_string(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            KatelloErratumReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(KatelloErratumReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class KernelReader(Reader):

    def __init__(self):
        super(KernelReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Kernel()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'version':
                obj.version = VersionReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            KernelReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(KernelReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class KsmReader(Reader):

    def __init__(self):
        super(KsmReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Ksm()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            elif tag == 'merge_across_nodes':
                obj.merge_across_nodes = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            KsmReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(KsmReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class LinkLayerDiscoveryProtocolElementReader(Reader):

    def __init__(self):
        super(LinkLayerDiscoveryProtocolElementReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.LinkLayerDiscoveryProtocolElement()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'oui':
                obj.oui = Reader.read_integer(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'subtype':
                obj.subtype = Reader.read_integer(reader)
            elif tag == 'type':
                obj.type = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            LinkLayerDiscoveryProtocolElementReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(LinkLayerDiscoveryProtocolElementReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class LogicalUnitReader(Reader):

    def __init__(self):
        super(LogicalUnitReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.LogicalUnit()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'discard_max_size':
                obj.discard_max_size = Reader.read_integer(reader)
            elif tag == 'discard_zeroes_data':
                obj.discard_zeroes_data = Reader.read_boolean(reader)
            elif tag == 'disk_id':
                obj.disk_id = Reader.read_string(reader)
            elif tag == 'lun_mapping':
                obj.lun_mapping = Reader.read_integer(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'paths':
                obj.paths = Reader.read_integer(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'portal':
                obj.portal = Reader.read_string(reader)
            elif tag == 'product_id':
                obj.product_id = Reader.read_string(reader)
            elif tag == 'serial':
                obj.serial = Reader.read_string(reader)
            elif tag == 'size':
                obj.size = Reader.read_integer(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.LunStatus, reader)
            elif tag == 'storage_domain_id':
                obj.storage_domain_id = Reader.read_string(reader)
            elif tag == 'target':
                obj.target = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'vendor_id':
                obj.vendor_id = Reader.read_string(reader)
            elif tag == 'volume_group_id':
                obj.volume_group_id = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            LogicalUnitReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(LogicalUnitReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class MDevTypeReader(Reader):

    def __init__(self):
        super(MDevTypeReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.MDevType()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'available_instances':
                obj.available_instances = Reader.read_integer(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'human_readable_name':
                obj.human_readable_name = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            MDevTypeReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MDevTypeReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class MacReader(Reader):

    def __init__(self):
        super(MacReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Mac()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            MacReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MacReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class MacPoolReader(Reader):

    def __init__(self):
        super(MacPoolReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.MacPool()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'allow_duplicates':
                obj.allow_duplicates = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'default_pool':
                obj.default_pool = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'ranges':
                obj.ranges = RangeReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            MacPoolReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MacPoolReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)


class MemoryOverCommitReader(Reader):

    def __init__(self):
        super(MemoryOverCommitReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.MemoryOverCommit()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'percent':
                obj.percent = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            MemoryOverCommitReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MemoryOverCommitReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class MemoryPolicyReader(Reader):

    def __init__(self):
        super(MemoryPolicyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.MemoryPolicy()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'ballooning':
                obj.ballooning = Reader.read_boolean(reader)
            elif tag == 'guaranteed':
                obj.guaranteed = Reader.read_integer(reader)
            elif tag == 'max':
                obj.max = Reader.read_integer(reader)
            elif tag == 'over_commit':
                obj.over_commit = MemoryOverCommitReader.read_one(reader)
            elif tag == 'transparent_hugepages':
                obj.transparent_huge_pages = TransparentHugePagesReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            MemoryPolicyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MemoryPolicyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class MethodReader(Reader):

    def __init__(self):
        super(MethodReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Method()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = types.SsoMethod(value.lower())

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        reader.next_element()

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MethodReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class MigrationBandwidthReader(Reader):

    def __init__(self):
        super(MigrationBandwidthReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.MigrationBandwidth()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'assignment_method':
                obj.assignment_method = Reader.read_enum(types.MigrationBandwidthAssignmentMethod, reader)
            elif tag == 'custom_value':
                obj.custom_value = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            MigrationBandwidthReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MigrationBandwidthReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class MigrationOptionsReader(Reader):

    def __init__(self):
        super(MigrationOptionsReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.MigrationOptions()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'auto_converge':
                obj.auto_converge = Reader.read_enum(types.InheritableBoolean, reader)
            elif tag == 'bandwidth':
                obj.bandwidth = MigrationBandwidthReader.read_one(reader)
            elif tag == 'compressed':
                obj.compressed = Reader.read_enum(types.InheritableBoolean, reader)
            elif tag == 'encrypted':
                obj.encrypted = Reader.read_enum(types.InheritableBoolean, reader)
            elif tag == 'policy':
                obj.policy = MigrationPolicyReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            MigrationOptionsReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MigrationOptionsReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class MigrationPolicyReader(Reader):

    def __init__(self):
        super(MigrationPolicyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.MigrationPolicy()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            MigrationPolicyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(MigrationPolicyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class NetworkReader(Reader):

    def __init__(self):
        super(NetworkReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Network()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'display':
                obj.display = Reader.read_boolean(reader)
            elif tag == 'dns_resolver_configuration':
                obj.dns_resolver_configuration = DnsResolverConfigurationReader.read_one(reader)
            elif tag == 'external_provider':
                obj.external_provider = OpenStackNetworkProviderReader.read_one(reader)
            elif tag == 'external_provider_physical_network':
                obj.external_provider_physical_network = NetworkReader.read_one(reader)
            elif tag == 'ip':
                obj.ip = IpReader.read_one(reader)
            elif tag == 'mtu':
                obj.mtu = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'network_labels':
                obj.network_labels = NetworkLabelReader.read_many(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'port_isolation':
                obj.port_isolation = Reader.read_boolean(reader)
            elif tag == 'profile_required':
                obj.profile_required = Reader.read_boolean(reader)
            elif tag == 'qos':
                obj.qos = QosReader.read_one(reader)
            elif tag == 'required':
                obj.required = Reader.read_boolean(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.NetworkStatus, reader)
            elif tag == 'stp':
                obj.stp = Reader.read_boolean(reader)
            elif tag == 'usages':
                obj.usages = Reader.read_enums(types.NetworkUsage, reader)
            elif tag == 'vdsm_name':
                obj.vdsm_name = Reader.read_string(reader)
            elif tag == 'vlan':
                obj.vlan = VlanReader.read_one(reader)
            elif tag == 'vnic_profiles':
                obj.vnic_profiles = VnicProfileReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            NetworkReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NetworkReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "networklabels":
                if obj.network_labels is not None:
                    obj.network_labels.href = href
                else:
                    obj.network_labels = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "vnicprofiles":
                if obj.vnic_profiles is not None:
                    obj.vnic_profiles.href = href
                else:
                    obj.vnic_profiles = List(href)


class NetworkAttachmentReader(Reader):

    def __init__(self):
        super(NetworkAttachmentReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NetworkAttachment()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'dns_resolver_configuration':
                obj.dns_resolver_configuration = DnsResolverConfigurationReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'host_nic':
                obj.host_nic = HostNicReader.read_one(reader)
            elif tag == 'in_sync':
                obj.in_sync = Reader.read_boolean(reader)
            elif tag == 'ip_address_assignments':
                obj.ip_address_assignments = IpAddressAssignmentReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'network':
                obj.network = NetworkReader.read_one(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'qos':
                obj.qos = QosReader.read_one(reader)
            elif tag == 'reported_configurations':
                obj.reported_configurations = ReportedConfigurationReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            NetworkAttachmentReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NetworkAttachmentReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class NetworkConfigurationReader(Reader):

    def __init__(self):
        super(NetworkConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NetworkConfiguration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'dns':
                obj.dns = DnsReader.read_one(reader)
            elif tag == 'nics':
                obj.nics = NicReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            NetworkConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NetworkConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class NetworkFilterReader(Reader):

    def __init__(self):
        super(NetworkFilterReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NetworkFilter()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'version':
                obj.version = VersionReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            NetworkFilterReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NetworkFilterReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class NetworkFilterParameterReader(Reader):

    def __init__(self):
        super(NetworkFilterParameterReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NetworkFilterParameter()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'nic':
                obj.nic = NicReader.read_one(reader)
            elif tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            NetworkFilterParameterReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NetworkFilterParameterReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class NetworkLabelReader(Reader):

    def __init__(self):
        super(NetworkLabelReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NetworkLabel()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'host_nic':
                obj.host_nic = HostNicReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'network':
                obj.network = NetworkReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            NetworkLabelReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NetworkLabelReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class NfsProfileDetailReader(Reader):

    def __init__(self):
        super(NfsProfileDetailReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NfsProfileDetail()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'nfs_server_ip':
                obj.nfs_server_ip = Reader.read_string(reader)
            elif tag == 'profile_details':
                obj.profile_details = ProfileDetailReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            NfsProfileDetailReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NfsProfileDetailReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class NicReader(Reader):

    def __init__(self):
        super(NicReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Nic()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'boot_protocol':
                obj.boot_protocol = Reader.read_enum(types.BootProtocol, reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'interface':
                obj.interface = Reader.read_enum(types.NicInterface, reader)
            elif tag == 'linked':
                obj.linked = Reader.read_boolean(reader)
            elif tag == 'mac':
                obj.mac = MacReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'network':
                obj.network = NetworkReader.read_one(reader)
            elif tag == 'network_attachments':
                obj.network_attachments = NetworkAttachmentReader.read_many(reader)
            elif tag == 'network_filter_parameters':
                obj.network_filter_parameters = NetworkFilterParameterReader.read_many(reader)
            elif tag == 'network_labels':
                obj.network_labels = NetworkLabelReader.read_many(reader)
            elif tag == 'on_boot':
                obj.on_boot = Reader.read_boolean(reader)
            elif tag == 'plugged':
                obj.plugged = Reader.read_boolean(reader)
            elif tag == 'reported_devices':
                obj.reported_devices = ReportedDeviceReader.read_many(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'synced':
                obj.synced = Reader.read_boolean(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'virtual_function_allowed_labels':
                obj.virtual_function_allowed_labels = NetworkLabelReader.read_many(reader)
            elif tag == 'virtual_function_allowed_networks':
                obj.virtual_function_allowed_networks = NetworkReader.read_many(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'vnic_profile':
                obj.vnic_profile = VnicProfileReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            NicReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NicReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "networkattachments":
                if obj.network_attachments is not None:
                    obj.network_attachments.href = href
                else:
                    obj.network_attachments = List(href)
            elif rel == "networkfilterparameters":
                if obj.network_filter_parameters is not None:
                    obj.network_filter_parameters.href = href
                else:
                    obj.network_filter_parameters = List(href)
            elif rel == "networklabels":
                if obj.network_labels is not None:
                    obj.network_labels.href = href
                else:
                    obj.network_labels = List(href)
            elif rel == "reporteddevices":
                if obj.reported_devices is not None:
                    obj.reported_devices.href = href
                else:
                    obj.reported_devices = List(href)
            elif rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)
            elif rel == "virtualfunctionallowedlabels":
                if obj.virtual_function_allowed_labels is not None:
                    obj.virtual_function_allowed_labels.href = href
                else:
                    obj.virtual_function_allowed_labels = List(href)
            elif rel == "virtualfunctionallowednetworks":
                if obj.virtual_function_allowed_networks is not None:
                    obj.virtual_function_allowed_networks.href = href
                else:
                    obj.virtual_function_allowed_networks = List(href)
            elif rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class NicConfigurationReader(Reader):

    def __init__(self):
        super(NicConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NicConfiguration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'boot_protocol':
                obj.boot_protocol = Reader.read_enum(types.BootProtocol, reader)
            elif tag == 'ip':
                obj.ip = IpReader.read_one(reader)
            elif tag == 'ipv6':
                obj.ipv6 = IpReader.read_one(reader)
            elif tag == 'ipv6_boot_protocol':
                obj.ipv6_boot_protocol = Reader.read_enum(types.BootProtocol, reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'on_boot':
                obj.on_boot = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            NicConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NicConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class NumaNodeReader(Reader):

    def __init__(self):
        super(NumaNodeReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NumaNode()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'index':
                obj.index = Reader.read_integer(reader)
            elif tag == 'memory':
                obj.memory = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'node_distance':
                obj.node_distance = Reader.read_string(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            NumaNodeReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NumaNodeReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)


class NumaNodePinReader(Reader):

    def __init__(self):
        super(NumaNodePinReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.NumaNodePin()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'host_numa_node':
                obj.host_numa_node = NumaNodeReader.read_one(reader)
            elif tag == 'index':
                obj.index = Reader.read_integer(reader)
            elif tag == 'pinned':
                obj.pinned = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            NumaNodePinReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(NumaNodePinReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OpenStackImageReader(Reader):

    def __init__(self):
        super(OpenStackImageReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenStackImage()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'openstack_image_provider':
                obj.openstack_image_provider = OpenStackImageProviderReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            OpenStackImageReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenStackImageReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OpenStackImageProviderReader(Reader):

    def __init__(self):
        super(OpenStackImageProviderReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenStackImageProvider()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'authentication_url':
                obj.authentication_url = Reader.read_string(reader)
            elif tag == 'certificates':
                obj.certificates = CertificateReader.read_many(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'images':
                obj.images = OpenStackImageReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'requires_authentication':
                obj.requires_authentication = Reader.read_boolean(reader)
            elif tag == 'tenant_name':
                obj.tenant_name = Reader.read_string(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            OpenStackImageProviderReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenStackImageProviderReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "certificates":
                if obj.certificates is not None:
                    obj.certificates.href = href
                else:
                    obj.certificates = List(href)
            elif rel == "images":
                if obj.images is not None:
                    obj.images.href = href
                else:
                    obj.images = List(href)


class OpenStackNetworkReader(Reader):

    def __init__(self):
        super(OpenStackNetworkReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenStackNetwork()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'openstack_network_provider':
                obj.openstack_network_provider = OpenStackNetworkProviderReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            OpenStackNetworkReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenStackNetworkReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OpenStackNetworkProviderReader(Reader):

    def __init__(self):
        super(OpenStackNetworkProviderReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenStackNetworkProvider()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'agent_configuration':
                obj.agent_configuration = AgentConfigurationReader.read_one(reader)
            elif tag == 'authentication_url':
                obj.authentication_url = Reader.read_string(reader)
            elif tag == 'auto_sync':
                obj.auto_sync = Reader.read_boolean(reader)
            elif tag == 'certificates':
                obj.certificates = CertificateReader.read_many(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'external_plugin_type':
                obj.external_plugin_type = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'networks':
                obj.networks = OpenStackNetworkReader.read_many(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'plugin_type':
                obj.plugin_type = Reader.read_enum(types.NetworkPluginType, reader)
            elif tag == 'project_domain_name':
                obj.project_domain_name = Reader.read_string(reader)
            elif tag == 'project_name':
                obj.project_name = Reader.read_string(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'read_only':
                obj.read_only = Reader.read_boolean(reader)
            elif tag == 'requires_authentication':
                obj.requires_authentication = Reader.read_boolean(reader)
            elif tag == 'subnets':
                obj.subnets = OpenStackSubnetReader.read_many(reader)
            elif tag == 'tenant_name':
                obj.tenant_name = Reader.read_string(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.OpenStackNetworkProviderType, reader)
            elif tag == 'unmanaged':
                obj.unmanaged = Reader.read_boolean(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            elif tag == 'user_domain_name':
                obj.user_domain_name = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            OpenStackNetworkProviderReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenStackNetworkProviderReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "certificates":
                if obj.certificates is not None:
                    obj.certificates.href = href
                else:
                    obj.certificates = List(href)
            elif rel == "networks":
                if obj.networks is not None:
                    obj.networks.href = href
                else:
                    obj.networks = List(href)
            elif rel == "subnets":
                if obj.subnets is not None:
                    obj.subnets.href = href
                else:
                    obj.subnets = List(href)


class OpenStackProviderReader(Reader):

    def __init__(self):
        super(OpenStackProviderReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenStackProvider()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'authentication_url':
                obj.authentication_url = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'requires_authentication':
                obj.requires_authentication = Reader.read_boolean(reader)
            elif tag == 'tenant_name':
                obj.tenant_name = Reader.read_string(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            OpenStackProviderReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenStackProviderReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OpenStackSubnetReader(Reader):

    def __init__(self):
        super(OpenStackSubnetReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenStackSubnet()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cidr':
                obj.cidr = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'dns_servers':
                obj.dns_servers = Reader.read_strings(reader)
            elif tag == 'gateway':
                obj.gateway = Reader.read_string(reader)
            elif tag == 'ip_version':
                obj.ip_version = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'openstack_network':
                obj.openstack_network = OpenStackNetworkReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            OpenStackSubnetReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenStackSubnetReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OpenStackVolumeProviderReader(Reader):

    def __init__(self):
        super(OpenStackVolumeProviderReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenStackVolumeProvider()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'authentication_keys':
                obj.authentication_keys = OpenstackVolumeAuthenticationKeyReader.read_many(reader)
            elif tag == 'authentication_url':
                obj.authentication_url = Reader.read_string(reader)
            elif tag == 'certificates':
                obj.certificates = CertificateReader.read_many(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'requires_authentication':
                obj.requires_authentication = Reader.read_boolean(reader)
            elif tag == 'tenant_name':
                obj.tenant_name = Reader.read_string(reader)
            elif tag == 'url':
                obj.url = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'volume_types':
                obj.volume_types = OpenStackVolumeTypeReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            OpenStackVolumeProviderReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenStackVolumeProviderReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "authenticationkeys":
                if obj.authentication_keys is not None:
                    obj.authentication_keys.href = href
                else:
                    obj.authentication_keys = List(href)
            elif rel == "certificates":
                if obj.certificates is not None:
                    obj.certificates.href = href
                else:
                    obj.certificates = List(href)
            elif rel == "volumetypes":
                if obj.volume_types is not None:
                    obj.volume_types.href = href
                else:
                    obj.volume_types = List(href)


class OpenStackVolumeTypeReader(Reader):

    def __init__(self):
        super(OpenStackVolumeTypeReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenStackVolumeType()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'openstack_volume_provider':
                obj.openstack_volume_provider = OpenStackVolumeProviderReader.read_one(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            OpenStackVolumeTypeReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenStackVolumeTypeReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OpenstackVolumeAuthenticationKeyReader(Reader):

    def __init__(self):
        super(OpenstackVolumeAuthenticationKeyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OpenstackVolumeAuthenticationKey()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'creation_date':
                obj.creation_date = Reader.read_date(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'openstack_volume_provider':
                obj.openstack_volume_provider = OpenStackVolumeProviderReader.read_one(reader)
            elif tag == 'usage_type':
                obj.usage_type = Reader.read_enum(types.OpenstackVolumeAuthenticationKeyUsageType, reader)
            elif tag == 'uuid':
                obj.uuid = Reader.read_string(reader)
            elif tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            OpenstackVolumeAuthenticationKeyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OpenstackVolumeAuthenticationKeyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OperatingSystemReader(Reader):

    def __init__(self):
        super(OperatingSystemReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OperatingSystem()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'boot':
                obj.boot = BootReader.read_one(reader)
            elif tag == 'cmdline':
                obj.cmdline = Reader.read_string(reader)
            elif tag == 'custom_kernel_cmdline':
                obj.custom_kernel_cmdline = Reader.read_string(reader)
            elif tag == 'initrd':
                obj.initrd = Reader.read_string(reader)
            elif tag == 'kernel':
                obj.kernel = Reader.read_string(reader)
            elif tag == 'reported_kernel_cmdline':
                obj.reported_kernel_cmdline = Reader.read_string(reader)
            elif tag == 'type':
                obj.type = Reader.read_string(reader)
            elif tag == 'version':
                obj.version = VersionReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            OperatingSystemReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OperatingSystemReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OperatingSystemInfoReader(Reader):

    def __init__(self):
        super(OperatingSystemInfoReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.OperatingSystemInfo()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'architecture':
                obj.architecture = Reader.read_enum(types.Architecture, reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'large_icon':
                obj.large_icon = IconReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'small_icon':
                obj.small_icon = IconReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            OperatingSystemInfoReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OperatingSystemInfoReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class OptionReader(Reader):

    def __init__(self):
        super(OptionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Option()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'type':
                obj.type = Reader.read_string(reader)
            elif tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            OptionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(OptionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class PackageReader(Reader):

    def __init__(self):
        super(PackageReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Package()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            PackageReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(PackageReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class PayloadReader(Reader):

    def __init__(self):
        super(PayloadReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Payload()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'files':
                obj.files = FileReader.read_many(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.VmDeviceType, reader)
            elif tag == 'volume_id':
                obj.volume_id = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            PayloadReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(PayloadReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class PermissionReader(Reader):

    def __init__(self):
        super(PermissionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Permission()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk':
                obj.disk = DiskReader.read_one(reader)
            elif tag == 'group':
                obj.group = GroupReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'role':
                obj.role = RoleReader.read_one(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vm_pool':
                obj.vm_pool = VmPoolReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            PermissionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(PermissionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class PermitReader(Reader):

    def __init__(self):
        super(PermitReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Permit()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'administrative':
                obj.administrative = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'role':
                obj.role = RoleReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            PermitReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(PermitReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class PmProxyReader(Reader):

    def __init__(self):
        super(PmProxyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.PmProxy()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'type':
                obj.type = Reader.read_enum(types.PmProxyType, reader)
            else:
                reader.next_element()
        for link in links:
            PmProxyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(PmProxyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class PortMirroringReader(Reader):

    def __init__(self):
        super(PortMirroringReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.PortMirroring()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        reader.next_element()

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(PortMirroringReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class PowerManagementReader(Reader):

    def __init__(self):
        super(PowerManagementReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.PowerManagement()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'agents':
                obj.agents = AgentReader.read_many(reader)
            elif tag == 'automatic_pm_enabled':
                obj.automatic_pm_enabled = Reader.read_boolean(reader)
            elif tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            elif tag == 'kdump_detection':
                obj.kdump_detection = Reader.read_boolean(reader)
            elif tag == 'options':
                obj.options = OptionReader.read_many(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'pm_proxies':
                obj.pm_proxies = PmProxyReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.PowerManagementStatus, reader)
            elif tag == 'type':
                obj.type = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            PowerManagementReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(PowerManagementReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ProductReader(Reader):

    def __init__(self):
        super(ProductReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Product()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ProductReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ProductReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ProductInfoReader(Reader):

    def __init__(self):
        super(ProductInfoReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ProductInfo()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'instance_id':
                obj.instance_id = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'vendor':
                obj.vendor = Reader.read_string(reader)
            elif tag == 'version':
                obj.version = VersionReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            ProductInfoReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ProductInfoReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ProfileDetailReader(Reader):

    def __init__(self):
        super(ProfileDetailReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ProfileDetail()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'block_statistics':
                obj.block_statistics = BlockStatisticReader.read_many(reader)
            elif tag == 'duration':
                obj.duration = Reader.read_integer(reader)
            elif tag == 'fop_statistics':
                obj.fop_statistics = FopStatisticReader.read_many(reader)
            elif tag == 'profile_type':
                obj.profile_type = Reader.read_string(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            ProfileDetailReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ProfileDetailReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class PropertyReader(Reader):

    def __init__(self):
        super(PropertyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Property()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            PropertyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(PropertyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ProxyTicketReader(Reader):

    def __init__(self):
        super(ProxyTicketReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ProxyTicket()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ProxyTicketReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ProxyTicketReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class QosReader(Reader):

    def __init__(self):
        super(QosReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Qos()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'cpu_limit':
                obj.cpu_limit = Reader.read_integer(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'inbound_average':
                obj.inbound_average = Reader.read_integer(reader)
            elif tag == 'inbound_burst':
                obj.inbound_burst = Reader.read_integer(reader)
            elif tag == 'inbound_peak':
                obj.inbound_peak = Reader.read_integer(reader)
            elif tag == 'max_iops':
                obj.max_iops = Reader.read_integer(reader)
            elif tag == 'max_read_iops':
                obj.max_read_iops = Reader.read_integer(reader)
            elif tag == 'max_read_throughput':
                obj.max_read_throughput = Reader.read_integer(reader)
            elif tag == 'max_throughput':
                obj.max_throughput = Reader.read_integer(reader)
            elif tag == 'max_write_iops':
                obj.max_write_iops = Reader.read_integer(reader)
            elif tag == 'max_write_throughput':
                obj.max_write_throughput = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'outbound_average':
                obj.outbound_average = Reader.read_integer(reader)
            elif tag == 'outbound_average_linkshare':
                obj.outbound_average_linkshare = Reader.read_integer(reader)
            elif tag == 'outbound_average_realtime':
                obj.outbound_average_realtime = Reader.read_integer(reader)
            elif tag == 'outbound_average_upperlimit':
                obj.outbound_average_upperlimit = Reader.read_integer(reader)
            elif tag == 'outbound_burst':
                obj.outbound_burst = Reader.read_integer(reader)
            elif tag == 'outbound_peak':
                obj.outbound_peak = Reader.read_integer(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.QosType, reader)
            else:
                reader.next_element()
        for link in links:
            QosReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(QosReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class QuotaReader(Reader):

    def __init__(self):
        super(QuotaReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Quota()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster_hard_limit_pct':
                obj.cluster_hard_limit_pct = Reader.read_integer(reader)
            elif tag == 'cluster_soft_limit_pct':
                obj.cluster_soft_limit_pct = Reader.read_integer(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disks':
                obj.disks = DiskReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'quota_cluster_limits':
                obj.quota_cluster_limits = QuotaClusterLimitReader.read_many(reader)
            elif tag == 'quota_storage_limits':
                obj.quota_storage_limits = QuotaStorageLimitReader.read_many(reader)
            elif tag == 'storage_hard_limit_pct':
                obj.storage_hard_limit_pct = Reader.read_integer(reader)
            elif tag == 'storage_soft_limit_pct':
                obj.storage_soft_limit_pct = Reader.read_integer(reader)
            elif tag == 'users':
                obj.users = UserReader.read_many(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            QuotaReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(QuotaReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "quotaclusterlimits":
                if obj.quota_cluster_limits is not None:
                    obj.quota_cluster_limits.href = href
                else:
                    obj.quota_cluster_limits = List(href)
            elif rel == "quotastoragelimits":
                if obj.quota_storage_limits is not None:
                    obj.quota_storage_limits.href = href
                else:
                    obj.quota_storage_limits = List(href)


class QuotaClusterLimitReader(Reader):

    def __init__(self):
        super(QuotaClusterLimitReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.QuotaClusterLimit()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'memory_limit':
                obj.memory_limit = Reader.read_decimal(reader)
            elif tag == 'memory_usage':
                obj.memory_usage = Reader.read_decimal(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'vcpu_limit':
                obj.vcpu_limit = Reader.read_integer(reader)
            elif tag == 'vcpu_usage':
                obj.vcpu_usage = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            QuotaClusterLimitReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(QuotaClusterLimitReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class QuotaStorageLimitReader(Reader):

    def __init__(self):
        super(QuotaStorageLimitReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.QuotaStorageLimit()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'limit':
                obj.limit = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'usage':
                obj.usage = Reader.read_decimal(reader)
            else:
                reader.next_element()
        for link in links:
            QuotaStorageLimitReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(QuotaStorageLimitReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RangeReader(Reader):

    def __init__(self):
        super(RangeReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Range()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'from':
                obj.from_ = Reader.read_string(reader)
            elif tag == 'to':
                obj.to = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            RangeReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RangeReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RateReader(Reader):

    def __init__(self):
        super(RateReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Rate()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'bytes':
                obj.bytes = Reader.read_integer(reader)
            elif tag == 'period':
                obj.period = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            RateReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RateReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RegistrationAffinityGroupMappingReader(Reader):

    def __init__(self):
        super(RegistrationAffinityGroupMappingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RegistrationAffinityGroupMapping()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'from':
                obj.from_ = AffinityGroupReader.read_one(reader)
            elif tag == 'to':
                obj.to = AffinityGroupReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            RegistrationAffinityGroupMappingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RegistrationAffinityGroupMappingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RegistrationAffinityLabelMappingReader(Reader):

    def __init__(self):
        super(RegistrationAffinityLabelMappingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RegistrationAffinityLabelMapping()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'from':
                obj.from_ = AffinityLabelReader.read_one(reader)
            elif tag == 'to':
                obj.to = AffinityLabelReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            RegistrationAffinityLabelMappingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RegistrationAffinityLabelMappingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RegistrationClusterMappingReader(Reader):

    def __init__(self):
        super(RegistrationClusterMappingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RegistrationClusterMapping()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'from':
                obj.from_ = ClusterReader.read_one(reader)
            elif tag == 'to':
                obj.to = ClusterReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            RegistrationClusterMappingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RegistrationClusterMappingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RegistrationConfigurationReader(Reader):

    def __init__(self):
        super(RegistrationConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RegistrationConfiguration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'affinity_group_mappings':
                obj.affinity_group_mappings = RegistrationAffinityGroupMappingReader.read_many(reader)
            elif tag == 'affinity_label_mappings':
                obj.affinity_label_mappings = RegistrationAffinityLabelMappingReader.read_many(reader)
            elif tag == 'cluster_mappings':
                obj.cluster_mappings = RegistrationClusterMappingReader.read_many(reader)
            elif tag == 'domain_mappings':
                obj.domain_mappings = RegistrationDomainMappingReader.read_many(reader)
            elif tag == 'lun_mappings':
                obj.lun_mappings = RegistrationLunMappingReader.read_many(reader)
            elif tag == 'role_mappings':
                obj.role_mappings = RegistrationRoleMappingReader.read_many(reader)
            elif tag == 'vnic_profile_mappings':
                obj.vnic_profile_mappings = RegistrationVnicProfileMappingReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            RegistrationConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RegistrationConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RegistrationDomainMappingReader(Reader):

    def __init__(self):
        super(RegistrationDomainMappingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RegistrationDomainMapping()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'from':
                obj.from_ = DomainReader.read_one(reader)
            elif tag == 'to':
                obj.to = DomainReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            RegistrationDomainMappingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RegistrationDomainMappingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RegistrationLunMappingReader(Reader):

    def __init__(self):
        super(RegistrationLunMappingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RegistrationLunMapping()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'from':
                obj.from_ = DiskReader.read_one(reader)
            elif tag == 'to':
                obj.to = DiskReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            RegistrationLunMappingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RegistrationLunMappingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RegistrationRoleMappingReader(Reader):

    def __init__(self):
        super(RegistrationRoleMappingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RegistrationRoleMapping()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'from':
                obj.from_ = RoleReader.read_one(reader)
            elif tag == 'to':
                obj.to = RoleReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            RegistrationRoleMappingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RegistrationRoleMappingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RegistrationVnicProfileMappingReader(Reader):

    def __init__(self):
        super(RegistrationVnicProfileMappingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RegistrationVnicProfileMapping()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'from':
                obj.from_ = VnicProfileReader.read_one(reader)
            elif tag == 'to':
                obj.to = VnicProfileReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            RegistrationVnicProfileMappingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RegistrationVnicProfileMappingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ReportedConfigurationReader(Reader):

    def __init__(self):
        super(ReportedConfigurationReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ReportedConfiguration()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'actual_value':
                obj.actual_value = Reader.read_string(reader)
            elif tag == 'expected_value':
                obj.expected_value = Reader.read_string(reader)
            elif tag == 'in_sync':
                obj.in_sync = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ReportedConfigurationReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ReportedConfigurationReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ReportedDeviceReader(Reader):

    def __init__(self):
        super(ReportedDeviceReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.ReportedDevice()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'ips':
                obj.ips = IpReader.read_many(reader)
            elif tag == 'mac':
                obj.mac = MacReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.ReportedDeviceType, reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            ReportedDeviceReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ReportedDeviceReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RngDeviceReader(Reader):

    def __init__(self):
        super(RngDeviceReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.RngDevice()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'rate':
                obj.rate = RateReader.read_one(reader)
            elif tag == 'source':
                obj.source = Reader.read_enum(types.RngSource, reader)
            else:
                reader.next_element()
        for link in links:
            RngDeviceReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RngDeviceReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class RoleReader(Reader):

    def __init__(self):
        super(RoleReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Role()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'administrative':
                obj.administrative = Reader.read_boolean(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'mutable':
                obj.mutable = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'permits':
                obj.permits = PermitReader.read_many(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            RoleReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(RoleReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "permits":
                if obj.permits is not None:
                    obj.permits.href = href
                else:
                    obj.permits = List(href)


class SchedulingPolicyReader(Reader):

    def __init__(self):
        super(SchedulingPolicyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SchedulingPolicy()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'balances':
                obj.balances = BalanceReader.read_many(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'default_policy':
                obj.default_policy = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'filters':
                obj.filters = FilterReader.read_many(reader)
            elif tag == 'locked':
                obj.locked = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'weight':
                obj.weight = WeightReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            SchedulingPolicyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SchedulingPolicyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "balances":
                if obj.balances is not None:
                    obj.balances.href = href
                else:
                    obj.balances = List(href)
            elif rel == "filters":
                if obj.filters is not None:
                    obj.filters.href = href
                else:
                    obj.filters = List(href)
            elif rel == "weight":
                if obj.weight is not None:
                    obj.weight.href = href
                else:
                    obj.weight = List(href)


class SchedulingPolicyUnitReader(Reader):

    def __init__(self):
        super(SchedulingPolicyUnitReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SchedulingPolicyUnit()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            elif tag == 'internal':
                obj.internal = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'properties':
                obj.properties = PropertyReader.read_many(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.PolicyUnitType, reader)
            else:
                reader.next_element()
        for link in links:
            SchedulingPolicyUnitReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SchedulingPolicyUnitReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SeLinuxReader(Reader):

    def __init__(self):
        super(SeLinuxReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SeLinux()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'mode':
                obj.mode = Reader.read_enum(types.SeLinuxMode, reader)
            else:
                reader.next_element()
        for link in links:
            SeLinuxReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SeLinuxReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SerialNumberReader(Reader):

    def __init__(self):
        super(SerialNumberReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SerialNumber()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'policy':
                obj.policy = Reader.read_enum(types.SerialNumberPolicy, reader)
            elif tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            SerialNumberReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SerialNumberReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SessionReader(Reader):

    def __init__(self):
        super(SessionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Session()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'console_user':
                obj.console_user = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'ip':
                obj.ip = IpReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'protocol':
                obj.protocol = Reader.read_string(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            SessionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SessionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SkipIfConnectivityBrokenReader(Reader):

    def __init__(self):
        super(SkipIfConnectivityBrokenReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SkipIfConnectivityBroken()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            elif tag == 'threshold':
                obj.threshold = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            SkipIfConnectivityBrokenReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SkipIfConnectivityBrokenReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SkipIfSdActiveReader(Reader):

    def __init__(self):
        super(SkipIfSdActiveReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SkipIfSdActive()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            SkipIfSdActiveReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SkipIfSdActiveReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SnapshotReader(Reader):

    def __init__(self):
        super(SnapshotReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Snapshot()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'affinity_labels':
                obj.affinity_labels = AffinityLabelReader.read_many(reader)
            elif tag == 'applications':
                obj.applications = ApplicationReader.read_many(reader)
            elif tag == 'auto_pinning_policy':
                obj.auto_pinning_policy = Reader.read_enum(types.AutoPinningPolicy, reader)
            elif tag == 'bios':
                obj.bios = BiosReader.read_one(reader)
            elif tag == 'cdroms':
                obj.cdroms = CdromReader.read_many(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'console':
                obj.console = ConsoleReader.read_one(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'cpu_profile':
                obj.cpu_profile = CpuProfileReader.read_one(reader)
            elif tag == 'cpu_shares':
                obj.cpu_shares = Reader.read_integer(reader)
            elif tag == 'creation_time':
                obj.creation_time = Reader.read_date(reader)
            elif tag == 'custom_compatibility_version':
                obj.custom_compatibility_version = VersionReader.read_one(reader)
            elif tag == 'custom_cpu_model':
                obj.custom_cpu_model = Reader.read_string(reader)
            elif tag == 'custom_emulated_machine':
                obj.custom_emulated_machine = Reader.read_string(reader)
            elif tag == 'custom_properties':
                obj.custom_properties = CustomPropertyReader.read_many(reader)
            elif tag == 'date':
                obj.date = Reader.read_date(reader)
            elif tag == 'delete_protected':
                obj.delete_protected = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk_attachments':
                obj.disk_attachments = DiskAttachmentReader.read_many(reader)
            elif tag == 'disks':
                obj.disks = DiskReader.read_many(reader)
            elif tag == 'display':
                obj.display = DisplayReader.read_one(reader)
            elif tag == 'domain':
                obj.domain = DomainReader.read_one(reader)
            elif tag == 'external_host_provider':
                obj.external_host_provider = ExternalHostProviderReader.read_one(reader)
            elif tag == 'floppies':
                obj.floppies = FloppyReader.read_many(reader)
            elif tag == 'fqdn':
                obj.fqdn = Reader.read_string(reader)
            elif tag == 'graphics_consoles':
                obj.graphics_consoles = GraphicsConsoleReader.read_many(reader)
            elif tag == 'guest_operating_system':
                obj.guest_operating_system = GuestOperatingSystemReader.read_one(reader)
            elif tag == 'guest_time_zone':
                obj.guest_time_zone = TimeZoneReader.read_one(reader)
            elif tag == 'has_illegal_images':
                obj.has_illegal_images = Reader.read_boolean(reader)
            elif tag == 'high_availability':
                obj.high_availability = HighAvailabilityReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'host_devices':
                obj.host_devices = HostDeviceReader.read_many(reader)
            elif tag == 'initialization':
                obj.initialization = InitializationReader.read_one(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'io':
                obj.io = IoReader.read_one(reader)
            elif tag == 'katello_errata':
                obj.katello_errata = KatelloErratumReader.read_many(reader)
            elif tag == 'large_icon':
                obj.large_icon = IconReader.read_one(reader)
            elif tag == 'lease':
                obj.lease = StorageDomainLeaseReader.read_one(reader)
            elif tag == 'memory':
                obj.memory = Reader.read_integer(reader)
            elif tag == 'memory_policy':
                obj.memory_policy = MemoryPolicyReader.read_one(reader)
            elif tag == 'migration':
                obj.migration = MigrationOptionsReader.read_one(reader)
            elif tag == 'migration_downtime':
                obj.migration_downtime = Reader.read_integer(reader)
            elif tag == 'multi_queues_enabled':
                obj.multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'next_run_configuration_exists':
                obj.next_run_configuration_exists = Reader.read_boolean(reader)
            elif tag == 'nics':
                obj.nics = NicReader.read_many(reader)
            elif tag == 'host_numa_nodes':
                obj.numa_nodes = NumaNodeReader.read_many(reader)
            elif tag == 'numa_tune_mode':
                obj.numa_tune_mode = Reader.read_enum(types.NumaTuneMode, reader)
            elif tag == 'origin':
                obj.origin = Reader.read_string(reader)
            elif tag == 'original_template':
                obj.original_template = TemplateReader.read_one(reader)
            elif tag == 'os':
                obj.os = OperatingSystemReader.read_one(reader)
            elif tag == 'payloads':
                obj.payloads = PayloadReader.read_many(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'persist_memorystate':
                obj.persist_memorystate = Reader.read_boolean(reader)
            elif tag == 'placement_policy':
                obj.placement_policy = VmPlacementPolicyReader.read_one(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'reported_devices':
                obj.reported_devices = ReportedDeviceReader.read_many(reader)
            elif tag == 'rng_device':
                obj.rng_device = RngDeviceReader.read_one(reader)
            elif tag == 'run_once':
                obj.run_once = Reader.read_boolean(reader)
            elif tag == 'serial_number':
                obj.serial_number = SerialNumberReader.read_one(reader)
            elif tag == 'sessions':
                obj.sessions = SessionReader.read_many(reader)
            elif tag == 'small_icon':
                obj.small_icon = IconReader.read_one(reader)
            elif tag == 'snapshot_status':
                obj.snapshot_status = Reader.read_enum(types.SnapshotStatus, reader)
            elif tag == 'snapshot_type':
                obj.snapshot_type = Reader.read_enum(types.SnapshotType, reader)
            elif tag == 'snapshots':
                obj.snapshots = SnapshotReader.read_many(reader)
            elif tag == 'soundcard_enabled':
                obj.soundcard_enabled = Reader.read_boolean(reader)
            elif tag == 'sso':
                obj.sso = SsoReader.read_one(reader)
            elif tag == 'start_paused':
                obj.start_paused = Reader.read_boolean(reader)
            elif tag == 'start_time':
                obj.start_time = Reader.read_date(reader)
            elif tag == 'stateless':
                obj.stateless = Reader.read_boolean(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.VmStatus, reader)
            elif tag == 'status_detail':
                obj.status_detail = Reader.read_string(reader)
            elif tag == 'stop_reason':
                obj.stop_reason = Reader.read_string(reader)
            elif tag == 'stop_time':
                obj.stop_time = Reader.read_date(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'storage_error_resume_behaviour':
                obj.storage_error_resume_behaviour = Reader.read_enum(types.VmStorageErrorResumeBehaviour, reader)
            elif tag == 'tags':
                obj.tags = TagReader.read_many(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'time_zone':
                obj.time_zone = TimeZoneReader.read_one(reader)
            elif tag == 'tpm_enabled':
                obj.tpm_enabled = Reader.read_boolean(reader)
            elif tag == 'tunnel_migration':
                obj.tunnel_migration = Reader.read_boolean(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.VmType, reader)
            elif tag == 'usb':
                obj.usb = UsbReader.read_one(reader)
            elif tag == 'use_latest_template_version':
                obj.use_latest_template_version = Reader.read_boolean(reader)
            elif tag == 'virtio_scsi':
                obj.virtio_scsi = VirtioScsiReader.read_one(reader)
            elif tag == 'virtio_scsi_multi_queues':
                obj.virtio_scsi_multi_queues = Reader.read_integer(reader)
            elif tag == 'virtio_scsi_multi_queues_enabled':
                obj.virtio_scsi_multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vm_pool':
                obj.vm_pool = VmPoolReader.read_one(reader)
            elif tag == 'watchdogs':
                obj.watchdogs = WatchdogReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            SnapshotReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SnapshotReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "affinitylabels":
                if obj.affinity_labels is not None:
                    obj.affinity_labels.href = href
                else:
                    obj.affinity_labels = List(href)
            elif rel == "applications":
                if obj.applications is not None:
                    obj.applications.href = href
                else:
                    obj.applications = List(href)
            elif rel == "cdroms":
                if obj.cdroms is not None:
                    obj.cdroms.href = href
                else:
                    obj.cdroms = List(href)
            elif rel == "diskattachments":
                if obj.disk_attachments is not None:
                    obj.disk_attachments.href = href
                else:
                    obj.disk_attachments = List(href)
            elif rel == "disks":
                if obj.disks is not None:
                    obj.disks.href = href
                else:
                    obj.disks = List(href)
            elif rel == "floppies":
                if obj.floppies is not None:
                    obj.floppies.href = href
                else:
                    obj.floppies = List(href)
            elif rel == "graphicsconsoles":
                if obj.graphics_consoles is not None:
                    obj.graphics_consoles.href = href
                else:
                    obj.graphics_consoles = List(href)
            elif rel == "hostdevices":
                if obj.host_devices is not None:
                    obj.host_devices.href = href
                else:
                    obj.host_devices = List(href)
            elif rel == "katelloerrata":
                if obj.katello_errata is not None:
                    obj.katello_errata.href = href
                else:
                    obj.katello_errata = List(href)
            elif rel == "nics":
                if obj.nics is not None:
                    obj.nics.href = href
                else:
                    obj.nics = List(href)
            elif rel == "numanodes":
                if obj.numa_nodes is not None:
                    obj.numa_nodes.href = href
                else:
                    obj.numa_nodes = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "reporteddevices":
                if obj.reported_devices is not None:
                    obj.reported_devices.href = href
                else:
                    obj.reported_devices = List(href)
            elif rel == "sessions":
                if obj.sessions is not None:
                    obj.sessions.href = href
                else:
                    obj.sessions = List(href)
            elif rel == "snapshots":
                if obj.snapshots is not None:
                    obj.snapshots.href = href
                else:
                    obj.snapshots = List(href)
            elif rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)
            elif rel == "tags":
                if obj.tags is not None:
                    obj.tags.href = href
                else:
                    obj.tags = List(href)
            elif rel == "watchdogs":
                if obj.watchdogs is not None:
                    obj.watchdogs.href = href
                else:
                    obj.watchdogs = List(href)


class SpecialObjectsReader(Reader):

    def __init__(self):
        super(SpecialObjectsReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SpecialObjects()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'blank_template':
                obj.blank_template = TemplateReader.read_one(reader)
            elif tag == 'root_tag':
                obj.root_tag = TagReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            SpecialObjectsReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SpecialObjectsReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SpmReader(Reader):

    def __init__(self):
        super(SpmReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Spm()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'priority':
                obj.priority = Reader.read_integer(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.SpmStatus, reader)
            else:
                reader.next_element()
        for link in links:
            SpmReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SpmReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SshReader(Reader):

    def __init__(self):
        super(SshReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Ssh()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'authentication_method':
                obj.authentication_method = Reader.read_enum(types.SshAuthenticationMethod, reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'fingerprint':
                obj.fingerprint = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'public_key':
                obj.public_key = Reader.read_string(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            SshReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SshReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SshPublicKeyReader(Reader):

    def __init__(self):
        super(SshPublicKeyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SshPublicKey()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'content':
                obj.content = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            SshPublicKeyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SshPublicKeyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SsoReader(Reader):

    def __init__(self):
        super(SsoReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Sso()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'methods':
                obj.methods = MethodReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            SsoReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SsoReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class StatisticReader(Reader):

    def __init__(self):
        super(StatisticReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Statistic()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'brick':
                obj.brick = GlusterBrickReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk':
                obj.disk = DiskReader.read_one(reader)
            elif tag == 'gluster_volume':
                obj.gluster_volume = GlusterVolumeReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'host_nic':
                obj.host_nic = HostNicReader.read_one(reader)
            elif tag == 'host_numa_node':
                obj.host_numa_node = NumaNodeReader.read_one(reader)
            elif tag == 'kind':
                obj.kind = Reader.read_enum(types.StatisticKind, reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'nic':
                obj.nic = NicReader.read_one(reader)
            elif tag == 'step':
                obj.step = StepReader.read_one(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.ValueType, reader)
            elif tag == 'unit':
                obj.unit = Reader.read_enum(types.StatisticUnit, reader)
            elif tag == 'values':
                obj.values = ValueReader.read_many(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            StatisticReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(StatisticReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class StepReader(Reader):

    def __init__(self):
        super(StepReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Step()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'end_time':
                obj.end_time = Reader.read_date(reader)
            elif tag == 'execution_host':
                obj.execution_host = HostReader.read_one(reader)
            elif tag == 'external':
                obj.external = Reader.read_boolean(reader)
            elif tag == 'external_type':
                obj.external_type = Reader.read_enum(types.ExternalSystemType, reader)
            elif tag == 'job':
                obj.job = JobReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'number':
                obj.number = Reader.read_integer(reader)
            elif tag == 'parent_step':
                obj.parent_step = StepReader.read_one(reader)
            elif tag == 'progress':
                obj.progress = Reader.read_integer(reader)
            elif tag == 'start_time':
                obj.start_time = Reader.read_date(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.StepStatus, reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.StepEnum, reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            StepReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(StepReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)


class StorageConnectionReader(Reader):

    def __init__(self):
        super(StorageConnectionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.StorageConnection()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'address':
                obj.address = Reader.read_string(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'gluster_volume':
                obj.gluster_volume = GlusterVolumeReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'mount_options':
                obj.mount_options = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'nfs_retrans':
                obj.nfs_retrans = Reader.read_integer(reader)
            elif tag == 'nfs_timeo':
                obj.nfs_timeo = Reader.read_integer(reader)
            elif tag == 'nfs_version':
                obj.nfs_version = Reader.read_enum(types.NfsVersion, reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'path':
                obj.path = Reader.read_string(reader)
            elif tag == 'port':
                obj.port = Reader.read_integer(reader)
            elif tag == 'portal':
                obj.portal = Reader.read_string(reader)
            elif tag == 'target':
                obj.target = Reader.read_string(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.StorageType, reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            elif tag == 'vfs_type':
                obj.vfs_type = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            StorageConnectionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(StorageConnectionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class StorageConnectionExtensionReader(Reader):

    def __init__(self):
        super(StorageConnectionExtensionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.StorageConnectionExtension()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'target':
                obj.target = Reader.read_string(reader)
            elif tag == 'username':
                obj.username = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            StorageConnectionExtensionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(StorageConnectionExtensionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class StorageDomainReader(Reader):

    def __init__(self):
        super(StorageDomainReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.StorageDomain()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'available':
                obj.available = Reader.read_integer(reader)
            elif tag == 'backup':
                obj.backup = Reader.read_boolean(reader)
            elif tag == 'block_size':
                obj.block_size = Reader.read_integer(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'committed':
                obj.committed = Reader.read_integer(reader)
            elif tag == 'critical_space_action_blocker':
                obj.critical_space_action_blocker = Reader.read_integer(reader)
            elif tag == 'data_center':
                obj.data_center = DataCenterReader.read_one(reader)
            elif tag == 'data_centers':
                obj.data_centers = DataCenterReader.read_many(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'discard_after_delete':
                obj.discard_after_delete = Reader.read_boolean(reader)
            elif tag == 'disk_profiles':
                obj.disk_profiles = DiskProfileReader.read_many(reader)
            elif tag == 'disk_snapshots':
                obj.disk_snapshots = DiskSnapshotReader.read_many(reader)
            elif tag == 'disks':
                obj.disks = DiskReader.read_many(reader)
            elif tag == 'external_status':
                obj.external_status = Reader.read_enum(types.ExternalStatus, reader)
            elif tag == 'files':
                obj.files = FileReader.read_many(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'images':
                obj.images = ImageReader.read_many(reader)
            elif tag == 'import':
                obj.import_ = Reader.read_boolean(reader)
            elif tag == 'master':
                obj.master = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.StorageDomainStatus, reader)
            elif tag == 'storage':
                obj.storage = HostStorageReader.read_one(reader)
            elif tag == 'storage_connections':
                obj.storage_connections = StorageConnectionReader.read_many(reader)
            elif tag == 'storage_format':
                obj.storage_format = Reader.read_enum(types.StorageFormat, reader)
            elif tag == 'supports_discard':
                obj.supports_discard = Reader.read_boolean(reader)
            elif tag == 'supports_discard_zeroes_data':
                obj.supports_discard_zeroes_data = Reader.read_boolean(reader)
            elif tag == 'templates':
                obj.templates = TemplateReader.read_many(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.StorageDomainType, reader)
            elif tag == 'used':
                obj.used = Reader.read_integer(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'warning_low_space_indicator':
                obj.warning_low_space_indicator = Reader.read_integer(reader)
            elif tag == 'wipe_after_delete':
                obj.wipe_after_delete = Reader.read_boolean(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            StorageDomainReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(StorageDomainReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "datacenters":
                if obj.data_centers is not None:
                    obj.data_centers.href = href
                else:
                    obj.data_centers = List(href)
            elif rel == "diskprofiles":
                if obj.disk_profiles is not None:
                    obj.disk_profiles.href = href
                else:
                    obj.disk_profiles = List(href)
            elif rel == "disksnapshots":
                if obj.disk_snapshots is not None:
                    obj.disk_snapshots.href = href
                else:
                    obj.disk_snapshots = List(href)
            elif rel == "disks":
                if obj.disks is not None:
                    obj.disks.href = href
                else:
                    obj.disks = List(href)
            elif rel == "files":
                if obj.files is not None:
                    obj.files.href = href
                else:
                    obj.files = List(href)
            elif rel == "images":
                if obj.images is not None:
                    obj.images.href = href
                else:
                    obj.images = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "storageconnections":
                if obj.storage_connections is not None:
                    obj.storage_connections.href = href
                else:
                    obj.storage_connections = List(href)
            elif rel == "templates":
                if obj.templates is not None:
                    obj.templates.href = href
                else:
                    obj.templates = List(href)
            elif rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class StorageDomainLeaseReader(Reader):

    def __init__(self):
        super(StorageDomainLeaseReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.StorageDomainLease()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            StorageDomainLeaseReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(StorageDomainLeaseReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SystemOptionReader(Reader):

    def __init__(self):
        super(SystemOptionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SystemOption()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'values':
                obj.values = SystemOptionValueReader.read_many(reader)
            else:
                reader.next_element()
        for link in links:
            SystemOptionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SystemOptionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class SystemOptionValueReader(Reader):

    def __init__(self):
        super(SystemOptionValueReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.SystemOptionValue()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'value':
                obj.value = Reader.read_string(reader)
            elif tag == 'version':
                obj.version = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            SystemOptionValueReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(SystemOptionValueReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class TagReader(Reader):

    def __init__(self):
        super(TagReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Tag()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'group':
                obj.group = GroupReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'parent':
                obj.parent = TagReader.read_one(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            TagReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(TagReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class TemplateReader(Reader):

    def __init__(self):
        super(TemplateReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Template()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'auto_pinning_policy':
                obj.auto_pinning_policy = Reader.read_enum(types.AutoPinningPolicy, reader)
            elif tag == 'bios':
                obj.bios = BiosReader.read_one(reader)
            elif tag == 'cdroms':
                obj.cdroms = CdromReader.read_many(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'console':
                obj.console = ConsoleReader.read_one(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'cpu_profile':
                obj.cpu_profile = CpuProfileReader.read_one(reader)
            elif tag == 'cpu_shares':
                obj.cpu_shares = Reader.read_integer(reader)
            elif tag == 'creation_time':
                obj.creation_time = Reader.read_date(reader)
            elif tag == 'custom_compatibility_version':
                obj.custom_compatibility_version = VersionReader.read_one(reader)
            elif tag == 'custom_cpu_model':
                obj.custom_cpu_model = Reader.read_string(reader)
            elif tag == 'custom_emulated_machine':
                obj.custom_emulated_machine = Reader.read_string(reader)
            elif tag == 'custom_properties':
                obj.custom_properties = CustomPropertyReader.read_many(reader)
            elif tag == 'delete_protected':
                obj.delete_protected = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk_attachments':
                obj.disk_attachments = DiskAttachmentReader.read_many(reader)
            elif tag == 'display':
                obj.display = DisplayReader.read_one(reader)
            elif tag == 'domain':
                obj.domain = DomainReader.read_one(reader)
            elif tag == 'graphics_consoles':
                obj.graphics_consoles = GraphicsConsoleReader.read_many(reader)
            elif tag == 'high_availability':
                obj.high_availability = HighAvailabilityReader.read_one(reader)
            elif tag == 'initialization':
                obj.initialization = InitializationReader.read_one(reader)
            elif tag == 'io':
                obj.io = IoReader.read_one(reader)
            elif tag == 'large_icon':
                obj.large_icon = IconReader.read_one(reader)
            elif tag == 'lease':
                obj.lease = StorageDomainLeaseReader.read_one(reader)
            elif tag == 'memory':
                obj.memory = Reader.read_integer(reader)
            elif tag == 'memory_policy':
                obj.memory_policy = MemoryPolicyReader.read_one(reader)
            elif tag == 'migration':
                obj.migration = MigrationOptionsReader.read_one(reader)
            elif tag == 'migration_downtime':
                obj.migration_downtime = Reader.read_integer(reader)
            elif tag == 'multi_queues_enabled':
                obj.multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'nics':
                obj.nics = NicReader.read_many(reader)
            elif tag == 'origin':
                obj.origin = Reader.read_string(reader)
            elif tag == 'os':
                obj.os = OperatingSystemReader.read_one(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'placement_policy':
                obj.placement_policy = VmPlacementPolicyReader.read_one(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'rng_device':
                obj.rng_device = RngDeviceReader.read_one(reader)
            elif tag == 'serial_number':
                obj.serial_number = SerialNumberReader.read_one(reader)
            elif tag == 'small_icon':
                obj.small_icon = IconReader.read_one(reader)
            elif tag == 'soundcard_enabled':
                obj.soundcard_enabled = Reader.read_boolean(reader)
            elif tag == 'sso':
                obj.sso = SsoReader.read_one(reader)
            elif tag == 'start_paused':
                obj.start_paused = Reader.read_boolean(reader)
            elif tag == 'stateless':
                obj.stateless = Reader.read_boolean(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.TemplateStatus, reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'storage_error_resume_behaviour':
                obj.storage_error_resume_behaviour = Reader.read_enum(types.VmStorageErrorResumeBehaviour, reader)
            elif tag == 'tags':
                obj.tags = TagReader.read_many(reader)
            elif tag == 'time_zone':
                obj.time_zone = TimeZoneReader.read_one(reader)
            elif tag == 'tpm_enabled':
                obj.tpm_enabled = Reader.read_boolean(reader)
            elif tag == 'tunnel_migration':
                obj.tunnel_migration = Reader.read_boolean(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.VmType, reader)
            elif tag == 'usb':
                obj.usb = UsbReader.read_one(reader)
            elif tag == 'version':
                obj.version = TemplateVersionReader.read_one(reader)
            elif tag == 'virtio_scsi':
                obj.virtio_scsi = VirtioScsiReader.read_one(reader)
            elif tag == 'virtio_scsi_multi_queues':
                obj.virtio_scsi_multi_queues = Reader.read_integer(reader)
            elif tag == 'virtio_scsi_multi_queues_enabled':
                obj.virtio_scsi_multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'watchdogs':
                obj.watchdogs = WatchdogReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            TemplateReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(TemplateReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "cdroms":
                if obj.cdroms is not None:
                    obj.cdroms.href = href
                else:
                    obj.cdroms = List(href)
            elif rel == "diskattachments":
                if obj.disk_attachments is not None:
                    obj.disk_attachments.href = href
                else:
                    obj.disk_attachments = List(href)
            elif rel == "graphicsconsoles":
                if obj.graphics_consoles is not None:
                    obj.graphics_consoles.href = href
                else:
                    obj.graphics_consoles = List(href)
            elif rel == "nics":
                if obj.nics is not None:
                    obj.nics.href = href
                else:
                    obj.nics = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "tags":
                if obj.tags is not None:
                    obj.tags.href = href
                else:
                    obj.tags = List(href)
            elif rel == "watchdogs":
                if obj.watchdogs is not None:
                    obj.watchdogs.href = href
                else:
                    obj.watchdogs = List(href)


class TemplateVersionReader(Reader):

    def __init__(self):
        super(TemplateVersionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.TemplateVersion()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'base_template':
                obj.base_template = TemplateReader.read_one(reader)
            elif tag == 'version_name':
                obj.version_name = Reader.read_string(reader)
            elif tag == 'version_number':
                obj.version_number = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            TemplateVersionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(TemplateVersionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class TicketReader(Reader):

    def __init__(self):
        super(TicketReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Ticket()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'expiry':
                obj.expiry = Reader.read_integer(reader)
            elif tag == 'value':
                obj.value = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            TicketReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(TicketReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class TimeZoneReader(Reader):

    def __init__(self):
        super(TimeZoneReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.TimeZone()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'utc_offset':
                obj.utc_offset = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            TimeZoneReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(TimeZoneReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class TransparentHugePagesReader(Reader):

    def __init__(self):
        super(TransparentHugePagesReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.TransparentHugePages()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            TransparentHugePagesReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(TransparentHugePagesReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class UnmanagedNetworkReader(Reader):

    def __init__(self):
        super(UnmanagedNetworkReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.UnmanagedNetwork()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'host_nic':
                obj.host_nic = HostNicReader.read_one(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            UnmanagedNetworkReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(UnmanagedNetworkReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class UsbReader(Reader):

    def __init__(self):
        super(UsbReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Usb()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.UsbType, reader)
            else:
                reader.next_element()
        for link in links:
            UsbReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(UsbReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class UserReader(Reader):

    def __init__(self):
        super(UserReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.User()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'department':
                obj.department = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'domain':
                obj.domain = DomainReader.read_one(reader)
            elif tag == 'domain_entry_id':
                obj.domain_entry_id = Reader.read_string(reader)
            elif tag == 'email':
                obj.email = Reader.read_string(reader)
            elif tag == 'groups':
                obj.groups = GroupReader.read_many(reader)
            elif tag == 'last_name':
                obj.last_name = Reader.read_string(reader)
            elif tag == 'logged_in':
                obj.logged_in = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'namespace':
                obj.namespace = Reader.read_string(reader)
            elif tag == 'options':
                obj.options = UserOptionReader.read_many(reader)
            elif tag == 'password':
                obj.password = Reader.read_string(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'principal':
                obj.principal = Reader.read_string(reader)
            elif tag == 'roles':
                obj.roles = RoleReader.read_many(reader)
            elif tag == 'ssh_public_keys':
                obj.ssh_public_keys = SshPublicKeyReader.read_many(reader)
            elif tag == 'tags':
                obj.tags = TagReader.read_many(reader)
            elif tag == 'user_name':
                obj.user_name = Reader.read_string(reader)
            elif tag == 'user_options':
                obj.user_options = PropertyReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            UserReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(UserReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "groups":
                if obj.groups is not None:
                    obj.groups.href = href
                else:
                    obj.groups = List(href)
            elif rel == "options":
                if obj.options is not None:
                    obj.options.href = href
                else:
                    obj.options = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "roles":
                if obj.roles is not None:
                    obj.roles.href = href
                else:
                    obj.roles = List(href)
            elif rel == "sshpublickeys":
                if obj.ssh_public_keys is not None:
                    obj.ssh_public_keys.href = href
                else:
                    obj.ssh_public_keys = List(href)
            elif rel == "tags":
                if obj.tags is not None:
                    obj.tags.href = href
                else:
                    obj.tags = List(href)


class UserOptionReader(Reader):

    def __init__(self):
        super(UserOptionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.UserOption()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'content':
                obj.content = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'user':
                obj.user = UserReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            UserOptionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(UserOptionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class ValueReader(Reader):

    def __init__(self):
        super(ValueReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Value()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'datum':
                obj.datum = Reader.read_decimal(reader)
            elif tag == 'detail':
                obj.detail = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            ValueReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(ValueReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VcpuPinReader(Reader):

    def __init__(self):
        super(VcpuPinReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VcpuPin()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'cpu_set':
                obj.cpu_set = Reader.read_string(reader)
            elif tag == 'vcpu':
                obj.vcpu = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            VcpuPinReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VcpuPinReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VendorReader(Reader):

    def __init__(self):
        super(VendorReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Vendor()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            VendorReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VendorReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VersionReader(Reader):

    def __init__(self):
        super(VersionReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Version()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'build':
                obj.build = Reader.read_integer(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'full_version':
                obj.full_version = Reader.read_string(reader)
            elif tag == 'major':
                obj.major = Reader.read_integer(reader)
            elif tag == 'minor':
                obj.minor = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'revision':
                obj.revision = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            VersionReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VersionReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VirtioScsiReader(Reader):

    def __init__(self):
        super(VirtioScsiReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VirtioScsi()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'enabled':
                obj.enabled = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            VirtioScsiReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VirtioScsiReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VirtualNumaNodeReader(Reader):

    def __init__(self):
        super(VirtualNumaNodeReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VirtualNumaNode()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'index':
                obj.index = Reader.read_integer(reader)
            elif tag == 'memory':
                obj.memory = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'node_distance':
                obj.node_distance = Reader.read_string(reader)
            elif tag == 'numa_node_pins':
                obj.numa_node_pins = NumaNodePinReader.read_many(reader)
            elif tag == 'numa_tune_mode':
                obj.numa_tune_mode = Reader.read_enum(types.NumaTuneMode, reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            VirtualNumaNodeReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VirtualNumaNodeReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)


class VlanReader(Reader):

    def __init__(self):
        super(VlanReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Vlan()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = Reader.parse_integer(value)

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        reader.next_element()

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VlanReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VmReader(Reader):

    def __init__(self):
        super(VmReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Vm()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'affinity_labels':
                obj.affinity_labels = AffinityLabelReader.read_many(reader)
            elif tag == 'applications':
                obj.applications = ApplicationReader.read_many(reader)
            elif tag == 'auto_pinning_policy':
                obj.auto_pinning_policy = Reader.read_enum(types.AutoPinningPolicy, reader)
            elif tag == 'bios':
                obj.bios = BiosReader.read_one(reader)
            elif tag == 'cdroms':
                obj.cdroms = CdromReader.read_many(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'console':
                obj.console = ConsoleReader.read_one(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'cpu_profile':
                obj.cpu_profile = CpuProfileReader.read_one(reader)
            elif tag == 'cpu_shares':
                obj.cpu_shares = Reader.read_integer(reader)
            elif tag == 'creation_time':
                obj.creation_time = Reader.read_date(reader)
            elif tag == 'custom_compatibility_version':
                obj.custom_compatibility_version = VersionReader.read_one(reader)
            elif tag == 'custom_cpu_model':
                obj.custom_cpu_model = Reader.read_string(reader)
            elif tag == 'custom_emulated_machine':
                obj.custom_emulated_machine = Reader.read_string(reader)
            elif tag == 'custom_properties':
                obj.custom_properties = CustomPropertyReader.read_many(reader)
            elif tag == 'delete_protected':
                obj.delete_protected = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'disk_attachments':
                obj.disk_attachments = DiskAttachmentReader.read_many(reader)
            elif tag == 'display':
                obj.display = DisplayReader.read_one(reader)
            elif tag == 'domain':
                obj.domain = DomainReader.read_one(reader)
            elif tag == 'external_host_provider':
                obj.external_host_provider = ExternalHostProviderReader.read_one(reader)
            elif tag == 'floppies':
                obj.floppies = FloppyReader.read_many(reader)
            elif tag == 'fqdn':
                obj.fqdn = Reader.read_string(reader)
            elif tag == 'graphics_consoles':
                obj.graphics_consoles = GraphicsConsoleReader.read_many(reader)
            elif tag == 'guest_operating_system':
                obj.guest_operating_system = GuestOperatingSystemReader.read_one(reader)
            elif tag == 'guest_time_zone':
                obj.guest_time_zone = TimeZoneReader.read_one(reader)
            elif tag == 'has_illegal_images':
                obj.has_illegal_images = Reader.read_boolean(reader)
            elif tag == 'high_availability':
                obj.high_availability = HighAvailabilityReader.read_one(reader)
            elif tag == 'host':
                obj.host = HostReader.read_one(reader)
            elif tag == 'host_devices':
                obj.host_devices = HostDeviceReader.read_many(reader)
            elif tag == 'initialization':
                obj.initialization = InitializationReader.read_one(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'io':
                obj.io = IoReader.read_one(reader)
            elif tag == 'katello_errata':
                obj.katello_errata = KatelloErratumReader.read_many(reader)
            elif tag == 'large_icon':
                obj.large_icon = IconReader.read_one(reader)
            elif tag == 'lease':
                obj.lease = StorageDomainLeaseReader.read_one(reader)
            elif tag == 'memory':
                obj.memory = Reader.read_integer(reader)
            elif tag == 'memory_policy':
                obj.memory_policy = MemoryPolicyReader.read_one(reader)
            elif tag == 'migration':
                obj.migration = MigrationOptionsReader.read_one(reader)
            elif tag == 'migration_downtime':
                obj.migration_downtime = Reader.read_integer(reader)
            elif tag == 'multi_queues_enabled':
                obj.multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'next_run_configuration_exists':
                obj.next_run_configuration_exists = Reader.read_boolean(reader)
            elif tag == 'nics':
                obj.nics = NicReader.read_many(reader)
            elif tag == 'host_numa_nodes':
                obj.numa_nodes = NumaNodeReader.read_many(reader)
            elif tag == 'numa_tune_mode':
                obj.numa_tune_mode = Reader.read_enum(types.NumaTuneMode, reader)
            elif tag == 'origin':
                obj.origin = Reader.read_string(reader)
            elif tag == 'original_template':
                obj.original_template = TemplateReader.read_one(reader)
            elif tag == 'os':
                obj.os = OperatingSystemReader.read_one(reader)
            elif tag == 'payloads':
                obj.payloads = PayloadReader.read_many(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'placement_policy':
                obj.placement_policy = VmPlacementPolicyReader.read_one(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'reported_devices':
                obj.reported_devices = ReportedDeviceReader.read_many(reader)
            elif tag == 'rng_device':
                obj.rng_device = RngDeviceReader.read_one(reader)
            elif tag == 'run_once':
                obj.run_once = Reader.read_boolean(reader)
            elif tag == 'serial_number':
                obj.serial_number = SerialNumberReader.read_one(reader)
            elif tag == 'sessions':
                obj.sessions = SessionReader.read_many(reader)
            elif tag == 'small_icon':
                obj.small_icon = IconReader.read_one(reader)
            elif tag == 'snapshots':
                obj.snapshots = SnapshotReader.read_many(reader)
            elif tag == 'soundcard_enabled':
                obj.soundcard_enabled = Reader.read_boolean(reader)
            elif tag == 'sso':
                obj.sso = SsoReader.read_one(reader)
            elif tag == 'start_paused':
                obj.start_paused = Reader.read_boolean(reader)
            elif tag == 'start_time':
                obj.start_time = Reader.read_date(reader)
            elif tag == 'stateless':
                obj.stateless = Reader.read_boolean(reader)
            elif tag == 'statistics':
                obj.statistics = StatisticReader.read_many(reader)
            elif tag == 'status':
                obj.status = Reader.read_enum(types.VmStatus, reader)
            elif tag == 'status_detail':
                obj.status_detail = Reader.read_string(reader)
            elif tag == 'stop_reason':
                obj.stop_reason = Reader.read_string(reader)
            elif tag == 'stop_time':
                obj.stop_time = Reader.read_date(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'storage_error_resume_behaviour':
                obj.storage_error_resume_behaviour = Reader.read_enum(types.VmStorageErrorResumeBehaviour, reader)
            elif tag == 'tags':
                obj.tags = TagReader.read_many(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'time_zone':
                obj.time_zone = TimeZoneReader.read_one(reader)
            elif tag == 'tpm_enabled':
                obj.tpm_enabled = Reader.read_boolean(reader)
            elif tag == 'tunnel_migration':
                obj.tunnel_migration = Reader.read_boolean(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.VmType, reader)
            elif tag == 'usb':
                obj.usb = UsbReader.read_one(reader)
            elif tag == 'use_latest_template_version':
                obj.use_latest_template_version = Reader.read_boolean(reader)
            elif tag == 'virtio_scsi':
                obj.virtio_scsi = VirtioScsiReader.read_one(reader)
            elif tag == 'virtio_scsi_multi_queues':
                obj.virtio_scsi_multi_queues = Reader.read_integer(reader)
            elif tag == 'virtio_scsi_multi_queues_enabled':
                obj.virtio_scsi_multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'vm_pool':
                obj.vm_pool = VmPoolReader.read_one(reader)
            elif tag == 'watchdogs':
                obj.watchdogs = WatchdogReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            VmReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VmReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "affinitylabels":
                if obj.affinity_labels is not None:
                    obj.affinity_labels.href = href
                else:
                    obj.affinity_labels = List(href)
            elif rel == "applications":
                if obj.applications is not None:
                    obj.applications.href = href
                else:
                    obj.applications = List(href)
            elif rel == "cdroms":
                if obj.cdroms is not None:
                    obj.cdroms.href = href
                else:
                    obj.cdroms = List(href)
            elif rel == "diskattachments":
                if obj.disk_attachments is not None:
                    obj.disk_attachments.href = href
                else:
                    obj.disk_attachments = List(href)
            elif rel == "floppies":
                if obj.floppies is not None:
                    obj.floppies.href = href
                else:
                    obj.floppies = List(href)
            elif rel == "graphicsconsoles":
                if obj.graphics_consoles is not None:
                    obj.graphics_consoles.href = href
                else:
                    obj.graphics_consoles = List(href)
            elif rel == "hostdevices":
                if obj.host_devices is not None:
                    obj.host_devices.href = href
                else:
                    obj.host_devices = List(href)
            elif rel == "katelloerrata":
                if obj.katello_errata is not None:
                    obj.katello_errata.href = href
                else:
                    obj.katello_errata = List(href)
            elif rel == "nics":
                if obj.nics is not None:
                    obj.nics.href = href
                else:
                    obj.nics = List(href)
            elif rel == "numanodes":
                if obj.numa_nodes is not None:
                    obj.numa_nodes.href = href
                else:
                    obj.numa_nodes = List(href)
            elif rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)
            elif rel == "reporteddevices":
                if obj.reported_devices is not None:
                    obj.reported_devices.href = href
                else:
                    obj.reported_devices = List(href)
            elif rel == "sessions":
                if obj.sessions is not None:
                    obj.sessions.href = href
                else:
                    obj.sessions = List(href)
            elif rel == "snapshots":
                if obj.snapshots is not None:
                    obj.snapshots.href = href
                else:
                    obj.snapshots = List(href)
            elif rel == "statistics":
                if obj.statistics is not None:
                    obj.statistics.href = href
                else:
                    obj.statistics = List(href)
            elif rel == "tags":
                if obj.tags is not None:
                    obj.tags.href = href
                else:
                    obj.tags = List(href)
            elif rel == "watchdogs":
                if obj.watchdogs is not None:
                    obj.watchdogs.href = href
                else:
                    obj.watchdogs = List(href)


class VmBaseReader(Reader):

    def __init__(self):
        super(VmBaseReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VmBase()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'auto_pinning_policy':
                obj.auto_pinning_policy = Reader.read_enum(types.AutoPinningPolicy, reader)
            elif tag == 'bios':
                obj.bios = BiosReader.read_one(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'console':
                obj.console = ConsoleReader.read_one(reader)
            elif tag == 'cpu':
                obj.cpu = CpuReader.read_one(reader)
            elif tag == 'cpu_profile':
                obj.cpu_profile = CpuProfileReader.read_one(reader)
            elif tag == 'cpu_shares':
                obj.cpu_shares = Reader.read_integer(reader)
            elif tag == 'creation_time':
                obj.creation_time = Reader.read_date(reader)
            elif tag == 'custom_compatibility_version':
                obj.custom_compatibility_version = VersionReader.read_one(reader)
            elif tag == 'custom_cpu_model':
                obj.custom_cpu_model = Reader.read_string(reader)
            elif tag == 'custom_emulated_machine':
                obj.custom_emulated_machine = Reader.read_string(reader)
            elif tag == 'custom_properties':
                obj.custom_properties = CustomPropertyReader.read_many(reader)
            elif tag == 'delete_protected':
                obj.delete_protected = Reader.read_boolean(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'display':
                obj.display = DisplayReader.read_one(reader)
            elif tag == 'domain':
                obj.domain = DomainReader.read_one(reader)
            elif tag == 'high_availability':
                obj.high_availability = HighAvailabilityReader.read_one(reader)
            elif tag == 'initialization':
                obj.initialization = InitializationReader.read_one(reader)
            elif tag == 'io':
                obj.io = IoReader.read_one(reader)
            elif tag == 'large_icon':
                obj.large_icon = IconReader.read_one(reader)
            elif tag == 'lease':
                obj.lease = StorageDomainLeaseReader.read_one(reader)
            elif tag == 'memory':
                obj.memory = Reader.read_integer(reader)
            elif tag == 'memory_policy':
                obj.memory_policy = MemoryPolicyReader.read_one(reader)
            elif tag == 'migration':
                obj.migration = MigrationOptionsReader.read_one(reader)
            elif tag == 'migration_downtime':
                obj.migration_downtime = Reader.read_integer(reader)
            elif tag == 'multi_queues_enabled':
                obj.multi_queues_enabled = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'origin':
                obj.origin = Reader.read_string(reader)
            elif tag == 'os':
                obj.os = OperatingSystemReader.read_one(reader)
            elif tag == 'placement_policy':
                obj.placement_policy = VmPlacementPolicyReader.read_one(reader)
            elif tag == 'quota':
                obj.quota = QuotaReader.read_one(reader)
            elif tag == 'rng_device':
                obj.rng_device = RngDeviceReader.read_one(reader)
            elif tag == 'serial_number':
                obj.serial_number = SerialNumberReader.read_one(reader)
            elif tag == 'small_icon':
                obj.small_icon = IconReader.read_one(reader)
            elif tag == 'soundcard_enabled':
                obj.soundcard_enabled = Reader.read_boolean(reader)
            elif tag == 'sso':
                obj.sso = SsoReader.read_one(reader)
            elif tag == 'start_paused':
                obj.start_paused = Reader.read_boolean(reader)
            elif tag == 'stateless':
                obj.stateless = Reader.read_boolean(reader)
            elif tag == 'storage_domain':
                obj.storage_domain = StorageDomainReader.read_one(reader)
            elif tag == 'storage_error_resume_behaviour':
                obj.storage_error_resume_behaviour = Reader.read_enum(types.VmStorageErrorResumeBehaviour, reader)
            elif tag == 'time_zone':
                obj.time_zone = TimeZoneReader.read_one(reader)
            elif tag == 'tpm_enabled':
                obj.tpm_enabled = Reader.read_boolean(reader)
            elif tag == 'tunnel_migration':
                obj.tunnel_migration = Reader.read_boolean(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.VmType, reader)
            elif tag == 'usb':
                obj.usb = UsbReader.read_one(reader)
            elif tag == 'virtio_scsi':
                obj.virtio_scsi = VirtioScsiReader.read_one(reader)
            elif tag == 'virtio_scsi_multi_queues':
                obj.virtio_scsi_multi_queues = Reader.read_integer(reader)
            elif tag == 'virtio_scsi_multi_queues_enabled':
                obj.virtio_scsi_multi_queues_enabled = Reader.read_boolean(reader)
            else:
                reader.next_element()
        for link in links:
            VmBaseReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VmBaseReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VmPlacementPolicyReader(Reader):

    def __init__(self):
        super(VmPlacementPolicyReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VmPlacementPolicy()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'affinity':
                obj.affinity = Reader.read_enum(types.VmAffinity, reader)
            elif tag == 'hosts':
                obj.hosts = HostReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            VmPlacementPolicyReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VmPlacementPolicyReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "hosts":
                if obj.hosts is not None:
                    obj.hosts.href = href
                else:
                    obj.hosts = List(href)


class VmPoolReader(Reader):

    def __init__(self):
        super(VmPoolReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VmPool()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'auto_storage_select':
                obj.auto_storage_select = Reader.read_boolean(reader)
            elif tag == 'cluster':
                obj.cluster = ClusterReader.read_one(reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'display':
                obj.display = DisplayReader.read_one(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'max_user_vms':
                obj.max_user_vms = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'prestarted_vms':
                obj.prestarted_vms = Reader.read_integer(reader)
            elif tag == 'rng_device':
                obj.rng_device = RngDeviceReader.read_one(reader)
            elif tag == 'size':
                obj.size = Reader.read_integer(reader)
            elif tag == 'soundcard_enabled':
                obj.soundcard_enabled = Reader.read_boolean(reader)
            elif tag == 'stateful':
                obj.stateful = Reader.read_boolean(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'tpm_enabled':
                obj.tpm_enabled = Reader.read_boolean(reader)
            elif tag == 'type':
                obj.type = Reader.read_enum(types.VmPoolType, reader)
            elif tag == 'use_latest_template_version':
                obj.use_latest_template_version = Reader.read_boolean(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            VmPoolReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VmPoolReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)


class VmSummaryReader(Reader):

    def __init__(self):
        super(VmSummaryReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VmSummary()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'active':
                obj.active = Reader.read_integer(reader)
            elif tag == 'migrating':
                obj.migrating = Reader.read_integer(reader)
            elif tag == 'total':
                obj.total = Reader.read_integer(reader)
            else:
                reader.next_element()
        for link in links:
            VmSummaryReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VmSummaryReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VnicPassThroughReader(Reader):

    def __init__(self):
        super(VnicPassThroughReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VnicPassThrough()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'mode':
                obj.mode = Reader.read_enum(types.VnicPassThroughMode, reader)
            else:
                reader.next_element()
        for link in links:
            VnicPassThroughReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VnicPassThroughReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VnicProfileReader(Reader):

    def __init__(self):
        super(VnicProfileReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VnicProfile()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'custom_properties':
                obj.custom_properties = CustomPropertyReader.read_many(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'failover':
                obj.failover = VnicProfileReader.read_one(reader)
            elif tag == 'migratable':
                obj.migratable = Reader.read_boolean(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'network':
                obj.network = NetworkReader.read_one(reader)
            elif tag == 'network_filter':
                obj.network_filter = NetworkFilterReader.read_one(reader)
            elif tag == 'pass_through':
                obj.pass_through = VnicPassThroughReader.read_one(reader)
            elif tag == 'permissions':
                obj.permissions = PermissionReader.read_many(reader)
            elif tag == 'port_mirroring':
                obj.port_mirroring = Reader.read_boolean(reader)
            elif tag == 'qos':
                obj.qos = QosReader.read_one(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            VnicProfileReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VnicProfileReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "permissions":
                if obj.permissions is not None:
                    obj.permissions.href = href
                else:
                    obj.permissions = List(href)


class VnicProfileMappingReader(Reader):

    def __init__(self):
        super(VnicProfileMappingReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VnicProfileMapping()

        # Process the attributes:
        obj.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'source_network_name':
                obj.source_network_name = Reader.read_string(reader)
            elif tag == 'source_network_profile_name':
                obj.source_network_profile_name = Reader.read_string(reader)
            elif tag == 'target_vnic_profile':
                obj.target_vnic_profile = VnicProfileReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            VnicProfileMappingReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VnicProfileMappingReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class VolumeGroupReader(Reader):

    def __init__(self):
        super(VolumeGroupReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.VolumeGroup()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'logical_units':
                obj.logical_units = LogicalUnitReader.read_many(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            else:
                reader.next_element()
        for link in links:
            VolumeGroupReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(VolumeGroupReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


class WatchdogReader(Reader):

    def __init__(self):
        super(WatchdogReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Watchdog()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'action':
                obj.action = Reader.read_enum(types.WatchdogAction, reader)
            elif tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'instance_type':
                obj.instance_type = InstanceTypeReader.read_one(reader)
            elif tag == 'model':
                obj.model = Reader.read_enum(types.WatchdogModel, reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'template':
                obj.template = TemplateReader.read_one(reader)
            elif tag == 'vm':
                obj.vm = VmReader.read_one(reader)
            elif tag == 'vms':
                obj.vms = VmReader.read_many(reader)
            elif tag == 'link':
                links.append((reader.get_attribute('rel'), reader.get_attribute('href')))
                reader.next_element()
            else:
                reader.next_element()
        for link in links:
            WatchdogReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(WatchdogReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs

    @staticmethod
    def _process_link(link, obj):
        # Process the attributes:
        rel = link[0]
        href = link[1]
        if href and rel:
            if rel == "vms":
                if obj.vms is not None:
                    obj.vms.href = href
                else:
                    obj.vms = List(href)


class WeightReader(Reader):

    def __init__(self):
        super(WeightReader, self).__init__()

    @staticmethod
    def read_one(reader):
        # Do nothing if there aren't more tags:
        if not reader.forward():
            return None

        # Create the object:
        obj = types.Weight()

        # Process the attributes:
        obj.href = reader.get_attribute('href')
        value = reader.get_attribute('id')
        if value is not None:
            obj.id = value

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return obj

        # Process the inner elements:
        links = []
        while reader.forward():
            tag = reader.node_name()
            if tag == 'comment':
                obj.comment = Reader.read_string(reader)
            elif tag == 'description':
                obj.description = Reader.read_string(reader)
            elif tag == 'factor':
                obj.factor = Reader.read_integer(reader)
            elif tag == 'name':
                obj.name = Reader.read_string(reader)
            elif tag == 'scheduling_policy':
                obj.scheduling_policy = SchedulingPolicyReader.read_one(reader)
            elif tag == 'scheduling_policy_unit':
                obj.scheduling_policy_unit = SchedulingPolicyUnitReader.read_one(reader)
            else:
                reader.next_element()
        for link in links:
            WeightReader._process_link(link, obj)

        # Discard the end tag:
        reader.read()

        return obj

    @staticmethod
    def read_many(reader):
        # Do nothing if there aren't more tags:
        objs = List()
        if not reader.forward():
            return objs

        # Process the attributes:
        objs.href = reader.get_attribute('href')

        # Discard the start tag:
        empty = reader.empty_element()
        reader.read()
        if empty:
            return objs

        # Process the inner elements:
        while reader.forward():
            objs.append(WeightReader.read_one(reader))

        # Discard the end tag:
        reader.read()

        return objs


Reader.register('action', ActionReader.read_one)
Reader.register('actions', ActionReader.read_many)
Reader.register('affinity_group', AffinityGroupReader.read_one)
Reader.register('affinity_groups', AffinityGroupReader.read_many)
Reader.register('affinity_label', AffinityLabelReader.read_one)
Reader.register('affinity_labels', AffinityLabelReader.read_many)
Reader.register('affinity_rule', AffinityRuleReader.read_one)
Reader.register('affinity_rules', AffinityRuleReader.read_many)
Reader.register('agent', AgentReader.read_one)
Reader.register('agents', AgentReader.read_many)
Reader.register('agent_configuration', AgentConfigurationReader.read_one)
Reader.register('agent_configurations', AgentConfigurationReader.read_many)
Reader.register('api', ApiReader.read_one)
Reader.register('apis', ApiReader.read_many)
Reader.register('api_summary', ApiSummaryReader.read_one)
Reader.register('api_summaries', ApiSummaryReader.read_many)
Reader.register('api_summary_item', ApiSummaryItemReader.read_one)
Reader.register('api_summary_items', ApiSummaryItemReader.read_many)
Reader.register('application', ApplicationReader.read_one)
Reader.register('applications', ApplicationReader.read_many)
Reader.register('authorized_key', AuthorizedKeyReader.read_one)
Reader.register('authorized_keys', AuthorizedKeyReader.read_many)
Reader.register('backup', BackupReader.read_one)
Reader.register('backups', BackupReader.read_many)
Reader.register('balance', BalanceReader.read_one)
Reader.register('balances', BalanceReader.read_many)
Reader.register('bios', BiosReader.read_one)
Reader.register('bioss', BiosReader.read_many)
Reader.register('block_statistic', BlockStatisticReader.read_one)
Reader.register('block_statistics', BlockStatisticReader.read_many)
Reader.register('bonding', BondingReader.read_one)
Reader.register('bondings', BondingReader.read_many)
Reader.register('bookmark', BookmarkReader.read_one)
Reader.register('bookmarks', BookmarkReader.read_many)
Reader.register('boot', BootReader.read_one)
Reader.register('boots', BootReader.read_many)
Reader.register('boot_menu', BootMenuReader.read_one)
Reader.register('boot_menus', BootMenuReader.read_many)
Reader.register('brick_profile_detail', BrickProfileDetailReader.read_one)
Reader.register('brick_profile_details', BrickProfileDetailReader.read_many)
Reader.register('cdrom', CdromReader.read_one)
Reader.register('cdroms', CdromReader.read_many)
Reader.register('certificate', CertificateReader.read_one)
Reader.register('certificates', CertificateReader.read_many)
Reader.register('checkpoint', CheckpointReader.read_one)
Reader.register('checkpoints', CheckpointReader.read_many)
Reader.register('cloud_init', CloudInitReader.read_one)
Reader.register('cloud_inits', CloudInitReader.read_many)
Reader.register('cluster', ClusterReader.read_one)
Reader.register('clusters', ClusterReader.read_many)
Reader.register('cluster_feature', ClusterFeatureReader.read_one)
Reader.register('cluster_features', ClusterFeatureReader.read_many)
Reader.register('cluster_level', ClusterLevelReader.read_one)
Reader.register('cluster_levels', ClusterLevelReader.read_many)
Reader.register('configuration', ConfigurationReader.read_one)
Reader.register('configurations', ConfigurationReader.read_many)
Reader.register('console', ConsoleReader.read_one)
Reader.register('consoles', ConsoleReader.read_many)
Reader.register('core', CoreReader.read_one)
Reader.register('cores', CoreReader.read_many)
Reader.register('cpu', CpuReader.read_one)
Reader.register('cpus', CpuReader.read_many)
Reader.register('cpu_profile', CpuProfileReader.read_one)
Reader.register('cpu_profiles', CpuProfileReader.read_many)
Reader.register('cpu_topology', CpuTopologyReader.read_one)
Reader.register('cpu_topologies', CpuTopologyReader.read_many)
Reader.register('cpu_tune', CpuTuneReader.read_one)
Reader.register('cpu_tunes', CpuTuneReader.read_many)
Reader.register('cpu_type', CpuTypeReader.read_one)
Reader.register('cpu_types', CpuTypeReader.read_many)
Reader.register('custom_property', CustomPropertyReader.read_one)
Reader.register('custom_properties', CustomPropertyReader.read_many)
Reader.register('data_center', DataCenterReader.read_one)
Reader.register('data_centers', DataCenterReader.read_many)
Reader.register('device', DeviceReader.read_one)
Reader.register('devices', DeviceReader.read_many)
Reader.register('disk', DiskReader.read_one)
Reader.register('disks', DiskReader.read_many)
Reader.register('disk_attachment', DiskAttachmentReader.read_one)
Reader.register('disk_attachments', DiskAttachmentReader.read_many)
Reader.register('disk_profile', DiskProfileReader.read_one)
Reader.register('disk_profiles', DiskProfileReader.read_many)
Reader.register('disk_snapshot', DiskSnapshotReader.read_one)
Reader.register('disk_snapshots', DiskSnapshotReader.read_many)
Reader.register('display', DisplayReader.read_one)
Reader.register('displays', DisplayReader.read_many)
Reader.register('dns', DnsReader.read_one)
Reader.register('dnss', DnsReader.read_many)
Reader.register('dns_resolver_configuration', DnsResolverConfigurationReader.read_one)
Reader.register('dns_resolver_configurations', DnsResolverConfigurationReader.read_many)
Reader.register('domain', DomainReader.read_one)
Reader.register('domains', DomainReader.read_many)
Reader.register('entity_profile_detail', EntityProfileDetailReader.read_one)
Reader.register('entity_profile_details', EntityProfileDetailReader.read_many)
Reader.register('error_handling', ErrorHandlingReader.read_one)
Reader.register('error_handlings', ErrorHandlingReader.read_many)
Reader.register('event', EventReader.read_one)
Reader.register('events', EventReader.read_many)
Reader.register('event_subscription', EventSubscriptionReader.read_one)
Reader.register('event_subscriptions', EventSubscriptionReader.read_many)
Reader.register('external_compute_resource', ExternalComputeResourceReader.read_one)
Reader.register('external_compute_resources', ExternalComputeResourceReader.read_many)
Reader.register('external_discovered_host', ExternalDiscoveredHostReader.read_one)
Reader.register('external_discovered_hosts', ExternalDiscoveredHostReader.read_many)
Reader.register('external_host', ExternalHostReader.read_one)
Reader.register('external_hosts', ExternalHostReader.read_many)
Reader.register('external_host_group', ExternalHostGroupReader.read_one)
Reader.register('external_host_groups', ExternalHostGroupReader.read_many)
Reader.register('external_host_provider', ExternalHostProviderReader.read_one)
Reader.register('external_host_providers', ExternalHostProviderReader.read_many)
Reader.register('external_network_provider_configuration', ExternalNetworkProviderConfigurationReader.read_one)
Reader.register('external_network_provider_configurations', ExternalNetworkProviderConfigurationReader.read_many)
Reader.register('external_provider', ExternalProviderReader.read_one)
Reader.register('external_providers', ExternalProviderReader.read_many)
Reader.register('external_template_import', ExternalTemplateImportReader.read_one)
Reader.register('external_template_imports', ExternalTemplateImportReader.read_many)
Reader.register('external_vm_import', ExternalVmImportReader.read_one)
Reader.register('external_vm_imports', ExternalVmImportReader.read_many)
Reader.register('fault', FaultReader.read_one)
Reader.register('faults', FaultReader.read_many)
Reader.register('fencing_policy', FencingPolicyReader.read_one)
Reader.register('fencing_policies', FencingPolicyReader.read_many)
Reader.register('file', FileReader.read_one)
Reader.register('files', FileReader.read_many)
Reader.register('filter', FilterReader.read_one)
Reader.register('filters', FilterReader.read_many)
Reader.register('floppy', FloppyReader.read_one)
Reader.register('floppies', FloppyReader.read_many)
Reader.register('fop_statistic', FopStatisticReader.read_one)
Reader.register('fop_statistics', FopStatisticReader.read_many)
Reader.register('brick', GlusterBrickReader.read_one)
Reader.register('bricks', GlusterBrickReader.read_many)
Reader.register('gluster_brick_advanced_details', GlusterBrickAdvancedDetailsReader.read_one)
Reader.register('gluster_brick_advanced_detailss', GlusterBrickAdvancedDetailsReader.read_many)
Reader.register('brick_memoryinfo', GlusterBrickMemoryInfoReader.read_one)
Reader.register('gluster_brick_memory_infos', GlusterBrickMemoryInfoReader.read_many)
Reader.register('gluster_client', GlusterClientReader.read_one)
Reader.register('gluster_clients', GlusterClientReader.read_many)
Reader.register('gluster_hook', GlusterHookReader.read_one)
Reader.register('gluster_hooks', GlusterHookReader.read_many)
Reader.register('memory_pool', GlusterMemoryPoolReader.read_one)
Reader.register('memory_pools', GlusterMemoryPoolReader.read_many)
Reader.register('server_hook', GlusterServerHookReader.read_one)
Reader.register('server_hooks', GlusterServerHookReader.read_many)
Reader.register('gluster_volume', GlusterVolumeReader.read_one)
Reader.register('gluster_volumes', GlusterVolumeReader.read_many)
Reader.register('gluster_volume_profile_details', GlusterVolumeProfileDetailsReader.read_one)
Reader.register('gluster_volume_profile_detailss', GlusterVolumeProfileDetailsReader.read_many)
Reader.register('grace_period', GracePeriodReader.read_one)
Reader.register('grace_periods', GracePeriodReader.read_many)
Reader.register('graphics_console', GraphicsConsoleReader.read_one)
Reader.register('graphics_consoles', GraphicsConsoleReader.read_many)
Reader.register('group', GroupReader.read_one)
Reader.register('groups', GroupReader.read_many)
Reader.register('guest_operating_system', GuestOperatingSystemReader.read_one)
Reader.register('guest_operating_systems', GuestOperatingSystemReader.read_many)
Reader.register('hardware_information', HardwareInformationReader.read_one)
Reader.register('hardware_informations', HardwareInformationReader.read_many)
Reader.register('high_availability', HighAvailabilityReader.read_one)
Reader.register('high_availabilities', HighAvailabilityReader.read_many)
Reader.register('hook', HookReader.read_one)
Reader.register('hooks', HookReader.read_many)
Reader.register('host', HostReader.read_one)
Reader.register('hosts', HostReader.read_many)
Reader.register('host_device', HostDeviceReader.read_one)
Reader.register('host_devices', HostDeviceReader.read_many)
Reader.register('host_device_passthrough', HostDevicePassthroughReader.read_one)
Reader.register('host_device_passthroughs', HostDevicePassthroughReader.read_many)
Reader.register('host_nic', HostNicReader.read_one)
Reader.register('host_nics', HostNicReader.read_many)
Reader.register('host_nic_virtual_functions_configuration', HostNicVirtualFunctionsConfigurationReader.read_one)
Reader.register('host_nic_virtual_functions_configurations', HostNicVirtualFunctionsConfigurationReader.read_many)
Reader.register('host_storage', HostStorageReader.read_one)
Reader.register('host_storages', HostStorageReader.read_many)
Reader.register('hosted_engine', HostedEngineReader.read_one)
Reader.register('hosted_engines', HostedEngineReader.read_many)
Reader.register('icon', IconReader.read_one)
Reader.register('icons', IconReader.read_many)
Reader.register('identified', IdentifiedReader.read_one)
Reader.register('identifieds', IdentifiedReader.read_many)
Reader.register('image', ImageReader.read_one)
Reader.register('images', ImageReader.read_many)
Reader.register('image_transfer', ImageTransferReader.read_one)
Reader.register('image_transfers', ImageTransferReader.read_many)
Reader.register('initialization', InitializationReader.read_one)
Reader.register('initializations', InitializationReader.read_many)
Reader.register('instance_type', InstanceTypeReader.read_one)
Reader.register('instance_types', InstanceTypeReader.read_many)
Reader.register('io', IoReader.read_one)
Reader.register('ios', IoReader.read_many)
Reader.register('ip', IpReader.read_one)
Reader.register('ips', IpReader.read_many)
Reader.register('ip_address_assignment', IpAddressAssignmentReader.read_one)
Reader.register('ip_address_assignments', IpAddressAssignmentReader.read_many)
Reader.register('iscsi_bond', IscsiBondReader.read_one)
Reader.register('iscsi_bonds', IscsiBondReader.read_many)
Reader.register('iscsi_details', IscsiDetailsReader.read_one)
Reader.register('iscsi_detailss', IscsiDetailsReader.read_many)
Reader.register('job', JobReader.read_one)
Reader.register('jobs', JobReader.read_many)
Reader.register('katello_erratum', KatelloErratumReader.read_one)
Reader.register('katello_errata', KatelloErratumReader.read_many)
Reader.register('kernel', KernelReader.read_one)
Reader.register('kernels', KernelReader.read_many)
Reader.register('ksm', KsmReader.read_one)
Reader.register('ksms', KsmReader.read_many)
Reader.register('link_layer_discovery_protocol_element', LinkLayerDiscoveryProtocolElementReader.read_one)
Reader.register('link_layer_discovery_protocol_elements', LinkLayerDiscoveryProtocolElementReader.read_many)
Reader.register('logical_unit', LogicalUnitReader.read_one)
Reader.register('logical_units', LogicalUnitReader.read_many)
Reader.register('m_dev_type', MDevTypeReader.read_one)
Reader.register('m_dev_types', MDevTypeReader.read_many)
Reader.register('mac', MacReader.read_one)
Reader.register('macs', MacReader.read_many)
Reader.register('mac_pool', MacPoolReader.read_one)
Reader.register('mac_pools', MacPoolReader.read_many)
Reader.register('memory_over_commit', MemoryOverCommitReader.read_one)
Reader.register('memory_over_commits', MemoryOverCommitReader.read_many)
Reader.register('memory_policy', MemoryPolicyReader.read_one)
Reader.register('memory_policies', MemoryPolicyReader.read_many)
Reader.register('method', MethodReader.read_one)
Reader.register('methods', MethodReader.read_many)
Reader.register('migration_bandwidth', MigrationBandwidthReader.read_one)
Reader.register('migration_bandwidths', MigrationBandwidthReader.read_many)
Reader.register('migration', MigrationOptionsReader.read_one)
Reader.register('migration_optionss', MigrationOptionsReader.read_many)
Reader.register('migration_policy', MigrationPolicyReader.read_one)
Reader.register('migration_policies', MigrationPolicyReader.read_many)
Reader.register('network', NetworkReader.read_one)
Reader.register('networks', NetworkReader.read_many)
Reader.register('network_attachment', NetworkAttachmentReader.read_one)
Reader.register('network_attachments', NetworkAttachmentReader.read_many)
Reader.register('network_configuration', NetworkConfigurationReader.read_one)
Reader.register('network_configurations', NetworkConfigurationReader.read_many)
Reader.register('network_filter', NetworkFilterReader.read_one)
Reader.register('network_filters', NetworkFilterReader.read_many)
Reader.register('network_filter_parameter', NetworkFilterParameterReader.read_one)
Reader.register('network_filter_parameters', NetworkFilterParameterReader.read_many)
Reader.register('network_label', NetworkLabelReader.read_one)
Reader.register('network_labels', NetworkLabelReader.read_many)
Reader.register('nfs_profile_detail', NfsProfileDetailReader.read_one)
Reader.register('nfs_profile_details', NfsProfileDetailReader.read_many)
Reader.register('nic', NicReader.read_one)
Reader.register('nics', NicReader.read_many)
Reader.register('nic_configuration', NicConfigurationReader.read_one)
Reader.register('nic_configurations', NicConfigurationReader.read_many)
Reader.register('host_numa_node', NumaNodeReader.read_one)
Reader.register('host_numa_nodes', NumaNodeReader.read_many)
Reader.register('numa_node_pin', NumaNodePinReader.read_one)
Reader.register('numa_node_pins', NumaNodePinReader.read_many)
Reader.register('openstack_image', OpenStackImageReader.read_one)
Reader.register('openstack_images', OpenStackImageReader.read_many)
Reader.register('openstack_image_provider', OpenStackImageProviderReader.read_one)
Reader.register('openstack_image_providers', OpenStackImageProviderReader.read_many)
Reader.register('openstack_network', OpenStackNetworkReader.read_one)
Reader.register('openstack_networks', OpenStackNetworkReader.read_many)
Reader.register('openstack_network_provider', OpenStackNetworkProviderReader.read_one)
Reader.register('openstack_network_providers', OpenStackNetworkProviderReader.read_many)
Reader.register('open_stack_provider', OpenStackProviderReader.read_one)
Reader.register('open_stack_providers', OpenStackProviderReader.read_many)
Reader.register('openstack_subnet', OpenStackSubnetReader.read_one)
Reader.register('openstack_subnets', OpenStackSubnetReader.read_many)
Reader.register('openstack_volume_provider', OpenStackVolumeProviderReader.read_one)
Reader.register('openstack_volume_providers', OpenStackVolumeProviderReader.read_many)
Reader.register('open_stack_volume_type', OpenStackVolumeTypeReader.read_one)
Reader.register('open_stack_volume_types', OpenStackVolumeTypeReader.read_many)
Reader.register('openstack_volume_authentication_key', OpenstackVolumeAuthenticationKeyReader.read_one)
Reader.register('openstack_volume_authentication_keys', OpenstackVolumeAuthenticationKeyReader.read_many)
Reader.register('os', OperatingSystemReader.read_one)
Reader.register('oss', OperatingSystemReader.read_many)
Reader.register('operating_system', OperatingSystemInfoReader.read_one)
Reader.register('operation_systems', OperatingSystemInfoReader.read_many)
Reader.register('option', OptionReader.read_one)
Reader.register('options', OptionReader.read_many)
Reader.register('package', PackageReader.read_one)
Reader.register('packages', PackageReader.read_many)
Reader.register('payload', PayloadReader.read_one)
Reader.register('payloads', PayloadReader.read_many)
Reader.register('permission', PermissionReader.read_one)
Reader.register('permissions', PermissionReader.read_many)
Reader.register('permit', PermitReader.read_one)
Reader.register('permits', PermitReader.read_many)
Reader.register('pm_proxy', PmProxyReader.read_one)
Reader.register('pm_proxies', PmProxyReader.read_many)
Reader.register('port_mirroring', PortMirroringReader.read_one)
Reader.register('port_mirrorings', PortMirroringReader.read_many)
Reader.register('power_management', PowerManagementReader.read_one)
Reader.register('power_managements', PowerManagementReader.read_many)
Reader.register('product', ProductReader.read_one)
Reader.register('products', ProductReader.read_many)
Reader.register('product_info', ProductInfoReader.read_one)
Reader.register('product_infos', ProductInfoReader.read_many)
Reader.register('profile_detail', ProfileDetailReader.read_one)
Reader.register('profile_details', ProfileDetailReader.read_many)
Reader.register('property', PropertyReader.read_one)
Reader.register('properties', PropertyReader.read_many)
Reader.register('proxy_ticket', ProxyTicketReader.read_one)
Reader.register('proxy_tickets', ProxyTicketReader.read_many)
Reader.register('qos', QosReader.read_one)
Reader.register('qoss', QosReader.read_many)
Reader.register('quota', QuotaReader.read_one)
Reader.register('quotas', QuotaReader.read_many)
Reader.register('quota_cluster_limit', QuotaClusterLimitReader.read_one)
Reader.register('quota_cluster_limits', QuotaClusterLimitReader.read_many)
Reader.register('quota_storage_limit', QuotaStorageLimitReader.read_one)
Reader.register('quota_storage_limits', QuotaStorageLimitReader.read_many)
Reader.register('range', RangeReader.read_one)
Reader.register('ranges', RangeReader.read_many)
Reader.register('rate', RateReader.read_one)
Reader.register('rates', RateReader.read_many)
Reader.register('registration_affinity_group_mapping', RegistrationAffinityGroupMappingReader.read_one)
Reader.register('registration_affinity_group_mappings', RegistrationAffinityGroupMappingReader.read_many)
Reader.register('registration_affinity_label_mapping', RegistrationAffinityLabelMappingReader.read_one)
Reader.register('registration_affinity_label_mappings', RegistrationAffinityLabelMappingReader.read_many)
Reader.register('registration_cluster_mapping', RegistrationClusterMappingReader.read_one)
Reader.register('registration_cluster_mappings', RegistrationClusterMappingReader.read_many)
Reader.register('registration_configuration', RegistrationConfigurationReader.read_one)
Reader.register('registration_configurations', RegistrationConfigurationReader.read_many)
Reader.register('registration_domain_mapping', RegistrationDomainMappingReader.read_one)
Reader.register('registration_domain_mappings', RegistrationDomainMappingReader.read_many)
Reader.register('registration_lun_mapping', RegistrationLunMappingReader.read_one)
Reader.register('registration_lun_mappings', RegistrationLunMappingReader.read_many)
Reader.register('registration_role_mapping', RegistrationRoleMappingReader.read_one)
Reader.register('registration_role_mappings', RegistrationRoleMappingReader.read_many)
Reader.register('registration_vnic_profile_mapping', RegistrationVnicProfileMappingReader.read_one)
Reader.register('registration_vnic_profile_mappings', RegistrationVnicProfileMappingReader.read_many)
Reader.register('reported_configuration', ReportedConfigurationReader.read_one)
Reader.register('reported_configurations', ReportedConfigurationReader.read_many)
Reader.register('reported_device', ReportedDeviceReader.read_one)
Reader.register('reported_devices', ReportedDeviceReader.read_many)
Reader.register('rng_device', RngDeviceReader.read_one)
Reader.register('rng_devices', RngDeviceReader.read_many)
Reader.register('role', RoleReader.read_one)
Reader.register('roles', RoleReader.read_many)
Reader.register('scheduling_policy', SchedulingPolicyReader.read_one)
Reader.register('scheduling_policies', SchedulingPolicyReader.read_many)
Reader.register('scheduling_policy_unit', SchedulingPolicyUnitReader.read_one)
Reader.register('scheduling_policy_units', SchedulingPolicyUnitReader.read_many)
Reader.register('se_linux', SeLinuxReader.read_one)
Reader.register('se_linuxs', SeLinuxReader.read_many)
Reader.register('serial_number', SerialNumberReader.read_one)
Reader.register('serial_numbers', SerialNumberReader.read_many)
Reader.register('session', SessionReader.read_one)
Reader.register('sessions', SessionReader.read_many)
Reader.register('skip_if_connectivity_broken', SkipIfConnectivityBrokenReader.read_one)
Reader.register('skip_if_connectivity_brokens', SkipIfConnectivityBrokenReader.read_many)
Reader.register('skip_if_sd_active', SkipIfSdActiveReader.read_one)
Reader.register('skip_if_sd_actives', SkipIfSdActiveReader.read_many)
Reader.register('snapshot', SnapshotReader.read_one)
Reader.register('snapshots', SnapshotReader.read_many)
Reader.register('special_objects', SpecialObjectsReader.read_one)
Reader.register('special_objectss', SpecialObjectsReader.read_many)
Reader.register('spm', SpmReader.read_one)
Reader.register('spms', SpmReader.read_many)
Reader.register('ssh', SshReader.read_one)
Reader.register('sshs', SshReader.read_many)
Reader.register('ssh_public_key', SshPublicKeyReader.read_one)
Reader.register('ssh_public_keys', SshPublicKeyReader.read_many)
Reader.register('sso', SsoReader.read_one)
Reader.register('ssos', SsoReader.read_many)
Reader.register('statistic', StatisticReader.read_one)
Reader.register('statistics', StatisticReader.read_many)
Reader.register('step', StepReader.read_one)
Reader.register('steps', StepReader.read_many)
Reader.register('storage_connection', StorageConnectionReader.read_one)
Reader.register('storage_connections', StorageConnectionReader.read_many)
Reader.register('storage_connection_extension', StorageConnectionExtensionReader.read_one)
Reader.register('storage_connection_extensions', StorageConnectionExtensionReader.read_many)
Reader.register('storage_domain', StorageDomainReader.read_one)
Reader.register('storage_domains', StorageDomainReader.read_many)
Reader.register('storage_domain_lease', StorageDomainLeaseReader.read_one)
Reader.register('storage_domain_leases', StorageDomainLeaseReader.read_many)
Reader.register('system_option', SystemOptionReader.read_one)
Reader.register('system_options', SystemOptionReader.read_many)
Reader.register('system_option_value', SystemOptionValueReader.read_one)
Reader.register('system_option_values', SystemOptionValueReader.read_many)
Reader.register('tag', TagReader.read_one)
Reader.register('tags', TagReader.read_many)
Reader.register('template', TemplateReader.read_one)
Reader.register('templates', TemplateReader.read_many)
Reader.register('template_version', TemplateVersionReader.read_one)
Reader.register('template_versions', TemplateVersionReader.read_many)
Reader.register('ticket', TicketReader.read_one)
Reader.register('tickets', TicketReader.read_many)
Reader.register('time_zone', TimeZoneReader.read_one)
Reader.register('time_zones', TimeZoneReader.read_many)
Reader.register('transparent_hugepages', TransparentHugePagesReader.read_one)
Reader.register('transparent_huge_pagess', TransparentHugePagesReader.read_many)
Reader.register('unmanaged_network', UnmanagedNetworkReader.read_one)
Reader.register('unmanaged_networks', UnmanagedNetworkReader.read_many)
Reader.register('usb', UsbReader.read_one)
Reader.register('usbs', UsbReader.read_many)
Reader.register('user', UserReader.read_one)
Reader.register('users', UserReader.read_many)
Reader.register('user_option', UserOptionReader.read_one)
Reader.register('user_options', UserOptionReader.read_many)
Reader.register('value', ValueReader.read_one)
Reader.register('values', ValueReader.read_many)
Reader.register('vcpu_pin', VcpuPinReader.read_one)
Reader.register('vcpu_pins', VcpuPinReader.read_many)
Reader.register('vendor', VendorReader.read_one)
Reader.register('vendors', VendorReader.read_many)
Reader.register('version', VersionReader.read_one)
Reader.register('versions', VersionReader.read_many)
Reader.register('virtio_scsi', VirtioScsiReader.read_one)
Reader.register('virtio_scsis', VirtioScsiReader.read_many)
Reader.register('vm_numa_node', VirtualNumaNodeReader.read_one)
Reader.register('vm_numa_nodes', VirtualNumaNodeReader.read_many)
Reader.register('vlan', VlanReader.read_one)
Reader.register('vlans', VlanReader.read_many)
Reader.register('vm', VmReader.read_one)
Reader.register('vms', VmReader.read_many)
Reader.register('vm_base', VmBaseReader.read_one)
Reader.register('vm_bases', VmBaseReader.read_many)
Reader.register('vm_placement_policy', VmPlacementPolicyReader.read_one)
Reader.register('vm_placement_policies', VmPlacementPolicyReader.read_many)
Reader.register('vm_pool', VmPoolReader.read_one)
Reader.register('vm_pools', VmPoolReader.read_many)
Reader.register('vm_summary', VmSummaryReader.read_one)
Reader.register('vm_summaries', VmSummaryReader.read_many)
Reader.register('vnic_pass_through', VnicPassThroughReader.read_one)
Reader.register('vnic_pass_throughs', VnicPassThroughReader.read_many)
Reader.register('vnic_profile', VnicProfileReader.read_one)
Reader.register('vnic_profiles', VnicProfileReader.read_many)
Reader.register('vnic_profile_mapping', VnicProfileMappingReader.read_one)
Reader.register('vnic_profile_mappings', VnicProfileMappingReader.read_many)
Reader.register('volume_group', VolumeGroupReader.read_one)
Reader.register('volume_groups', VolumeGroupReader.read_many)
Reader.register('watchdog', WatchdogReader.read_one)
Reader.register('watchdogs', WatchdogReader.read_many)
Reader.register('weight', WeightReader.read_one)
Reader.register('weights', WeightReader.read_many)
