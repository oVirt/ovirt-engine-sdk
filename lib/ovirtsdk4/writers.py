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
from ovirtsdk4.writer import Writer


class ActionWriter(Writer):

    def __init__(self):
        super(ActionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'action'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.activate is not None:
            Writer.write_boolean(writer, 'activate', obj.activate)
        if obj.allow_partial_import is not None:
            Writer.write_boolean(writer, 'allow_partial_import', obj.allow_partial_import)
        if obj.async_ is not None:
            Writer.write_boolean(writer, 'async', obj.async_)
        if obj.attachment is not None:
            DiskAttachmentWriter.write_one(obj.attachment, writer, 'attachment')
        if obj.authorized_key is not None:
            AuthorizedKeyWriter.write_one(obj.authorized_key, writer, 'authorized_key')
        if obj.auto_pinning_policy is not None:
            Writer.write_string(writer, 'auto_pinning_policy', obj.auto_pinning_policy.value)
        if obj.bricks is not None:
            GlusterBrickWriter.write_many(obj.bricks, writer, 'brick', 'bricks')
        if obj.certificates is not None:
            CertificateWriter.write_many(obj.certificates, writer, 'certificate', 'certificates')
        if obj.check_connectivity is not None:
            Writer.write_boolean(writer, 'check_connectivity', obj.check_connectivity)
        if obj.clone is not None:
            Writer.write_boolean(writer, 'clone', obj.clone)
        if obj.clone_permissions is not None:
            Writer.write_boolean(writer, 'clone_permissions', obj.clone_permissions)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.collapse_snapshots is not None:
            Writer.write_boolean(writer, 'collapse_snapshots', obj.collapse_snapshots)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.commit_on_success is not None:
            Writer.write_boolean(writer, 'commit_on_success', obj.commit_on_success)
        if obj.connection is not None:
            StorageConnectionWriter.write_one(obj.connection, writer, 'connection')
        if obj.connectivity_timeout is not None:
            Writer.write_integer(writer, 'connectivity_timeout', obj.connectivity_timeout)
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.deploy_hosted_engine is not None:
            Writer.write_boolean(writer, 'deploy_hosted_engine', obj.deploy_hosted_engine)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.details is not None:
            GlusterVolumeProfileDetailsWriter.write_one(obj.details, writer, 'details')
        if obj.directory is not None:
            Writer.write_string(writer, 'directory', obj.directory)
        if obj.discard_snapshots is not None:
            Writer.write_boolean(writer, 'discard_snapshots', obj.discard_snapshots)
        if obj.discovered_targets is not None:
            IscsiDetailsWriter.write_many(obj.discovered_targets, writer, 'iscsi_details', 'discovered_targets')
        if obj.disk is not None:
            DiskWriter.write_one(obj.disk, writer, 'disk')
        if obj.disk_profile is not None:
            DiskProfileWriter.write_one(obj.disk_profile, writer, 'disk_profile')
        if obj.disks is not None:
            DiskWriter.write_many(obj.disks, writer, 'disk', 'disks')
        if obj.exclusive is not None:
            Writer.write_boolean(writer, 'exclusive', obj.exclusive)
        if obj.fault is not None:
            FaultWriter.write_one(obj.fault, writer, 'fault')
        if obj.fence_type is not None:
            Writer.write_string(writer, 'fence_type', obj.fence_type)
        if obj.filename is not None:
            Writer.write_string(writer, 'filename', obj.filename)
        if obj.filter is not None:
            Writer.write_boolean(writer, 'filter', obj.filter)
        if obj.fix_layout is not None:
            Writer.write_boolean(writer, 'fix_layout', obj.fix_layout)
        if obj.force is not None:
            Writer.write_boolean(writer, 'force', obj.force)
        if obj.grace_period is not None:
            GracePeriodWriter.write_one(obj.grace_period, writer, 'grace_period')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.image is not None:
            Writer.write_string(writer, 'image', obj.image)
        if obj.image_transfer is not None:
            ImageTransferWriter.write_one(obj.image_transfer, writer, 'image_transfer')
        if obj.import_as_template is not None:
            Writer.write_boolean(writer, 'import_as_template', obj.import_as_template)
        if obj.is_attached is not None:
            Writer.write_boolean(writer, 'is_attached', obj.is_attached)
        if obj.iscsi is not None:
            IscsiDetailsWriter.write_one(obj.iscsi, writer, 'iscsi')
        if obj.iscsi_targets is not None:
            writer.write_start('iscsi_targets')
            for item in obj.iscsi_targets:
                if item is not None:
                    Writer.write_string(writer, 'iscsi_target', item)
            writer.write_end()
        if obj.job is not None:
            JobWriter.write_one(obj.job, writer, 'job')
        if obj.lease is not None:
            StorageDomainLeaseWriter.write_one(obj.lease, writer, 'lease')
        if obj.logical_units is not None:
            LogicalUnitWriter.write_many(obj.logical_units, writer, 'logical_unit', 'logical_units')
        if obj.maintenance_after_restart is not None:
            Writer.write_boolean(writer, 'maintenance_after_restart', obj.maintenance_after_restart)
        if obj.maintenance_enabled is not None:
            Writer.write_boolean(writer, 'maintenance_enabled', obj.maintenance_enabled)
        if obj.migrate_vms_in_affinity_closure is not None:
            Writer.write_boolean(writer, 'migrate_vms_in_affinity_closure', obj.migrate_vms_in_affinity_closure)
        if obj.modified_bonds is not None:
            HostNicWriter.write_many(obj.modified_bonds, writer, 'host_nic', 'modified_bonds')
        if obj.modified_labels is not None:
            NetworkLabelWriter.write_many(obj.modified_labels, writer, 'network_label', 'modified_labels')
        if obj.modified_network_attachments is not None:
            NetworkAttachmentWriter.write_many(obj.modified_network_attachments, writer, 'network_attachment', 'modified_network_attachments')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.optimize_cpu_settings is not None:
            Writer.write_boolean(writer, 'optimize_cpu_settings', obj.optimize_cpu_settings)
        if obj.option is not None:
            OptionWriter.write_one(obj.option, writer, 'option')
        if obj.pause is not None:
            Writer.write_boolean(writer, 'pause', obj.pause)
        if obj.permission is not None:
            PermissionWriter.write_one(obj.permission, writer, 'permission')
        if obj.power_management is not None:
            PowerManagementWriter.write_one(obj.power_management, writer, 'power_management')
        if obj.proxy_ticket is not None:
            ProxyTicketWriter.write_one(obj.proxy_ticket, writer, 'proxy_ticket')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.reason is not None:
            Writer.write_string(writer, 'reason', obj.reason)
        if obj.reassign_bad_macs is not None:
            Writer.write_boolean(writer, 'reassign_bad_macs', obj.reassign_bad_macs)
        if obj.reboot is not None:
            Writer.write_boolean(writer, 'reboot', obj.reboot)
        if obj.registration_configuration is not None:
            RegistrationConfigurationWriter.write_one(obj.registration_configuration, writer, 'registration_configuration')
        if obj.remote_viewer_connection_file is not None:
            Writer.write_string(writer, 'remote_viewer_connection_file', obj.remote_viewer_connection_file)
        if obj.removed_bonds is not None:
            HostNicWriter.write_many(obj.removed_bonds, writer, 'host_nic', 'removed_bonds')
        if obj.removed_labels is not None:
            NetworkLabelWriter.write_many(obj.removed_labels, writer, 'network_label', 'removed_labels')
        if obj.removed_network_attachments is not None:
            NetworkAttachmentWriter.write_many(obj.removed_network_attachments, writer, 'network_attachment', 'removed_network_attachments')
        if obj.resolution_type is not None:
            Writer.write_string(writer, 'resolution_type', obj.resolution_type)
        if obj.restore_memory is not None:
            Writer.write_boolean(writer, 'restore_memory', obj.restore_memory)
        if obj.root_password is not None:
            Writer.write_string(writer, 'root_password', obj.root_password)
        if obj.seal is not None:
            Writer.write_boolean(writer, 'seal', obj.seal)
        if obj.snapshot is not None:
            SnapshotWriter.write_one(obj.snapshot, writer, 'snapshot')
        if obj.source_host is not None:
            HostWriter.write_one(obj.source_host, writer, 'source_host')
        if obj.ssh is not None:
            SshWriter.write_one(obj.ssh, writer, 'ssh')
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status)
        if obj.stop_gluster_service is not None:
            Writer.write_boolean(writer, 'stop_gluster_service', obj.stop_gluster_service)
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.storage_domains is not None:
            StorageDomainWriter.write_many(obj.storage_domains, writer, 'storage_domain', 'storage_domains')
        if obj.succeeded is not None:
            Writer.write_boolean(writer, 'succeeded', obj.succeeded)
        if obj.synchronized_network_attachments is not None:
            NetworkAttachmentWriter.write_many(obj.synchronized_network_attachments, writer, 'network_attachment', 'synchronized_network_attachments')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.ticket is not None:
            TicketWriter.write_one(obj.ticket, writer, 'ticket')
        if obj.timeout is not None:
            Writer.write_integer(writer, 'timeout', obj.timeout)
        if obj.undeploy_hosted_engine is not None:
            Writer.write_boolean(writer, 'undeploy_hosted_engine', obj.undeploy_hosted_engine)
        if obj.upgrade_action is not None:
            Writer.write_string(writer, 'upgrade_action', obj.upgrade_action.value)
        if obj.use_cloud_init is not None:
            Writer.write_boolean(writer, 'use_cloud_init', obj.use_cloud_init)
        if obj.use_ignition is not None:
            Writer.write_boolean(writer, 'use_ignition', obj.use_ignition)
        if obj.use_initialization is not None:
            Writer.write_boolean(writer, 'use_initialization', obj.use_initialization)
        if obj.use_sysprep is not None:
            Writer.write_boolean(writer, 'use_sysprep', obj.use_sysprep)
        if obj.virtual_functions_configuration is not None:
            HostNicVirtualFunctionsConfigurationWriter.write_one(obj.virtual_functions_configuration, writer, 'virtual_functions_configuration')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vnic_profile_mappings is not None:
            VnicProfileMappingWriter.write_many(obj.vnic_profile_mappings, writer, 'vnic_profile_mapping', 'vnic_profile_mappings')
        if obj.volatile is not None:
            Writer.write_boolean(writer, 'volatile', obj.volatile)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'action'
        if plural is None:
            plural = 'actions'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ActionWriter.write_one(obj, writer, singular)
        writer.write_end()


class AffinityGroupWriter(Writer):

    def __init__(self):
        super(AffinityGroupWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'affinity_group'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.broken is not None:
            Writer.write_boolean(writer, 'broken', obj.broken)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.enforcing is not None:
            Writer.write_boolean(writer, 'enforcing', obj.enforcing)
        if obj.hosts_rule is not None:
            AffinityRuleWriter.write_one(obj.hosts_rule, writer, 'hosts_rule')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.positive is not None:
            Writer.write_boolean(writer, 'positive', obj.positive)
        if obj.priority is not None:
            Writer.write_decimal(writer, 'priority', obj.priority)
        if obj.vms_rule is not None:
            AffinityRuleWriter.write_one(obj.vms_rule, writer, 'vms_rule')
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.host_labels is not None:
            AffinityLabelWriter.write_many(obj.host_labels, writer, 'affinity_label', 'host_labels')
        if obj.hosts is not None:
            HostWriter.write_many(obj.hosts, writer, 'host', 'hosts')
        if obj.vm_labels is not None:
            AffinityLabelWriter.write_many(obj.vm_labels, writer, 'affinity_label', 'vm_labels')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'affinity_group'
        if plural is None:
            plural = 'affinity_groups'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            AffinityGroupWriter.write_one(obj, writer, singular)
        writer.write_end()


class AffinityLabelWriter(Writer):

    def __init__(self):
        super(AffinityLabelWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'affinity_label'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.has_implicit_affinity_group is not None:
            Writer.write_boolean(writer, 'has_implicit_affinity_group', obj.has_implicit_affinity_group)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.read_only is not None:
            Writer.write_boolean(writer, 'read_only', obj.read_only)
        if obj.hosts is not None:
            HostWriter.write_many(obj.hosts, writer, 'host', 'hosts')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'affinity_label'
        if plural is None:
            plural = 'affinity_labels'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            AffinityLabelWriter.write_one(obj, writer, singular)
        writer.write_end()


class AffinityRuleWriter(Writer):

    def __init__(self):
        super(AffinityRuleWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'affinity_rule'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        if obj.enforcing is not None:
            Writer.write_boolean(writer, 'enforcing', obj.enforcing)
        if obj.positive is not None:
            Writer.write_boolean(writer, 'positive', obj.positive)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'affinity_rule'
        if plural is None:
            plural = 'affinity_rules'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            AffinityRuleWriter.write_one(obj, writer, singular)
        writer.write_end()


class AgentWriter(Writer):

    def __init__(self):
        super(AgentWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'agent'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.concurrent is not None:
            Writer.write_boolean(writer, 'concurrent', obj.concurrent)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.encrypt_options is not None:
            Writer.write_boolean(writer, 'encrypt_options', obj.encrypt_options)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.options is not None:
            OptionWriter.write_many(obj.options, writer, 'option', 'options')
        if obj.order is not None:
            Writer.write_integer(writer, 'order', obj.order)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'agent'
        if plural is None:
            plural = 'agents'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            AgentWriter.write_one(obj, writer, singular)
        writer.write_end()


class AgentConfigurationWriter(Writer):

    def __init__(self):
        super(AgentConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'agent_configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.broker_type is not None:
            Writer.write_string(writer, 'broker_type', obj.broker_type.value)
        if obj.network_mappings is not None:
            Writer.write_string(writer, 'network_mappings', obj.network_mappings)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'agent_configuration'
        if plural is None:
            plural = 'agent_configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            AgentConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class ApiWriter(Writer):

    def __init__(self):
        super(ApiWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'api'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.product_info is not None:
            ProductInfoWriter.write_one(obj.product_info, writer, 'product_info')
        if obj.special_objects is not None:
            SpecialObjectsWriter.write_one(obj.special_objects, writer, 'special_objects')
        if obj.summary is not None:
            ApiSummaryWriter.write_one(obj.summary, writer, 'summary')
        if obj.time is not None:
            Writer.write_date(writer, 'time', obj.time)
        if obj.authenticated_user is not None:
            UserWriter.write_one(obj.authenticated_user, writer, 'authenticated_user')
        if obj.effective_user is not None:
            UserWriter.write_one(obj.effective_user, writer, 'effective_user')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'api'
        if plural is None:
            plural = 'apis'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ApiWriter.write_one(obj, writer, singular)
        writer.write_end()


class ApiSummaryWriter(Writer):

    def __init__(self):
        super(ApiSummaryWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'api_summary'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.hosts is not None:
            ApiSummaryItemWriter.write_one(obj.hosts, writer, 'hosts')
        if obj.storage_domains is not None:
            ApiSummaryItemWriter.write_one(obj.storage_domains, writer, 'storage_domains')
        if obj.users is not None:
            ApiSummaryItemWriter.write_one(obj.users, writer, 'users')
        if obj.vms is not None:
            ApiSummaryItemWriter.write_one(obj.vms, writer, 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'api_summary'
        if plural is None:
            plural = 'api_summaries'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ApiSummaryWriter.write_one(obj, writer, singular)
        writer.write_end()


class ApiSummaryItemWriter(Writer):

    def __init__(self):
        super(ApiSummaryItemWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'api_summary_item'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.active is not None:
            Writer.write_integer(writer, 'active', obj.active)
        if obj.total is not None:
            Writer.write_integer(writer, 'total', obj.total)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'api_summary_item'
        if plural is None:
            plural = 'api_summary_items'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ApiSummaryItemWriter.write_one(obj, writer, singular)
        writer.write_end()


class ApplicationWriter(Writer):

    def __init__(self):
        super(ApplicationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'application'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'application'
        if plural is None:
            plural = 'applications'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ApplicationWriter.write_one(obj, writer, singular)
        writer.write_end()


class AuthorizedKeyWriter(Writer):

    def __init__(self):
        super(AuthorizedKeyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'authorized_key'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.key is not None:
            Writer.write_string(writer, 'key', obj.key)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'authorized_key'
        if plural is None:
            plural = 'authorized_keys'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            AuthorizedKeyWriter.write_one(obj, writer, singular)
        writer.write_end()


class BackupWriter(Writer):

    def __init__(self):
        super(BackupWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'backup'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.creation_date is not None:
            Writer.write_date(writer, 'creation_date', obj.creation_date)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.from_checkpoint_id is not None:
            Writer.write_string(writer, 'from_checkpoint_id', obj.from_checkpoint_id)
        if obj.modification_date is not None:
            Writer.write_date(writer, 'modification_date', obj.modification_date)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.phase is not None:
            Writer.write_string(writer, 'phase', obj.phase.value)
        if obj.to_checkpoint_id is not None:
            Writer.write_string(writer, 'to_checkpoint_id', obj.to_checkpoint_id)
        if obj.disks is not None:
            DiskWriter.write_many(obj.disks, writer, 'disk', 'disks')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'backup'
        if plural is None:
            plural = 'backups'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BackupWriter.write_one(obj, writer, singular)
        writer.write_end()


class BalanceWriter(Writer):

    def __init__(self):
        super(BalanceWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'balance'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.scheduling_policy is not None:
            SchedulingPolicyWriter.write_one(obj.scheduling_policy, writer, 'scheduling_policy')
        if obj.scheduling_policy_unit is not None:
            SchedulingPolicyUnitWriter.write_one(obj.scheduling_policy_unit, writer, 'scheduling_policy_unit')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'balance'
        if plural is None:
            plural = 'balances'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BalanceWriter.write_one(obj, writer, singular)
        writer.write_end()


class BiosWriter(Writer):

    def __init__(self):
        super(BiosWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'bios'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.boot_menu is not None:
            BootMenuWriter.write_one(obj.boot_menu, writer, 'boot_menu')
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'bios'
        if plural is None:
            plural = 'bioss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BiosWriter.write_one(obj, writer, singular)
        writer.write_end()


class BlockStatisticWriter(Writer):

    def __init__(self):
        super(BlockStatisticWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'block_statistic'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'block_statistic'
        if plural is None:
            plural = 'block_statistics'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BlockStatisticWriter.write_one(obj, writer, singular)
        writer.write_end()


class BondingWriter(Writer):

    def __init__(self):
        super(BondingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'bonding'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.ad_partner_mac is not None:
            MacWriter.write_one(obj.ad_partner_mac, writer, 'ad_partner_mac')
        if obj.options is not None:
            OptionWriter.write_many(obj.options, writer, 'option', 'options')
        if obj.slaves is not None:
            HostNicWriter.write_many(obj.slaves, writer, 'host_nic', 'slaves')
        if obj.active_slave is not None:
            HostNicWriter.write_one(obj.active_slave, writer, 'active_slave')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'bonding'
        if plural is None:
            plural = 'bondings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BondingWriter.write_one(obj, writer, singular)
        writer.write_end()


class BookmarkWriter(Writer):

    def __init__(self):
        super(BookmarkWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'bookmark'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'bookmark'
        if plural is None:
            plural = 'bookmarks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BookmarkWriter.write_one(obj, writer, singular)
        writer.write_end()


class BootWriter(Writer):

    def __init__(self):
        super(BootWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'boot'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.devices is not None:
            writer.write_start('devices')
            for item in obj.devices:
                if item is not None:
                    Writer.write_string(writer, 'device', item.value)
            writer.write_end()
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'boot'
        if plural is None:
            plural = 'boots'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BootWriter.write_one(obj, writer, singular)
        writer.write_end()


class BootMenuWriter(Writer):

    def __init__(self):
        super(BootMenuWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'boot_menu'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'boot_menu'
        if plural is None:
            plural = 'boot_menus'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BootMenuWriter.write_one(obj, writer, singular)
        writer.write_end()


class BrickProfileDetailWriter(Writer):

    def __init__(self):
        super(BrickProfileDetailWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'brick_profile_detail'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.profile_details is not None:
            ProfileDetailWriter.write_many(obj.profile_details, writer, 'profile_detail', 'profile_details')
        if obj.brick is not None:
            GlusterBrickWriter.write_one(obj.brick, writer, 'brick')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'brick_profile_detail'
        if plural is None:
            plural = 'brick_profile_details'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            BrickProfileDetailWriter.write_one(obj, writer, singular)
        writer.write_end()


class CdromWriter(Writer):

    def __init__(self):
        super(CdromWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cdrom'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.file is not None:
            FileWriter.write_one(obj.file, writer, 'file')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cdrom'
        if plural is None:
            plural = 'cdroms'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CdromWriter.write_one(obj, writer, singular)
        writer.write_end()


class CertificateWriter(Writer):

    def __init__(self):
        super(CertificateWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'certificate'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.content is not None:
            Writer.write_string(writer, 'content', obj.content)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.organization is not None:
            Writer.write_string(writer, 'organization', obj.organization)
        if obj.subject is not None:
            Writer.write_string(writer, 'subject', obj.subject)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'certificate'
        if plural is None:
            plural = 'certificates'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CertificateWriter.write_one(obj, writer, singular)
        writer.write_end()


class CheckpointWriter(Writer):

    def __init__(self):
        super(CheckpointWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'checkpoint'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.creation_date is not None:
            Writer.write_date(writer, 'creation_date', obj.creation_date)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.parent_id is not None:
            Writer.write_string(writer, 'parent_id', obj.parent_id)
        if obj.state is not None:
            Writer.write_string(writer, 'state', obj.state.value)
        if obj.disks is not None:
            DiskWriter.write_many(obj.disks, writer, 'disk', 'disks')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'checkpoint'
        if plural is None:
            plural = 'checkpoints'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CheckpointWriter.write_one(obj, writer, singular)
        writer.write_end()


class CloudInitWriter(Writer):

    def __init__(self):
        super(CloudInitWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cloud_init'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.authorized_keys is not None:
            AuthorizedKeyWriter.write_many(obj.authorized_keys, writer, 'authorized_key', 'authorized_keys')
        if obj.files is not None:
            FileWriter.write_many(obj.files, writer, 'file', 'files')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.network_configuration is not None:
            NetworkConfigurationWriter.write_one(obj.network_configuration, writer, 'network_configuration')
        if obj.regenerate_ssh_keys is not None:
            Writer.write_boolean(writer, 'regenerate_ssh_keys', obj.regenerate_ssh_keys)
        if obj.timezone is not None:
            Writer.write_string(writer, 'timezone', obj.timezone)
        if obj.users is not None:
            UserWriter.write_many(obj.users, writer, 'user', 'users')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cloud_init'
        if plural is None:
            plural = 'cloud_inits'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CloudInitWriter.write_one(obj, writer, singular)
        writer.write_end()


class ClusterWriter(Writer):

    def __init__(self):
        super(ClusterWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cluster'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.ballooning_enabled is not None:
            Writer.write_boolean(writer, 'ballooning_enabled', obj.ballooning_enabled)
        if obj.bios_type is not None:
            Writer.write_string(writer, 'bios_type', obj.bios_type.value)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.custom_scheduling_policy_properties is not None:
            PropertyWriter.write_many(obj.custom_scheduling_policy_properties, writer, 'property', 'custom_scheduling_policy_properties')
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.display is not None:
            DisplayWriter.write_one(obj.display, writer, 'display')
        if obj.error_handling is not None:
            ErrorHandlingWriter.write_one(obj.error_handling, writer, 'error_handling')
        if obj.fencing_policy is not None:
            FencingPolicyWriter.write_one(obj.fencing_policy, writer, 'fencing_policy')
        if obj.fips_mode is not None:
            Writer.write_string(writer, 'fips_mode', obj.fips_mode.value)
        if obj.firewall_type is not None:
            Writer.write_string(writer, 'firewall_type', obj.firewall_type.value)
        if obj.gluster_service is not None:
            Writer.write_boolean(writer, 'gluster_service', obj.gluster_service)
        if obj.gluster_tuned_profile is not None:
            Writer.write_string(writer, 'gluster_tuned_profile', obj.gluster_tuned_profile)
        if obj.ha_reservation is not None:
            Writer.write_boolean(writer, 'ha_reservation', obj.ha_reservation)
        if obj.ksm is not None:
            KsmWriter.write_one(obj.ksm, writer, 'ksm')
        if obj.log_max_memory_used_threshold is not None:
            Writer.write_integer(writer, 'log_max_memory_used_threshold', obj.log_max_memory_used_threshold)
        if obj.log_max_memory_used_threshold_type is not None:
            Writer.write_string(writer, 'log_max_memory_used_threshold_type', obj.log_max_memory_used_threshold_type.value)
        if obj.maintenance_reason_required is not None:
            Writer.write_boolean(writer, 'maintenance_reason_required', obj.maintenance_reason_required)
        if obj.memory_policy is not None:
            MemoryPolicyWriter.write_one(obj.memory_policy, writer, 'memory_policy')
        if obj.migration is not None:
            MigrationOptionsWriter.write_one(obj.migration, writer, 'migration')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.optional_reason is not None:
            Writer.write_boolean(writer, 'optional_reason', obj.optional_reason)
        if obj.required_rng_sources is not None:
            writer.write_start('required_rng_sources')
            for item in obj.required_rng_sources:
                if item is not None:
                    Writer.write_string(writer, 'required_rng_source', item.value)
            writer.write_end()
        if obj.serial_number is not None:
            SerialNumberWriter.write_one(obj.serial_number, writer, 'serial_number')
        if obj.supported_versions is not None:
            VersionWriter.write_many(obj.supported_versions, writer, 'version', 'supported_versions')
        if obj.switch_type is not None:
            Writer.write_string(writer, 'switch_type', obj.switch_type.value)
        if obj.threads_as_cores is not None:
            Writer.write_boolean(writer, 'threads_as_cores', obj.threads_as_cores)
        if obj.trusted_service is not None:
            Writer.write_boolean(writer, 'trusted_service', obj.trusted_service)
        if obj.tunnel_migration is not None:
            Writer.write_boolean(writer, 'tunnel_migration', obj.tunnel_migration)
        if obj.version is not None:
            VersionWriter.write_one(obj.version, writer, 'version')
        if obj.virt_service is not None:
            Writer.write_boolean(writer, 'virt_service', obj.virt_service)
        if obj.vnc_encryption is not None:
            Writer.write_boolean(writer, 'vnc_encryption', obj.vnc_encryption)
        if obj.affinity_groups is not None:
            AffinityGroupWriter.write_many(obj.affinity_groups, writer, 'affinity_group', 'affinity_groups')
        if obj.cpu_profiles is not None:
            CpuProfileWriter.write_many(obj.cpu_profiles, writer, 'cpu_profile', 'cpu_profiles')
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.enabled_features is not None:
            ClusterFeatureWriter.write_many(obj.enabled_features, writer, 'cluster_feature', 'enabled_features')
        if obj.external_network_providers is not None:
            ExternalProviderWriter.write_many(obj.external_network_providers, writer, 'external_provider', 'external_network_providers')
        if obj.gluster_hooks is not None:
            GlusterHookWriter.write_many(obj.gluster_hooks, writer, 'gluster_hook', 'gluster_hooks')
        if obj.gluster_volumes is not None:
            GlusterVolumeWriter.write_many(obj.gluster_volumes, writer, 'gluster_volume', 'gluster_volumes')
        if obj.mac_pool is not None:
            MacPoolWriter.write_one(obj.mac_pool, writer, 'mac_pool')
        if obj.management_network is not None:
            NetworkWriter.write_one(obj.management_network, writer, 'management_network')
        if obj.network_filters is not None:
            NetworkFilterWriter.write_many(obj.network_filters, writer, 'network_filter', 'network_filters')
        if obj.networks is not None:
            NetworkWriter.write_many(obj.networks, writer, 'network', 'networks')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.scheduling_policy is not None:
            SchedulingPolicyWriter.write_one(obj.scheduling_policy, writer, 'scheduling_policy')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cluster'
        if plural is None:
            plural = 'clusters'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ClusterWriter.write_one(obj, writer, singular)
        writer.write_end()


class ClusterFeatureWriter(Writer):

    def __init__(self):
        super(ClusterFeatureWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cluster_feature'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.cluster_level is not None:
            ClusterLevelWriter.write_one(obj.cluster_level, writer, 'cluster_level')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cluster_feature'
        if plural is None:
            plural = 'cluster_features'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ClusterFeatureWriter.write_one(obj, writer, singular)
        writer.write_end()


class ClusterLevelWriter(Writer):

    def __init__(self):
        super(ClusterLevelWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cluster_level'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.cpu_types is not None:
            CpuTypeWriter.write_many(obj.cpu_types, writer, 'cpu_type', 'cpu_types')
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.permits is not None:
            PermitWriter.write_many(obj.permits, writer, 'permit', 'permits')
        if obj.cluster_features is not None:
            ClusterFeatureWriter.write_many(obj.cluster_features, writer, 'cluster_feature', 'cluster_features')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cluster_level'
        if plural is None:
            plural = 'cluster_levels'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ClusterLevelWriter.write_one(obj, writer, singular)
        writer.write_end()


class ConfigurationWriter(Writer):

    def __init__(self):
        super(ConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.data is not None:
            Writer.write_string(writer, 'data', obj.data)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'configuration'
        if plural is None:
            plural = 'configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class ConsoleWriter(Writer):

    def __init__(self):
        super(ConsoleWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'console'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'console'
        if plural is None:
            plural = 'consoles'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ConsoleWriter.write_one(obj, writer, singular)
        writer.write_end()


class CoreWriter(Writer):

    def __init__(self):
        super(CoreWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'core'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.index is not None:
            Writer.write_integer(writer, 'index', obj.index)
        if obj.socket is not None:
            Writer.write_integer(writer, 'socket', obj.socket)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'core'
        if plural is None:
            plural = 'cores'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CoreWriter.write_one(obj, writer, singular)
        writer.write_end()


class CpuWriter(Writer):

    def __init__(self):
        super(CpuWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cpu'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.architecture is not None:
            Writer.write_string(writer, 'architecture', obj.architecture.value)
        if obj.cores is not None:
            CoreWriter.write_many(obj.cores, writer, 'core', 'cores')
        if obj.cpu_tune is not None:
            CpuTuneWriter.write_one(obj.cpu_tune, writer, 'cpu_tune')
        if obj.level is not None:
            Writer.write_integer(writer, 'level', obj.level)
        if obj.mode is not None:
            Writer.write_string(writer, 'mode', obj.mode.value)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.speed is not None:
            Writer.write_decimal(writer, 'speed', obj.speed)
        if obj.topology is not None:
            CpuTopologyWriter.write_one(obj.topology, writer, 'topology')
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cpu'
        if plural is None:
            plural = 'cpus'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CpuWriter.write_one(obj, writer, singular)
        writer.write_end()


class CpuProfileWriter(Writer):

    def __init__(self):
        super(CpuProfileWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cpu_profile'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.qos is not None:
            QosWriter.write_one(obj.qos, writer, 'qos')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cpu_profile'
        if plural is None:
            plural = 'cpu_profiles'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CpuProfileWriter.write_one(obj, writer, singular)
        writer.write_end()


class CpuTopologyWriter(Writer):

    def __init__(self):
        super(CpuTopologyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cpu_topology'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.cores is not None:
            Writer.write_integer(writer, 'cores', obj.cores)
        if obj.sockets is not None:
            Writer.write_integer(writer, 'sockets', obj.sockets)
        if obj.threads is not None:
            Writer.write_integer(writer, 'threads', obj.threads)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cpu_topology'
        if plural is None:
            plural = 'cpu_topologies'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CpuTopologyWriter.write_one(obj, writer, singular)
        writer.write_end()


class CpuTuneWriter(Writer):

    def __init__(self):
        super(CpuTuneWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cpu_tune'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.vcpu_pins is not None:
            VcpuPinWriter.write_many(obj.vcpu_pins, writer, 'vcpu_pin', 'vcpu_pins')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cpu_tune'
        if plural is None:
            plural = 'cpu_tunes'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CpuTuneWriter.write_one(obj, writer, singular)
        writer.write_end()


class CpuTypeWriter(Writer):

    def __init__(self):
        super(CpuTypeWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'cpu_type'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.architecture is not None:
            Writer.write_string(writer, 'architecture', obj.architecture.value)
        if obj.level is not None:
            Writer.write_integer(writer, 'level', obj.level)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'cpu_type'
        if plural is None:
            plural = 'cpu_types'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CpuTypeWriter.write_one(obj, writer, singular)
        writer.write_end()


class CustomPropertyWriter(Writer):

    def __init__(self):
        super(CustomPropertyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'custom_property'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.regexp is not None:
            Writer.write_string(writer, 'regexp', obj.regexp)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'custom_property'
        if plural is None:
            plural = 'custom_properties'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            CustomPropertyWriter.write_one(obj, writer, singular)
        writer.write_end()


class DataCenterWriter(Writer):

    def __init__(self):
        super(DataCenterWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'data_center'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.local is not None:
            Writer.write_boolean(writer, 'local', obj.local)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.quota_mode is not None:
            Writer.write_string(writer, 'quota_mode', obj.quota_mode.value)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.storage_format is not None:
            Writer.write_string(writer, 'storage_format', obj.storage_format.value)
        if obj.supported_versions is not None:
            VersionWriter.write_many(obj.supported_versions, writer, 'version', 'supported_versions')
        if obj.version is not None:
            VersionWriter.write_one(obj.version, writer, 'version')
        if obj.clusters is not None:
            ClusterWriter.write_many(obj.clusters, writer, 'cluster', 'clusters')
        if obj.iscsi_bonds is not None:
            IscsiBondWriter.write_many(obj.iscsi_bonds, writer, 'iscsi_bond', 'iscsi_bonds')
        if obj.mac_pool is not None:
            MacPoolWriter.write_one(obj.mac_pool, writer, 'mac_pool')
        if obj.networks is not None:
            NetworkWriter.write_many(obj.networks, writer, 'network', 'networks')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.qoss is not None:
            QosWriter.write_many(obj.qoss, writer, 'qos', 'qoss')
        if obj.quotas is not None:
            QuotaWriter.write_many(obj.quotas, writer, 'quota', 'quotas')
        if obj.storage_domains is not None:
            StorageDomainWriter.write_many(obj.storage_domains, writer, 'storage_domain', 'storage_domains')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'data_center'
        if plural is None:
            plural = 'data_centers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DataCenterWriter.write_one(obj, writer, singular)
        writer.write_end()


class DeviceWriter(Writer):

    def __init__(self):
        super(DeviceWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'device'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'device'
        if plural is None:
            plural = 'devices'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DeviceWriter.write_one(obj, writer, singular)
        writer.write_end()


class DiskWriter(Writer):

    def __init__(self):
        super(DiskWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'disk'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.active is not None:
            Writer.write_boolean(writer, 'active', obj.active)
        if obj.actual_size is not None:
            Writer.write_integer(writer, 'actual_size', obj.actual_size)
        if obj.alias is not None:
            Writer.write_string(writer, 'alias', obj.alias)
        if obj.backup is not None:
            Writer.write_string(writer, 'backup', obj.backup.value)
        if obj.backup_mode is not None:
            Writer.write_string(writer, 'backup_mode', obj.backup_mode.value)
        if obj.bootable is not None:
            Writer.write_boolean(writer, 'bootable', obj.bootable)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.content_type is not None:
            Writer.write_string(writer, 'content_type', obj.content_type.value)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.external_disk is not None:
            Writer.write_string(writer, 'external_disk', obj.external_disk)
        if obj.format is not None:
            Writer.write_string(writer, 'format', obj.format.value)
        if obj.image_id is not None:
            Writer.write_string(writer, 'image_id', obj.image_id)
        if obj.initial_size is not None:
            Writer.write_integer(writer, 'initial_size', obj.initial_size)
        if obj.interface is not None:
            Writer.write_string(writer, 'interface', obj.interface.value)
        if obj.logical_name is not None:
            Writer.write_string(writer, 'logical_name', obj.logical_name)
        if obj.lun_storage is not None:
            HostStorageWriter.write_one(obj.lun_storage, writer, 'lun_storage')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.propagate_errors is not None:
            Writer.write_boolean(writer, 'propagate_errors', obj.propagate_errors)
        if obj.provisioned_size is not None:
            Writer.write_integer(writer, 'provisioned_size', obj.provisioned_size)
        if obj.qcow_version is not None:
            Writer.write_string(writer, 'qcow_version', obj.qcow_version.value)
        if obj.read_only is not None:
            Writer.write_boolean(writer, 'read_only', obj.read_only)
        if obj.sgio is not None:
            Writer.write_string(writer, 'sgio', obj.sgio.value)
        if obj.shareable is not None:
            Writer.write_boolean(writer, 'shareable', obj.shareable)
        if obj.sparse is not None:
            Writer.write_boolean(writer, 'sparse', obj.sparse)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.storage_type is not None:
            Writer.write_string(writer, 'storage_type', obj.storage_type.value)
        if obj.total_size is not None:
            Writer.write_integer(writer, 'total_size', obj.total_size)
        if obj.uses_scsi_reservation is not None:
            Writer.write_boolean(writer, 'uses_scsi_reservation', obj.uses_scsi_reservation)
        if obj.wipe_after_delete is not None:
            Writer.write_boolean(writer, 'wipe_after_delete', obj.wipe_after_delete)
        if obj.disk_profile is not None:
            DiskProfileWriter.write_one(obj.disk_profile, writer, 'disk_profile')
        if obj.disk_snapshots is not None:
            DiskSnapshotWriter.write_many(obj.disk_snapshots, writer, 'disk_snapshot', 'disk_snapshots')
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.openstack_volume_type is not None:
            OpenStackVolumeTypeWriter.write_one(obj.openstack_volume_type, writer, 'openstack_volume_type')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.snapshot is not None:
            SnapshotWriter.write_one(obj.snapshot, writer, 'snapshot')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.storage_domains is not None:
            StorageDomainWriter.write_many(obj.storage_domains, writer, 'storage_domain', 'storage_domains')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'disk'
        if plural is None:
            plural = 'disks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DiskWriter.write_one(obj, writer, singular)
        writer.write_end()


class DiskAttachmentWriter(Writer):

    def __init__(self):
        super(DiskAttachmentWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'disk_attachment'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.active is not None:
            Writer.write_boolean(writer, 'active', obj.active)
        if obj.bootable is not None:
            Writer.write_boolean(writer, 'bootable', obj.bootable)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.interface is not None:
            Writer.write_string(writer, 'interface', obj.interface.value)
        if obj.logical_name is not None:
            Writer.write_string(writer, 'logical_name', obj.logical_name)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.pass_discard is not None:
            Writer.write_boolean(writer, 'pass_discard', obj.pass_discard)
        if obj.read_only is not None:
            Writer.write_boolean(writer, 'read_only', obj.read_only)
        if obj.uses_scsi_reservation is not None:
            Writer.write_boolean(writer, 'uses_scsi_reservation', obj.uses_scsi_reservation)
        if obj.disk is not None:
            DiskWriter.write_one(obj.disk, writer, 'disk')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'disk_attachment'
        if plural is None:
            plural = 'disk_attachments'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DiskAttachmentWriter.write_one(obj, writer, singular)
        writer.write_end()


class DiskProfileWriter(Writer):

    def __init__(self):
        super(DiskProfileWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'disk_profile'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.qos is not None:
            QosWriter.write_one(obj.qos, writer, 'qos')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'disk_profile'
        if plural is None:
            plural = 'disk_profiles'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DiskProfileWriter.write_one(obj, writer, singular)
        writer.write_end()


class DiskSnapshotWriter(Writer):

    def __init__(self):
        super(DiskSnapshotWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'disk_snapshot'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.active is not None:
            Writer.write_boolean(writer, 'active', obj.active)
        if obj.actual_size is not None:
            Writer.write_integer(writer, 'actual_size', obj.actual_size)
        if obj.alias is not None:
            Writer.write_string(writer, 'alias', obj.alias)
        if obj.backup is not None:
            Writer.write_string(writer, 'backup', obj.backup.value)
        if obj.backup_mode is not None:
            Writer.write_string(writer, 'backup_mode', obj.backup_mode.value)
        if obj.bootable is not None:
            Writer.write_boolean(writer, 'bootable', obj.bootable)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.content_type is not None:
            Writer.write_string(writer, 'content_type', obj.content_type.value)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.external_disk is not None:
            Writer.write_string(writer, 'external_disk', obj.external_disk)
        if obj.format is not None:
            Writer.write_string(writer, 'format', obj.format.value)
        if obj.image_id is not None:
            Writer.write_string(writer, 'image_id', obj.image_id)
        if obj.initial_size is not None:
            Writer.write_integer(writer, 'initial_size', obj.initial_size)
        if obj.interface is not None:
            Writer.write_string(writer, 'interface', obj.interface.value)
        if obj.logical_name is not None:
            Writer.write_string(writer, 'logical_name', obj.logical_name)
        if obj.lun_storage is not None:
            HostStorageWriter.write_one(obj.lun_storage, writer, 'lun_storage')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.propagate_errors is not None:
            Writer.write_boolean(writer, 'propagate_errors', obj.propagate_errors)
        if obj.provisioned_size is not None:
            Writer.write_integer(writer, 'provisioned_size', obj.provisioned_size)
        if obj.qcow_version is not None:
            Writer.write_string(writer, 'qcow_version', obj.qcow_version.value)
        if obj.read_only is not None:
            Writer.write_boolean(writer, 'read_only', obj.read_only)
        if obj.sgio is not None:
            Writer.write_string(writer, 'sgio', obj.sgio.value)
        if obj.shareable is not None:
            Writer.write_boolean(writer, 'shareable', obj.shareable)
        if obj.sparse is not None:
            Writer.write_boolean(writer, 'sparse', obj.sparse)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.storage_type is not None:
            Writer.write_string(writer, 'storage_type', obj.storage_type.value)
        if obj.total_size is not None:
            Writer.write_integer(writer, 'total_size', obj.total_size)
        if obj.uses_scsi_reservation is not None:
            Writer.write_boolean(writer, 'uses_scsi_reservation', obj.uses_scsi_reservation)
        if obj.wipe_after_delete is not None:
            Writer.write_boolean(writer, 'wipe_after_delete', obj.wipe_after_delete)
        if obj.disk is not None:
            DiskWriter.write_one(obj.disk, writer, 'disk')
        if obj.disk_profile is not None:
            DiskProfileWriter.write_one(obj.disk_profile, writer, 'disk_profile')
        if obj.disk_snapshots is not None:
            DiskSnapshotWriter.write_many(obj.disk_snapshots, writer, 'disk_snapshot', 'disk_snapshots')
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.openstack_volume_type is not None:
            OpenStackVolumeTypeWriter.write_one(obj.openstack_volume_type, writer, 'openstack_volume_type')
        if obj.parent is not None:
            DiskSnapshotWriter.write_one(obj.parent, writer, 'parent')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.snapshot is not None:
            SnapshotWriter.write_one(obj.snapshot, writer, 'snapshot')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.storage_domains is not None:
            StorageDomainWriter.write_many(obj.storage_domains, writer, 'storage_domain', 'storage_domains')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'disk_snapshot'
        if plural is None:
            plural = 'disk_snapshots'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DiskSnapshotWriter.write_one(obj, writer, singular)
        writer.write_end()


class DisplayWriter(Writer):

    def __init__(self):
        super(DisplayWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'display'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.allow_override is not None:
            Writer.write_boolean(writer, 'allow_override', obj.allow_override)
        if obj.certificate is not None:
            CertificateWriter.write_one(obj.certificate, writer, 'certificate')
        if obj.copy_paste_enabled is not None:
            Writer.write_boolean(writer, 'copy_paste_enabled', obj.copy_paste_enabled)
        if obj.disconnect_action is not None:
            Writer.write_string(writer, 'disconnect_action', obj.disconnect_action)
        if obj.file_transfer_enabled is not None:
            Writer.write_boolean(writer, 'file_transfer_enabled', obj.file_transfer_enabled)
        if obj.keyboard_layout is not None:
            Writer.write_string(writer, 'keyboard_layout', obj.keyboard_layout)
        if obj.monitors is not None:
            Writer.write_integer(writer, 'monitors', obj.monitors)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.proxy is not None:
            Writer.write_string(writer, 'proxy', obj.proxy)
        if obj.secure_port is not None:
            Writer.write_integer(writer, 'secure_port', obj.secure_port)
        if obj.single_qxl_pci is not None:
            Writer.write_boolean(writer, 'single_qxl_pci', obj.single_qxl_pci)
        if obj.smartcard_enabled is not None:
            Writer.write_boolean(writer, 'smartcard_enabled', obj.smartcard_enabled)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'display'
        if plural is None:
            plural = 'displays'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DisplayWriter.write_one(obj, writer, singular)
        writer.write_end()


class DnsWriter(Writer):

    def __init__(self):
        super(DnsWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'dns'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.search_domains is not None:
            HostWriter.write_many(obj.search_domains, writer, 'host', 'search_domains')
        if obj.servers is not None:
            HostWriter.write_many(obj.servers, writer, 'host', 'servers')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'dns'
        if plural is None:
            plural = 'dnss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DnsWriter.write_one(obj, writer, singular)
        writer.write_end()


class DnsResolverConfigurationWriter(Writer):

    def __init__(self):
        super(DnsResolverConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'dns_resolver_configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.name_servers is not None:
            writer.write_start('name_servers')
            for item in obj.name_servers:
                if item is not None:
                    Writer.write_string(writer, 'name_server', item)
            writer.write_end()
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'dns_resolver_configuration'
        if plural is None:
            plural = 'dns_resolver_configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DnsResolverConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class DomainWriter(Writer):

    def __init__(self):
        super(DomainWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'domain'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        if obj.groups is not None:
            GroupWriter.write_many(obj.groups, writer, 'group', 'groups')
        if obj.users is not None:
            UserWriter.write_many(obj.users, writer, 'user', 'users')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'domain'
        if plural is None:
            plural = 'domains'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            DomainWriter.write_one(obj, writer, singular)
        writer.write_end()


class EntityProfileDetailWriter(Writer):

    def __init__(self):
        super(EntityProfileDetailWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'entity_profile_detail'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.profile_details is not None:
            ProfileDetailWriter.write_many(obj.profile_details, writer, 'profile_detail', 'profile_details')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'entity_profile_detail'
        if plural is None:
            plural = 'entity_profile_details'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            EntityProfileDetailWriter.write_one(obj, writer, singular)
        writer.write_end()


class ErrorHandlingWriter(Writer):

    def __init__(self):
        super(ErrorHandlingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'error_handling'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.on_error is not None:
            Writer.write_string(writer, 'on_error', obj.on_error.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'error_handling'
        if plural is None:
            plural = 'error_handlings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ErrorHandlingWriter.write_one(obj, writer, singular)
        writer.write_end()


class EventWriter(Writer):

    def __init__(self):
        super(EventWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'event'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.code is not None:
            Writer.write_integer(writer, 'code', obj.code)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.correlation_id is not None:
            Writer.write_string(writer, 'correlation_id', obj.correlation_id)
        if obj.custom_data is not None:
            Writer.write_string(writer, 'custom_data', obj.custom_data)
        if obj.custom_id is not None:
            Writer.write_integer(writer, 'custom_id', obj.custom_id)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.flood_rate is not None:
            Writer.write_integer(writer, 'flood_rate', obj.flood_rate)
        if obj.index is not None:
            Writer.write_integer(writer, 'index', obj.index)
        if obj.log_on_host is not None:
            Writer.write_boolean(writer, 'log_on_host', obj.log_on_host)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.origin is not None:
            Writer.write_string(writer, 'origin', obj.origin)
        if obj.severity is not None:
            Writer.write_string(writer, 'severity', obj.severity.value)
        if obj.time is not None:
            Writer.write_date(writer, 'time', obj.time)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'event'
        if plural is None:
            plural = 'events'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            EventWriter.write_one(obj, writer, singular)
        writer.write_end()


class EventSubscriptionWriter(Writer):

    def __init__(self):
        super(EventSubscriptionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'event_subscription'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.event is not None:
            Writer.write_string(writer, 'event', obj.event.value)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.notification_method is not None:
            Writer.write_string(writer, 'notification_method', obj.notification_method.value)
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'event_subscription'
        if plural is None:
            plural = 'event_subscriptions'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            EventSubscriptionWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalComputeResourceWriter(Writer):

    def __init__(self):
        super(ExternalComputeResourceWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_compute_resource'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.provider is not None:
            Writer.write_string(writer, 'provider', obj.provider)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.user is not None:
            Writer.write_string(writer, 'user', obj.user)
        if obj.external_host_provider is not None:
            ExternalHostProviderWriter.write_one(obj.external_host_provider, writer, 'external_host_provider')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_compute_resource'
        if plural is None:
            plural = 'external_compute_resources'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalComputeResourceWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalDiscoveredHostWriter(Writer):

    def __init__(self):
        super(ExternalDiscoveredHostWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_discovered_host'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.ip is not None:
            Writer.write_string(writer, 'ip', obj.ip)
        if obj.last_report is not None:
            Writer.write_string(writer, 'last_report', obj.last_report)
        if obj.mac is not None:
            Writer.write_string(writer, 'mac', obj.mac)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.subnet_name is not None:
            Writer.write_string(writer, 'subnet_name', obj.subnet_name)
        if obj.external_host_provider is not None:
            ExternalHostProviderWriter.write_one(obj.external_host_provider, writer, 'external_host_provider')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_discovered_host'
        if plural is None:
            plural = 'external_discovered_hosts'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalDiscoveredHostWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalHostWriter(Writer):

    def __init__(self):
        super(ExternalHostWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_host'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.external_host_provider is not None:
            ExternalHostProviderWriter.write_one(obj.external_host_provider, writer, 'external_host_provider')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_host'
        if plural is None:
            plural = 'external_hosts'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalHostWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalHostGroupWriter(Writer):

    def __init__(self):
        super(ExternalHostGroupWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_host_group'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.architecture_name is not None:
            Writer.write_string(writer, 'architecture_name', obj.architecture_name)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.domain_name is not None:
            Writer.write_string(writer, 'domain_name', obj.domain_name)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.operating_system_name is not None:
            Writer.write_string(writer, 'operating_system_name', obj.operating_system_name)
        if obj.subnet_name is not None:
            Writer.write_string(writer, 'subnet_name', obj.subnet_name)
        if obj.external_host_provider is not None:
            ExternalHostProviderWriter.write_one(obj.external_host_provider, writer, 'external_host_provider')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_host_group'
        if plural is None:
            plural = 'external_host_groups'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalHostGroupWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalHostProviderWriter(Writer):

    def __init__(self):
        super(ExternalHostProviderWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_host_provider'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.authentication_url is not None:
            Writer.write_string(writer, 'authentication_url', obj.authentication_url)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.requires_authentication is not None:
            Writer.write_boolean(writer, 'requires_authentication', obj.requires_authentication)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.certificates is not None:
            CertificateWriter.write_many(obj.certificates, writer, 'certificate', 'certificates')
        if obj.compute_resources is not None:
            ExternalComputeResourceWriter.write_many(obj.compute_resources, writer, 'external_compute_resource', 'compute_resources')
        if obj.discovered_hosts is not None:
            ExternalDiscoveredHostWriter.write_many(obj.discovered_hosts, writer, 'external_discovered_host', 'discovered_hosts')
        if obj.host_groups is not None:
            ExternalHostGroupWriter.write_many(obj.host_groups, writer, 'external_host_group', 'host_groups')
        if obj.hosts is not None:
            HostWriter.write_many(obj.hosts, writer, 'host', 'hosts')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_host_provider'
        if plural is None:
            plural = 'external_host_providers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalHostProviderWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalNetworkProviderConfigurationWriter(Writer):

    def __init__(self):
        super(ExternalNetworkProviderConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_network_provider_configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.external_network_provider is not None:
            ExternalProviderWriter.write_one(obj.external_network_provider, writer, 'external_network_provider')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_network_provider_configuration'
        if plural is None:
            plural = 'external_network_provider_configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalNetworkProviderConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalProviderWriter(Writer):

    def __init__(self):
        super(ExternalProviderWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_provider'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.authentication_url is not None:
            Writer.write_string(writer, 'authentication_url', obj.authentication_url)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.requires_authentication is not None:
            Writer.write_boolean(writer, 'requires_authentication', obj.requires_authentication)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_provider'
        if plural is None:
            plural = 'external_providers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalProviderWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalTemplateImportWriter(Writer):

    def __init__(self):
        super(ExternalTemplateImportWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_template_import'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.clone is not None:
            Writer.write_boolean(writer, 'clone', obj.clone)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.cpu_profile is not None:
            CpuProfileWriter.write_one(obj.cpu_profile, writer, 'cpu_profile')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_template_import'
        if plural is None:
            plural = 'external_template_imports'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalTemplateImportWriter.write_one(obj, writer, singular)
        writer.write_end()


class ExternalVmImportWriter(Writer):

    def __init__(self):
        super(ExternalVmImportWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'external_vm_import'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.provider is not None:
            Writer.write_string(writer, 'provider', obj.provider.value)
        if obj.sparse is not None:
            Writer.write_boolean(writer, 'sparse', obj.sparse)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.cpu_profile is not None:
            CpuProfileWriter.write_one(obj.cpu_profile, writer, 'cpu_profile')
        if obj.drivers_iso is not None:
            FileWriter.write_one(obj.drivers_iso, writer, 'drivers_iso')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'external_vm_import'
        if plural is None:
            plural = 'external_vm_imports'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ExternalVmImportWriter.write_one(obj, writer, singular)
        writer.write_end()


class FaultWriter(Writer):

    def __init__(self):
        super(FaultWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'fault'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.detail is not None:
            Writer.write_string(writer, 'detail', obj.detail)
        if obj.reason is not None:
            Writer.write_string(writer, 'reason', obj.reason)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'fault'
        if plural is None:
            plural = 'faults'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            FaultWriter.write_one(obj, writer, singular)
        writer.write_end()


class FencingPolicyWriter(Writer):

    def __init__(self):
        super(FencingPolicyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'fencing_policy'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        if obj.skip_if_connectivity_broken is not None:
            SkipIfConnectivityBrokenWriter.write_one(obj.skip_if_connectivity_broken, writer, 'skip_if_connectivity_broken')
        if obj.skip_if_gluster_bricks_up is not None:
            Writer.write_boolean(writer, 'skip_if_gluster_bricks_up', obj.skip_if_gluster_bricks_up)
        if obj.skip_if_gluster_quorum_not_met is not None:
            Writer.write_boolean(writer, 'skip_if_gluster_quorum_not_met', obj.skip_if_gluster_quorum_not_met)
        if obj.skip_if_sd_active is not None:
            SkipIfSdActiveWriter.write_one(obj.skip_if_sd_active, writer, 'skip_if_sd_active')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'fencing_policy'
        if plural is None:
            plural = 'fencing_policies'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            FencingPolicyWriter.write_one(obj, writer, singular)
        writer.write_end()


class FileWriter(Writer):

    def __init__(self):
        super(FileWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'file'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.content is not None:
            Writer.write_string(writer, 'content', obj.content)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type)
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'file'
        if plural is None:
            plural = 'files'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            FileWriter.write_one(obj, writer, singular)
        writer.write_end()


class FilterWriter(Writer):

    def __init__(self):
        super(FilterWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'filter'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.position is not None:
            Writer.write_integer(writer, 'position', obj.position)
        if obj.scheduling_policy_unit is not None:
            SchedulingPolicyUnitWriter.write_one(obj.scheduling_policy_unit, writer, 'scheduling_policy_unit')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'filter'
        if plural is None:
            plural = 'filters'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            FilterWriter.write_one(obj, writer, singular)
        writer.write_end()


class FloppyWriter(Writer):

    def __init__(self):
        super(FloppyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'floppy'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.file is not None:
            FileWriter.write_one(obj.file, writer, 'file')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'floppy'
        if plural is None:
            plural = 'floppies'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            FloppyWriter.write_one(obj, writer, singular)
        writer.write_end()


class FopStatisticWriter(Writer):

    def __init__(self):
        super(FopStatisticWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'fop_statistic'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'fop_statistic'
        if plural is None:
            plural = 'fop_statistics'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            FopStatisticWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterBrickWriter(Writer):

    def __init__(self):
        super(GlusterBrickWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'brick'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.brick_dir is not None:
            Writer.write_string(writer, 'brick_dir', obj.brick_dir)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.device is not None:
            Writer.write_string(writer, 'device', obj.device)
        if obj.fs_name is not None:
            Writer.write_string(writer, 'fs_name', obj.fs_name)
        if obj.gluster_clients is not None:
            GlusterClientWriter.write_many(obj.gluster_clients, writer, 'gluster_client', 'gluster_clients')
        if obj.memory_pools is not None:
            GlusterMemoryPoolWriter.write_many(obj.memory_pools, writer, 'memory_pool', 'memory_pools')
        if obj.mnt_options is not None:
            Writer.write_string(writer, 'mnt_options', obj.mnt_options)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.pid is not None:
            Writer.write_integer(writer, 'pid', obj.pid)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.server_id is not None:
            Writer.write_string(writer, 'server_id', obj.server_id)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.gluster_volume is not None:
            GlusterVolumeWriter.write_one(obj.gluster_volume, writer, 'gluster_volume')
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'brick'
        if plural is None:
            plural = 'bricks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterBrickWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterBrickAdvancedDetailsWriter(Writer):

    def __init__(self):
        super(GlusterBrickAdvancedDetailsWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'gluster_brick_advanced_details'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.device is not None:
            Writer.write_string(writer, 'device', obj.device)
        if obj.fs_name is not None:
            Writer.write_string(writer, 'fs_name', obj.fs_name)
        if obj.gluster_clients is not None:
            GlusterClientWriter.write_many(obj.gluster_clients, writer, 'gluster_client', 'gluster_clients')
        if obj.memory_pools is not None:
            GlusterMemoryPoolWriter.write_many(obj.memory_pools, writer, 'memory_pool', 'memory_pools')
        if obj.mnt_options is not None:
            Writer.write_string(writer, 'mnt_options', obj.mnt_options)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.pid is not None:
            Writer.write_integer(writer, 'pid', obj.pid)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'gluster_brick_advanced_details'
        if plural is None:
            plural = 'gluster_brick_advanced_detailss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterBrickAdvancedDetailsWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterBrickMemoryInfoWriter(Writer):

    def __init__(self):
        super(GlusterBrickMemoryInfoWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'brick_memoryinfo'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.memory_pools is not None:
            GlusterMemoryPoolWriter.write_many(obj.memory_pools, writer, 'memory_pool', 'memory_pools')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'brick_memoryinfo'
        if plural is None:
            plural = 'gluster_brick_memory_infos'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterBrickMemoryInfoWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterClientWriter(Writer):

    def __init__(self):
        super(GlusterClientWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'gluster_client'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.bytes_read is not None:
            Writer.write_integer(writer, 'bytes_read', obj.bytes_read)
        if obj.bytes_written is not None:
            Writer.write_integer(writer, 'bytes_written', obj.bytes_written)
        if obj.client_port is not None:
            Writer.write_integer(writer, 'client_port', obj.client_port)
        if obj.host_name is not None:
            Writer.write_string(writer, 'host_name', obj.host_name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'gluster_client'
        if plural is None:
            plural = 'gluster_clients'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterClientWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterHookWriter(Writer):

    def __init__(self):
        super(GlusterHookWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'gluster_hook'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.checksum is not None:
            Writer.write_string(writer, 'checksum', obj.checksum)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.conflict_status is not None:
            Writer.write_integer(writer, 'conflict_status', obj.conflict_status)
        if obj.conflicts is not None:
            Writer.write_string(writer, 'conflicts', obj.conflicts)
        if obj.content is not None:
            Writer.write_string(writer, 'content', obj.content)
        if obj.content_type is not None:
            Writer.write_string(writer, 'content_type', obj.content_type.value)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.gluster_command is not None:
            Writer.write_string(writer, 'gluster_command', obj.gluster_command)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.stage is not None:
            Writer.write_string(writer, 'stage', obj.stage.value)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.server_hooks is not None:
            GlusterServerHookWriter.write_many(obj.server_hooks, writer, 'server_hook', 'server_hooks')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'gluster_hook'
        if plural is None:
            plural = 'gluster_hooks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterHookWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterMemoryPoolWriter(Writer):

    def __init__(self):
        super(GlusterMemoryPoolWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'memory_pool'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.alloc_count is not None:
            Writer.write_integer(writer, 'alloc_count', obj.alloc_count)
        if obj.cold_count is not None:
            Writer.write_integer(writer, 'cold_count', obj.cold_count)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.hot_count is not None:
            Writer.write_integer(writer, 'hot_count', obj.hot_count)
        if obj.max_alloc is not None:
            Writer.write_integer(writer, 'max_alloc', obj.max_alloc)
        if obj.max_stdalloc is not None:
            Writer.write_integer(writer, 'max_stdalloc', obj.max_stdalloc)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.padded_size is not None:
            Writer.write_integer(writer, 'padded_size', obj.padded_size)
        if obj.pool_misses is not None:
            Writer.write_integer(writer, 'pool_misses', obj.pool_misses)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'memory_pool'
        if plural is None:
            plural = 'memory_pools'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterMemoryPoolWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterServerHookWriter(Writer):

    def __init__(self):
        super(GlusterServerHookWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'server_hook'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.checksum is not None:
            Writer.write_string(writer, 'checksum', obj.checksum)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.content_type is not None:
            Writer.write_string(writer, 'content_type', obj.content_type.value)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'server_hook'
        if plural is None:
            plural = 'server_hooks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterServerHookWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterVolumeWriter(Writer):

    def __init__(self):
        super(GlusterVolumeWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'gluster_volume'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.disperse_count is not None:
            Writer.write_integer(writer, 'disperse_count', obj.disperse_count)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.options is not None:
            OptionWriter.write_many(obj.options, writer, 'option', 'options')
        if obj.redundancy_count is not None:
            Writer.write_integer(writer, 'redundancy_count', obj.redundancy_count)
        if obj.replica_count is not None:
            Writer.write_integer(writer, 'replica_count', obj.replica_count)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.stripe_count is not None:
            Writer.write_integer(writer, 'stripe_count', obj.stripe_count)
        if obj.transport_types is not None:
            writer.write_start('transport_types')
            for item in obj.transport_types:
                if item is not None:
                    Writer.write_string(writer, 'transport_type', item.value)
            writer.write_end()
        if obj.volume_type is not None:
            Writer.write_string(writer, 'volume_type', obj.volume_type.value)
        if obj.bricks is not None:
            GlusterBrickWriter.write_many(obj.bricks, writer, 'brick', 'bricks')
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'gluster_volume'
        if plural is None:
            plural = 'gluster_volumes'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterVolumeWriter.write_one(obj, writer, singular)
        writer.write_end()


class GlusterVolumeProfileDetailsWriter(Writer):

    def __init__(self):
        super(GlusterVolumeProfileDetailsWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'gluster_volume_profile_details'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.brick_profile_details is not None:
            BrickProfileDetailWriter.write_many(obj.brick_profile_details, writer, 'brick_profile_detail', 'brick_profile_details')
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.nfs_profile_details is not None:
            NfsProfileDetailWriter.write_many(obj.nfs_profile_details, writer, 'nfs_profile_detail', 'nfs_profile_details')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'gluster_volume_profile_details'
        if plural is None:
            plural = 'gluster_volume_profile_detailss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GlusterVolumeProfileDetailsWriter.write_one(obj, writer, singular)
        writer.write_end()


class GracePeriodWriter(Writer):

    def __init__(self):
        super(GracePeriodWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'grace_period'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.expiry is not None:
            Writer.write_integer(writer, 'expiry', obj.expiry)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'grace_period'
        if plural is None:
            plural = 'grace_periods'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GracePeriodWriter.write_one(obj, writer, singular)
        writer.write_end()


class GraphicsConsoleWriter(Writer):

    def __init__(self):
        super(GraphicsConsoleWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'graphics_console'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.protocol is not None:
            Writer.write_string(writer, 'protocol', obj.protocol.value)
        if obj.tls_port is not None:
            Writer.write_integer(writer, 'tls_port', obj.tls_port)
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'graphics_console'
        if plural is None:
            plural = 'graphics_consoles'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GraphicsConsoleWriter.write_one(obj, writer, singular)
        writer.write_end()


class GroupWriter(Writer):

    def __init__(self):
        super(GroupWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'group'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.domain_entry_id is not None:
            Writer.write_string(writer, 'domain_entry_id', obj.domain_entry_id)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.namespace is not None:
            Writer.write_string(writer, 'namespace', obj.namespace)
        if obj.domain is not None:
            DomainWriter.write_one(obj.domain, writer, 'domain')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.roles is not None:
            RoleWriter.write_many(obj.roles, writer, 'role', 'roles')
        if obj.tags is not None:
            TagWriter.write_many(obj.tags, writer, 'tag', 'tags')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'group'
        if plural is None:
            plural = 'groups'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GroupWriter.write_one(obj, writer, singular)
        writer.write_end()


class GuestOperatingSystemWriter(Writer):

    def __init__(self):
        super(GuestOperatingSystemWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'guest_operating_system'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.architecture is not None:
            Writer.write_string(writer, 'architecture', obj.architecture)
        if obj.codename is not None:
            Writer.write_string(writer, 'codename', obj.codename)
        if obj.distribution is not None:
            Writer.write_string(writer, 'distribution', obj.distribution)
        if obj.family is not None:
            Writer.write_string(writer, 'family', obj.family)
        if obj.kernel is not None:
            KernelWriter.write_one(obj.kernel, writer, 'kernel')
        if obj.version is not None:
            VersionWriter.write_one(obj.version, writer, 'version')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'guest_operating_system'
        if plural is None:
            plural = 'guest_operating_systems'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            GuestOperatingSystemWriter.write_one(obj, writer, singular)
        writer.write_end()


class HardwareInformationWriter(Writer):

    def __init__(self):
        super(HardwareInformationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'hardware_information'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.family is not None:
            Writer.write_string(writer, 'family', obj.family)
        if obj.manufacturer is not None:
            Writer.write_string(writer, 'manufacturer', obj.manufacturer)
        if obj.product_name is not None:
            Writer.write_string(writer, 'product_name', obj.product_name)
        if obj.serial_number is not None:
            Writer.write_string(writer, 'serial_number', obj.serial_number)
        if obj.supported_rng_sources is not None:
            writer.write_start('supported_rng_sources')
            for item in obj.supported_rng_sources:
                if item is not None:
                    Writer.write_string(writer, 'supported_rng_source', item.value)
            writer.write_end()
        if obj.uuid is not None:
            Writer.write_string(writer, 'uuid', obj.uuid)
        if obj.version is not None:
            Writer.write_string(writer, 'version', obj.version)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'hardware_information'
        if plural is None:
            plural = 'hardware_informations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HardwareInformationWriter.write_one(obj, writer, singular)
        writer.write_end()


class HighAvailabilityWriter(Writer):

    def __init__(self):
        super(HighAvailabilityWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'high_availability'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        if obj.priority is not None:
            Writer.write_integer(writer, 'priority', obj.priority)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'high_availability'
        if plural is None:
            plural = 'high_availabilities'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HighAvailabilityWriter.write_one(obj, writer, singular)
        writer.write_end()


class HookWriter(Writer):

    def __init__(self):
        super(HookWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'hook'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.event_name is not None:
            Writer.write_string(writer, 'event_name', obj.event_name)
        if obj.md5 is not None:
            Writer.write_string(writer, 'md5', obj.md5)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'hook'
        if plural is None:
            plural = 'hooks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HookWriter.write_one(obj, writer, singular)
        writer.write_end()


class HostWriter(Writer):

    def __init__(self):
        super(HostWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'host'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.auto_numa_status is not None:
            Writer.write_string(writer, 'auto_numa_status', obj.auto_numa_status.value)
        if obj.certificate is not None:
            CertificateWriter.write_one(obj.certificate, writer, 'certificate')
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.device_passthrough is not None:
            HostDevicePassthroughWriter.write_one(obj.device_passthrough, writer, 'device_passthrough')
        if obj.display is not None:
            DisplayWriter.write_one(obj.display, writer, 'display')
        if obj.external_status is not None:
            Writer.write_string(writer, 'external_status', obj.external_status.value)
        if obj.hardware_information is not None:
            HardwareInformationWriter.write_one(obj.hardware_information, writer, 'hardware_information')
        if obj.hosted_engine is not None:
            HostedEngineWriter.write_one(obj.hosted_engine, writer, 'hosted_engine')
        if obj.iscsi is not None:
            IscsiDetailsWriter.write_one(obj.iscsi, writer, 'iscsi')
        if obj.kdump_status is not None:
            Writer.write_string(writer, 'kdump_status', obj.kdump_status.value)
        if obj.ksm is not None:
            KsmWriter.write_one(obj.ksm, writer, 'ksm')
        if obj.libvirt_version is not None:
            VersionWriter.write_one(obj.libvirt_version, writer, 'libvirt_version')
        if obj.max_scheduling_memory is not None:
            Writer.write_integer(writer, 'max_scheduling_memory', obj.max_scheduling_memory)
        if obj.memory is not None:
            Writer.write_integer(writer, 'memory', obj.memory)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.network_operation_in_progress is not None:
            Writer.write_boolean(writer, 'network_operation_in_progress', obj.network_operation_in_progress)
        if obj.numa_supported is not None:
            Writer.write_boolean(writer, 'numa_supported', obj.numa_supported)
        if obj.os is not None:
            OperatingSystemWriter.write_one(obj.os, writer, 'os')
        if obj.override_iptables is not None:
            Writer.write_boolean(writer, 'override_iptables', obj.override_iptables)
        if obj.ovn_configured is not None:
            Writer.write_boolean(writer, 'ovn_configured', obj.ovn_configured)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.power_management is not None:
            PowerManagementWriter.write_one(obj.power_management, writer, 'power_management')
        if obj.protocol is not None:
            Writer.write_string(writer, 'protocol', obj.protocol.value)
        if obj.reinstallation_required is not None:
            Writer.write_boolean(writer, 'reinstallation_required', obj.reinstallation_required)
        if obj.root_password is not None:
            Writer.write_string(writer, 'root_password', obj.root_password)
        if obj.se_linux is not None:
            SeLinuxWriter.write_one(obj.se_linux, writer, 'se_linux')
        if obj.spm is not None:
            SpmWriter.write_one(obj.spm, writer, 'spm')
        if obj.ssh is not None:
            SshWriter.write_one(obj.ssh, writer, 'ssh')
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.status_detail is not None:
            Writer.write_string(writer, 'status_detail', obj.status_detail)
        if obj.summary is not None:
            VmSummaryWriter.write_one(obj.summary, writer, 'summary')
        if obj.transparent_huge_pages is not None:
            TransparentHugePagesWriter.write_one(obj.transparent_huge_pages, writer, 'transparent_hugepages')
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.update_available is not None:
            Writer.write_boolean(writer, 'update_available', obj.update_available)
        if obj.version is not None:
            VersionWriter.write_one(obj.version, writer, 'version')
        if obj.vgpu_placement is not None:
            Writer.write_string(writer, 'vgpu_placement', obj.vgpu_placement.value)
        if obj.affinity_labels is not None:
            AffinityLabelWriter.write_many(obj.affinity_labels, writer, 'affinity_label', 'affinity_labels')
        if obj.agents is not None:
            AgentWriter.write_many(obj.agents, writer, 'agent', 'agents')
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.devices is not None:
            HostDeviceWriter.write_many(obj.devices, writer, 'host_device', 'devices')
        if obj.external_host_provider is not None:
            ExternalHostProviderWriter.write_one(obj.external_host_provider, writer, 'external_host_provider')
        if obj.external_network_provider_configurations is not None:
            ExternalNetworkProviderConfigurationWriter.write_many(obj.external_network_provider_configurations, writer, 'external_network_provider_configuration', 'external_network_provider_configurations')
        if obj.hooks is not None:
            HookWriter.write_many(obj.hooks, writer, 'hook', 'hooks')
        if obj.katello_errata is not None:
            KatelloErratumWriter.write_many(obj.katello_errata, writer, 'katello_erratum', 'katello_errata')
        if obj.network_attachments is not None:
            NetworkAttachmentWriter.write_many(obj.network_attachments, writer, 'network_attachment', 'network_attachments')
        if obj.nics is not None:
            HostNicWriter.write_many(obj.nics, writer, 'host_nic', 'nics')
        if obj.numa_nodes is not None:
            NumaNodeWriter.write_many(obj.numa_nodes, writer, 'host_numa_node', 'host_numa_nodes')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        if obj.storage_connection_extensions is not None:
            StorageConnectionExtensionWriter.write_many(obj.storage_connection_extensions, writer, 'storage_connection_extension', 'storage_connection_extensions')
        if obj.storages is not None:
            HostStorageWriter.write_many(obj.storages, writer, 'host_storage', 'storages')
        if obj.tags is not None:
            TagWriter.write_many(obj.tags, writer, 'tag', 'tags')
        if obj.unmanaged_networks is not None:
            UnmanagedNetworkWriter.write_many(obj.unmanaged_networks, writer, 'unmanaged_network', 'unmanaged_networks')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'host'
        if plural is None:
            plural = 'hosts'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HostWriter.write_one(obj, writer, singular)
        writer.write_end()


class HostDeviceWriter(Writer):

    def __init__(self):
        super(HostDeviceWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'host_device'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.capability is not None:
            Writer.write_string(writer, 'capability', obj.capability)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.driver is not None:
            Writer.write_string(writer, 'driver', obj.driver)
        if obj.iommu_group is not None:
            Writer.write_integer(writer, 'iommu_group', obj.iommu_group)
        if obj.m_dev_types is not None:
            MDevTypeWriter.write_many(obj.m_dev_types, writer, 'm_dev_type', 'm_dev_types')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.physical_function is not None:
            HostDeviceWriter.write_one(obj.physical_function, writer, 'physical_function')
        if obj.placeholder is not None:
            Writer.write_boolean(writer, 'placeholder', obj.placeholder)
        if obj.product is not None:
            ProductWriter.write_one(obj.product, writer, 'product')
        if obj.vendor is not None:
            VendorWriter.write_one(obj.vendor, writer, 'vendor')
        if obj.virtual_functions is not None:
            Writer.write_integer(writer, 'virtual_functions', obj.virtual_functions)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.parent_device is not None:
            HostDeviceWriter.write_one(obj.parent_device, writer, 'parent_device')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'host_device'
        if plural is None:
            plural = 'host_devices'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HostDeviceWriter.write_one(obj, writer, singular)
        writer.write_end()


class HostDevicePassthroughWriter(Writer):

    def __init__(self):
        super(HostDevicePassthroughWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'host_device_passthrough'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'host_device_passthrough'
        if plural is None:
            plural = 'host_device_passthroughs'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HostDevicePassthroughWriter.write_one(obj, writer, singular)
        writer.write_end()


class HostNicWriter(Writer):

    def __init__(self):
        super(HostNicWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'host_nic'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.ad_aggregator_id is not None:
            Writer.write_integer(writer, 'ad_aggregator_id', obj.ad_aggregator_id)
        if obj.base_interface is not None:
            Writer.write_string(writer, 'base_interface', obj.base_interface)
        if obj.bonding is not None:
            BondingWriter.write_one(obj.bonding, writer, 'bonding')
        if obj.boot_protocol is not None:
            Writer.write_string(writer, 'boot_protocol', obj.boot_protocol.value)
        if obj.bridged is not None:
            Writer.write_boolean(writer, 'bridged', obj.bridged)
        if obj.check_connectivity is not None:
            Writer.write_boolean(writer, 'check_connectivity', obj.check_connectivity)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.custom_configuration is not None:
            Writer.write_boolean(writer, 'custom_configuration', obj.custom_configuration)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.ip is not None:
            IpWriter.write_one(obj.ip, writer, 'ip')
        if obj.ipv6 is not None:
            IpWriter.write_one(obj.ipv6, writer, 'ipv6')
        if obj.ipv6_boot_protocol is not None:
            Writer.write_string(writer, 'ipv6_boot_protocol', obj.ipv6_boot_protocol.value)
        if obj.mac is not None:
            MacWriter.write_one(obj.mac, writer, 'mac')
        if obj.mtu is not None:
            Writer.write_integer(writer, 'mtu', obj.mtu)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.override_configuration is not None:
            Writer.write_boolean(writer, 'override_configuration', obj.override_configuration)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.speed is not None:
            Writer.write_integer(writer, 'speed', obj.speed)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.virtual_functions_configuration is not None:
            HostNicVirtualFunctionsConfigurationWriter.write_one(obj.virtual_functions_configuration, writer, 'virtual_functions_configuration')
        if obj.vlan is not None:
            VlanWriter.write_one(obj.vlan, writer, 'vlan')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.network is not None:
            NetworkWriter.write_one(obj.network, writer, 'network')
        if obj.network_labels is not None:
            NetworkLabelWriter.write_many(obj.network_labels, writer, 'network_label', 'network_labels')
        if obj.physical_function is not None:
            HostNicWriter.write_one(obj.physical_function, writer, 'physical_function')
        if obj.qos is not None:
            QosWriter.write_one(obj.qos, writer, 'qos')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'host_nic'
        if plural is None:
            plural = 'host_nics'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HostNicWriter.write_one(obj, writer, singular)
        writer.write_end()


class HostNicVirtualFunctionsConfigurationWriter(Writer):

    def __init__(self):
        super(HostNicVirtualFunctionsConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'host_nic_virtual_functions_configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.all_networks_allowed is not None:
            Writer.write_boolean(writer, 'all_networks_allowed', obj.all_networks_allowed)
        if obj.max_number_of_virtual_functions is not None:
            Writer.write_integer(writer, 'max_number_of_virtual_functions', obj.max_number_of_virtual_functions)
        if obj.number_of_virtual_functions is not None:
            Writer.write_integer(writer, 'number_of_virtual_functions', obj.number_of_virtual_functions)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'host_nic_virtual_functions_configuration'
        if plural is None:
            plural = 'host_nic_virtual_functions_configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HostNicVirtualFunctionsConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class HostStorageWriter(Writer):

    def __init__(self):
        super(HostStorageWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'host_storage'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.driver_options is not None:
            PropertyWriter.write_many(obj.driver_options, writer, 'property', 'driver_options')
        if obj.driver_sensitive_options is not None:
            PropertyWriter.write_many(obj.driver_sensitive_options, writer, 'property', 'driver_sensitive_options')
        if obj.logical_units is not None:
            LogicalUnitWriter.write_many(obj.logical_units, writer, 'logical_unit', 'logical_units')
        if obj.mount_options is not None:
            Writer.write_string(writer, 'mount_options', obj.mount_options)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.nfs_retrans is not None:
            Writer.write_integer(writer, 'nfs_retrans', obj.nfs_retrans)
        if obj.nfs_timeo is not None:
            Writer.write_integer(writer, 'nfs_timeo', obj.nfs_timeo)
        if obj.nfs_version is not None:
            Writer.write_string(writer, 'nfs_version', obj.nfs_version.value)
        if obj.override_luns is not None:
            Writer.write_boolean(writer, 'override_luns', obj.override_luns)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.path is not None:
            Writer.write_string(writer, 'path', obj.path)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.portal is not None:
            Writer.write_string(writer, 'portal', obj.portal)
        if obj.target is not None:
            Writer.write_string(writer, 'target', obj.target)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.vfs_type is not None:
            Writer.write_string(writer, 'vfs_type', obj.vfs_type)
        if obj.volume_group is not None:
            VolumeGroupWriter.write_one(obj.volume_group, writer, 'volume_group')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'host_storage'
        if plural is None:
            plural = 'host_storages'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HostStorageWriter.write_one(obj, writer, singular)
        writer.write_end()


class HostedEngineWriter(Writer):

    def __init__(self):
        super(HostedEngineWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'hosted_engine'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.active is not None:
            Writer.write_boolean(writer, 'active', obj.active)
        if obj.configured is not None:
            Writer.write_boolean(writer, 'configured', obj.configured)
        if obj.global_maintenance is not None:
            Writer.write_boolean(writer, 'global_maintenance', obj.global_maintenance)
        if obj.local_maintenance is not None:
            Writer.write_boolean(writer, 'local_maintenance', obj.local_maintenance)
        if obj.score is not None:
            Writer.write_integer(writer, 'score', obj.score)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'hosted_engine'
        if plural is None:
            plural = 'hosted_engines'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            HostedEngineWriter.write_one(obj, writer, singular)
        writer.write_end()


class IconWriter(Writer):

    def __init__(self):
        super(IconWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'icon'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.data is not None:
            Writer.write_string(writer, 'data', obj.data)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.media_type is not None:
            Writer.write_string(writer, 'media_type', obj.media_type)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'icon'
        if plural is None:
            plural = 'icons'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            IconWriter.write_one(obj, writer, singular)
        writer.write_end()


class IdentifiedWriter(Writer):

    def __init__(self):
        super(IdentifiedWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'identified'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'identified'
        if plural is None:
            plural = 'identifieds'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            IdentifiedWriter.write_one(obj, writer, singular)
        writer.write_end()


class ImageWriter(Writer):

    def __init__(self):
        super(ImageWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'image'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.size is not None:
            Writer.write_integer(writer, 'size', obj.size)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'image'
        if plural is None:
            plural = 'images'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ImageWriter.write_one(obj, writer, singular)
        writer.write_end()


class ImageTransferWriter(Writer):

    def __init__(self):
        super(ImageTransferWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'image_transfer'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.active is not None:
            Writer.write_boolean(writer, 'active', obj.active)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.direction is not None:
            Writer.write_string(writer, 'direction', obj.direction.value)
        if obj.format is not None:
            Writer.write_string(writer, 'format', obj.format.value)
        if obj.inactivity_timeout is not None:
            Writer.write_integer(writer, 'inactivity_timeout', obj.inactivity_timeout)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.phase is not None:
            Writer.write_string(writer, 'phase', obj.phase.value)
        if obj.proxy_url is not None:
            Writer.write_string(writer, 'proxy_url', obj.proxy_url)
        if obj.shallow is not None:
            Writer.write_boolean(writer, 'shallow', obj.shallow)
        if obj.timeout_policy is not None:
            Writer.write_string(writer, 'timeout_policy', obj.timeout_policy.value)
        if obj.transfer_url is not None:
            Writer.write_string(writer, 'transfer_url', obj.transfer_url)
        if obj.transferred is not None:
            Writer.write_integer(writer, 'transferred', obj.transferred)
        if obj.backup is not None:
            BackupWriter.write_one(obj.backup, writer, 'backup')
        if obj.disk is not None:
            DiskWriter.write_one(obj.disk, writer, 'disk')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.image is not None:
            ImageWriter.write_one(obj.image, writer, 'image')
        if obj.snapshot is not None:
            DiskSnapshotWriter.write_one(obj.snapshot, writer, 'snapshot')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'image_transfer'
        if plural is None:
            plural = 'image_transfers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ImageTransferWriter.write_one(obj, writer, singular)
        writer.write_end()


class InitializationWriter(Writer):

    def __init__(self):
        super(InitializationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'initialization'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.active_directory_ou is not None:
            Writer.write_string(writer, 'active_directory_ou', obj.active_directory_ou)
        if obj.authorized_ssh_keys is not None:
            Writer.write_string(writer, 'authorized_ssh_keys', obj.authorized_ssh_keys)
        if obj.cloud_init is not None:
            CloudInitWriter.write_one(obj.cloud_init, writer, 'cloud_init')
        if obj.cloud_init_network_protocol is not None:
            Writer.write_string(writer, 'cloud_init_network_protocol', obj.cloud_init_network_protocol.value)
        if obj.configuration is not None:
            ConfigurationWriter.write_one(obj.configuration, writer, 'configuration')
        if obj.custom_script is not None:
            Writer.write_string(writer, 'custom_script', obj.custom_script)
        if obj.dns_search is not None:
            Writer.write_string(writer, 'dns_search', obj.dns_search)
        if obj.dns_servers is not None:
            Writer.write_string(writer, 'dns_servers', obj.dns_servers)
        if obj.domain is not None:
            Writer.write_string(writer, 'domain', obj.domain)
        if obj.host_name is not None:
            Writer.write_string(writer, 'host_name', obj.host_name)
        if obj.input_locale is not None:
            Writer.write_string(writer, 'input_locale', obj.input_locale)
        if obj.nic_configurations is not None:
            NicConfigurationWriter.write_many(obj.nic_configurations, writer, 'nic_configuration', 'nic_configurations')
        if obj.org_name is not None:
            Writer.write_string(writer, 'org_name', obj.org_name)
        if obj.regenerate_ids is not None:
            Writer.write_boolean(writer, 'regenerate_ids', obj.regenerate_ids)
        if obj.regenerate_ssh_keys is not None:
            Writer.write_boolean(writer, 'regenerate_ssh_keys', obj.regenerate_ssh_keys)
        if obj.root_password is not None:
            Writer.write_string(writer, 'root_password', obj.root_password)
        if obj.system_locale is not None:
            Writer.write_string(writer, 'system_locale', obj.system_locale)
        if obj.timezone is not None:
            Writer.write_string(writer, 'timezone', obj.timezone)
        if obj.ui_language is not None:
            Writer.write_string(writer, 'ui_language', obj.ui_language)
        if obj.user_locale is not None:
            Writer.write_string(writer, 'user_locale', obj.user_locale)
        if obj.user_name is not None:
            Writer.write_string(writer, 'user_name', obj.user_name)
        if obj.windows_license_key is not None:
            Writer.write_string(writer, 'windows_license_key', obj.windows_license_key)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'initialization'
        if plural is None:
            plural = 'initializations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            InitializationWriter.write_one(obj, writer, singular)
        writer.write_end()


class InstanceTypeWriter(Writer):

    def __init__(self):
        super(InstanceTypeWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'instance_type'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.auto_pinning_policy is not None:
            Writer.write_string(writer, 'auto_pinning_policy', obj.auto_pinning_policy.value)
        if obj.bios is not None:
            BiosWriter.write_one(obj.bios, writer, 'bios')
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.console is not None:
            ConsoleWriter.write_one(obj.console, writer, 'console')
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.cpu_shares is not None:
            Writer.write_integer(writer, 'cpu_shares', obj.cpu_shares)
        if obj.creation_time is not None:
            Writer.write_date(writer, 'creation_time', obj.creation_time)
        if obj.custom_compatibility_version is not None:
            VersionWriter.write_one(obj.custom_compatibility_version, writer, 'custom_compatibility_version')
        if obj.custom_cpu_model is not None:
            Writer.write_string(writer, 'custom_cpu_model', obj.custom_cpu_model)
        if obj.custom_emulated_machine is not None:
            Writer.write_string(writer, 'custom_emulated_machine', obj.custom_emulated_machine)
        if obj.custom_properties is not None:
            CustomPropertyWriter.write_many(obj.custom_properties, writer, 'custom_property', 'custom_properties')
        if obj.delete_protected is not None:
            Writer.write_boolean(writer, 'delete_protected', obj.delete_protected)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.display is not None:
            DisplayWriter.write_one(obj.display, writer, 'display')
        if obj.domain is not None:
            DomainWriter.write_one(obj.domain, writer, 'domain')
        if obj.high_availability is not None:
            HighAvailabilityWriter.write_one(obj.high_availability, writer, 'high_availability')
        if obj.initialization is not None:
            InitializationWriter.write_one(obj.initialization, writer, 'initialization')
        if obj.io is not None:
            IoWriter.write_one(obj.io, writer, 'io')
        if obj.large_icon is not None:
            IconWriter.write_one(obj.large_icon, writer, 'large_icon')
        if obj.lease is not None:
            StorageDomainLeaseWriter.write_one(obj.lease, writer, 'lease')
        if obj.memory is not None:
            Writer.write_integer(writer, 'memory', obj.memory)
        if obj.memory_policy is not None:
            MemoryPolicyWriter.write_one(obj.memory_policy, writer, 'memory_policy')
        if obj.migration is not None:
            MigrationOptionsWriter.write_one(obj.migration, writer, 'migration')
        if obj.migration_downtime is not None:
            Writer.write_integer(writer, 'migration_downtime', obj.migration_downtime)
        if obj.multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'multi_queues_enabled', obj.multi_queues_enabled)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.origin is not None:
            Writer.write_string(writer, 'origin', obj.origin)
        if obj.os is not None:
            OperatingSystemWriter.write_one(obj.os, writer, 'os')
        if obj.placement_policy is not None:
            VmPlacementPolicyWriter.write_one(obj.placement_policy, writer, 'placement_policy')
        if obj.rng_device is not None:
            RngDeviceWriter.write_one(obj.rng_device, writer, 'rng_device')
        if obj.serial_number is not None:
            SerialNumberWriter.write_one(obj.serial_number, writer, 'serial_number')
        if obj.small_icon is not None:
            IconWriter.write_one(obj.small_icon, writer, 'small_icon')
        if obj.soundcard_enabled is not None:
            Writer.write_boolean(writer, 'soundcard_enabled', obj.soundcard_enabled)
        if obj.sso is not None:
            SsoWriter.write_one(obj.sso, writer, 'sso')
        if obj.start_paused is not None:
            Writer.write_boolean(writer, 'start_paused', obj.start_paused)
        if obj.stateless is not None:
            Writer.write_boolean(writer, 'stateless', obj.stateless)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.storage_error_resume_behaviour is not None:
            Writer.write_string(writer, 'storage_error_resume_behaviour', obj.storage_error_resume_behaviour.value)
        if obj.time_zone is not None:
            TimeZoneWriter.write_one(obj.time_zone, writer, 'time_zone')
        if obj.tpm_enabled is not None:
            Writer.write_boolean(writer, 'tpm_enabled', obj.tpm_enabled)
        if obj.tunnel_migration is not None:
            Writer.write_boolean(writer, 'tunnel_migration', obj.tunnel_migration)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.usb is not None:
            UsbWriter.write_one(obj.usb, writer, 'usb')
        if obj.version is not None:
            TemplateVersionWriter.write_one(obj.version, writer, 'version')
        if obj.virtio_scsi is not None:
            VirtioScsiWriter.write_one(obj.virtio_scsi, writer, 'virtio_scsi')
        if obj.virtio_scsi_multi_queues is not None:
            Writer.write_integer(writer, 'virtio_scsi_multi_queues', obj.virtio_scsi_multi_queues)
        if obj.virtio_scsi_multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'virtio_scsi_multi_queues_enabled', obj.virtio_scsi_multi_queues_enabled)
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.cdroms is not None:
            CdromWriter.write_many(obj.cdroms, writer, 'cdrom', 'cdroms')
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.cpu_profile is not None:
            CpuProfileWriter.write_one(obj.cpu_profile, writer, 'cpu_profile')
        if obj.disk_attachments is not None:
            DiskAttachmentWriter.write_many(obj.disk_attachments, writer, 'disk_attachment', 'disk_attachments')
        if obj.graphics_consoles is not None:
            GraphicsConsoleWriter.write_many(obj.graphics_consoles, writer, 'graphics_console', 'graphics_consoles')
        if obj.nics is not None:
            NicWriter.write_many(obj.nics, writer, 'nic', 'nics')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.tags is not None:
            TagWriter.write_many(obj.tags, writer, 'tag', 'tags')
        if obj.watchdogs is not None:
            WatchdogWriter.write_many(obj.watchdogs, writer, 'watchdog', 'watchdogs')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'instance_type'
        if plural is None:
            plural = 'instance_types'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            InstanceTypeWriter.write_one(obj, writer, singular)
        writer.write_end()


class IoWriter(Writer):

    def __init__(self):
        super(IoWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'io'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.threads is not None:
            Writer.write_integer(writer, 'threads', obj.threads)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'io'
        if plural is None:
            plural = 'ios'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            IoWriter.write_one(obj, writer, singular)
        writer.write_end()


class IpWriter(Writer):

    def __init__(self):
        super(IpWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'ip'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.gateway is not None:
            Writer.write_string(writer, 'gateway', obj.gateway)
        if obj.netmask is not None:
            Writer.write_string(writer, 'netmask', obj.netmask)
        if obj.version is not None:
            Writer.write_string(writer, 'version', obj.version.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'ip'
        if plural is None:
            plural = 'ips'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            IpWriter.write_one(obj, writer, singular)
        writer.write_end()


class IpAddressAssignmentWriter(Writer):

    def __init__(self):
        super(IpAddressAssignmentWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'ip_address_assignment'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.assignment_method is not None:
            Writer.write_string(writer, 'assignment_method', obj.assignment_method.value)
        if obj.ip is not None:
            IpWriter.write_one(obj.ip, writer, 'ip')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'ip_address_assignment'
        if plural is None:
            plural = 'ip_address_assignments'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            IpAddressAssignmentWriter.write_one(obj, writer, singular)
        writer.write_end()


class IscsiBondWriter(Writer):

    def __init__(self):
        super(IscsiBondWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'iscsi_bond'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.networks is not None:
            NetworkWriter.write_many(obj.networks, writer, 'network', 'networks')
        if obj.storage_connections is not None:
            StorageConnectionWriter.write_many(obj.storage_connections, writer, 'storage_connection', 'storage_connections')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'iscsi_bond'
        if plural is None:
            plural = 'iscsi_bonds'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            IscsiBondWriter.write_one(obj, writer, singular)
        writer.write_end()


class IscsiDetailsWriter(Writer):

    def __init__(self):
        super(IscsiDetailsWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'iscsi_details'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.disk_id is not None:
            Writer.write_string(writer, 'disk_id', obj.disk_id)
        if obj.initiator is not None:
            Writer.write_string(writer, 'initiator', obj.initiator)
        if obj.lun_mapping is not None:
            Writer.write_integer(writer, 'lun_mapping', obj.lun_mapping)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.paths is not None:
            Writer.write_integer(writer, 'paths', obj.paths)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.portal is not None:
            Writer.write_string(writer, 'portal', obj.portal)
        if obj.product_id is not None:
            Writer.write_string(writer, 'product_id', obj.product_id)
        if obj.serial is not None:
            Writer.write_string(writer, 'serial', obj.serial)
        if obj.size is not None:
            Writer.write_integer(writer, 'size', obj.size)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status)
        if obj.storage_domain_id is not None:
            Writer.write_string(writer, 'storage_domain_id', obj.storage_domain_id)
        if obj.target is not None:
            Writer.write_string(writer, 'target', obj.target)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.vendor_id is not None:
            Writer.write_string(writer, 'vendor_id', obj.vendor_id)
        if obj.volume_group_id is not None:
            Writer.write_string(writer, 'volume_group_id', obj.volume_group_id)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'iscsi_details'
        if plural is None:
            plural = 'iscsi_detailss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            IscsiDetailsWriter.write_one(obj, writer, singular)
        writer.write_end()


class JobWriter(Writer):

    def __init__(self):
        super(JobWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'job'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.auto_cleared is not None:
            Writer.write_boolean(writer, 'auto_cleared', obj.auto_cleared)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.end_time is not None:
            Writer.write_date(writer, 'end_time', obj.end_time)
        if obj.external is not None:
            Writer.write_boolean(writer, 'external', obj.external)
        if obj.last_updated is not None:
            Writer.write_date(writer, 'last_updated', obj.last_updated)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.start_time is not None:
            Writer.write_date(writer, 'start_time', obj.start_time)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.owner is not None:
            UserWriter.write_one(obj.owner, writer, 'owner')
        if obj.steps is not None:
            StepWriter.write_many(obj.steps, writer, 'step', 'steps')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'job'
        if plural is None:
            plural = 'jobs'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            JobWriter.write_one(obj, writer, singular)
        writer.write_end()


class KatelloErratumWriter(Writer):

    def __init__(self):
        super(KatelloErratumWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'katello_erratum'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.issued is not None:
            Writer.write_date(writer, 'issued', obj.issued)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.packages is not None:
            PackageWriter.write_many(obj.packages, writer, 'package', 'packages')
        if obj.severity is not None:
            Writer.write_string(writer, 'severity', obj.severity)
        if obj.solution is not None:
            Writer.write_string(writer, 'solution', obj.solution)
        if obj.summary is not None:
            Writer.write_string(writer, 'summary', obj.summary)
        if obj.title is not None:
            Writer.write_string(writer, 'title', obj.title)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'katello_erratum'
        if plural is None:
            plural = 'katello_errata'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            KatelloErratumWriter.write_one(obj, writer, singular)
        writer.write_end()


class KernelWriter(Writer):

    def __init__(self):
        super(KernelWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'kernel'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.version is not None:
            VersionWriter.write_one(obj.version, writer, 'version')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'kernel'
        if plural is None:
            plural = 'kernels'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            KernelWriter.write_one(obj, writer, singular)
        writer.write_end()


class KsmWriter(Writer):

    def __init__(self):
        super(KsmWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'ksm'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        if obj.merge_across_nodes is not None:
            Writer.write_boolean(writer, 'merge_across_nodes', obj.merge_across_nodes)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'ksm'
        if plural is None:
            plural = 'ksms'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            KsmWriter.write_one(obj, writer, singular)
        writer.write_end()


class LinkLayerDiscoveryProtocolElementWriter(Writer):

    def __init__(self):
        super(LinkLayerDiscoveryProtocolElementWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'link_layer_discovery_protocol_element'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.oui is not None:
            Writer.write_integer(writer, 'oui', obj.oui)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.subtype is not None:
            Writer.write_integer(writer, 'subtype', obj.subtype)
        if obj.type is not None:
            Writer.write_integer(writer, 'type', obj.type)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'link_layer_discovery_protocol_element'
        if plural is None:
            plural = 'link_layer_discovery_protocol_elements'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            LinkLayerDiscoveryProtocolElementWriter.write_one(obj, writer, singular)
        writer.write_end()


class LogicalUnitWriter(Writer):

    def __init__(self):
        super(LogicalUnitWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'logical_unit'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.discard_max_size is not None:
            Writer.write_integer(writer, 'discard_max_size', obj.discard_max_size)
        if obj.discard_zeroes_data is not None:
            Writer.write_boolean(writer, 'discard_zeroes_data', obj.discard_zeroes_data)
        if obj.disk_id is not None:
            Writer.write_string(writer, 'disk_id', obj.disk_id)
        if obj.lun_mapping is not None:
            Writer.write_integer(writer, 'lun_mapping', obj.lun_mapping)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.paths is not None:
            Writer.write_integer(writer, 'paths', obj.paths)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.portal is not None:
            Writer.write_string(writer, 'portal', obj.portal)
        if obj.product_id is not None:
            Writer.write_string(writer, 'product_id', obj.product_id)
        if obj.serial is not None:
            Writer.write_string(writer, 'serial', obj.serial)
        if obj.size is not None:
            Writer.write_integer(writer, 'size', obj.size)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.storage_domain_id is not None:
            Writer.write_string(writer, 'storage_domain_id', obj.storage_domain_id)
        if obj.target is not None:
            Writer.write_string(writer, 'target', obj.target)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.vendor_id is not None:
            Writer.write_string(writer, 'vendor_id', obj.vendor_id)
        if obj.volume_group_id is not None:
            Writer.write_string(writer, 'volume_group_id', obj.volume_group_id)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'logical_unit'
        if plural is None:
            plural = 'logical_units'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            LogicalUnitWriter.write_one(obj, writer, singular)
        writer.write_end()


class MDevTypeWriter(Writer):

    def __init__(self):
        super(MDevTypeWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'm_dev_type'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.available_instances is not None:
            Writer.write_integer(writer, 'available_instances', obj.available_instances)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.human_readable_name is not None:
            Writer.write_string(writer, 'human_readable_name', obj.human_readable_name)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'm_dev_type'
        if plural is None:
            plural = 'm_dev_types'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MDevTypeWriter.write_one(obj, writer, singular)
        writer.write_end()


class MacWriter(Writer):

    def __init__(self):
        super(MacWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'mac'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'mac'
        if plural is None:
            plural = 'macs'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MacWriter.write_one(obj, writer, singular)
        writer.write_end()


class MacPoolWriter(Writer):

    def __init__(self):
        super(MacPoolWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'mac_pool'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.allow_duplicates is not None:
            Writer.write_boolean(writer, 'allow_duplicates', obj.allow_duplicates)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.default_pool is not None:
            Writer.write_boolean(writer, 'default_pool', obj.default_pool)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.ranges is not None:
            RangeWriter.write_many(obj.ranges, writer, 'range', 'ranges')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'mac_pool'
        if plural is None:
            plural = 'mac_pools'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MacPoolWriter.write_one(obj, writer, singular)
        writer.write_end()


class MemoryOverCommitWriter(Writer):

    def __init__(self):
        super(MemoryOverCommitWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'memory_over_commit'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.percent is not None:
            Writer.write_integer(writer, 'percent', obj.percent)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'memory_over_commit'
        if plural is None:
            plural = 'memory_over_commits'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MemoryOverCommitWriter.write_one(obj, writer, singular)
        writer.write_end()


class MemoryPolicyWriter(Writer):

    def __init__(self):
        super(MemoryPolicyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'memory_policy'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.ballooning is not None:
            Writer.write_boolean(writer, 'ballooning', obj.ballooning)
        if obj.guaranteed is not None:
            Writer.write_integer(writer, 'guaranteed', obj.guaranteed)
        if obj.max is not None:
            Writer.write_integer(writer, 'max', obj.max)
        if obj.over_commit is not None:
            MemoryOverCommitWriter.write_one(obj.over_commit, writer, 'over_commit')
        if obj.transparent_huge_pages is not None:
            TransparentHugePagesWriter.write_one(obj.transparent_huge_pages, writer, 'transparent_hugepages')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'memory_policy'
        if plural is None:
            plural = 'memory_policies'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MemoryPolicyWriter.write_one(obj, writer, singular)
        writer.write_end()


class MethodWriter(Writer):

    def __init__(self):
        super(MethodWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'method'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'method'
        if plural is None:
            plural = 'methods'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MethodWriter.write_one(obj, writer, singular)
        writer.write_end()


class MigrationBandwidthWriter(Writer):

    def __init__(self):
        super(MigrationBandwidthWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'migration_bandwidth'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.assignment_method is not None:
            Writer.write_string(writer, 'assignment_method', obj.assignment_method.value)
        if obj.custom_value is not None:
            Writer.write_integer(writer, 'custom_value', obj.custom_value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'migration_bandwidth'
        if plural is None:
            plural = 'migration_bandwidths'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MigrationBandwidthWriter.write_one(obj, writer, singular)
        writer.write_end()


class MigrationOptionsWriter(Writer):

    def __init__(self):
        super(MigrationOptionsWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'migration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.auto_converge is not None:
            Writer.write_string(writer, 'auto_converge', obj.auto_converge.value)
        if obj.bandwidth is not None:
            MigrationBandwidthWriter.write_one(obj.bandwidth, writer, 'bandwidth')
        if obj.compressed is not None:
            Writer.write_string(writer, 'compressed', obj.compressed.value)
        if obj.encrypted is not None:
            Writer.write_string(writer, 'encrypted', obj.encrypted.value)
        if obj.policy is not None:
            MigrationPolicyWriter.write_one(obj.policy, writer, 'policy')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'migration'
        if plural is None:
            plural = 'migration_optionss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MigrationOptionsWriter.write_one(obj, writer, singular)
        writer.write_end()


class MigrationPolicyWriter(Writer):

    def __init__(self):
        super(MigrationPolicyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'migration_policy'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'migration_policy'
        if plural is None:
            plural = 'migration_policies'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            MigrationPolicyWriter.write_one(obj, writer, singular)
        writer.write_end()


class NetworkWriter(Writer):

    def __init__(self):
        super(NetworkWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'network'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.display is not None:
            Writer.write_boolean(writer, 'display', obj.display)
        if obj.dns_resolver_configuration is not None:
            DnsResolverConfigurationWriter.write_one(obj.dns_resolver_configuration, writer, 'dns_resolver_configuration')
        if obj.ip is not None:
            IpWriter.write_one(obj.ip, writer, 'ip')
        if obj.mtu is not None:
            Writer.write_integer(writer, 'mtu', obj.mtu)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.port_isolation is not None:
            Writer.write_boolean(writer, 'port_isolation', obj.port_isolation)
        if obj.profile_required is not None:
            Writer.write_boolean(writer, 'profile_required', obj.profile_required)
        if obj.required is not None:
            Writer.write_boolean(writer, 'required', obj.required)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.stp is not None:
            Writer.write_boolean(writer, 'stp', obj.stp)
        if obj.usages is not None:
            writer.write_start('usages')
            for item in obj.usages:
                if item is not None:
                    Writer.write_string(writer, 'usage', item.value)
            writer.write_end()
        if obj.vdsm_name is not None:
            Writer.write_string(writer, 'vdsm_name', obj.vdsm_name)
        if obj.vlan is not None:
            VlanWriter.write_one(obj.vlan, writer, 'vlan')
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.external_provider is not None:
            OpenStackNetworkProviderWriter.write_one(obj.external_provider, writer, 'external_provider')
        if obj.external_provider_physical_network is not None:
            NetworkWriter.write_one(obj.external_provider_physical_network, writer, 'external_provider_physical_network')
        if obj.network_labels is not None:
            NetworkLabelWriter.write_many(obj.network_labels, writer, 'network_label', 'network_labels')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.qos is not None:
            QosWriter.write_one(obj.qos, writer, 'qos')
        if obj.vnic_profiles is not None:
            VnicProfileWriter.write_many(obj.vnic_profiles, writer, 'vnic_profile', 'vnic_profiles')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'network'
        if plural is None:
            plural = 'networks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NetworkWriter.write_one(obj, writer, singular)
        writer.write_end()


class NetworkAttachmentWriter(Writer):

    def __init__(self):
        super(NetworkAttachmentWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'network_attachment'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.dns_resolver_configuration is not None:
            DnsResolverConfigurationWriter.write_one(obj.dns_resolver_configuration, writer, 'dns_resolver_configuration')
        if obj.in_sync is not None:
            Writer.write_boolean(writer, 'in_sync', obj.in_sync)
        if obj.ip_address_assignments is not None:
            IpAddressAssignmentWriter.write_many(obj.ip_address_assignments, writer, 'ip_address_assignment', 'ip_address_assignments')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.reported_configurations is not None:
            ReportedConfigurationWriter.write_many(obj.reported_configurations, writer, 'reported_configuration', 'reported_configurations')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.host_nic is not None:
            HostNicWriter.write_one(obj.host_nic, writer, 'host_nic')
        if obj.network is not None:
            NetworkWriter.write_one(obj.network, writer, 'network')
        if obj.qos is not None:
            QosWriter.write_one(obj.qos, writer, 'qos')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'network_attachment'
        if plural is None:
            plural = 'network_attachments'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NetworkAttachmentWriter.write_one(obj, writer, singular)
        writer.write_end()


class NetworkConfigurationWriter(Writer):

    def __init__(self):
        super(NetworkConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'network_configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.dns is not None:
            DnsWriter.write_one(obj.dns, writer, 'dns')
        if obj.nics is not None:
            NicWriter.write_many(obj.nics, writer, 'nic', 'nics')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'network_configuration'
        if plural is None:
            plural = 'network_configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NetworkConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class NetworkFilterWriter(Writer):

    def __init__(self):
        super(NetworkFilterWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'network_filter'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.version is not None:
            VersionWriter.write_one(obj.version, writer, 'version')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'network_filter'
        if plural is None:
            plural = 'network_filters'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NetworkFilterWriter.write_one(obj, writer, singular)
        writer.write_end()


class NetworkFilterParameterWriter(Writer):

    def __init__(self):
        super(NetworkFilterParameterWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'network_filter_parameter'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        if obj.nic is not None:
            NicWriter.write_one(obj.nic, writer, 'nic')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'network_filter_parameter'
        if plural is None:
            plural = 'network_filter_parameters'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NetworkFilterParameterWriter.write_one(obj, writer, singular)
        writer.write_end()


class NetworkLabelWriter(Writer):

    def __init__(self):
        super(NetworkLabelWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'network_label'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.host_nic is not None:
            HostNicWriter.write_one(obj.host_nic, writer, 'host_nic')
        if obj.network is not None:
            NetworkWriter.write_one(obj.network, writer, 'network')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'network_label'
        if plural is None:
            plural = 'network_labels'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NetworkLabelWriter.write_one(obj, writer, singular)
        writer.write_end()


class NfsProfileDetailWriter(Writer):

    def __init__(self):
        super(NfsProfileDetailWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'nfs_profile_detail'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.nfs_server_ip is not None:
            Writer.write_string(writer, 'nfs_server_ip', obj.nfs_server_ip)
        if obj.profile_details is not None:
            ProfileDetailWriter.write_many(obj.profile_details, writer, 'profile_detail', 'profile_details')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'nfs_profile_detail'
        if plural is None:
            plural = 'nfs_profile_details'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NfsProfileDetailWriter.write_one(obj, writer, singular)
        writer.write_end()


class NicWriter(Writer):

    def __init__(self):
        super(NicWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'nic'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.boot_protocol is not None:
            Writer.write_string(writer, 'boot_protocol', obj.boot_protocol.value)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.interface is not None:
            Writer.write_string(writer, 'interface', obj.interface.value)
        if obj.linked is not None:
            Writer.write_boolean(writer, 'linked', obj.linked)
        if obj.mac is not None:
            MacWriter.write_one(obj.mac, writer, 'mac')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.on_boot is not None:
            Writer.write_boolean(writer, 'on_boot', obj.on_boot)
        if obj.plugged is not None:
            Writer.write_boolean(writer, 'plugged', obj.plugged)
        if obj.synced is not None:
            Writer.write_boolean(writer, 'synced', obj.synced)
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.network is not None:
            NetworkWriter.write_one(obj.network, writer, 'network')
        if obj.network_attachments is not None:
            NetworkAttachmentWriter.write_many(obj.network_attachments, writer, 'network_attachment', 'network_attachments')
        if obj.network_filter_parameters is not None:
            NetworkFilterParameterWriter.write_many(obj.network_filter_parameters, writer, 'network_filter_parameter', 'network_filter_parameters')
        if obj.network_labels is not None:
            NetworkLabelWriter.write_many(obj.network_labels, writer, 'network_label', 'network_labels')
        if obj.reported_devices is not None:
            ReportedDeviceWriter.write_many(obj.reported_devices, writer, 'reported_device', 'reported_devices')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.virtual_function_allowed_labels is not None:
            NetworkLabelWriter.write_many(obj.virtual_function_allowed_labels, writer, 'network_label', 'virtual_function_allowed_labels')
        if obj.virtual_function_allowed_networks is not None:
            NetworkWriter.write_many(obj.virtual_function_allowed_networks, writer, 'network', 'virtual_function_allowed_networks')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        if obj.vnic_profile is not None:
            VnicProfileWriter.write_one(obj.vnic_profile, writer, 'vnic_profile')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'nic'
        if plural is None:
            plural = 'nics'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NicWriter.write_one(obj, writer, singular)
        writer.write_end()


class NicConfigurationWriter(Writer):

    def __init__(self):
        super(NicConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'nic_configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.boot_protocol is not None:
            Writer.write_string(writer, 'boot_protocol', obj.boot_protocol.value)
        if obj.ip is not None:
            IpWriter.write_one(obj.ip, writer, 'ip')
        if obj.ipv6 is not None:
            IpWriter.write_one(obj.ipv6, writer, 'ipv6')
        if obj.ipv6_boot_protocol is not None:
            Writer.write_string(writer, 'ipv6_boot_protocol', obj.ipv6_boot_protocol.value)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.on_boot is not None:
            Writer.write_boolean(writer, 'on_boot', obj.on_boot)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'nic_configuration'
        if plural is None:
            plural = 'nic_configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NicConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class NumaNodeWriter(Writer):

    def __init__(self):
        super(NumaNodeWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'host_numa_node'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.index is not None:
            Writer.write_integer(writer, 'index', obj.index)
        if obj.memory is not None:
            Writer.write_integer(writer, 'memory', obj.memory)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.node_distance is not None:
            Writer.write_string(writer, 'node_distance', obj.node_distance)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'host_numa_node'
        if plural is None:
            plural = 'host_numa_nodes'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NumaNodeWriter.write_one(obj, writer, singular)
        writer.write_end()


class NumaNodePinWriter(Writer):

    def __init__(self):
        super(NumaNodePinWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'numa_node_pin'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.host_numa_node is not None:
            NumaNodeWriter.write_one(obj.host_numa_node, writer, 'host_numa_node')
        if obj.index is not None:
            Writer.write_integer(writer, 'index', obj.index)
        if obj.pinned is not None:
            Writer.write_boolean(writer, 'pinned', obj.pinned)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'numa_node_pin'
        if plural is None:
            plural = 'numa_node_pins'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            NumaNodePinWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenStackImageWriter(Writer):

    def __init__(self):
        super(OpenStackImageWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'openstack_image'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.openstack_image_provider is not None:
            OpenStackImageProviderWriter.write_one(obj.openstack_image_provider, writer, 'openstack_image_provider')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'openstack_image'
        if plural is None:
            plural = 'openstack_images'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenStackImageWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenStackImageProviderWriter(Writer):

    def __init__(self):
        super(OpenStackImageProviderWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'openstack_image_provider'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.authentication_url is not None:
            Writer.write_string(writer, 'authentication_url', obj.authentication_url)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.requires_authentication is not None:
            Writer.write_boolean(writer, 'requires_authentication', obj.requires_authentication)
        if obj.tenant_name is not None:
            Writer.write_string(writer, 'tenant_name', obj.tenant_name)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.certificates is not None:
            CertificateWriter.write_many(obj.certificates, writer, 'certificate', 'certificates')
        if obj.images is not None:
            OpenStackImageWriter.write_many(obj.images, writer, 'openstack_image', 'images')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'openstack_image_provider'
        if plural is None:
            plural = 'openstack_image_providers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenStackImageProviderWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenStackNetworkWriter(Writer):

    def __init__(self):
        super(OpenStackNetworkWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'openstack_network'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.openstack_network_provider is not None:
            OpenStackNetworkProviderWriter.write_one(obj.openstack_network_provider, writer, 'openstack_network_provider')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'openstack_network'
        if plural is None:
            plural = 'openstack_networks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenStackNetworkWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenStackNetworkProviderWriter(Writer):

    def __init__(self):
        super(OpenStackNetworkProviderWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'openstack_network_provider'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.agent_configuration is not None:
            AgentConfigurationWriter.write_one(obj.agent_configuration, writer, 'agent_configuration')
        if obj.authentication_url is not None:
            Writer.write_string(writer, 'authentication_url', obj.authentication_url)
        if obj.auto_sync is not None:
            Writer.write_boolean(writer, 'auto_sync', obj.auto_sync)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.external_plugin_type is not None:
            Writer.write_string(writer, 'external_plugin_type', obj.external_plugin_type)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.plugin_type is not None:
            Writer.write_string(writer, 'plugin_type', obj.plugin_type.value)
        if obj.project_domain_name is not None:
            Writer.write_string(writer, 'project_domain_name', obj.project_domain_name)
        if obj.project_name is not None:
            Writer.write_string(writer, 'project_name', obj.project_name)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.read_only is not None:
            Writer.write_boolean(writer, 'read_only', obj.read_only)
        if obj.requires_authentication is not None:
            Writer.write_boolean(writer, 'requires_authentication', obj.requires_authentication)
        if obj.tenant_name is not None:
            Writer.write_string(writer, 'tenant_name', obj.tenant_name)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.unmanaged is not None:
            Writer.write_boolean(writer, 'unmanaged', obj.unmanaged)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.user_domain_name is not None:
            Writer.write_string(writer, 'user_domain_name', obj.user_domain_name)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.certificates is not None:
            CertificateWriter.write_many(obj.certificates, writer, 'certificate', 'certificates')
        if obj.networks is not None:
            OpenStackNetworkWriter.write_many(obj.networks, writer, 'openstack_network', 'networks')
        if obj.subnets is not None:
            OpenStackSubnetWriter.write_many(obj.subnets, writer, 'openstack_subnet', 'subnets')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'openstack_network_provider'
        if plural is None:
            plural = 'openstack_network_providers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenStackNetworkProviderWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenStackProviderWriter(Writer):

    def __init__(self):
        super(OpenStackProviderWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'open_stack_provider'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.authentication_url is not None:
            Writer.write_string(writer, 'authentication_url', obj.authentication_url)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.requires_authentication is not None:
            Writer.write_boolean(writer, 'requires_authentication', obj.requires_authentication)
        if obj.tenant_name is not None:
            Writer.write_string(writer, 'tenant_name', obj.tenant_name)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'open_stack_provider'
        if plural is None:
            plural = 'open_stack_providers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenStackProviderWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenStackSubnetWriter(Writer):

    def __init__(self):
        super(OpenStackSubnetWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'openstack_subnet'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.cidr is not None:
            Writer.write_string(writer, 'cidr', obj.cidr)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.dns_servers is not None:
            writer.write_start('dns_servers')
            for item in obj.dns_servers:
                if item is not None:
                    Writer.write_string(writer, 'dns_server', item)
            writer.write_end()
        if obj.gateway is not None:
            Writer.write_string(writer, 'gateway', obj.gateway)
        if obj.ip_version is not None:
            Writer.write_string(writer, 'ip_version', obj.ip_version)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.openstack_network is not None:
            OpenStackNetworkWriter.write_one(obj.openstack_network, writer, 'openstack_network')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'openstack_subnet'
        if plural is None:
            plural = 'openstack_subnets'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenStackSubnetWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenStackVolumeProviderWriter(Writer):

    def __init__(self):
        super(OpenStackVolumeProviderWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'openstack_volume_provider'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.authentication_url is not None:
            Writer.write_string(writer, 'authentication_url', obj.authentication_url)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.requires_authentication is not None:
            Writer.write_boolean(writer, 'requires_authentication', obj.requires_authentication)
        if obj.tenant_name is not None:
            Writer.write_string(writer, 'tenant_name', obj.tenant_name)
        if obj.url is not None:
            Writer.write_string(writer, 'url', obj.url)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.authentication_keys is not None:
            OpenstackVolumeAuthenticationKeyWriter.write_many(obj.authentication_keys, writer, 'openstack_volume_authentication_key', 'authentication_keys')
        if obj.certificates is not None:
            CertificateWriter.write_many(obj.certificates, writer, 'certificate', 'certificates')
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.volume_types is not None:
            OpenStackVolumeTypeWriter.write_many(obj.volume_types, writer, 'open_stack_volume_type', 'volume_types')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'openstack_volume_provider'
        if plural is None:
            plural = 'openstack_volume_providers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenStackVolumeProviderWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenStackVolumeTypeWriter(Writer):

    def __init__(self):
        super(OpenStackVolumeTypeWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'open_stack_volume_type'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.openstack_volume_provider is not None:
            OpenStackVolumeProviderWriter.write_one(obj.openstack_volume_provider, writer, 'openstack_volume_provider')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'open_stack_volume_type'
        if plural is None:
            plural = 'open_stack_volume_types'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenStackVolumeTypeWriter.write_one(obj, writer, singular)
        writer.write_end()


class OpenstackVolumeAuthenticationKeyWriter(Writer):

    def __init__(self):
        super(OpenstackVolumeAuthenticationKeyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'openstack_volume_authentication_key'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.creation_date is not None:
            Writer.write_date(writer, 'creation_date', obj.creation_date)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.usage_type is not None:
            Writer.write_string(writer, 'usage_type', obj.usage_type.value)
        if obj.uuid is not None:
            Writer.write_string(writer, 'uuid', obj.uuid)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        if obj.openstack_volume_provider is not None:
            OpenStackVolumeProviderWriter.write_one(obj.openstack_volume_provider, writer, 'openstack_volume_provider')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'openstack_volume_authentication_key'
        if plural is None:
            plural = 'openstack_volume_authentication_keys'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OpenstackVolumeAuthenticationKeyWriter.write_one(obj, writer, singular)
        writer.write_end()


class OperatingSystemWriter(Writer):

    def __init__(self):
        super(OperatingSystemWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'os'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.boot is not None:
            BootWriter.write_one(obj.boot, writer, 'boot')
        if obj.cmdline is not None:
            Writer.write_string(writer, 'cmdline', obj.cmdline)
        if obj.custom_kernel_cmdline is not None:
            Writer.write_string(writer, 'custom_kernel_cmdline', obj.custom_kernel_cmdline)
        if obj.initrd is not None:
            Writer.write_string(writer, 'initrd', obj.initrd)
        if obj.kernel is not None:
            Writer.write_string(writer, 'kernel', obj.kernel)
        if obj.reported_kernel_cmdline is not None:
            Writer.write_string(writer, 'reported_kernel_cmdline', obj.reported_kernel_cmdline)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type)
        if obj.version is not None:
            VersionWriter.write_one(obj.version, writer, 'version')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'os'
        if plural is None:
            plural = 'oss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OperatingSystemWriter.write_one(obj, writer, singular)
        writer.write_end()


class OperatingSystemInfoWriter(Writer):

    def __init__(self):
        super(OperatingSystemInfoWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'operating_system'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.architecture is not None:
            Writer.write_string(writer, 'architecture', obj.architecture.value)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.large_icon is not None:
            IconWriter.write_one(obj.large_icon, writer, 'large_icon')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.small_icon is not None:
            IconWriter.write_one(obj.small_icon, writer, 'small_icon')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'operating_system'
        if plural is None:
            plural = 'operation_systems'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OperatingSystemInfoWriter.write_one(obj, writer, singular)
        writer.write_end()


class OptionWriter(Writer):

    def __init__(self):
        super(OptionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'option'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'option'
        if plural is None:
            plural = 'options'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            OptionWriter.write_one(obj, writer, singular)
        writer.write_end()


class PackageWriter(Writer):

    def __init__(self):
        super(PackageWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'package'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'package'
        if plural is None:
            plural = 'packages'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            PackageWriter.write_one(obj, writer, singular)
        writer.write_end()


class PayloadWriter(Writer):

    def __init__(self):
        super(PayloadWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'payload'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.files is not None:
            FileWriter.write_many(obj.files, writer, 'file', 'files')
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.volume_id is not None:
            Writer.write_string(writer, 'volume_id', obj.volume_id)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'payload'
        if plural is None:
            plural = 'payloads'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            PayloadWriter.write_one(obj, writer, singular)
        writer.write_end()


class PermissionWriter(Writer):

    def __init__(self):
        super(PermissionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'permission'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.disk is not None:
            DiskWriter.write_one(obj.disk, writer, 'disk')
        if obj.group is not None:
            GroupWriter.write_one(obj.group, writer, 'group')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.role is not None:
            RoleWriter.write_one(obj.role, writer, 'role')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vm_pool is not None:
            VmPoolWriter.write_one(obj.vm_pool, writer, 'vm_pool')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'permission'
        if plural is None:
            plural = 'permissions'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            PermissionWriter.write_one(obj, writer, singular)
        writer.write_end()


class PermitWriter(Writer):

    def __init__(self):
        super(PermitWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'permit'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.administrative is not None:
            Writer.write_boolean(writer, 'administrative', obj.administrative)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.role is not None:
            RoleWriter.write_one(obj.role, writer, 'role')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'permit'
        if plural is None:
            plural = 'permits'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            PermitWriter.write_one(obj, writer, singular)
        writer.write_end()


class PmProxyWriter(Writer):

    def __init__(self):
        super(PmProxyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'pm_proxy'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'pm_proxy'
        if plural is None:
            plural = 'pm_proxies'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            PmProxyWriter.write_one(obj, writer, singular)
        writer.write_end()


class PortMirroringWriter(Writer):

    def __init__(self):
        super(PortMirroringWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'port_mirroring'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'port_mirroring'
        if plural is None:
            plural = 'port_mirrorings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            PortMirroringWriter.write_one(obj, writer, singular)
        writer.write_end()


class PowerManagementWriter(Writer):

    def __init__(self):
        super(PowerManagementWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'power_management'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.agents is not None:
            AgentWriter.write_many(obj.agents, writer, 'agent', 'agents')
        if obj.automatic_pm_enabled is not None:
            Writer.write_boolean(writer, 'automatic_pm_enabled', obj.automatic_pm_enabled)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        if obj.kdump_detection is not None:
            Writer.write_boolean(writer, 'kdump_detection', obj.kdump_detection)
        if obj.options is not None:
            OptionWriter.write_many(obj.options, writer, 'option', 'options')
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.pm_proxies is not None:
            PmProxyWriter.write_many(obj.pm_proxies, writer, 'pm_proxy', 'pm_proxies')
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'power_management'
        if plural is None:
            plural = 'power_managements'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            PowerManagementWriter.write_one(obj, writer, singular)
        writer.write_end()


class ProductWriter(Writer):

    def __init__(self):
        super(ProductWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'product'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'product'
        if plural is None:
            plural = 'products'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ProductWriter.write_one(obj, writer, singular)
        writer.write_end()


class ProductInfoWriter(Writer):

    def __init__(self):
        super(ProductInfoWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'product_info'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.instance_id is not None:
            Writer.write_string(writer, 'instance_id', obj.instance_id)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.vendor is not None:
            Writer.write_string(writer, 'vendor', obj.vendor)
        if obj.version is not None:
            VersionWriter.write_one(obj.version, writer, 'version')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'product_info'
        if plural is None:
            plural = 'product_infos'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ProductInfoWriter.write_one(obj, writer, singular)
        writer.write_end()


class ProfileDetailWriter(Writer):

    def __init__(self):
        super(ProfileDetailWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'profile_detail'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.block_statistics is not None:
            BlockStatisticWriter.write_many(obj.block_statistics, writer, 'block_statistic', 'block_statistics')
        if obj.duration is not None:
            Writer.write_integer(writer, 'duration', obj.duration)
        if obj.fop_statistics is not None:
            FopStatisticWriter.write_many(obj.fop_statistics, writer, 'fop_statistic', 'fop_statistics')
        if obj.profile_type is not None:
            Writer.write_string(writer, 'profile_type', obj.profile_type)
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'profile_detail'
        if plural is None:
            plural = 'profile_details'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ProfileDetailWriter.write_one(obj, writer, singular)
        writer.write_end()


class PropertyWriter(Writer):

    def __init__(self):
        super(PropertyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'property'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'property'
        if plural is None:
            plural = 'properties'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            PropertyWriter.write_one(obj, writer, singular)
        writer.write_end()


class ProxyTicketWriter(Writer):

    def __init__(self):
        super(ProxyTicketWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'proxy_ticket'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'proxy_ticket'
        if plural is None:
            plural = 'proxy_tickets'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ProxyTicketWriter.write_one(obj, writer, singular)
        writer.write_end()


class QosWriter(Writer):

    def __init__(self):
        super(QosWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'qos'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.cpu_limit is not None:
            Writer.write_integer(writer, 'cpu_limit', obj.cpu_limit)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.inbound_average is not None:
            Writer.write_integer(writer, 'inbound_average', obj.inbound_average)
        if obj.inbound_burst is not None:
            Writer.write_integer(writer, 'inbound_burst', obj.inbound_burst)
        if obj.inbound_peak is not None:
            Writer.write_integer(writer, 'inbound_peak', obj.inbound_peak)
        if obj.max_iops is not None:
            Writer.write_integer(writer, 'max_iops', obj.max_iops)
        if obj.max_read_iops is not None:
            Writer.write_integer(writer, 'max_read_iops', obj.max_read_iops)
        if obj.max_read_throughput is not None:
            Writer.write_integer(writer, 'max_read_throughput', obj.max_read_throughput)
        if obj.max_throughput is not None:
            Writer.write_integer(writer, 'max_throughput', obj.max_throughput)
        if obj.max_write_iops is not None:
            Writer.write_integer(writer, 'max_write_iops', obj.max_write_iops)
        if obj.max_write_throughput is not None:
            Writer.write_integer(writer, 'max_write_throughput', obj.max_write_throughput)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.outbound_average is not None:
            Writer.write_integer(writer, 'outbound_average', obj.outbound_average)
        if obj.outbound_average_linkshare is not None:
            Writer.write_integer(writer, 'outbound_average_linkshare', obj.outbound_average_linkshare)
        if obj.outbound_average_realtime is not None:
            Writer.write_integer(writer, 'outbound_average_realtime', obj.outbound_average_realtime)
        if obj.outbound_average_upperlimit is not None:
            Writer.write_integer(writer, 'outbound_average_upperlimit', obj.outbound_average_upperlimit)
        if obj.outbound_burst is not None:
            Writer.write_integer(writer, 'outbound_burst', obj.outbound_burst)
        if obj.outbound_peak is not None:
            Writer.write_integer(writer, 'outbound_peak', obj.outbound_peak)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'qos'
        if plural is None:
            plural = 'qoss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            QosWriter.write_one(obj, writer, singular)
        writer.write_end()


class QuotaWriter(Writer):

    def __init__(self):
        super(QuotaWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'quota'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.cluster_hard_limit_pct is not None:
            Writer.write_integer(writer, 'cluster_hard_limit_pct', obj.cluster_hard_limit_pct)
        if obj.cluster_soft_limit_pct is not None:
            Writer.write_integer(writer, 'cluster_soft_limit_pct', obj.cluster_soft_limit_pct)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.disks is not None:
            DiskWriter.write_many(obj.disks, writer, 'disk', 'disks')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.storage_hard_limit_pct is not None:
            Writer.write_integer(writer, 'storage_hard_limit_pct', obj.storage_hard_limit_pct)
        if obj.storage_soft_limit_pct is not None:
            Writer.write_integer(writer, 'storage_soft_limit_pct', obj.storage_soft_limit_pct)
        if obj.users is not None:
            UserWriter.write_many(obj.users, writer, 'user', 'users')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.quota_cluster_limits is not None:
            QuotaClusterLimitWriter.write_many(obj.quota_cluster_limits, writer, 'quota_cluster_limit', 'quota_cluster_limits')
        if obj.quota_storage_limits is not None:
            QuotaStorageLimitWriter.write_many(obj.quota_storage_limits, writer, 'quota_storage_limit', 'quota_storage_limits')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'quota'
        if plural is None:
            plural = 'quotas'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            QuotaWriter.write_one(obj, writer, singular)
        writer.write_end()


class QuotaClusterLimitWriter(Writer):

    def __init__(self):
        super(QuotaClusterLimitWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'quota_cluster_limit'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.memory_limit is not None:
            Writer.write_decimal(writer, 'memory_limit', obj.memory_limit)
        if obj.memory_usage is not None:
            Writer.write_decimal(writer, 'memory_usage', obj.memory_usage)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.vcpu_limit is not None:
            Writer.write_integer(writer, 'vcpu_limit', obj.vcpu_limit)
        if obj.vcpu_usage is not None:
            Writer.write_integer(writer, 'vcpu_usage', obj.vcpu_usage)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'quota_cluster_limit'
        if plural is None:
            plural = 'quota_cluster_limits'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            QuotaClusterLimitWriter.write_one(obj, writer, singular)
        writer.write_end()


class QuotaStorageLimitWriter(Writer):

    def __init__(self):
        super(QuotaStorageLimitWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'quota_storage_limit'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.limit is not None:
            Writer.write_integer(writer, 'limit', obj.limit)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.usage is not None:
            Writer.write_decimal(writer, 'usage', obj.usage)
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'quota_storage_limit'
        if plural is None:
            plural = 'quota_storage_limits'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            QuotaStorageLimitWriter.write_one(obj, writer, singular)
        writer.write_end()


class RangeWriter(Writer):

    def __init__(self):
        super(RangeWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'range'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.from_ is not None:
            Writer.write_string(writer, 'from', obj.from_)
        if obj.to is not None:
            Writer.write_string(writer, 'to', obj.to)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'range'
        if plural is None:
            plural = 'ranges'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RangeWriter.write_one(obj, writer, singular)
        writer.write_end()


class RateWriter(Writer):

    def __init__(self):
        super(RateWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'rate'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.bytes is not None:
            Writer.write_integer(writer, 'bytes', obj.bytes)
        if obj.period is not None:
            Writer.write_integer(writer, 'period', obj.period)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'rate'
        if plural is None:
            plural = 'rates'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RateWriter.write_one(obj, writer, singular)
        writer.write_end()


class RegistrationAffinityGroupMappingWriter(Writer):

    def __init__(self):
        super(RegistrationAffinityGroupMappingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'registration_affinity_group_mapping'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.from_ is not None:
            AffinityGroupWriter.write_one(obj.from_, writer, 'from')
        if obj.to is not None:
            AffinityGroupWriter.write_one(obj.to, writer, 'to')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'registration_affinity_group_mapping'
        if plural is None:
            plural = 'registration_affinity_group_mappings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RegistrationAffinityGroupMappingWriter.write_one(obj, writer, singular)
        writer.write_end()


class RegistrationAffinityLabelMappingWriter(Writer):

    def __init__(self):
        super(RegistrationAffinityLabelMappingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'registration_affinity_label_mapping'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.from_ is not None:
            AffinityLabelWriter.write_one(obj.from_, writer, 'from')
        if obj.to is not None:
            AffinityLabelWriter.write_one(obj.to, writer, 'to')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'registration_affinity_label_mapping'
        if plural is None:
            plural = 'registration_affinity_label_mappings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RegistrationAffinityLabelMappingWriter.write_one(obj, writer, singular)
        writer.write_end()


class RegistrationClusterMappingWriter(Writer):

    def __init__(self):
        super(RegistrationClusterMappingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'registration_cluster_mapping'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.from_ is not None:
            ClusterWriter.write_one(obj.from_, writer, 'from')
        if obj.to is not None:
            ClusterWriter.write_one(obj.to, writer, 'to')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'registration_cluster_mapping'
        if plural is None:
            plural = 'registration_cluster_mappings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RegistrationClusterMappingWriter.write_one(obj, writer, singular)
        writer.write_end()


class RegistrationConfigurationWriter(Writer):

    def __init__(self):
        super(RegistrationConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'registration_configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.affinity_group_mappings is not None:
            RegistrationAffinityGroupMappingWriter.write_many(obj.affinity_group_mappings, writer, 'registration_affinity_group_mapping', 'affinity_group_mappings')
        if obj.affinity_label_mappings is not None:
            RegistrationAffinityLabelMappingWriter.write_many(obj.affinity_label_mappings, writer, 'registration_affinity_label_mapping', 'affinity_label_mappings')
        if obj.cluster_mappings is not None:
            RegistrationClusterMappingWriter.write_many(obj.cluster_mappings, writer, 'registration_cluster_mapping', 'cluster_mappings')
        if obj.domain_mappings is not None:
            RegistrationDomainMappingWriter.write_many(obj.domain_mappings, writer, 'registration_domain_mapping', 'domain_mappings')
        if obj.lun_mappings is not None:
            RegistrationLunMappingWriter.write_many(obj.lun_mappings, writer, 'registration_lun_mapping', 'lun_mappings')
        if obj.role_mappings is not None:
            RegistrationRoleMappingWriter.write_many(obj.role_mappings, writer, 'registration_role_mapping', 'role_mappings')
        if obj.vnic_profile_mappings is not None:
            RegistrationVnicProfileMappingWriter.write_many(obj.vnic_profile_mappings, writer, 'registration_vnic_profile_mapping', 'vnic_profile_mappings')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'registration_configuration'
        if plural is None:
            plural = 'registration_configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RegistrationConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class RegistrationDomainMappingWriter(Writer):

    def __init__(self):
        super(RegistrationDomainMappingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'registration_domain_mapping'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.from_ is not None:
            DomainWriter.write_one(obj.from_, writer, 'from')
        if obj.to is not None:
            DomainWriter.write_one(obj.to, writer, 'to')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'registration_domain_mapping'
        if plural is None:
            plural = 'registration_domain_mappings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RegistrationDomainMappingWriter.write_one(obj, writer, singular)
        writer.write_end()


class RegistrationLunMappingWriter(Writer):

    def __init__(self):
        super(RegistrationLunMappingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'registration_lun_mapping'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.from_ is not None:
            DiskWriter.write_one(obj.from_, writer, 'from')
        if obj.to is not None:
            DiskWriter.write_one(obj.to, writer, 'to')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'registration_lun_mapping'
        if plural is None:
            plural = 'registration_lun_mappings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RegistrationLunMappingWriter.write_one(obj, writer, singular)
        writer.write_end()


class RegistrationRoleMappingWriter(Writer):

    def __init__(self):
        super(RegistrationRoleMappingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'registration_role_mapping'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.from_ is not None:
            RoleWriter.write_one(obj.from_, writer, 'from')
        if obj.to is not None:
            RoleWriter.write_one(obj.to, writer, 'to')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'registration_role_mapping'
        if plural is None:
            plural = 'registration_role_mappings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RegistrationRoleMappingWriter.write_one(obj, writer, singular)
        writer.write_end()


class RegistrationVnicProfileMappingWriter(Writer):

    def __init__(self):
        super(RegistrationVnicProfileMappingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'registration_vnic_profile_mapping'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.from_ is not None:
            VnicProfileWriter.write_one(obj.from_, writer, 'from')
        if obj.to is not None:
            VnicProfileWriter.write_one(obj.to, writer, 'to')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'registration_vnic_profile_mapping'
        if plural is None:
            plural = 'registration_vnic_profile_mappings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RegistrationVnicProfileMappingWriter.write_one(obj, writer, singular)
        writer.write_end()


class ReportedConfigurationWriter(Writer):

    def __init__(self):
        super(ReportedConfigurationWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'reported_configuration'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.actual_value is not None:
            Writer.write_string(writer, 'actual_value', obj.actual_value)
        if obj.expected_value is not None:
            Writer.write_string(writer, 'expected_value', obj.expected_value)
        if obj.in_sync is not None:
            Writer.write_boolean(writer, 'in_sync', obj.in_sync)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'reported_configuration'
        if plural is None:
            plural = 'reported_configurations'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ReportedConfigurationWriter.write_one(obj, writer, singular)
        writer.write_end()


class ReportedDeviceWriter(Writer):

    def __init__(self):
        super(ReportedDeviceWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'reported_device'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.ips is not None:
            IpWriter.write_many(obj.ips, writer, 'ip', 'ips')
        if obj.mac is not None:
            MacWriter.write_one(obj.mac, writer, 'mac')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'reported_device'
        if plural is None:
            plural = 'reported_devices'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ReportedDeviceWriter.write_one(obj, writer, singular)
        writer.write_end()


class RngDeviceWriter(Writer):

    def __init__(self):
        super(RngDeviceWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'rng_device'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.rate is not None:
            RateWriter.write_one(obj.rate, writer, 'rate')
        if obj.source is not None:
            Writer.write_string(writer, 'source', obj.source.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'rng_device'
        if plural is None:
            plural = 'rng_devices'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RngDeviceWriter.write_one(obj, writer, singular)
        writer.write_end()


class RoleWriter(Writer):

    def __init__(self):
        super(RoleWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'role'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.administrative is not None:
            Writer.write_boolean(writer, 'administrative', obj.administrative)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.mutable is not None:
            Writer.write_boolean(writer, 'mutable', obj.mutable)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.permits is not None:
            PermitWriter.write_many(obj.permits, writer, 'permit', 'permits')
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'role'
        if plural is None:
            plural = 'roles'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            RoleWriter.write_one(obj, writer, singular)
        writer.write_end()


class SchedulingPolicyWriter(Writer):

    def __init__(self):
        super(SchedulingPolicyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'scheduling_policy'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.default_policy is not None:
            Writer.write_boolean(writer, 'default_policy', obj.default_policy)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.locked is not None:
            Writer.write_boolean(writer, 'locked', obj.locked)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.balances is not None:
            BalanceWriter.write_many(obj.balances, writer, 'balance', 'balances')
        if obj.filters is not None:
            FilterWriter.write_many(obj.filters, writer, 'filter', 'filters')
        if obj.weight is not None:
            WeightWriter.write_many(obj.weight, writer, 'weight', 'weight')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'scheduling_policy'
        if plural is None:
            plural = 'scheduling_policies'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SchedulingPolicyWriter.write_one(obj, writer, singular)
        writer.write_end()


class SchedulingPolicyUnitWriter(Writer):

    def __init__(self):
        super(SchedulingPolicyUnitWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'scheduling_policy_unit'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        if obj.internal is not None:
            Writer.write_boolean(writer, 'internal', obj.internal)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.properties is not None:
            PropertyWriter.write_many(obj.properties, writer, 'property', 'properties')
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'scheduling_policy_unit'
        if plural is None:
            plural = 'scheduling_policy_units'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SchedulingPolicyUnitWriter.write_one(obj, writer, singular)
        writer.write_end()


class SeLinuxWriter(Writer):

    def __init__(self):
        super(SeLinuxWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'se_linux'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.mode is not None:
            Writer.write_string(writer, 'mode', obj.mode.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'se_linux'
        if plural is None:
            plural = 'se_linuxs'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SeLinuxWriter.write_one(obj, writer, singular)
        writer.write_end()


class SerialNumberWriter(Writer):

    def __init__(self):
        super(SerialNumberWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'serial_number'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.policy is not None:
            Writer.write_string(writer, 'policy', obj.policy.value)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'serial_number'
        if plural is None:
            plural = 'serial_numbers'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SerialNumberWriter.write_one(obj, writer, singular)
        writer.write_end()


class SessionWriter(Writer):

    def __init__(self):
        super(SessionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'session'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.console_user is not None:
            Writer.write_boolean(writer, 'console_user', obj.console_user)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.ip is not None:
            IpWriter.write_one(obj.ip, writer, 'ip')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.protocol is not None:
            Writer.write_string(writer, 'protocol', obj.protocol)
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'session'
        if plural is None:
            plural = 'sessions'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SessionWriter.write_one(obj, writer, singular)
        writer.write_end()


class SkipIfConnectivityBrokenWriter(Writer):

    def __init__(self):
        super(SkipIfConnectivityBrokenWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'skip_if_connectivity_broken'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        if obj.threshold is not None:
            Writer.write_integer(writer, 'threshold', obj.threshold)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'skip_if_connectivity_broken'
        if plural is None:
            plural = 'skip_if_connectivity_brokens'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SkipIfConnectivityBrokenWriter.write_one(obj, writer, singular)
        writer.write_end()


class SkipIfSdActiveWriter(Writer):

    def __init__(self):
        super(SkipIfSdActiveWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'skip_if_sd_active'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'skip_if_sd_active'
        if plural is None:
            plural = 'skip_if_sd_actives'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SkipIfSdActiveWriter.write_one(obj, writer, singular)
        writer.write_end()


class SnapshotWriter(Writer):

    def __init__(self):
        super(SnapshotWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'snapshot'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.auto_pinning_policy is not None:
            Writer.write_string(writer, 'auto_pinning_policy', obj.auto_pinning_policy.value)
        if obj.bios is not None:
            BiosWriter.write_one(obj.bios, writer, 'bios')
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.console is not None:
            ConsoleWriter.write_one(obj.console, writer, 'console')
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.cpu_shares is not None:
            Writer.write_integer(writer, 'cpu_shares', obj.cpu_shares)
        if obj.creation_time is not None:
            Writer.write_date(writer, 'creation_time', obj.creation_time)
        if obj.custom_compatibility_version is not None:
            VersionWriter.write_one(obj.custom_compatibility_version, writer, 'custom_compatibility_version')
        if obj.custom_cpu_model is not None:
            Writer.write_string(writer, 'custom_cpu_model', obj.custom_cpu_model)
        if obj.custom_emulated_machine is not None:
            Writer.write_string(writer, 'custom_emulated_machine', obj.custom_emulated_machine)
        if obj.custom_properties is not None:
            CustomPropertyWriter.write_many(obj.custom_properties, writer, 'custom_property', 'custom_properties')
        if obj.date is not None:
            Writer.write_date(writer, 'date', obj.date)
        if obj.delete_protected is not None:
            Writer.write_boolean(writer, 'delete_protected', obj.delete_protected)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.display is not None:
            DisplayWriter.write_one(obj.display, writer, 'display')
        if obj.domain is not None:
            DomainWriter.write_one(obj.domain, writer, 'domain')
        if obj.fqdn is not None:
            Writer.write_string(writer, 'fqdn', obj.fqdn)
        if obj.guest_operating_system is not None:
            GuestOperatingSystemWriter.write_one(obj.guest_operating_system, writer, 'guest_operating_system')
        if obj.guest_time_zone is not None:
            TimeZoneWriter.write_one(obj.guest_time_zone, writer, 'guest_time_zone')
        if obj.has_illegal_images is not None:
            Writer.write_boolean(writer, 'has_illegal_images', obj.has_illegal_images)
        if obj.high_availability is not None:
            HighAvailabilityWriter.write_one(obj.high_availability, writer, 'high_availability')
        if obj.initialization is not None:
            InitializationWriter.write_one(obj.initialization, writer, 'initialization')
        if obj.io is not None:
            IoWriter.write_one(obj.io, writer, 'io')
        if obj.large_icon is not None:
            IconWriter.write_one(obj.large_icon, writer, 'large_icon')
        if obj.lease is not None:
            StorageDomainLeaseWriter.write_one(obj.lease, writer, 'lease')
        if obj.memory is not None:
            Writer.write_integer(writer, 'memory', obj.memory)
        if obj.memory_policy is not None:
            MemoryPolicyWriter.write_one(obj.memory_policy, writer, 'memory_policy')
        if obj.migration is not None:
            MigrationOptionsWriter.write_one(obj.migration, writer, 'migration')
        if obj.migration_downtime is not None:
            Writer.write_integer(writer, 'migration_downtime', obj.migration_downtime)
        if obj.multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'multi_queues_enabled', obj.multi_queues_enabled)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.next_run_configuration_exists is not None:
            Writer.write_boolean(writer, 'next_run_configuration_exists', obj.next_run_configuration_exists)
        if obj.numa_tune_mode is not None:
            Writer.write_string(writer, 'numa_tune_mode', obj.numa_tune_mode.value)
        if obj.origin is not None:
            Writer.write_string(writer, 'origin', obj.origin)
        if obj.os is not None:
            OperatingSystemWriter.write_one(obj.os, writer, 'os')
        if obj.payloads is not None:
            PayloadWriter.write_many(obj.payloads, writer, 'payload', 'payloads')
        if obj.persist_memorystate is not None:
            Writer.write_boolean(writer, 'persist_memorystate', obj.persist_memorystate)
        if obj.placement_policy is not None:
            VmPlacementPolicyWriter.write_one(obj.placement_policy, writer, 'placement_policy')
        if obj.rng_device is not None:
            RngDeviceWriter.write_one(obj.rng_device, writer, 'rng_device')
        if obj.run_once is not None:
            Writer.write_boolean(writer, 'run_once', obj.run_once)
        if obj.serial_number is not None:
            SerialNumberWriter.write_one(obj.serial_number, writer, 'serial_number')
        if obj.small_icon is not None:
            IconWriter.write_one(obj.small_icon, writer, 'small_icon')
        if obj.snapshot_status is not None:
            Writer.write_string(writer, 'snapshot_status', obj.snapshot_status.value)
        if obj.snapshot_type is not None:
            Writer.write_string(writer, 'snapshot_type', obj.snapshot_type.value)
        if obj.soundcard_enabled is not None:
            Writer.write_boolean(writer, 'soundcard_enabled', obj.soundcard_enabled)
        if obj.sso is not None:
            SsoWriter.write_one(obj.sso, writer, 'sso')
        if obj.start_paused is not None:
            Writer.write_boolean(writer, 'start_paused', obj.start_paused)
        if obj.start_time is not None:
            Writer.write_date(writer, 'start_time', obj.start_time)
        if obj.stateless is not None:
            Writer.write_boolean(writer, 'stateless', obj.stateless)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.status_detail is not None:
            Writer.write_string(writer, 'status_detail', obj.status_detail)
        if obj.stop_reason is not None:
            Writer.write_string(writer, 'stop_reason', obj.stop_reason)
        if obj.stop_time is not None:
            Writer.write_date(writer, 'stop_time', obj.stop_time)
        if obj.storage_error_resume_behaviour is not None:
            Writer.write_string(writer, 'storage_error_resume_behaviour', obj.storage_error_resume_behaviour.value)
        if obj.time_zone is not None:
            TimeZoneWriter.write_one(obj.time_zone, writer, 'time_zone')
        if obj.tpm_enabled is not None:
            Writer.write_boolean(writer, 'tpm_enabled', obj.tpm_enabled)
        if obj.tunnel_migration is not None:
            Writer.write_boolean(writer, 'tunnel_migration', obj.tunnel_migration)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.usb is not None:
            UsbWriter.write_one(obj.usb, writer, 'usb')
        if obj.use_latest_template_version is not None:
            Writer.write_boolean(writer, 'use_latest_template_version', obj.use_latest_template_version)
        if obj.virtio_scsi is not None:
            VirtioScsiWriter.write_one(obj.virtio_scsi, writer, 'virtio_scsi')
        if obj.virtio_scsi_multi_queues is not None:
            Writer.write_integer(writer, 'virtio_scsi_multi_queues', obj.virtio_scsi_multi_queues)
        if obj.virtio_scsi_multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'virtio_scsi_multi_queues_enabled', obj.virtio_scsi_multi_queues_enabled)
        if obj.affinity_labels is not None:
            AffinityLabelWriter.write_many(obj.affinity_labels, writer, 'affinity_label', 'affinity_labels')
        if obj.applications is not None:
            ApplicationWriter.write_many(obj.applications, writer, 'application', 'applications')
        if obj.cdroms is not None:
            CdromWriter.write_many(obj.cdroms, writer, 'cdrom', 'cdroms')
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.cpu_profile is not None:
            CpuProfileWriter.write_one(obj.cpu_profile, writer, 'cpu_profile')
        if obj.disk_attachments is not None:
            DiskAttachmentWriter.write_many(obj.disk_attachments, writer, 'disk_attachment', 'disk_attachments')
        if obj.disks is not None:
            DiskWriter.write_many(obj.disks, writer, 'disk', 'disks')
        if obj.external_host_provider is not None:
            ExternalHostProviderWriter.write_one(obj.external_host_provider, writer, 'external_host_provider')
        if obj.floppies is not None:
            FloppyWriter.write_many(obj.floppies, writer, 'floppy', 'floppies')
        if obj.graphics_consoles is not None:
            GraphicsConsoleWriter.write_many(obj.graphics_consoles, writer, 'graphics_console', 'graphics_consoles')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.host_devices is not None:
            HostDeviceWriter.write_many(obj.host_devices, writer, 'host_device', 'host_devices')
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.katello_errata is not None:
            KatelloErratumWriter.write_many(obj.katello_errata, writer, 'katello_erratum', 'katello_errata')
        if obj.nics is not None:
            NicWriter.write_many(obj.nics, writer, 'nic', 'nics')
        if obj.numa_nodes is not None:
            NumaNodeWriter.write_many(obj.numa_nodes, writer, 'host_numa_node', 'host_numa_nodes')
        if obj.original_template is not None:
            TemplateWriter.write_one(obj.original_template, writer, 'original_template')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.reported_devices is not None:
            ReportedDeviceWriter.write_many(obj.reported_devices, writer, 'reported_device', 'reported_devices')
        if obj.sessions is not None:
            SessionWriter.write_many(obj.sessions, writer, 'session', 'sessions')
        if obj.snapshots is not None:
            SnapshotWriter.write_many(obj.snapshots, writer, 'snapshot', 'snapshots')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.tags is not None:
            TagWriter.write_many(obj.tags, writer, 'tag', 'tags')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vm_pool is not None:
            VmPoolWriter.write_one(obj.vm_pool, writer, 'vm_pool')
        if obj.watchdogs is not None:
            WatchdogWriter.write_many(obj.watchdogs, writer, 'watchdog', 'watchdogs')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'snapshot'
        if plural is None:
            plural = 'snapshots'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SnapshotWriter.write_one(obj, writer, singular)
        writer.write_end()


class SpecialObjectsWriter(Writer):

    def __init__(self):
        super(SpecialObjectsWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'special_objects'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.blank_template is not None:
            TemplateWriter.write_one(obj.blank_template, writer, 'blank_template')
        if obj.root_tag is not None:
            TagWriter.write_one(obj.root_tag, writer, 'root_tag')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'special_objects'
        if plural is None:
            plural = 'special_objectss'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SpecialObjectsWriter.write_one(obj, writer, singular)
        writer.write_end()


class SpmWriter(Writer):

    def __init__(self):
        super(SpmWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'spm'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.priority is not None:
            Writer.write_integer(writer, 'priority', obj.priority)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'spm'
        if plural is None:
            plural = 'spms'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SpmWriter.write_one(obj, writer, singular)
        writer.write_end()


class SshWriter(Writer):

    def __init__(self):
        super(SshWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'ssh'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.authentication_method is not None:
            Writer.write_string(writer, 'authentication_method', obj.authentication_method.value)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.fingerprint is not None:
            Writer.write_string(writer, 'fingerprint', obj.fingerprint)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.public_key is not None:
            Writer.write_string(writer, 'public_key', obj.public_key)
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'ssh'
        if plural is None:
            plural = 'sshs'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SshWriter.write_one(obj, writer, singular)
        writer.write_end()


class SshPublicKeyWriter(Writer):

    def __init__(self):
        super(SshPublicKeyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'ssh_public_key'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.content is not None:
            Writer.write_string(writer, 'content', obj.content)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'ssh_public_key'
        if plural is None:
            plural = 'ssh_public_keys'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SshPublicKeyWriter.write_one(obj, writer, singular)
        writer.write_end()


class SsoWriter(Writer):

    def __init__(self):
        super(SsoWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'sso'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.methods is not None:
            MethodWriter.write_many(obj.methods, writer, 'method', 'methods')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'sso'
        if plural is None:
            plural = 'ssos'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SsoWriter.write_one(obj, writer, singular)
        writer.write_end()


class StatisticWriter(Writer):

    def __init__(self):
        super(StatisticWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'statistic'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.kind is not None:
            Writer.write_string(writer, 'kind', obj.kind.value)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.unit is not None:
            Writer.write_string(writer, 'unit', obj.unit.value)
        if obj.values is not None:
            ValueWriter.write_many(obj.values, writer, 'value', 'values')
        if obj.brick is not None:
            GlusterBrickWriter.write_one(obj.brick, writer, 'brick')
        if obj.disk is not None:
            DiskWriter.write_one(obj.disk, writer, 'disk')
        if obj.gluster_volume is not None:
            GlusterVolumeWriter.write_one(obj.gluster_volume, writer, 'gluster_volume')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.host_nic is not None:
            HostNicWriter.write_one(obj.host_nic, writer, 'host_nic')
        if obj.host_numa_node is not None:
            NumaNodeWriter.write_one(obj.host_numa_node, writer, 'host_numa_node')
        if obj.nic is not None:
            NicWriter.write_one(obj.nic, writer, 'nic')
        if obj.step is not None:
            StepWriter.write_one(obj.step, writer, 'step')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'statistic'
        if plural is None:
            plural = 'statistics'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            StatisticWriter.write_one(obj, writer, singular)
        writer.write_end()


class StepWriter(Writer):

    def __init__(self):
        super(StepWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'step'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.end_time is not None:
            Writer.write_date(writer, 'end_time', obj.end_time)
        if obj.external is not None:
            Writer.write_boolean(writer, 'external', obj.external)
        if obj.external_type is not None:
            Writer.write_string(writer, 'external_type', obj.external_type.value)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.number is not None:
            Writer.write_integer(writer, 'number', obj.number)
        if obj.progress is not None:
            Writer.write_integer(writer, 'progress', obj.progress)
        if obj.start_time is not None:
            Writer.write_date(writer, 'start_time', obj.start_time)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.execution_host is not None:
            HostWriter.write_one(obj.execution_host, writer, 'execution_host')
        if obj.job is not None:
            JobWriter.write_one(obj.job, writer, 'job')
        if obj.parent_step is not None:
            StepWriter.write_one(obj.parent_step, writer, 'parent_step')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'step'
        if plural is None:
            plural = 'steps'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            StepWriter.write_one(obj, writer, singular)
        writer.write_end()


class StorageConnectionWriter(Writer):

    def __init__(self):
        super(StorageConnectionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'storage_connection'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.address is not None:
            Writer.write_string(writer, 'address', obj.address)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.mount_options is not None:
            Writer.write_string(writer, 'mount_options', obj.mount_options)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.nfs_retrans is not None:
            Writer.write_integer(writer, 'nfs_retrans', obj.nfs_retrans)
        if obj.nfs_timeo is not None:
            Writer.write_integer(writer, 'nfs_timeo', obj.nfs_timeo)
        if obj.nfs_version is not None:
            Writer.write_string(writer, 'nfs_version', obj.nfs_version.value)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.path is not None:
            Writer.write_string(writer, 'path', obj.path)
        if obj.port is not None:
            Writer.write_integer(writer, 'port', obj.port)
        if obj.portal is not None:
            Writer.write_string(writer, 'portal', obj.portal)
        if obj.target is not None:
            Writer.write_string(writer, 'target', obj.target)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.vfs_type is not None:
            Writer.write_string(writer, 'vfs_type', obj.vfs_type)
        if obj.gluster_volume is not None:
            GlusterVolumeWriter.write_one(obj.gluster_volume, writer, 'gluster_volume')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'storage_connection'
        if plural is None:
            plural = 'storage_connections'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            StorageConnectionWriter.write_one(obj, writer, singular)
        writer.write_end()


class StorageConnectionExtensionWriter(Writer):

    def __init__(self):
        super(StorageConnectionExtensionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'storage_connection_extension'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.target is not None:
            Writer.write_string(writer, 'target', obj.target)
        if obj.username is not None:
            Writer.write_string(writer, 'username', obj.username)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'storage_connection_extension'
        if plural is None:
            plural = 'storage_connection_extensions'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            StorageConnectionExtensionWriter.write_one(obj, writer, singular)
        writer.write_end()


class StorageDomainWriter(Writer):

    def __init__(self):
        super(StorageDomainWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'storage_domain'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.available is not None:
            Writer.write_integer(writer, 'available', obj.available)
        if obj.backup is not None:
            Writer.write_boolean(writer, 'backup', obj.backup)
        if obj.block_size is not None:
            Writer.write_integer(writer, 'block_size', obj.block_size)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.committed is not None:
            Writer.write_integer(writer, 'committed', obj.committed)
        if obj.critical_space_action_blocker is not None:
            Writer.write_integer(writer, 'critical_space_action_blocker', obj.critical_space_action_blocker)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.discard_after_delete is not None:
            Writer.write_boolean(writer, 'discard_after_delete', obj.discard_after_delete)
        if obj.external_status is not None:
            Writer.write_string(writer, 'external_status', obj.external_status.value)
        if obj.import_ is not None:
            Writer.write_boolean(writer, 'import', obj.import_)
        if obj.master is not None:
            Writer.write_boolean(writer, 'master', obj.master)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.storage is not None:
            HostStorageWriter.write_one(obj.storage, writer, 'storage')
        if obj.storage_format is not None:
            Writer.write_string(writer, 'storage_format', obj.storage_format.value)
        if obj.supports_discard is not None:
            Writer.write_boolean(writer, 'supports_discard', obj.supports_discard)
        if obj.supports_discard_zeroes_data is not None:
            Writer.write_boolean(writer, 'supports_discard_zeroes_data', obj.supports_discard_zeroes_data)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.used is not None:
            Writer.write_integer(writer, 'used', obj.used)
        if obj.warning_low_space_indicator is not None:
            Writer.write_integer(writer, 'warning_low_space_indicator', obj.warning_low_space_indicator)
        if obj.wipe_after_delete is not None:
            Writer.write_boolean(writer, 'wipe_after_delete', obj.wipe_after_delete)
        if obj.data_center is not None:
            DataCenterWriter.write_one(obj.data_center, writer, 'data_center')
        if obj.data_centers is not None:
            DataCenterWriter.write_many(obj.data_centers, writer, 'data_center', 'data_centers')
        if obj.disk_profiles is not None:
            DiskProfileWriter.write_many(obj.disk_profiles, writer, 'disk_profile', 'disk_profiles')
        if obj.disk_snapshots is not None:
            DiskSnapshotWriter.write_many(obj.disk_snapshots, writer, 'disk_snapshot', 'disk_snapshots')
        if obj.disks is not None:
            DiskWriter.write_many(obj.disks, writer, 'disk', 'disks')
        if obj.files is not None:
            FileWriter.write_many(obj.files, writer, 'file', 'files')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.images is not None:
            ImageWriter.write_many(obj.images, writer, 'image', 'images')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.storage_connections is not None:
            StorageConnectionWriter.write_many(obj.storage_connections, writer, 'storage_connection', 'storage_connections')
        if obj.templates is not None:
            TemplateWriter.write_many(obj.templates, writer, 'template', 'templates')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'storage_domain'
        if plural is None:
            plural = 'storage_domains'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            StorageDomainWriter.write_one(obj, writer, singular)
        writer.write_end()


class StorageDomainLeaseWriter(Writer):

    def __init__(self):
        super(StorageDomainLeaseWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'storage_domain_lease'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'storage_domain_lease'
        if plural is None:
            plural = 'storage_domain_leases'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            StorageDomainLeaseWriter.write_one(obj, writer, singular)
        writer.write_end()


class SystemOptionWriter(Writer):

    def __init__(self):
        super(SystemOptionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'system_option'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.values is not None:
            SystemOptionValueWriter.write_many(obj.values, writer, 'system_option_value', 'values')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'system_option'
        if plural is None:
            plural = 'system_options'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SystemOptionWriter.write_one(obj, writer, singular)
        writer.write_end()


class SystemOptionValueWriter(Writer):

    def __init__(self):
        super(SystemOptionValueWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'system_option_value'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        if obj.version is not None:
            Writer.write_string(writer, 'version', obj.version)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'system_option_value'
        if plural is None:
            plural = 'system_option_values'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            SystemOptionValueWriter.write_one(obj, writer, singular)
        writer.write_end()


class TagWriter(Writer):

    def __init__(self):
        super(TagWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'tag'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.group is not None:
            GroupWriter.write_one(obj.group, writer, 'group')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.parent is not None:
            TagWriter.write_one(obj.parent, writer, 'parent')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'tag'
        if plural is None:
            plural = 'tags'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            TagWriter.write_one(obj, writer, singular)
        writer.write_end()


class TemplateWriter(Writer):

    def __init__(self):
        super(TemplateWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'template'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.auto_pinning_policy is not None:
            Writer.write_string(writer, 'auto_pinning_policy', obj.auto_pinning_policy.value)
        if obj.bios is not None:
            BiosWriter.write_one(obj.bios, writer, 'bios')
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.console is not None:
            ConsoleWriter.write_one(obj.console, writer, 'console')
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.cpu_shares is not None:
            Writer.write_integer(writer, 'cpu_shares', obj.cpu_shares)
        if obj.creation_time is not None:
            Writer.write_date(writer, 'creation_time', obj.creation_time)
        if obj.custom_compatibility_version is not None:
            VersionWriter.write_one(obj.custom_compatibility_version, writer, 'custom_compatibility_version')
        if obj.custom_cpu_model is not None:
            Writer.write_string(writer, 'custom_cpu_model', obj.custom_cpu_model)
        if obj.custom_emulated_machine is not None:
            Writer.write_string(writer, 'custom_emulated_machine', obj.custom_emulated_machine)
        if obj.custom_properties is not None:
            CustomPropertyWriter.write_many(obj.custom_properties, writer, 'custom_property', 'custom_properties')
        if obj.delete_protected is not None:
            Writer.write_boolean(writer, 'delete_protected', obj.delete_protected)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.display is not None:
            DisplayWriter.write_one(obj.display, writer, 'display')
        if obj.domain is not None:
            DomainWriter.write_one(obj.domain, writer, 'domain')
        if obj.high_availability is not None:
            HighAvailabilityWriter.write_one(obj.high_availability, writer, 'high_availability')
        if obj.initialization is not None:
            InitializationWriter.write_one(obj.initialization, writer, 'initialization')
        if obj.io is not None:
            IoWriter.write_one(obj.io, writer, 'io')
        if obj.large_icon is not None:
            IconWriter.write_one(obj.large_icon, writer, 'large_icon')
        if obj.lease is not None:
            StorageDomainLeaseWriter.write_one(obj.lease, writer, 'lease')
        if obj.memory is not None:
            Writer.write_integer(writer, 'memory', obj.memory)
        if obj.memory_policy is not None:
            MemoryPolicyWriter.write_one(obj.memory_policy, writer, 'memory_policy')
        if obj.migration is not None:
            MigrationOptionsWriter.write_one(obj.migration, writer, 'migration')
        if obj.migration_downtime is not None:
            Writer.write_integer(writer, 'migration_downtime', obj.migration_downtime)
        if obj.multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'multi_queues_enabled', obj.multi_queues_enabled)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.origin is not None:
            Writer.write_string(writer, 'origin', obj.origin)
        if obj.os is not None:
            OperatingSystemWriter.write_one(obj.os, writer, 'os')
        if obj.placement_policy is not None:
            VmPlacementPolicyWriter.write_one(obj.placement_policy, writer, 'placement_policy')
        if obj.rng_device is not None:
            RngDeviceWriter.write_one(obj.rng_device, writer, 'rng_device')
        if obj.serial_number is not None:
            SerialNumberWriter.write_one(obj.serial_number, writer, 'serial_number')
        if obj.small_icon is not None:
            IconWriter.write_one(obj.small_icon, writer, 'small_icon')
        if obj.soundcard_enabled is not None:
            Writer.write_boolean(writer, 'soundcard_enabled', obj.soundcard_enabled)
        if obj.sso is not None:
            SsoWriter.write_one(obj.sso, writer, 'sso')
        if obj.start_paused is not None:
            Writer.write_boolean(writer, 'start_paused', obj.start_paused)
        if obj.stateless is not None:
            Writer.write_boolean(writer, 'stateless', obj.stateless)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.storage_error_resume_behaviour is not None:
            Writer.write_string(writer, 'storage_error_resume_behaviour', obj.storage_error_resume_behaviour.value)
        if obj.time_zone is not None:
            TimeZoneWriter.write_one(obj.time_zone, writer, 'time_zone')
        if obj.tpm_enabled is not None:
            Writer.write_boolean(writer, 'tpm_enabled', obj.tpm_enabled)
        if obj.tunnel_migration is not None:
            Writer.write_boolean(writer, 'tunnel_migration', obj.tunnel_migration)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.usb is not None:
            UsbWriter.write_one(obj.usb, writer, 'usb')
        if obj.version is not None:
            TemplateVersionWriter.write_one(obj.version, writer, 'version')
        if obj.virtio_scsi is not None:
            VirtioScsiWriter.write_one(obj.virtio_scsi, writer, 'virtio_scsi')
        if obj.virtio_scsi_multi_queues is not None:
            Writer.write_integer(writer, 'virtio_scsi_multi_queues', obj.virtio_scsi_multi_queues)
        if obj.virtio_scsi_multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'virtio_scsi_multi_queues_enabled', obj.virtio_scsi_multi_queues_enabled)
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.cdroms is not None:
            CdromWriter.write_many(obj.cdroms, writer, 'cdrom', 'cdroms')
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.cpu_profile is not None:
            CpuProfileWriter.write_one(obj.cpu_profile, writer, 'cpu_profile')
        if obj.disk_attachments is not None:
            DiskAttachmentWriter.write_many(obj.disk_attachments, writer, 'disk_attachment', 'disk_attachments')
        if obj.graphics_consoles is not None:
            GraphicsConsoleWriter.write_many(obj.graphics_consoles, writer, 'graphics_console', 'graphics_consoles')
        if obj.nics is not None:
            NicWriter.write_many(obj.nics, writer, 'nic', 'nics')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.tags is not None:
            TagWriter.write_many(obj.tags, writer, 'tag', 'tags')
        if obj.watchdogs is not None:
            WatchdogWriter.write_many(obj.watchdogs, writer, 'watchdog', 'watchdogs')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'template'
        if plural is None:
            plural = 'templates'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            TemplateWriter.write_one(obj, writer, singular)
        writer.write_end()


class TemplateVersionWriter(Writer):

    def __init__(self):
        super(TemplateVersionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'template_version'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.version_name is not None:
            Writer.write_string(writer, 'version_name', obj.version_name)
        if obj.version_number is not None:
            Writer.write_integer(writer, 'version_number', obj.version_number)
        if obj.base_template is not None:
            TemplateWriter.write_one(obj.base_template, writer, 'base_template')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'template_version'
        if plural is None:
            plural = 'template_versions'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            TemplateVersionWriter.write_one(obj, writer, singular)
        writer.write_end()


class TicketWriter(Writer):

    def __init__(self):
        super(TicketWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'ticket'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.expiry is not None:
            Writer.write_integer(writer, 'expiry', obj.expiry)
        if obj.value is not None:
            Writer.write_string(writer, 'value', obj.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'ticket'
        if plural is None:
            plural = 'tickets'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            TicketWriter.write_one(obj, writer, singular)
        writer.write_end()


class TimeZoneWriter(Writer):

    def __init__(self):
        super(TimeZoneWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'time_zone'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.utc_offset is not None:
            Writer.write_string(writer, 'utc_offset', obj.utc_offset)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'time_zone'
        if plural is None:
            plural = 'time_zones'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            TimeZoneWriter.write_one(obj, writer, singular)
        writer.write_end()


class TransparentHugePagesWriter(Writer):

    def __init__(self):
        super(TransparentHugePagesWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'transparent_hugepages'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'transparent_hugepages'
        if plural is None:
            plural = 'transparent_huge_pagess'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            TransparentHugePagesWriter.write_one(obj, writer, singular)
        writer.write_end()


class UnmanagedNetworkWriter(Writer):

    def __init__(self):
        super(UnmanagedNetworkWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'unmanaged_network'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.host_nic is not None:
            HostNicWriter.write_one(obj.host_nic, writer, 'host_nic')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'unmanaged_network'
        if plural is None:
            plural = 'unmanaged_networks'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            UnmanagedNetworkWriter.write_one(obj, writer, singular)
        writer.write_end()


class UsbWriter(Writer):

    def __init__(self):
        super(UsbWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'usb'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'usb'
        if plural is None:
            plural = 'usbs'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            UsbWriter.write_one(obj, writer, singular)
        writer.write_end()


class UserWriter(Writer):

    def __init__(self):
        super(UserWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'user'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.department is not None:
            Writer.write_string(writer, 'department', obj.department)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.domain_entry_id is not None:
            Writer.write_string(writer, 'domain_entry_id', obj.domain_entry_id)
        if obj.email is not None:
            Writer.write_string(writer, 'email', obj.email)
        if obj.last_name is not None:
            Writer.write_string(writer, 'last_name', obj.last_name)
        if obj.logged_in is not None:
            Writer.write_boolean(writer, 'logged_in', obj.logged_in)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.namespace is not None:
            Writer.write_string(writer, 'namespace', obj.namespace)
        if obj.password is not None:
            Writer.write_string(writer, 'password', obj.password)
        if obj.principal is not None:
            Writer.write_string(writer, 'principal', obj.principal)
        if obj.user_name is not None:
            Writer.write_string(writer, 'user_name', obj.user_name)
        if obj.user_options is not None:
            PropertyWriter.write_many(obj.user_options, writer, 'property', 'user_options')
        if obj.domain is not None:
            DomainWriter.write_one(obj.domain, writer, 'domain')
        if obj.groups is not None:
            GroupWriter.write_many(obj.groups, writer, 'group', 'groups')
        if obj.options is not None:
            UserOptionWriter.write_many(obj.options, writer, 'user_option', 'options')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.roles is not None:
            RoleWriter.write_many(obj.roles, writer, 'role', 'roles')
        if obj.ssh_public_keys is not None:
            SshPublicKeyWriter.write_many(obj.ssh_public_keys, writer, 'ssh_public_key', 'ssh_public_keys')
        if obj.tags is not None:
            TagWriter.write_many(obj.tags, writer, 'tag', 'tags')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'user'
        if plural is None:
            plural = 'users'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            UserWriter.write_one(obj, writer, singular)
        writer.write_end()


class UserOptionWriter(Writer):

    def __init__(self):
        super(UserOptionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'user_option'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.content is not None:
            Writer.write_string(writer, 'content', obj.content)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.user is not None:
            UserWriter.write_one(obj.user, writer, 'user')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'user_option'
        if plural is None:
            plural = 'user_options'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            UserOptionWriter.write_one(obj, writer, singular)
        writer.write_end()


class ValueWriter(Writer):

    def __init__(self):
        super(ValueWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'value'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.datum is not None:
            Writer.write_decimal(writer, 'datum', obj.datum)
        if obj.detail is not None:
            Writer.write_string(writer, 'detail', obj.detail)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'value'
        if plural is None:
            plural = 'values'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            ValueWriter.write_one(obj, writer, singular)
        writer.write_end()


class VcpuPinWriter(Writer):

    def __init__(self):
        super(VcpuPinWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vcpu_pin'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.cpu_set is not None:
            Writer.write_string(writer, 'cpu_set', obj.cpu_set)
        if obj.vcpu is not None:
            Writer.write_integer(writer, 'vcpu', obj.vcpu)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vcpu_pin'
        if plural is None:
            plural = 'vcpu_pins'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VcpuPinWriter.write_one(obj, writer, singular)
        writer.write_end()


class VendorWriter(Writer):

    def __init__(self):
        super(VendorWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vendor'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vendor'
        if plural is None:
            plural = 'vendors'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VendorWriter.write_one(obj, writer, singular)
        writer.write_end()


class VersionWriter(Writer):

    def __init__(self):
        super(VersionWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'version'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.build is not None:
            Writer.write_integer(writer, 'build', obj.build)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.full_version is not None:
            Writer.write_string(writer, 'full_version', obj.full_version)
        if obj.major is not None:
            Writer.write_integer(writer, 'major', obj.major)
        if obj.minor is not None:
            Writer.write_integer(writer, 'minor', obj.minor)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.revision is not None:
            Writer.write_integer(writer, 'revision', obj.revision)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'version'
        if plural is None:
            plural = 'versions'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VersionWriter.write_one(obj, writer, singular)
        writer.write_end()


class VirtioScsiWriter(Writer):

    def __init__(self):
        super(VirtioScsiWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'virtio_scsi'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.enabled is not None:
            Writer.write_boolean(writer, 'enabled', obj.enabled)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'virtio_scsi'
        if plural is None:
            plural = 'virtio_scsis'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VirtioScsiWriter.write_one(obj, writer, singular)
        writer.write_end()


class VirtualNumaNodeWriter(Writer):

    def __init__(self):
        super(VirtualNumaNodeWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vm_numa_node'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.index is not None:
            Writer.write_integer(writer, 'index', obj.index)
        if obj.memory is not None:
            Writer.write_integer(writer, 'memory', obj.memory)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.node_distance is not None:
            Writer.write_string(writer, 'node_distance', obj.node_distance)
        if obj.numa_node_pins is not None:
            NumaNodePinWriter.write_many(obj.numa_node_pins, writer, 'numa_node_pin', 'numa_node_pins')
        if obj.numa_tune_mode is not None:
            Writer.write_string(writer, 'numa_tune_mode', obj.numa_tune_mode.value)
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vm_numa_node'
        if plural is None:
            plural = 'vm_numa_nodes'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VirtualNumaNodeWriter.write_one(obj, writer, singular)
        writer.write_end()


class VlanWriter(Writer):

    def __init__(self):
        super(VlanWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vlan'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', str(obj.id))
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vlan'
        if plural is None:
            plural = 'vlans'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VlanWriter.write_one(obj, writer, singular)
        writer.write_end()


class VmWriter(Writer):

    def __init__(self):
        super(VmWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vm'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.auto_pinning_policy is not None:
            Writer.write_string(writer, 'auto_pinning_policy', obj.auto_pinning_policy.value)
        if obj.bios is not None:
            BiosWriter.write_one(obj.bios, writer, 'bios')
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.console is not None:
            ConsoleWriter.write_one(obj.console, writer, 'console')
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.cpu_shares is not None:
            Writer.write_integer(writer, 'cpu_shares', obj.cpu_shares)
        if obj.creation_time is not None:
            Writer.write_date(writer, 'creation_time', obj.creation_time)
        if obj.custom_compatibility_version is not None:
            VersionWriter.write_one(obj.custom_compatibility_version, writer, 'custom_compatibility_version')
        if obj.custom_cpu_model is not None:
            Writer.write_string(writer, 'custom_cpu_model', obj.custom_cpu_model)
        if obj.custom_emulated_machine is not None:
            Writer.write_string(writer, 'custom_emulated_machine', obj.custom_emulated_machine)
        if obj.custom_properties is not None:
            CustomPropertyWriter.write_many(obj.custom_properties, writer, 'custom_property', 'custom_properties')
        if obj.delete_protected is not None:
            Writer.write_boolean(writer, 'delete_protected', obj.delete_protected)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.display is not None:
            DisplayWriter.write_one(obj.display, writer, 'display')
        if obj.domain is not None:
            DomainWriter.write_one(obj.domain, writer, 'domain')
        if obj.fqdn is not None:
            Writer.write_string(writer, 'fqdn', obj.fqdn)
        if obj.guest_operating_system is not None:
            GuestOperatingSystemWriter.write_one(obj.guest_operating_system, writer, 'guest_operating_system')
        if obj.guest_time_zone is not None:
            TimeZoneWriter.write_one(obj.guest_time_zone, writer, 'guest_time_zone')
        if obj.has_illegal_images is not None:
            Writer.write_boolean(writer, 'has_illegal_images', obj.has_illegal_images)
        if obj.high_availability is not None:
            HighAvailabilityWriter.write_one(obj.high_availability, writer, 'high_availability')
        if obj.initialization is not None:
            InitializationWriter.write_one(obj.initialization, writer, 'initialization')
        if obj.io is not None:
            IoWriter.write_one(obj.io, writer, 'io')
        if obj.large_icon is not None:
            IconWriter.write_one(obj.large_icon, writer, 'large_icon')
        if obj.lease is not None:
            StorageDomainLeaseWriter.write_one(obj.lease, writer, 'lease')
        if obj.memory is not None:
            Writer.write_integer(writer, 'memory', obj.memory)
        if obj.memory_policy is not None:
            MemoryPolicyWriter.write_one(obj.memory_policy, writer, 'memory_policy')
        if obj.migration is not None:
            MigrationOptionsWriter.write_one(obj.migration, writer, 'migration')
        if obj.migration_downtime is not None:
            Writer.write_integer(writer, 'migration_downtime', obj.migration_downtime)
        if obj.multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'multi_queues_enabled', obj.multi_queues_enabled)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.next_run_configuration_exists is not None:
            Writer.write_boolean(writer, 'next_run_configuration_exists', obj.next_run_configuration_exists)
        if obj.numa_tune_mode is not None:
            Writer.write_string(writer, 'numa_tune_mode', obj.numa_tune_mode.value)
        if obj.origin is not None:
            Writer.write_string(writer, 'origin', obj.origin)
        if obj.os is not None:
            OperatingSystemWriter.write_one(obj.os, writer, 'os')
        if obj.payloads is not None:
            PayloadWriter.write_many(obj.payloads, writer, 'payload', 'payloads')
        if obj.placement_policy is not None:
            VmPlacementPolicyWriter.write_one(obj.placement_policy, writer, 'placement_policy')
        if obj.rng_device is not None:
            RngDeviceWriter.write_one(obj.rng_device, writer, 'rng_device')
        if obj.run_once is not None:
            Writer.write_boolean(writer, 'run_once', obj.run_once)
        if obj.serial_number is not None:
            SerialNumberWriter.write_one(obj.serial_number, writer, 'serial_number')
        if obj.small_icon is not None:
            IconWriter.write_one(obj.small_icon, writer, 'small_icon')
        if obj.soundcard_enabled is not None:
            Writer.write_boolean(writer, 'soundcard_enabled', obj.soundcard_enabled)
        if obj.sso is not None:
            SsoWriter.write_one(obj.sso, writer, 'sso')
        if obj.start_paused is not None:
            Writer.write_boolean(writer, 'start_paused', obj.start_paused)
        if obj.start_time is not None:
            Writer.write_date(writer, 'start_time', obj.start_time)
        if obj.stateless is not None:
            Writer.write_boolean(writer, 'stateless', obj.stateless)
        if obj.status is not None:
            Writer.write_string(writer, 'status', obj.status.value)
        if obj.status_detail is not None:
            Writer.write_string(writer, 'status_detail', obj.status_detail)
        if obj.stop_reason is not None:
            Writer.write_string(writer, 'stop_reason', obj.stop_reason)
        if obj.stop_time is not None:
            Writer.write_date(writer, 'stop_time', obj.stop_time)
        if obj.storage_error_resume_behaviour is not None:
            Writer.write_string(writer, 'storage_error_resume_behaviour', obj.storage_error_resume_behaviour.value)
        if obj.time_zone is not None:
            TimeZoneWriter.write_one(obj.time_zone, writer, 'time_zone')
        if obj.tpm_enabled is not None:
            Writer.write_boolean(writer, 'tpm_enabled', obj.tpm_enabled)
        if obj.tunnel_migration is not None:
            Writer.write_boolean(writer, 'tunnel_migration', obj.tunnel_migration)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.usb is not None:
            UsbWriter.write_one(obj.usb, writer, 'usb')
        if obj.use_latest_template_version is not None:
            Writer.write_boolean(writer, 'use_latest_template_version', obj.use_latest_template_version)
        if obj.virtio_scsi is not None:
            VirtioScsiWriter.write_one(obj.virtio_scsi, writer, 'virtio_scsi')
        if obj.virtio_scsi_multi_queues is not None:
            Writer.write_integer(writer, 'virtio_scsi_multi_queues', obj.virtio_scsi_multi_queues)
        if obj.virtio_scsi_multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'virtio_scsi_multi_queues_enabled', obj.virtio_scsi_multi_queues_enabled)
        if obj.affinity_labels is not None:
            AffinityLabelWriter.write_many(obj.affinity_labels, writer, 'affinity_label', 'affinity_labels')
        if obj.applications is not None:
            ApplicationWriter.write_many(obj.applications, writer, 'application', 'applications')
        if obj.cdroms is not None:
            CdromWriter.write_many(obj.cdroms, writer, 'cdrom', 'cdroms')
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.cpu_profile is not None:
            CpuProfileWriter.write_one(obj.cpu_profile, writer, 'cpu_profile')
        if obj.disk_attachments is not None:
            DiskAttachmentWriter.write_many(obj.disk_attachments, writer, 'disk_attachment', 'disk_attachments')
        if obj.external_host_provider is not None:
            ExternalHostProviderWriter.write_one(obj.external_host_provider, writer, 'external_host_provider')
        if obj.floppies is not None:
            FloppyWriter.write_many(obj.floppies, writer, 'floppy', 'floppies')
        if obj.graphics_consoles is not None:
            GraphicsConsoleWriter.write_many(obj.graphics_consoles, writer, 'graphics_console', 'graphics_consoles')
        if obj.host is not None:
            HostWriter.write_one(obj.host, writer, 'host')
        if obj.host_devices is not None:
            HostDeviceWriter.write_many(obj.host_devices, writer, 'host_device', 'host_devices')
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.katello_errata is not None:
            KatelloErratumWriter.write_many(obj.katello_errata, writer, 'katello_erratum', 'katello_errata')
        if obj.nics is not None:
            NicWriter.write_many(obj.nics, writer, 'nic', 'nics')
        if obj.numa_nodes is not None:
            NumaNodeWriter.write_many(obj.numa_nodes, writer, 'host_numa_node', 'host_numa_nodes')
        if obj.original_template is not None:
            TemplateWriter.write_one(obj.original_template, writer, 'original_template')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.reported_devices is not None:
            ReportedDeviceWriter.write_many(obj.reported_devices, writer, 'reported_device', 'reported_devices')
        if obj.sessions is not None:
            SessionWriter.write_many(obj.sessions, writer, 'session', 'sessions')
        if obj.snapshots is not None:
            SnapshotWriter.write_many(obj.snapshots, writer, 'snapshot', 'snapshots')
        if obj.statistics is not None:
            StatisticWriter.write_many(obj.statistics, writer, 'statistic', 'statistics')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        if obj.tags is not None:
            TagWriter.write_many(obj.tags, writer, 'tag', 'tags')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm_pool is not None:
            VmPoolWriter.write_one(obj.vm_pool, writer, 'vm_pool')
        if obj.watchdogs is not None:
            WatchdogWriter.write_many(obj.watchdogs, writer, 'watchdog', 'watchdogs')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vm'
        if plural is None:
            plural = 'vms'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VmWriter.write_one(obj, writer, singular)
        writer.write_end()


class VmBaseWriter(Writer):

    def __init__(self):
        super(VmBaseWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vm_base'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.auto_pinning_policy is not None:
            Writer.write_string(writer, 'auto_pinning_policy', obj.auto_pinning_policy.value)
        if obj.bios is not None:
            BiosWriter.write_one(obj.bios, writer, 'bios')
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.console is not None:
            ConsoleWriter.write_one(obj.console, writer, 'console')
        if obj.cpu is not None:
            CpuWriter.write_one(obj.cpu, writer, 'cpu')
        if obj.cpu_shares is not None:
            Writer.write_integer(writer, 'cpu_shares', obj.cpu_shares)
        if obj.creation_time is not None:
            Writer.write_date(writer, 'creation_time', obj.creation_time)
        if obj.custom_compatibility_version is not None:
            VersionWriter.write_one(obj.custom_compatibility_version, writer, 'custom_compatibility_version')
        if obj.custom_cpu_model is not None:
            Writer.write_string(writer, 'custom_cpu_model', obj.custom_cpu_model)
        if obj.custom_emulated_machine is not None:
            Writer.write_string(writer, 'custom_emulated_machine', obj.custom_emulated_machine)
        if obj.custom_properties is not None:
            CustomPropertyWriter.write_many(obj.custom_properties, writer, 'custom_property', 'custom_properties')
        if obj.delete_protected is not None:
            Writer.write_boolean(writer, 'delete_protected', obj.delete_protected)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.display is not None:
            DisplayWriter.write_one(obj.display, writer, 'display')
        if obj.domain is not None:
            DomainWriter.write_one(obj.domain, writer, 'domain')
        if obj.high_availability is not None:
            HighAvailabilityWriter.write_one(obj.high_availability, writer, 'high_availability')
        if obj.initialization is not None:
            InitializationWriter.write_one(obj.initialization, writer, 'initialization')
        if obj.io is not None:
            IoWriter.write_one(obj.io, writer, 'io')
        if obj.large_icon is not None:
            IconWriter.write_one(obj.large_icon, writer, 'large_icon')
        if obj.lease is not None:
            StorageDomainLeaseWriter.write_one(obj.lease, writer, 'lease')
        if obj.memory is not None:
            Writer.write_integer(writer, 'memory', obj.memory)
        if obj.memory_policy is not None:
            MemoryPolicyWriter.write_one(obj.memory_policy, writer, 'memory_policy')
        if obj.migration is not None:
            MigrationOptionsWriter.write_one(obj.migration, writer, 'migration')
        if obj.migration_downtime is not None:
            Writer.write_integer(writer, 'migration_downtime', obj.migration_downtime)
        if obj.multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'multi_queues_enabled', obj.multi_queues_enabled)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.origin is not None:
            Writer.write_string(writer, 'origin', obj.origin)
        if obj.os is not None:
            OperatingSystemWriter.write_one(obj.os, writer, 'os')
        if obj.placement_policy is not None:
            VmPlacementPolicyWriter.write_one(obj.placement_policy, writer, 'placement_policy')
        if obj.rng_device is not None:
            RngDeviceWriter.write_one(obj.rng_device, writer, 'rng_device')
        if obj.serial_number is not None:
            SerialNumberWriter.write_one(obj.serial_number, writer, 'serial_number')
        if obj.small_icon is not None:
            IconWriter.write_one(obj.small_icon, writer, 'small_icon')
        if obj.soundcard_enabled is not None:
            Writer.write_boolean(writer, 'soundcard_enabled', obj.soundcard_enabled)
        if obj.sso is not None:
            SsoWriter.write_one(obj.sso, writer, 'sso')
        if obj.start_paused is not None:
            Writer.write_boolean(writer, 'start_paused', obj.start_paused)
        if obj.stateless is not None:
            Writer.write_boolean(writer, 'stateless', obj.stateless)
        if obj.storage_error_resume_behaviour is not None:
            Writer.write_string(writer, 'storage_error_resume_behaviour', obj.storage_error_resume_behaviour.value)
        if obj.time_zone is not None:
            TimeZoneWriter.write_one(obj.time_zone, writer, 'time_zone')
        if obj.tpm_enabled is not None:
            Writer.write_boolean(writer, 'tpm_enabled', obj.tpm_enabled)
        if obj.tunnel_migration is not None:
            Writer.write_boolean(writer, 'tunnel_migration', obj.tunnel_migration)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.usb is not None:
            UsbWriter.write_one(obj.usb, writer, 'usb')
        if obj.virtio_scsi is not None:
            VirtioScsiWriter.write_one(obj.virtio_scsi, writer, 'virtio_scsi')
        if obj.virtio_scsi_multi_queues is not None:
            Writer.write_integer(writer, 'virtio_scsi_multi_queues', obj.virtio_scsi_multi_queues)
        if obj.virtio_scsi_multi_queues_enabled is not None:
            Writer.write_boolean(writer, 'virtio_scsi_multi_queues_enabled', obj.virtio_scsi_multi_queues_enabled)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.cpu_profile is not None:
            CpuProfileWriter.write_one(obj.cpu_profile, writer, 'cpu_profile')
        if obj.quota is not None:
            QuotaWriter.write_one(obj.quota, writer, 'quota')
        if obj.storage_domain is not None:
            StorageDomainWriter.write_one(obj.storage_domain, writer, 'storage_domain')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vm_base'
        if plural is None:
            plural = 'vm_bases'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VmBaseWriter.write_one(obj, writer, singular)
        writer.write_end()


class VmPlacementPolicyWriter(Writer):

    def __init__(self):
        super(VmPlacementPolicyWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vm_placement_policy'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.affinity is not None:
            Writer.write_string(writer, 'affinity', obj.affinity.value)
        if obj.hosts is not None:
            HostWriter.write_many(obj.hosts, writer, 'host', 'hosts')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vm_placement_policy'
        if plural is None:
            plural = 'vm_placement_policies'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VmPlacementPolicyWriter.write_one(obj, writer, singular)
        writer.write_end()


class VmPoolWriter(Writer):

    def __init__(self):
        super(VmPoolWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vm_pool'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.auto_storage_select is not None:
            Writer.write_boolean(writer, 'auto_storage_select', obj.auto_storage_select)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.display is not None:
            DisplayWriter.write_one(obj.display, writer, 'display')
        if obj.max_user_vms is not None:
            Writer.write_integer(writer, 'max_user_vms', obj.max_user_vms)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.prestarted_vms is not None:
            Writer.write_integer(writer, 'prestarted_vms', obj.prestarted_vms)
        if obj.rng_device is not None:
            RngDeviceWriter.write_one(obj.rng_device, writer, 'rng_device')
        if obj.size is not None:
            Writer.write_integer(writer, 'size', obj.size)
        if obj.soundcard_enabled is not None:
            Writer.write_boolean(writer, 'soundcard_enabled', obj.soundcard_enabled)
        if obj.stateful is not None:
            Writer.write_boolean(writer, 'stateful', obj.stateful)
        if obj.tpm_enabled is not None:
            Writer.write_boolean(writer, 'tpm_enabled', obj.tpm_enabled)
        if obj.type is not None:
            Writer.write_string(writer, 'type', obj.type.value)
        if obj.use_latest_template_version is not None:
            Writer.write_boolean(writer, 'use_latest_template_version', obj.use_latest_template_version)
        if obj.cluster is not None:
            ClusterWriter.write_one(obj.cluster, writer, 'cluster')
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vm_pool'
        if plural is None:
            plural = 'vm_pools'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VmPoolWriter.write_one(obj, writer, singular)
        writer.write_end()


class VmSummaryWriter(Writer):

    def __init__(self):
        super(VmSummaryWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vm_summary'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.active is not None:
            Writer.write_integer(writer, 'active', obj.active)
        if obj.migrating is not None:
            Writer.write_integer(writer, 'migrating', obj.migrating)
        if obj.total is not None:
            Writer.write_integer(writer, 'total', obj.total)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vm_summary'
        if plural is None:
            plural = 'vm_summaries'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VmSummaryWriter.write_one(obj, writer, singular)
        writer.write_end()


class VnicPassThroughWriter(Writer):

    def __init__(self):
        super(VnicPassThroughWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vnic_pass_through'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.mode is not None:
            Writer.write_string(writer, 'mode', obj.mode.value)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vnic_pass_through'
        if plural is None:
            plural = 'vnic_pass_throughs'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VnicPassThroughWriter.write_one(obj, writer, singular)
        writer.write_end()


class VnicProfileWriter(Writer):

    def __init__(self):
        super(VnicProfileWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vnic_profile'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.custom_properties is not None:
            CustomPropertyWriter.write_many(obj.custom_properties, writer, 'custom_property', 'custom_properties')
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.migratable is not None:
            Writer.write_boolean(writer, 'migratable', obj.migratable)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.pass_through is not None:
            VnicPassThroughWriter.write_one(obj.pass_through, writer, 'pass_through')
        if obj.port_mirroring is not None:
            Writer.write_boolean(writer, 'port_mirroring', obj.port_mirroring)
        if obj.failover is not None:
            VnicProfileWriter.write_one(obj.failover, writer, 'failover')
        if obj.network is not None:
            NetworkWriter.write_one(obj.network, writer, 'network')
        if obj.network_filter is not None:
            NetworkFilterWriter.write_one(obj.network_filter, writer, 'network_filter')
        if obj.permissions is not None:
            PermissionWriter.write_many(obj.permissions, writer, 'permission', 'permissions')
        if obj.qos is not None:
            QosWriter.write_one(obj.qos, writer, 'qos')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vnic_profile'
        if plural is None:
            plural = 'vnic_profiles'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VnicProfileWriter.write_one(obj, writer, singular)
        writer.write_end()


class VnicProfileMappingWriter(Writer):

    def __init__(self):
        super(VnicProfileMappingWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'vnic_profile_mapping'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.source_network_name is not None:
            Writer.write_string(writer, 'source_network_name', obj.source_network_name)
        if obj.source_network_profile_name is not None:
            Writer.write_string(writer, 'source_network_profile_name', obj.source_network_profile_name)
        if obj.target_vnic_profile is not None:
            VnicProfileWriter.write_one(obj.target_vnic_profile, writer, 'target_vnic_profile')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'vnic_profile_mapping'
        if plural is None:
            plural = 'vnic_profile_mappings'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VnicProfileMappingWriter.write_one(obj, writer, singular)
        writer.write_end()


class VolumeGroupWriter(Writer):

    def __init__(self):
        super(VolumeGroupWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'volume_group'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.logical_units is not None:
            LogicalUnitWriter.write_many(obj.logical_units, writer, 'logical_unit', 'logical_units')
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'volume_group'
        if plural is None:
            plural = 'volume_groups'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            VolumeGroupWriter.write_one(obj, writer, singular)
        writer.write_end()


class WatchdogWriter(Writer):

    def __init__(self):
        super(WatchdogWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'watchdog'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.action is not None:
            Writer.write_string(writer, 'action', obj.action.value)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.model is not None:
            Writer.write_string(writer, 'model', obj.model.value)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.instance_type is not None:
            InstanceTypeWriter.write_one(obj.instance_type, writer, 'instance_type')
        if obj.template is not None:
            TemplateWriter.write_one(obj.template, writer, 'template')
        if obj.vm is not None:
            VmWriter.write_one(obj.vm, writer, 'vm')
        if obj.vms is not None:
            VmWriter.write_many(obj.vms, writer, 'vm', 'vms')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'watchdog'
        if plural is None:
            plural = 'watchdogs'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            WatchdogWriter.write_one(obj, writer, singular)
        writer.write_end()


class WeightWriter(Writer):

    def __init__(self):
        super(WeightWriter, self).__init__()

    @staticmethod
    def write_one(obj, writer, singular=None):
        if singular is None:
            singular = 'weight'
        writer.write_start(singular)
        href = obj.href
        if href is not None:
            writer.write_attribute('href', href)
        if obj.id is not None:
            writer.write_attribute('id', obj.id)
        if obj.comment is not None:
            Writer.write_string(writer, 'comment', obj.comment)
        if obj.description is not None:
            Writer.write_string(writer, 'description', obj.description)
        if obj.factor is not None:
            Writer.write_integer(writer, 'factor', obj.factor)
        if obj.name is not None:
            Writer.write_string(writer, 'name', obj.name)
        if obj.scheduling_policy is not None:
            SchedulingPolicyWriter.write_one(obj.scheduling_policy, writer, 'scheduling_policy')
        if obj.scheduling_policy_unit is not None:
            SchedulingPolicyUnitWriter.write_one(obj.scheduling_policy_unit, writer, 'scheduling_policy_unit')
        writer.write_end()

    @staticmethod
    def write_many(objs, writer, singular=None, plural=None):
        if singular is None:
            singular = 'weight'
        if plural is None:
            plural = 'weights'
        writer.write_start(plural)
        if type(objs) == List:
            href = objs.href
            if href is not None:
                writer.write_attribute('href', href)
        for obj in objs:
            WeightWriter.write_one(obj, writer, singular)
        writer.write_end()


Writer.register(types.Action, ActionWriter.write_one)
Writer.register(types.AffinityGroup, AffinityGroupWriter.write_one)
Writer.register(types.AffinityLabel, AffinityLabelWriter.write_one)
Writer.register(types.AffinityRule, AffinityRuleWriter.write_one)
Writer.register(types.Agent, AgentWriter.write_one)
Writer.register(types.AgentConfiguration, AgentConfigurationWriter.write_one)
Writer.register(types.Api, ApiWriter.write_one)
Writer.register(types.ApiSummary, ApiSummaryWriter.write_one)
Writer.register(types.ApiSummaryItem, ApiSummaryItemWriter.write_one)
Writer.register(types.Application, ApplicationWriter.write_one)
Writer.register(types.AuthorizedKey, AuthorizedKeyWriter.write_one)
Writer.register(types.Backup, BackupWriter.write_one)
Writer.register(types.Balance, BalanceWriter.write_one)
Writer.register(types.Bios, BiosWriter.write_one)
Writer.register(types.BlockStatistic, BlockStatisticWriter.write_one)
Writer.register(types.Bonding, BondingWriter.write_one)
Writer.register(types.Bookmark, BookmarkWriter.write_one)
Writer.register(types.Boot, BootWriter.write_one)
Writer.register(types.BootMenu, BootMenuWriter.write_one)
Writer.register(types.BrickProfileDetail, BrickProfileDetailWriter.write_one)
Writer.register(types.Cdrom, CdromWriter.write_one)
Writer.register(types.Certificate, CertificateWriter.write_one)
Writer.register(types.Checkpoint, CheckpointWriter.write_one)
Writer.register(types.CloudInit, CloudInitWriter.write_one)
Writer.register(types.Cluster, ClusterWriter.write_one)
Writer.register(types.ClusterFeature, ClusterFeatureWriter.write_one)
Writer.register(types.ClusterLevel, ClusterLevelWriter.write_one)
Writer.register(types.Configuration, ConfigurationWriter.write_one)
Writer.register(types.Console, ConsoleWriter.write_one)
Writer.register(types.Core, CoreWriter.write_one)
Writer.register(types.Cpu, CpuWriter.write_one)
Writer.register(types.CpuProfile, CpuProfileWriter.write_one)
Writer.register(types.CpuTopology, CpuTopologyWriter.write_one)
Writer.register(types.CpuTune, CpuTuneWriter.write_one)
Writer.register(types.CpuType, CpuTypeWriter.write_one)
Writer.register(types.CustomProperty, CustomPropertyWriter.write_one)
Writer.register(types.DataCenter, DataCenterWriter.write_one)
Writer.register(types.Device, DeviceWriter.write_one)
Writer.register(types.Disk, DiskWriter.write_one)
Writer.register(types.DiskAttachment, DiskAttachmentWriter.write_one)
Writer.register(types.DiskProfile, DiskProfileWriter.write_one)
Writer.register(types.DiskSnapshot, DiskSnapshotWriter.write_one)
Writer.register(types.Display, DisplayWriter.write_one)
Writer.register(types.Dns, DnsWriter.write_one)
Writer.register(types.DnsResolverConfiguration, DnsResolverConfigurationWriter.write_one)
Writer.register(types.Domain, DomainWriter.write_one)
Writer.register(types.EntityProfileDetail, EntityProfileDetailWriter.write_one)
Writer.register(types.ErrorHandling, ErrorHandlingWriter.write_one)
Writer.register(types.Event, EventWriter.write_one)
Writer.register(types.EventSubscription, EventSubscriptionWriter.write_one)
Writer.register(types.ExternalComputeResource, ExternalComputeResourceWriter.write_one)
Writer.register(types.ExternalDiscoveredHost, ExternalDiscoveredHostWriter.write_one)
Writer.register(types.ExternalHost, ExternalHostWriter.write_one)
Writer.register(types.ExternalHostGroup, ExternalHostGroupWriter.write_one)
Writer.register(types.ExternalHostProvider, ExternalHostProviderWriter.write_one)
Writer.register(types.ExternalNetworkProviderConfiguration, ExternalNetworkProviderConfigurationWriter.write_one)
Writer.register(types.ExternalProvider, ExternalProviderWriter.write_one)
Writer.register(types.ExternalTemplateImport, ExternalTemplateImportWriter.write_one)
Writer.register(types.ExternalVmImport, ExternalVmImportWriter.write_one)
Writer.register(types.Fault, FaultWriter.write_one)
Writer.register(types.FencingPolicy, FencingPolicyWriter.write_one)
Writer.register(types.File, FileWriter.write_one)
Writer.register(types.Filter, FilterWriter.write_one)
Writer.register(types.Floppy, FloppyWriter.write_one)
Writer.register(types.FopStatistic, FopStatisticWriter.write_one)
Writer.register(types.GlusterBrick, GlusterBrickWriter.write_one)
Writer.register(types.GlusterBrickAdvancedDetails, GlusterBrickAdvancedDetailsWriter.write_one)
Writer.register(types.GlusterBrickMemoryInfo, GlusterBrickMemoryInfoWriter.write_one)
Writer.register(types.GlusterClient, GlusterClientWriter.write_one)
Writer.register(types.GlusterHook, GlusterHookWriter.write_one)
Writer.register(types.GlusterMemoryPool, GlusterMemoryPoolWriter.write_one)
Writer.register(types.GlusterServerHook, GlusterServerHookWriter.write_one)
Writer.register(types.GlusterVolume, GlusterVolumeWriter.write_one)
Writer.register(types.GlusterVolumeProfileDetails, GlusterVolumeProfileDetailsWriter.write_one)
Writer.register(types.GracePeriod, GracePeriodWriter.write_one)
Writer.register(types.GraphicsConsole, GraphicsConsoleWriter.write_one)
Writer.register(types.Group, GroupWriter.write_one)
Writer.register(types.GuestOperatingSystem, GuestOperatingSystemWriter.write_one)
Writer.register(types.HardwareInformation, HardwareInformationWriter.write_one)
Writer.register(types.HighAvailability, HighAvailabilityWriter.write_one)
Writer.register(types.Hook, HookWriter.write_one)
Writer.register(types.Host, HostWriter.write_one)
Writer.register(types.HostDevice, HostDeviceWriter.write_one)
Writer.register(types.HostDevicePassthrough, HostDevicePassthroughWriter.write_one)
Writer.register(types.HostNic, HostNicWriter.write_one)
Writer.register(types.HostNicVirtualFunctionsConfiguration, HostNicVirtualFunctionsConfigurationWriter.write_one)
Writer.register(types.HostStorage, HostStorageWriter.write_one)
Writer.register(types.HostedEngine, HostedEngineWriter.write_one)
Writer.register(types.Icon, IconWriter.write_one)
Writer.register(types.Identified, IdentifiedWriter.write_one)
Writer.register(types.Image, ImageWriter.write_one)
Writer.register(types.ImageTransfer, ImageTransferWriter.write_one)
Writer.register(types.Initialization, InitializationWriter.write_one)
Writer.register(types.InstanceType, InstanceTypeWriter.write_one)
Writer.register(types.Io, IoWriter.write_one)
Writer.register(types.Ip, IpWriter.write_one)
Writer.register(types.IpAddressAssignment, IpAddressAssignmentWriter.write_one)
Writer.register(types.IscsiBond, IscsiBondWriter.write_one)
Writer.register(types.IscsiDetails, IscsiDetailsWriter.write_one)
Writer.register(types.Job, JobWriter.write_one)
Writer.register(types.KatelloErratum, KatelloErratumWriter.write_one)
Writer.register(types.Kernel, KernelWriter.write_one)
Writer.register(types.Ksm, KsmWriter.write_one)
Writer.register(types.LinkLayerDiscoveryProtocolElement, LinkLayerDiscoveryProtocolElementWriter.write_one)
Writer.register(types.LogicalUnit, LogicalUnitWriter.write_one)
Writer.register(types.MDevType, MDevTypeWriter.write_one)
Writer.register(types.Mac, MacWriter.write_one)
Writer.register(types.MacPool, MacPoolWriter.write_one)
Writer.register(types.MemoryOverCommit, MemoryOverCommitWriter.write_one)
Writer.register(types.MemoryPolicy, MemoryPolicyWriter.write_one)
Writer.register(types.Method, MethodWriter.write_one)
Writer.register(types.MigrationBandwidth, MigrationBandwidthWriter.write_one)
Writer.register(types.MigrationOptions, MigrationOptionsWriter.write_one)
Writer.register(types.MigrationPolicy, MigrationPolicyWriter.write_one)
Writer.register(types.Network, NetworkWriter.write_one)
Writer.register(types.NetworkAttachment, NetworkAttachmentWriter.write_one)
Writer.register(types.NetworkConfiguration, NetworkConfigurationWriter.write_one)
Writer.register(types.NetworkFilter, NetworkFilterWriter.write_one)
Writer.register(types.NetworkFilterParameter, NetworkFilterParameterWriter.write_one)
Writer.register(types.NetworkLabel, NetworkLabelWriter.write_one)
Writer.register(types.NfsProfileDetail, NfsProfileDetailWriter.write_one)
Writer.register(types.Nic, NicWriter.write_one)
Writer.register(types.NicConfiguration, NicConfigurationWriter.write_one)
Writer.register(types.NumaNode, NumaNodeWriter.write_one)
Writer.register(types.NumaNodePin, NumaNodePinWriter.write_one)
Writer.register(types.OpenStackImage, OpenStackImageWriter.write_one)
Writer.register(types.OpenStackImageProvider, OpenStackImageProviderWriter.write_one)
Writer.register(types.OpenStackNetwork, OpenStackNetworkWriter.write_one)
Writer.register(types.OpenStackNetworkProvider, OpenStackNetworkProviderWriter.write_one)
Writer.register(types.OpenStackProvider, OpenStackProviderWriter.write_one)
Writer.register(types.OpenStackSubnet, OpenStackSubnetWriter.write_one)
Writer.register(types.OpenStackVolumeProvider, OpenStackVolumeProviderWriter.write_one)
Writer.register(types.OpenStackVolumeType, OpenStackVolumeTypeWriter.write_one)
Writer.register(types.OpenstackVolumeAuthenticationKey, OpenstackVolumeAuthenticationKeyWriter.write_one)
Writer.register(types.OperatingSystem, OperatingSystemWriter.write_one)
Writer.register(types.OperatingSystemInfo, OperatingSystemInfoWriter.write_one)
Writer.register(types.Option, OptionWriter.write_one)
Writer.register(types.Package, PackageWriter.write_one)
Writer.register(types.Payload, PayloadWriter.write_one)
Writer.register(types.Permission, PermissionWriter.write_one)
Writer.register(types.Permit, PermitWriter.write_one)
Writer.register(types.PmProxy, PmProxyWriter.write_one)
Writer.register(types.PortMirroring, PortMirroringWriter.write_one)
Writer.register(types.PowerManagement, PowerManagementWriter.write_one)
Writer.register(types.Product, ProductWriter.write_one)
Writer.register(types.ProductInfo, ProductInfoWriter.write_one)
Writer.register(types.ProfileDetail, ProfileDetailWriter.write_one)
Writer.register(types.Property, PropertyWriter.write_one)
Writer.register(types.ProxyTicket, ProxyTicketWriter.write_one)
Writer.register(types.Qos, QosWriter.write_one)
Writer.register(types.Quota, QuotaWriter.write_one)
Writer.register(types.QuotaClusterLimit, QuotaClusterLimitWriter.write_one)
Writer.register(types.QuotaStorageLimit, QuotaStorageLimitWriter.write_one)
Writer.register(types.Range, RangeWriter.write_one)
Writer.register(types.Rate, RateWriter.write_one)
Writer.register(types.RegistrationAffinityGroupMapping, RegistrationAffinityGroupMappingWriter.write_one)
Writer.register(types.RegistrationAffinityLabelMapping, RegistrationAffinityLabelMappingWriter.write_one)
Writer.register(types.RegistrationClusterMapping, RegistrationClusterMappingWriter.write_one)
Writer.register(types.RegistrationConfiguration, RegistrationConfigurationWriter.write_one)
Writer.register(types.RegistrationDomainMapping, RegistrationDomainMappingWriter.write_one)
Writer.register(types.RegistrationLunMapping, RegistrationLunMappingWriter.write_one)
Writer.register(types.RegistrationRoleMapping, RegistrationRoleMappingWriter.write_one)
Writer.register(types.RegistrationVnicProfileMapping, RegistrationVnicProfileMappingWriter.write_one)
Writer.register(types.ReportedConfiguration, ReportedConfigurationWriter.write_one)
Writer.register(types.ReportedDevice, ReportedDeviceWriter.write_one)
Writer.register(types.RngDevice, RngDeviceWriter.write_one)
Writer.register(types.Role, RoleWriter.write_one)
Writer.register(types.SchedulingPolicy, SchedulingPolicyWriter.write_one)
Writer.register(types.SchedulingPolicyUnit, SchedulingPolicyUnitWriter.write_one)
Writer.register(types.SeLinux, SeLinuxWriter.write_one)
Writer.register(types.SerialNumber, SerialNumberWriter.write_one)
Writer.register(types.Session, SessionWriter.write_one)
Writer.register(types.SkipIfConnectivityBroken, SkipIfConnectivityBrokenWriter.write_one)
Writer.register(types.SkipIfSdActive, SkipIfSdActiveWriter.write_one)
Writer.register(types.Snapshot, SnapshotWriter.write_one)
Writer.register(types.SpecialObjects, SpecialObjectsWriter.write_one)
Writer.register(types.Spm, SpmWriter.write_one)
Writer.register(types.Ssh, SshWriter.write_one)
Writer.register(types.SshPublicKey, SshPublicKeyWriter.write_one)
Writer.register(types.Sso, SsoWriter.write_one)
Writer.register(types.Statistic, StatisticWriter.write_one)
Writer.register(types.Step, StepWriter.write_one)
Writer.register(types.StorageConnection, StorageConnectionWriter.write_one)
Writer.register(types.StorageConnectionExtension, StorageConnectionExtensionWriter.write_one)
Writer.register(types.StorageDomain, StorageDomainWriter.write_one)
Writer.register(types.StorageDomainLease, StorageDomainLeaseWriter.write_one)
Writer.register(types.SystemOption, SystemOptionWriter.write_one)
Writer.register(types.SystemOptionValue, SystemOptionValueWriter.write_one)
Writer.register(types.Tag, TagWriter.write_one)
Writer.register(types.Template, TemplateWriter.write_one)
Writer.register(types.TemplateVersion, TemplateVersionWriter.write_one)
Writer.register(types.Ticket, TicketWriter.write_one)
Writer.register(types.TimeZone, TimeZoneWriter.write_one)
Writer.register(types.TransparentHugePages, TransparentHugePagesWriter.write_one)
Writer.register(types.UnmanagedNetwork, UnmanagedNetworkWriter.write_one)
Writer.register(types.Usb, UsbWriter.write_one)
Writer.register(types.User, UserWriter.write_one)
Writer.register(types.UserOption, UserOptionWriter.write_one)
Writer.register(types.Value, ValueWriter.write_one)
Writer.register(types.VcpuPin, VcpuPinWriter.write_one)
Writer.register(types.Vendor, VendorWriter.write_one)
Writer.register(types.Version, VersionWriter.write_one)
Writer.register(types.VirtioScsi, VirtioScsiWriter.write_one)
Writer.register(types.VirtualNumaNode, VirtualNumaNodeWriter.write_one)
Writer.register(types.Vlan, VlanWriter.write_one)
Writer.register(types.Vm, VmWriter.write_one)
Writer.register(types.VmBase, VmBaseWriter.write_one)
Writer.register(types.VmPlacementPolicy, VmPlacementPolicyWriter.write_one)
Writer.register(types.VmPool, VmPoolWriter.write_one)
Writer.register(types.VmSummary, VmSummaryWriter.write_one)
Writer.register(types.VnicPassThrough, VnicPassThroughWriter.write_one)
Writer.register(types.VnicProfile, VnicProfileWriter.write_one)
Writer.register(types.VnicProfileMapping, VnicProfileMappingWriter.write_one)
Writer.register(types.VolumeGroup, VolumeGroupWriter.write_one)
Writer.register(types.Watchdog, WatchdogWriter.write_one)
Writer.register(types.Weight, WeightWriter.write_one)
