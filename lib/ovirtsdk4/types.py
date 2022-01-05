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


from enum import Enum, unique
from ovirtsdk4 import Struct


class AffinityRule(Struct):

    def __init__(
        self,
        enabled=None,
        enforcing=None,
        positive=None,
    ):
        super(AffinityRule, self).__init__(
        )
        self.enabled = enabled
        self.enforcing = enforcing
        self.positive = positive

    @property
    def enforcing(self):
        """
        Returns the value of the `enforcing` property.
        """
        return self._enforcing

    @enforcing.setter
    def enforcing(self, value):
        """
        Sets the value of the `enforcing` property.
        """
        self._enforcing = value

    @property
    def positive(self):
        """
        Returns the value of the `positive` property.
        """
        return self._positive

    @positive.setter
    def positive(self, value):
        """
        Sets the value of the `positive` property.
        """
        self._positive = value

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class AgentConfiguration(Struct):

    def __init__(
        self,
        address=None,
        broker_type=None,
        network_mappings=None,
        password=None,
        port=None,
        username=None,
    ):
        super(AgentConfiguration, self).__init__(
        )
        self.address = address
        self.broker_type = broker_type
        self.network_mappings = network_mappings
        self.password = password
        self.port = port
        self.username = username

    @property
    def broker_type(self):
        """
        Returns the value of the `broker_type` property.
        """
        return self._broker_type

    @broker_type.setter
    def broker_type(self, value):
        """
        Sets the value of the `broker_type` property.
        """
        Struct._check_type('broker_type', value, MessageBrokerType)
        self._broker_type = value

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def network_mappings(self):
        """
        Returns the value of the `network_mappings` property.
        """
        return self._network_mappings

    @network_mappings.setter
    def network_mappings(self, value):
        """
        Sets the value of the `network_mappings` property.
        """
        self._network_mappings = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value


class Api(Struct):

    def __init__(
        self,
        authenticated_user=None,
        effective_user=None,
        product_info=None,
        special_objects=None,
        summary=None,
        time=None,
    ):
        super(Api, self).__init__(
        )
        self.authenticated_user = authenticated_user
        self.effective_user = effective_user
        self.product_info = product_info
        self.special_objects = special_objects
        self.summary = summary
        self.time = time

    @property
    def effective_user(self):
        """
        Returns the value of the `effective_user` property.
        """
        return self._effective_user

    @effective_user.setter
    def effective_user(self, value):
        """
        Sets the value of the `effective_user` property.
        """
        Struct._check_type('effective_user', value, User)
        self._effective_user = value

    @property
    def summary(self):
        """
        Returns the value of the `summary` property.
        """
        return self._summary

    @summary.setter
    def summary(self, value):
        """
        Sets the value of the `summary` property.
        """
        Struct._check_type('summary', value, ApiSummary)
        self._summary = value

    @property
    def authenticated_user(self):
        """
        Returns the value of the `authenticated_user` property.
        """
        return self._authenticated_user

    @authenticated_user.setter
    def authenticated_user(self, value):
        """
        Sets the value of the `authenticated_user` property.
        """
        Struct._check_type('authenticated_user', value, User)
        self._authenticated_user = value

    @property
    def time(self):
        """
        Returns the value of the `time` property.
        """
        return self._time

    @time.setter
    def time(self, value):
        """
        Sets the value of the `time` property.
        """
        self._time = value

    @property
    def product_info(self):
        """
        Returns the value of the `product_info` property.
        """
        return self._product_info

    @product_info.setter
    def product_info(self, value):
        """
        Sets the value of the `product_info` property.
        """
        Struct._check_type('product_info', value, ProductInfo)
        self._product_info = value

    @property
    def special_objects(self):
        """
        Returns the value of the `special_objects` property.
        """
        return self._special_objects

    @special_objects.setter
    def special_objects(self, value):
        """
        Sets the value of the `special_objects` property.
        """
        Struct._check_type('special_objects', value, SpecialObjects)
        self._special_objects = value


class ApiSummary(Struct):

    def __init__(
        self,
        hosts=None,
        storage_domains=None,
        users=None,
        vms=None,
    ):
        super(ApiSummary, self).__init__(
        )
        self.hosts = hosts
        self.storage_domains = storage_domains
        self.users = users
        self.vms = vms

    @property
    def users(self):
        """
        Returns the value of the `users` property.
        """
        return self._users

    @users.setter
    def users(self, value):
        """
        Sets the value of the `users` property.
        """
        Struct._check_type('users', value, ApiSummaryItem)
        self._users = value

    @property
    def hosts(self):
        """
        Returns the value of the `hosts` property.
        """
        return self._hosts

    @hosts.setter
    def hosts(self, value):
        """
        Sets the value of the `hosts` property.
        """
        Struct._check_type('hosts', value, ApiSummaryItem)
        self._hosts = value

    @property
    def vms(self):
        """
        Returns the value of the `vms` property.
        """
        return self._vms

    @vms.setter
    def vms(self, value):
        """
        Sets the value of the `vms` property.
        """
        Struct._check_type('vms', value, ApiSummaryItem)
        self._vms = value

    @property
    def storage_domains(self):
        """
        Returns the value of the `storage_domains` property.
        """
        return self._storage_domains

    @storage_domains.setter
    def storage_domains(self, value):
        """
        Sets the value of the `storage_domains` property.
        """
        Struct._check_type('storage_domains', value, ApiSummaryItem)
        self._storage_domains = value


class ApiSummaryItem(Struct):

    def __init__(
        self,
        active=None,
        total=None,
    ):
        super(ApiSummaryItem, self).__init__(
        )
        self.active = active
        self.total = total

    @property
    def total(self):
        """
        Returns the value of the `total` property.
        """
        return self._total

    @total.setter
    def total(self, value):
        """
        Sets the value of the `total` property.
        """
        self._total = value

    @property
    def active(self):
        """
        Returns the value of the `active` property.
        """
        return self._active

    @active.setter
    def active(self, value):
        """
        Sets the value of the `active` property.
        """
        self._active = value


class Bios(Struct):

    def __init__(
        self,
        boot_menu=None,
        type=None,
    ):
        super(Bios, self).__init__(
        )
        self.boot_menu = boot_menu
        self.type = type

    @property
    def boot_menu(self):
        """
        Returns the value of the `boot_menu` property.
        """
        return self._boot_menu

    @boot_menu.setter
    def boot_menu(self, value):
        """
        Sets the value of the `boot_menu` property.
        """
        Struct._check_type('boot_menu', value, BootMenu)
        self._boot_menu = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, BiosType)
        self._type = value


class BlockStatistic(Struct):

    def __init__(
        self,
        statistics=None,
    ):
        super(BlockStatistic, self).__init__(
        )
        self.statistics = statistics

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value


class Bonding(Struct):

    def __init__(
        self,
        active_slave=None,
        ad_partner_mac=None,
        options=None,
        slaves=None,
    ):
        super(Bonding, self).__init__(
        )
        self.active_slave = active_slave
        self.ad_partner_mac = ad_partner_mac
        self.options = options
        self.slaves = slaves

    @property
    def active_slave(self):
        """
        Returns the value of the `active_slave` property.
        """
        return self._active_slave

    @active_slave.setter
    def active_slave(self, value):
        """
        Sets the value of the `active_slave` property.
        """
        Struct._check_type('active_slave', value, HostNic)
        self._active_slave = value

    @property
    def slaves(self):
        """
        Returns the value of the `slaves` property.
        """
        return self._slaves

    @slaves.setter
    def slaves(self, value):
        """
        Sets the value of the `slaves` property.
        """
        self._slaves = value

    @property
    def ad_partner_mac(self):
        """
        Returns the value of the `ad_partner_mac` property.
        """
        return self._ad_partner_mac

    @ad_partner_mac.setter
    def ad_partner_mac(self, value):
        """
        Sets the value of the `ad_partner_mac` property.
        """
        Struct._check_type('ad_partner_mac', value, Mac)
        self._ad_partner_mac = value

    @property
    def options(self):
        """
        Returns the value of the `options` property.
        """
        return self._options

    @options.setter
    def options(self, value):
        """
        Sets the value of the `options` property.
        """
        self._options = value


class Boot(Struct):

    def __init__(
        self,
        devices=None,
    ):
        super(Boot, self).__init__(
        )
        self.devices = devices

    @property
    def devices(self):
        """
        Returns the value of the `devices` property.
        """
        return self._devices

    @devices.setter
    def devices(self, value):
        """
        Sets the value of the `devices` property.
        """
        self._devices = value


class BootMenu(Struct):

    def __init__(
        self,
        enabled=None,
    ):
        super(BootMenu, self).__init__(
        )
        self.enabled = enabled

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class CloudInit(Struct):

    def __init__(
        self,
        authorized_keys=None,
        files=None,
        host=None,
        network_configuration=None,
        regenerate_ssh_keys=None,
        timezone=None,
        users=None,
    ):
        super(CloudInit, self).__init__(
        )
        self.authorized_keys = authorized_keys
        self.files = files
        self.host = host
        self.network_configuration = network_configuration
        self.regenerate_ssh_keys = regenerate_ssh_keys
        self.timezone = timezone
        self.users = users

    @property
    def users(self):
        """
        Returns the value of the `users` property.
        """
        return self._users

    @users.setter
    def users(self, value):
        """
        Sets the value of the `users` property.
        """
        self._users = value

    @property
    def network_configuration(self):
        """
        Returns the value of the `network_configuration` property.
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, value):
        """
        Sets the value of the `network_configuration` property.
        """
        Struct._check_type('network_configuration', value, NetworkConfiguration)
        self._network_configuration = value

    @property
    def regenerate_ssh_keys(self):
        """
        Returns the value of the `regenerate_ssh_keys` property.
        """
        return self._regenerate_ssh_keys

    @regenerate_ssh_keys.setter
    def regenerate_ssh_keys(self, value):
        """
        Sets the value of the `regenerate_ssh_keys` property.
        """
        self._regenerate_ssh_keys = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def timezone(self):
        """
        Returns the value of the `timezone` property.
        """
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        """
        Sets the value of the `timezone` property.
        """
        self._timezone = value

    @property
    def files(self):
        """
        Returns the value of the `files` property.
        """
        return self._files

    @files.setter
    def files(self, value):
        """
        Sets the value of the `files` property.
        """
        self._files = value

    @property
    def authorized_keys(self):
        """
        Returns the value of the `authorized_keys` property.
        """
        return self._authorized_keys

    @authorized_keys.setter
    def authorized_keys(self, value):
        """
        Sets the value of the `authorized_keys` property.
        """
        self._authorized_keys = value


class Configuration(Struct):

    def __init__(
        self,
        data=None,
        type=None,
    ):
        super(Configuration, self).__init__(
        )
        self.data = data
        self.type = type

    @property
    def data(self):
        """
        Returns the value of the `data` property.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the value of the `data` property.
        """
        self._data = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, ConfigurationType)
        self._type = value


class Console(Struct):

    def __init__(
        self,
        enabled=None,
    ):
        super(Console, self).__init__(
        )
        self.enabled = enabled

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class Core(Struct):

    def __init__(
        self,
        index=None,
        socket=None,
    ):
        super(Core, self).__init__(
        )
        self.index = index
        self.socket = socket

    @property
    def index(self):
        """
        Returns the value of the `index` property.
        """
        return self._index

    @index.setter
    def index(self, value):
        """
        Sets the value of the `index` property.
        """
        self._index = value

    @property
    def socket(self):
        """
        Returns the value of the `socket` property.
        """
        return self._socket

    @socket.setter
    def socket(self, value):
        """
        Sets the value of the `socket` property.
        """
        self._socket = value


class Cpu(Struct):

    def __init__(
        self,
        architecture=None,
        cores=None,
        cpu_tune=None,
        level=None,
        mode=None,
        name=None,
        speed=None,
        topology=None,
        type=None,
    ):
        super(Cpu, self).__init__(
        )
        self.architecture = architecture
        self.cores = cores
        self.cpu_tune = cpu_tune
        self.level = level
        self.mode = mode
        self.name = name
        self.speed = speed
        self.topology = topology
        self.type = type

    @property
    def mode(self):
        """
        Returns the value of the `mode` property.
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """
        Sets the value of the `mode` property.
        """
        Struct._check_type('mode', value, CpuMode)
        self._mode = value

    @property
    def level(self):
        """
        Returns the value of the `level` property.
        """
        return self._level

    @level.setter
    def level(self, value):
        """
        Sets the value of the `level` property.
        """
        self._level = value

    @property
    def cpu_tune(self):
        """
        Returns the value of the `cpu_tune` property.
        """
        return self._cpu_tune

    @cpu_tune.setter
    def cpu_tune(self, value):
        """
        Sets the value of the `cpu_tune` property.
        """
        Struct._check_type('cpu_tune', value, CpuTune)
        self._cpu_tune = value

    @property
    def cores(self):
        """
        Returns the value of the `cores` property.
        """
        return self._cores

    @cores.setter
    def cores(self, value):
        """
        Sets the value of the `cores` property.
        """
        self._cores = value

    @property
    def topology(self):
        """
        Returns the value of the `topology` property.
        """
        return self._topology

    @topology.setter
    def topology(self, value):
        """
        Sets the value of the `topology` property.
        """
        Struct._check_type('topology', value, CpuTopology)
        self._topology = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def architecture(self):
        """
        Returns the value of the `architecture` property.
        """
        return self._architecture

    @architecture.setter
    def architecture(self, value):
        """
        Sets the value of the `architecture` property.
        """
        Struct._check_type('architecture', value, Architecture)
        self._architecture = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value

    @property
    def speed(self):
        """
        Returns the value of the `speed` property.
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        """
        Sets the value of the `speed` property.
        """
        self._speed = value


class CpuTopology(Struct):

    def __init__(
        self,
        cores=None,
        sockets=None,
        threads=None,
    ):
        super(CpuTopology, self).__init__(
        )
        self.cores = cores
        self.sockets = sockets
        self.threads = threads

    @property
    def sockets(self):
        """
        Returns the value of the `sockets` property.
        """
        return self._sockets

    @sockets.setter
    def sockets(self, value):
        """
        Sets the value of the `sockets` property.
        """
        self._sockets = value

    @property
    def cores(self):
        """
        Returns the value of the `cores` property.
        """
        return self._cores

    @cores.setter
    def cores(self, value):
        """
        Sets the value of the `cores` property.
        """
        self._cores = value

    @property
    def threads(self):
        """
        Returns the value of the `threads` property.
        """
        return self._threads

    @threads.setter
    def threads(self, value):
        """
        Sets the value of the `threads` property.
        """
        self._threads = value


class CpuTune(Struct):

    def __init__(
        self,
        vcpu_pins=None,
    ):
        super(CpuTune, self).__init__(
        )
        self.vcpu_pins = vcpu_pins

    @property
    def vcpu_pins(self):
        """
        Returns the value of the `vcpu_pins` property.
        """
        return self._vcpu_pins

    @vcpu_pins.setter
    def vcpu_pins(self, value):
        """
        Sets the value of the `vcpu_pins` property.
        """
        self._vcpu_pins = value


class CpuType(Struct):

    def __init__(
        self,
        architecture=None,
        level=None,
        name=None,
    ):
        super(CpuType, self).__init__(
        )
        self.architecture = architecture
        self.level = level
        self.name = name

    @property
    def level(self):
        """
        Returns the value of the `level` property.
        """
        return self._level

    @level.setter
    def level(self, value):
        """
        Sets the value of the `level` property.
        """
        self._level = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def architecture(self):
        """
        Returns the value of the `architecture` property.
        """
        return self._architecture

    @architecture.setter
    def architecture(self, value):
        """
        Sets the value of the `architecture` property.
        """
        Struct._check_type('architecture', value, Architecture)
        self._architecture = value


class CustomProperty(Struct):

    def __init__(
        self,
        name=None,
        regexp=None,
        value=None,
    ):
        super(CustomProperty, self).__init__(
        )
        self.name = name
        self.regexp = regexp
        self.value = value

    @property
    def regexp(self):
        """
        Returns the value of the `regexp` property.
        """
        return self._regexp

    @regexp.setter
    def regexp(self, value):
        """
        Sets the value of the `regexp` property.
        """
        self._regexp = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class Display(Struct):

    def __init__(
        self,
        address=None,
        allow_override=None,
        certificate=None,
        copy_paste_enabled=None,
        disconnect_action=None,
        file_transfer_enabled=None,
        keyboard_layout=None,
        monitors=None,
        port=None,
        proxy=None,
        secure_port=None,
        single_qxl_pci=None,
        smartcard_enabled=None,
        type=None,
    ):
        super(Display, self).__init__(
        )
        self.address = address
        self.allow_override = allow_override
        self.certificate = certificate
        self.copy_paste_enabled = copy_paste_enabled
        self.disconnect_action = disconnect_action
        self.file_transfer_enabled = file_transfer_enabled
        self.keyboard_layout = keyboard_layout
        self.monitors = monitors
        self.port = port
        self.proxy = proxy
        self.secure_port = secure_port
        self.single_qxl_pci = single_qxl_pci
        self.smartcard_enabled = smartcard_enabled
        self.type = type

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def allow_override(self):
        """
        Returns the value of the `allow_override` property.
        """
        return self._allow_override

    @allow_override.setter
    def allow_override(self, value):
        """
        Sets the value of the `allow_override` property.
        """
        self._allow_override = value

    @property
    def disconnect_action(self):
        """
        Returns the value of the `disconnect_action` property.
        """
        return self._disconnect_action

    @disconnect_action.setter
    def disconnect_action(self, value):
        """
        Sets the value of the `disconnect_action` property.
        """
        self._disconnect_action = value

    @property
    def single_qxl_pci(self):
        """
        Returns the value of the `single_qxl_pci` property.
        """
        return self._single_qxl_pci

    @single_qxl_pci.setter
    def single_qxl_pci(self, value):
        """
        Sets the value of the `single_qxl_pci` property.
        """
        self._single_qxl_pci = value

    @property
    def keyboard_layout(self):
        """
        Returns the value of the `keyboard_layout` property.
        """
        return self._keyboard_layout

    @keyboard_layout.setter
    def keyboard_layout(self, value):
        """
        Sets the value of the `keyboard_layout` property.
        """
        self._keyboard_layout = value

    @property
    def file_transfer_enabled(self):
        """
        Returns the value of the `file_transfer_enabled` property.
        """
        return self._file_transfer_enabled

    @file_transfer_enabled.setter
    def file_transfer_enabled(self, value):
        """
        Sets the value of the `file_transfer_enabled` property.
        """
        self._file_transfer_enabled = value

    @property
    def certificate(self):
        """
        Returns the value of the `certificate` property.
        """
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        """
        Sets the value of the `certificate` property.
        """
        Struct._check_type('certificate', value, Certificate)
        self._certificate = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, DisplayType)
        self._type = value

    @property
    def secure_port(self):
        """
        Returns the value of the `secure_port` property.
        """
        return self._secure_port

    @secure_port.setter
    def secure_port(self, value):
        """
        Sets the value of the `secure_port` property.
        """
        self._secure_port = value

    @property
    def proxy(self):
        """
        Returns the value of the `proxy` property.
        """
        return self._proxy

    @proxy.setter
    def proxy(self, value):
        """
        Sets the value of the `proxy` property.
        """
        self._proxy = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def smartcard_enabled(self):
        """
        Returns the value of the `smartcard_enabled` property.
        """
        return self._smartcard_enabled

    @smartcard_enabled.setter
    def smartcard_enabled(self, value):
        """
        Sets the value of the `smartcard_enabled` property.
        """
        self._smartcard_enabled = value

    @property
    def monitors(self):
        """
        Returns the value of the `monitors` property.
        """
        return self._monitors

    @monitors.setter
    def monitors(self, value):
        """
        Sets the value of the `monitors` property.
        """
        self._monitors = value

    @property
    def copy_paste_enabled(self):
        """
        Returns the value of the `copy_paste_enabled` property.
        """
        return self._copy_paste_enabled

    @copy_paste_enabled.setter
    def copy_paste_enabled(self, value):
        """
        Sets the value of the `copy_paste_enabled` property.
        """
        self._copy_paste_enabled = value


class Dns(Struct):

    def __init__(
        self,
        search_domains=None,
        servers=None,
    ):
        super(Dns, self).__init__(
        )
        self.search_domains = search_domains
        self.servers = servers

    @property
    def search_domains(self):
        """
        Returns the value of the `search_domains` property.
        """
        return self._search_domains

    @search_domains.setter
    def search_domains(self, value):
        """
        Sets the value of the `search_domains` property.
        """
        self._search_domains = value

    @property
    def servers(self):
        """
        Returns the value of the `servers` property.
        """
        return self._servers

    @servers.setter
    def servers(self, value):
        """
        Sets the value of the `servers` property.
        """
        self._servers = value


class DnsResolverConfiguration(Struct):

    def __init__(
        self,
        name_servers=None,
    ):
        super(DnsResolverConfiguration, self).__init__(
        )
        self.name_servers = name_servers

    @property
    def name_servers(self):
        """
        Returns the value of the `name_servers` property.
        """
        return self._name_servers

    @name_servers.setter
    def name_servers(self, value):
        """
        Sets the value of the `name_servers` property.
        """
        self._name_servers = value


class EntityProfileDetail(Struct):

    def __init__(
        self,
        profile_details=None,
    ):
        super(EntityProfileDetail, self).__init__(
        )
        self.profile_details = profile_details

    @property
    def profile_details(self):
        """
        Returns the value of the `profile_details` property.
        """
        return self._profile_details

    @profile_details.setter
    def profile_details(self, value):
        """
        Sets the value of the `profile_details` property.
        """
        self._profile_details = value


class ErrorHandling(Struct):

    def __init__(
        self,
        on_error=None,
    ):
        super(ErrorHandling, self).__init__(
        )
        self.on_error = on_error

    @property
    def on_error(self):
        """
        Returns the value of the `on_error` property.
        """
        return self._on_error

    @on_error.setter
    def on_error(self, value):
        """
        Sets the value of the `on_error` property.
        """
        Struct._check_type('on_error', value, MigrateOnError)
        self._on_error = value


class ExternalTemplateImport(Struct):

    def __init__(
        self,
        clone=None,
        cluster=None,
        cpu_profile=None,
        host=None,
        quota=None,
        storage_domain=None,
        template=None,
        url=None,
    ):
        super(ExternalTemplateImport, self).__init__(
        )
        self.clone = clone
        self.cluster = cluster
        self.cpu_profile = cpu_profile
        self.host = host
        self.quota = quota
        self.storage_domain = storage_domain
        self.template = template
        self.url = url

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def quota(self):
        """
        Returns the value of the `quota` property.
        """
        return self._quota

    @quota.setter
    def quota(self, value):
        """
        Sets the value of the `quota` property.
        """
        Struct._check_type('quota', value, Quota)
        self._quota = value

    @property
    def clone(self):
        """
        Returns the value of the `clone` property.
        """
        return self._clone

    @clone.setter
    def clone(self, value):
        """
        Sets the value of the `clone` property.
        """
        self._clone = value

    @property
    def url(self):
        """
        Returns the value of the `url` property.
        """
        return self._url

    @url.setter
    def url(self, value):
        """
        Sets the value of the `url` property.
        """
        self._url = value

    @property
    def cpu_profile(self):
        """
        Returns the value of the `cpu_profile` property.
        """
        return self._cpu_profile

    @cpu_profile.setter
    def cpu_profile(self, value):
        """
        Sets the value of the `cpu_profile` property.
        """
        Struct._check_type('cpu_profile', value, CpuProfile)
        self._cpu_profile = value


class ExternalVmImport(Struct):

    def __init__(
        self,
        cluster=None,
        cpu_profile=None,
        drivers_iso=None,
        host=None,
        name=None,
        password=None,
        provider=None,
        quota=None,
        sparse=None,
        storage_domain=None,
        url=None,
        username=None,
        vm=None,
    ):
        super(ExternalVmImport, self).__init__(
        )
        self.cluster = cluster
        self.cpu_profile = cpu_profile
        self.drivers_iso = drivers_iso
        self.host = host
        self.name = name
        self.password = password
        self.provider = provider
        self.quota = quota
        self.sparse = sparse
        self.storage_domain = storage_domain
        self.url = url
        self.username = username
        self.vm = vm

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def drivers_iso(self):
        """
        Returns the value of the `drivers_iso` property.
        """
        return self._drivers_iso

    @drivers_iso.setter
    def drivers_iso(self, value):
        """
        Sets the value of the `drivers_iso` property.
        """
        Struct._check_type('drivers_iso', value, File)
        self._drivers_iso = value

    @property
    def sparse(self):
        """
        Returns the value of the `sparse` property.
        """
        return self._sparse

    @sparse.setter
    def sparse(self, value):
        """
        Sets the value of the `sparse` property.
        """
        self._sparse = value

    @property
    def url(self):
        """
        Returns the value of the `url` property.
        """
        return self._url

    @url.setter
    def url(self, value):
        """
        Sets the value of the `url` property.
        """
        self._url = value

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def provider(self):
        """
        Returns the value of the `provider` property.
        """
        return self._provider

    @provider.setter
    def provider(self, value):
        """
        Sets the value of the `provider` property.
        """
        Struct._check_type('provider', value, ExternalVmProviderType)
        self._provider = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def quota(self):
        """
        Returns the value of the `quota` property.
        """
        return self._quota

    @quota.setter
    def quota(self, value):
        """
        Sets the value of the `quota` property.
        """
        Struct._check_type('quota', value, Quota)
        self._quota = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def cpu_profile(self):
        """
        Returns the value of the `cpu_profile` property.
        """
        return self._cpu_profile

    @cpu_profile.setter
    def cpu_profile(self, value):
        """
        Sets the value of the `cpu_profile` property.
        """
        Struct._check_type('cpu_profile', value, CpuProfile)
        self._cpu_profile = value


class Fault(Struct):

    def __init__(
        self,
        detail=None,
        reason=None,
    ):
        super(Fault, self).__init__(
        )
        self.detail = detail
        self.reason = reason

    @property
    def reason(self):
        """
        Returns the value of the `reason` property.
        """
        return self._reason

    @reason.setter
    def reason(self, value):
        """
        Sets the value of the `reason` property.
        """
        self._reason = value

    @property
    def detail(self):
        """
        Returns the value of the `detail` property.
        """
        return self._detail

    @detail.setter
    def detail(self, value):
        """
        Sets the value of the `detail` property.
        """
        self._detail = value


class FencingPolicy(Struct):

    def __init__(
        self,
        enabled=None,
        skip_if_connectivity_broken=None,
        skip_if_gluster_bricks_up=None,
        skip_if_gluster_quorum_not_met=None,
        skip_if_sd_active=None,
    ):
        super(FencingPolicy, self).__init__(
        )
        self.enabled = enabled
        self.skip_if_connectivity_broken = skip_if_connectivity_broken
        self.skip_if_gluster_bricks_up = skip_if_gluster_bricks_up
        self.skip_if_gluster_quorum_not_met = skip_if_gluster_quorum_not_met
        self.skip_if_sd_active = skip_if_sd_active

    @property
    def skip_if_connectivity_broken(self):
        """
        Returns the value of the `skip_if_connectivity_broken` property.
        """
        return self._skip_if_connectivity_broken

    @skip_if_connectivity_broken.setter
    def skip_if_connectivity_broken(self, value):
        """
        Sets the value of the `skip_if_connectivity_broken` property.
        """
        Struct._check_type('skip_if_connectivity_broken', value, SkipIfConnectivityBroken)
        self._skip_if_connectivity_broken = value

    @property
    def skip_if_gluster_quorum_not_met(self):
        """
        Returns the value of the `skip_if_gluster_quorum_not_met` property.
        """
        return self._skip_if_gluster_quorum_not_met

    @skip_if_gluster_quorum_not_met.setter
    def skip_if_gluster_quorum_not_met(self, value):
        """
        Sets the value of the `skip_if_gluster_quorum_not_met` property.
        """
        self._skip_if_gluster_quorum_not_met = value

    @property
    def skip_if_sd_active(self):
        """
        Returns the value of the `skip_if_sd_active` property.
        """
        return self._skip_if_sd_active

    @skip_if_sd_active.setter
    def skip_if_sd_active(self, value):
        """
        Sets the value of the `skip_if_sd_active` property.
        """
        Struct._check_type('skip_if_sd_active', value, SkipIfSdActive)
        self._skip_if_sd_active = value

    @property
    def skip_if_gluster_bricks_up(self):
        """
        Returns the value of the `skip_if_gluster_bricks_up` property.
        """
        return self._skip_if_gluster_bricks_up

    @skip_if_gluster_bricks_up.setter
    def skip_if_gluster_bricks_up(self, value):
        """
        Sets the value of the `skip_if_gluster_bricks_up` property.
        """
        self._skip_if_gluster_bricks_up = value

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class FopStatistic(Struct):

    def __init__(
        self,
        name=None,
        statistics=None,
    ):
        super(FopStatistic, self).__init__(
        )
        self.name = name
        self.statistics = statistics

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value


class GlusterBrickMemoryInfo(Struct):

    def __init__(
        self,
        memory_pools=None,
    ):
        super(GlusterBrickMemoryInfo, self).__init__(
        )
        self.memory_pools = memory_pools

    @property
    def memory_pools(self):
        """
        Returns the value of the `memory_pools` property.
        """
        return self._memory_pools

    @memory_pools.setter
    def memory_pools(self, value):
        """
        Sets the value of the `memory_pools` property.
        """
        self._memory_pools = value


class GlusterClient(Struct):

    def __init__(
        self,
        bytes_read=None,
        bytes_written=None,
        client_port=None,
        host_name=None,
    ):
        super(GlusterClient, self).__init__(
        )
        self.bytes_read = bytes_read
        self.bytes_written = bytes_written
        self.client_port = client_port
        self.host_name = host_name

    @property
    def bytes_read(self):
        """
        Returns the value of the `bytes_read` property.
        """
        return self._bytes_read

    @bytes_read.setter
    def bytes_read(self, value):
        """
        Sets the value of the `bytes_read` property.
        """
        self._bytes_read = value

    @property
    def host_name(self):
        """
        Returns the value of the `host_name` property.
        """
        return self._host_name

    @host_name.setter
    def host_name(self, value):
        """
        Sets the value of the `host_name` property.
        """
        self._host_name = value

    @property
    def client_port(self):
        """
        Returns the value of the `client_port` property.
        """
        return self._client_port

    @client_port.setter
    def client_port(self, value):
        """
        Sets the value of the `client_port` property.
        """
        self._client_port = value

    @property
    def bytes_written(self):
        """
        Returns the value of the `bytes_written` property.
        """
        return self._bytes_written

    @bytes_written.setter
    def bytes_written(self, value):
        """
        Sets the value of the `bytes_written` property.
        """
        self._bytes_written = value


class GracePeriod(Struct):

    def __init__(
        self,
        expiry=None,
    ):
        super(GracePeriod, self).__init__(
        )
        self.expiry = expiry

    @property
    def expiry(self):
        """
        Returns the value of the `expiry` property.
        """
        return self._expiry

    @expiry.setter
    def expiry(self, value):
        """
        Sets the value of the `expiry` property.
        """
        self._expiry = value


class GuestOperatingSystem(Struct):

    def __init__(
        self,
        architecture=None,
        codename=None,
        distribution=None,
        family=None,
        kernel=None,
        version=None,
    ):
        super(GuestOperatingSystem, self).__init__(
        )
        self.architecture = architecture
        self.codename = codename
        self.distribution = distribution
        self.family = family
        self.kernel = kernel
        self.version = version

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, Version)
        self._version = value

    @property
    def kernel(self):
        """
        Returns the value of the `kernel` property.
        """
        return self._kernel

    @kernel.setter
    def kernel(self, value):
        """
        Sets the value of the `kernel` property.
        """
        Struct._check_type('kernel', value, Kernel)
        self._kernel = value

    @property
    def codename(self):
        """
        Returns the value of the `codename` property.
        """
        return self._codename

    @codename.setter
    def codename(self, value):
        """
        Sets the value of the `codename` property.
        """
        self._codename = value

    @property
    def distribution(self):
        """
        Returns the value of the `distribution` property.
        """
        return self._distribution

    @distribution.setter
    def distribution(self, value):
        """
        Sets the value of the `distribution` property.
        """
        self._distribution = value

    @property
    def family(self):
        """
        Returns the value of the `family` property.
        """
        return self._family

    @family.setter
    def family(self, value):
        """
        Sets the value of the `family` property.
        """
        self._family = value

    @property
    def architecture(self):
        """
        Returns the value of the `architecture` property.
        """
        return self._architecture

    @architecture.setter
    def architecture(self, value):
        """
        Sets the value of the `architecture` property.
        """
        self._architecture = value


class HardwareInformation(Struct):

    def __init__(
        self,
        family=None,
        manufacturer=None,
        product_name=None,
        serial_number=None,
        supported_rng_sources=None,
        uuid=None,
        version=None,
    ):
        super(HardwareInformation, self).__init__(
        )
        self.family = family
        self.manufacturer = manufacturer
        self.product_name = product_name
        self.serial_number = serial_number
        self.supported_rng_sources = supported_rng_sources
        self.uuid = uuid
        self.version = version

    @property
    def serial_number(self):
        """
        Returns the value of the `serial_number` property.
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """
        Sets the value of the `serial_number` property.
        """
        self._serial_number = value

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        self._version = value

    @property
    def product_name(self):
        """
        Returns the value of the `product_name` property.
        """
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        """
        Sets the value of the `product_name` property.
        """
        self._product_name = value

    @property
    def family(self):
        """
        Returns the value of the `family` property.
        """
        return self._family

    @family.setter
    def family(self, value):
        """
        Sets the value of the `family` property.
        """
        self._family = value

    @property
    def supported_rng_sources(self):
        """
        Returns the value of the `supported_rng_sources` property.
        """
        return self._supported_rng_sources

    @supported_rng_sources.setter
    def supported_rng_sources(self, value):
        """
        Sets the value of the `supported_rng_sources` property.
        """
        self._supported_rng_sources = value

    @property
    def uuid(self):
        """
        Returns the value of the `uuid` property.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """
        Sets the value of the `uuid` property.
        """
        self._uuid = value

    @property
    def manufacturer(self):
        """
        Returns the value of the `manufacturer` property.
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        """
        Sets the value of the `manufacturer` property.
        """
        self._manufacturer = value


class HighAvailability(Struct):

    def __init__(
        self,
        enabled=None,
        priority=None,
    ):
        super(HighAvailability, self).__init__(
        )
        self.enabled = enabled
        self.priority = priority

    @property
    def priority(self):
        """
        Returns the value of the `priority` property.
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """
        Sets the value of the `priority` property.
        """
        self._priority = value

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class HostDevicePassthrough(Struct):

    def __init__(
        self,
        enabled=None,
    ):
        super(HostDevicePassthrough, self).__init__(
        )
        self.enabled = enabled

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class HostNicVirtualFunctionsConfiguration(Struct):

    def __init__(
        self,
        all_networks_allowed=None,
        max_number_of_virtual_functions=None,
        number_of_virtual_functions=None,
    ):
        super(HostNicVirtualFunctionsConfiguration, self).__init__(
        )
        self.all_networks_allowed = all_networks_allowed
        self.max_number_of_virtual_functions = max_number_of_virtual_functions
        self.number_of_virtual_functions = number_of_virtual_functions

    @property
    def max_number_of_virtual_functions(self):
        """
        Returns the value of the `max_number_of_virtual_functions` property.
        """
        return self._max_number_of_virtual_functions

    @max_number_of_virtual_functions.setter
    def max_number_of_virtual_functions(self, value):
        """
        Sets the value of the `max_number_of_virtual_functions` property.
        """
        self._max_number_of_virtual_functions = value

    @property
    def all_networks_allowed(self):
        """
        Returns the value of the `all_networks_allowed` property.
        """
        return self._all_networks_allowed

    @all_networks_allowed.setter
    def all_networks_allowed(self, value):
        """
        Sets the value of the `all_networks_allowed` property.
        """
        self._all_networks_allowed = value

    @property
    def number_of_virtual_functions(self):
        """
        Returns the value of the `number_of_virtual_functions` property.
        """
        return self._number_of_virtual_functions

    @number_of_virtual_functions.setter
    def number_of_virtual_functions(self, value):
        """
        Sets the value of the `number_of_virtual_functions` property.
        """
        self._number_of_virtual_functions = value


class HostedEngine(Struct):

    def __init__(
        self,
        active=None,
        configured=None,
        global_maintenance=None,
        local_maintenance=None,
        score=None,
    ):
        super(HostedEngine, self).__init__(
        )
        self.active = active
        self.configured = configured
        self.global_maintenance = global_maintenance
        self.local_maintenance = local_maintenance
        self.score = score

    @property
    def score(self):
        """
        Returns the value of the `score` property.
        """
        return self._score

    @score.setter
    def score(self, value):
        """
        Sets the value of the `score` property.
        """
        self._score = value

    @property
    def configured(self):
        """
        Returns the value of the `configured` property.
        """
        return self._configured

    @configured.setter
    def configured(self, value):
        """
        Sets the value of the `configured` property.
        """
        self._configured = value

    @property
    def global_maintenance(self):
        """
        Returns the value of the `global_maintenance` property.
        """
        return self._global_maintenance

    @global_maintenance.setter
    def global_maintenance(self, value):
        """
        Sets the value of the `global_maintenance` property.
        """
        self._global_maintenance = value

    @property
    def active(self):
        """
        Returns the value of the `active` property.
        """
        return self._active

    @active.setter
    def active(self, value):
        """
        Sets the value of the `active` property.
        """
        self._active = value

    @property
    def local_maintenance(self):
        """
        Returns the value of the `local_maintenance` property.
        """
        return self._local_maintenance

    @local_maintenance.setter
    def local_maintenance(self, value):
        """
        Sets the value of the `local_maintenance` property.
        """
        self._local_maintenance = value


class Identified(Struct):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
    ):
        super(Identified, self).__init__(
        )
        self.comment = comment
        self.description = description
        self.id = id
        self.name = name

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def id(self):
        """
        Returns the value of the `id` property.
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        Sets the value of the `id` property.
        """
        self._id = value

    @property
    def comment(self):
        """
        Returns the value of the `comment` property.
        """
        return self._comment

    @comment.setter
    def comment(self, value):
        """
        Sets the value of the `comment` property.
        """
        self._comment = value

    @property
    def description(self):
        """
        Returns the value of the `description` property.
        """
        return self._description

    @description.setter
    def description(self, value):
        """
        Sets the value of the `description` property.
        """
        self._description = value


class Image(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        size=None,
        storage_domain=None,
        type=None,
    ):
        super(Image, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.size = size
        self.storage_domain = storage_domain
        self.type = type

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def size(self):
        """
        Returns the value of the `size` property.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the value of the `size` property.
        """
        self._size = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, ImageFileType)
        self._type = value


class ImageTransfer(Identified):

    def __init__(
        self,
        active=None,
        backup=None,
        comment=None,
        description=None,
        direction=None,
        disk=None,
        format=None,
        host=None,
        id=None,
        image=None,
        inactivity_timeout=None,
        name=None,
        phase=None,
        proxy_url=None,
        shallow=None,
        snapshot=None,
        timeout_policy=None,
        transfer_url=None,
        transferred=None,
    ):
        super(ImageTransfer, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.active = active
        self.backup = backup
        self.direction = direction
        self.disk = disk
        self.format = format
        self.host = host
        self.image = image
        self.inactivity_timeout = inactivity_timeout
        self.phase = phase
        self.proxy_url = proxy_url
        self.shallow = shallow
        self.snapshot = snapshot
        self.timeout_policy = timeout_policy
        self.transfer_url = transfer_url
        self.transferred = transferred

    @property
    def image(self):
        """
        Returns the value of the `image` property.
        """
        return self._image

    @image.setter
    def image(self, value):
        """
        Sets the value of the `image` property.
        """
        Struct._check_type('image', value, Image)
        self._image = value

    @property
    def phase(self):
        """
        Returns the value of the `phase` property.
        """
        return self._phase

    @phase.setter
    def phase(self, value):
        """
        Sets the value of the `phase` property.
        """
        Struct._check_type('phase', value, ImageTransferPhase)
        self._phase = value

    @property
    def transferred(self):
        """
        Returns the value of the `transferred` property.
        """
        return self._transferred

    @transferred.setter
    def transferred(self, value):
        """
        Sets the value of the `transferred` property.
        """
        self._transferred = value

    @property
    def backup(self):
        """
        Returns the value of the `backup` property.
        """
        return self._backup

    @backup.setter
    def backup(self, value):
        """
        Sets the value of the `backup` property.
        """
        Struct._check_type('backup', value, Backup)
        self._backup = value

    @property
    def transfer_url(self):
        """
        Returns the value of the `transfer_url` property.
        """
        return self._transfer_url

    @transfer_url.setter
    def transfer_url(self, value):
        """
        Sets the value of the `transfer_url` property.
        """
        self._transfer_url = value

    @property
    def format(self):
        """
        Returns the value of the `format` property.
        """
        return self._format

    @format.setter
    def format(self, value):
        """
        Sets the value of the `format` property.
        """
        Struct._check_type('format', value, DiskFormat)
        self._format = value

    @property
    def active(self):
        """
        Returns the value of the `active` property.
        """
        return self._active

    @active.setter
    def active(self, value):
        """
        Sets the value of the `active` property.
        """
        self._active = value

    @property
    def inactivity_timeout(self):
        """
        Returns the value of the `inactivity_timeout` property.
        """
        return self._inactivity_timeout

    @inactivity_timeout.setter
    def inactivity_timeout(self, value):
        """
        Sets the value of the `inactivity_timeout` property.
        """
        self._inactivity_timeout = value

    @property
    def disk(self):
        """
        Returns the value of the `disk` property.
        """
        return self._disk

    @disk.setter
    def disk(self, value):
        """
        Sets the value of the `disk` property.
        """
        Struct._check_type('disk', value, Disk)
        self._disk = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def proxy_url(self):
        """
        Returns the value of the `proxy_url` property.
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, value):
        """
        Sets the value of the `proxy_url` property.
        """
        self._proxy_url = value

    @property
    def snapshot(self):
        """
        Returns the value of the `snapshot` property.
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value):
        """
        Sets the value of the `snapshot` property.
        """
        Struct._check_type('snapshot', value, DiskSnapshot)
        self._snapshot = value

    @property
    def timeout_policy(self):
        """
        Returns the value of the `timeout_policy` property.
        """
        return self._timeout_policy

    @timeout_policy.setter
    def timeout_policy(self, value):
        """
        Sets the value of the `timeout_policy` property.
        """
        Struct._check_type('timeout_policy', value, ImageTransferTimeoutPolicy)
        self._timeout_policy = value

    @property
    def shallow(self):
        """
        Returns the value of the `shallow` property.
        """
        return self._shallow

    @shallow.setter
    def shallow(self, value):
        """
        Sets the value of the `shallow` property.
        """
        self._shallow = value

    @property
    def direction(self):
        """
        Returns the value of the `direction` property.
        """
        return self._direction

    @direction.setter
    def direction(self, value):
        """
        Sets the value of the `direction` property.
        """
        Struct._check_type('direction', value, ImageTransferDirection)
        self._direction = value


class Initialization(Struct):

    def __init__(
        self,
        active_directory_ou=None,
        authorized_ssh_keys=None,
        cloud_init=None,
        cloud_init_network_protocol=None,
        configuration=None,
        custom_script=None,
        dns_search=None,
        dns_servers=None,
        domain=None,
        host_name=None,
        input_locale=None,
        nic_configurations=None,
        org_name=None,
        regenerate_ids=None,
        regenerate_ssh_keys=None,
        root_password=None,
        system_locale=None,
        timezone=None,
        ui_language=None,
        user_locale=None,
        user_name=None,
        windows_license_key=None,
    ):
        super(Initialization, self).__init__(
        )
        self.active_directory_ou = active_directory_ou
        self.authorized_ssh_keys = authorized_ssh_keys
        self.cloud_init = cloud_init
        self.cloud_init_network_protocol = cloud_init_network_protocol
        self.configuration = configuration
        self.custom_script = custom_script
        self.dns_search = dns_search
        self.dns_servers = dns_servers
        self.domain = domain
        self.host_name = host_name
        self.input_locale = input_locale
        self.nic_configurations = nic_configurations
        self.org_name = org_name
        self.regenerate_ids = regenerate_ids
        self.regenerate_ssh_keys = regenerate_ssh_keys
        self.root_password = root_password
        self.system_locale = system_locale
        self.timezone = timezone
        self.ui_language = ui_language
        self.user_locale = user_locale
        self.user_name = user_name
        self.windows_license_key = windows_license_key

    @property
    def regenerate_ssh_keys(self):
        """
        Returns the value of the `regenerate_ssh_keys` property.
        """
        return self._regenerate_ssh_keys

    @regenerate_ssh_keys.setter
    def regenerate_ssh_keys(self, value):
        """
        Sets the value of the `regenerate_ssh_keys` property.
        """
        self._regenerate_ssh_keys = value

    @property
    def host_name(self):
        """
        Returns the value of the `host_name` property.
        """
        return self._host_name

    @host_name.setter
    def host_name(self, value):
        """
        Sets the value of the `host_name` property.
        """
        self._host_name = value

    @property
    def configuration(self):
        """
        Returns the value of the `configuration` property.
        """
        return self._configuration

    @configuration.setter
    def configuration(self, value):
        """
        Sets the value of the `configuration` property.
        """
        Struct._check_type('configuration', value, Configuration)
        self._configuration = value

    @property
    def timezone(self):
        """
        Returns the value of the `timezone` property.
        """
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        """
        Sets the value of the `timezone` property.
        """
        self._timezone = value

    @property
    def authorized_ssh_keys(self):
        """
        Returns the value of the `authorized_ssh_keys` property.
        """
        return self._authorized_ssh_keys

    @authorized_ssh_keys.setter
    def authorized_ssh_keys(self, value):
        """
        Sets the value of the `authorized_ssh_keys` property.
        """
        self._authorized_ssh_keys = value

    @property
    def dns_search(self):
        """
        Returns the value of the `dns_search` property.
        """
        return self._dns_search

    @dns_search.setter
    def dns_search(self, value):
        """
        Sets the value of the `dns_search` property.
        """
        self._dns_search = value

    @property
    def cloud_init_network_protocol(self):
        """
        Returns the value of the `cloud_init_network_protocol` property.
        """
        return self._cloud_init_network_protocol

    @cloud_init_network_protocol.setter
    def cloud_init_network_protocol(self, value):
        """
        Sets the value of the `cloud_init_network_protocol` property.
        """
        Struct._check_type('cloud_init_network_protocol', value, CloudInitNetworkProtocol)
        self._cloud_init_network_protocol = value

    @property
    def system_locale(self):
        """
        Returns the value of the `system_locale` property.
        """
        return self._system_locale

    @system_locale.setter
    def system_locale(self, value):
        """
        Sets the value of the `system_locale` property.
        """
        self._system_locale = value

    @property
    def user_locale(self):
        """
        Returns the value of the `user_locale` property.
        """
        return self._user_locale

    @user_locale.setter
    def user_locale(self, value):
        """
        Sets the value of the `user_locale` property.
        """
        self._user_locale = value

    @property
    def active_directory_ou(self):
        """
        Returns the value of the `active_directory_ou` property.
        """
        return self._active_directory_ou

    @active_directory_ou.setter
    def active_directory_ou(self, value):
        """
        Sets the value of the `active_directory_ou` property.
        """
        self._active_directory_ou = value

    @property
    def org_name(self):
        """
        Returns the value of the `org_name` property.
        """
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        """
        Sets the value of the `org_name` property.
        """
        self._org_name = value

    @property
    def domain(self):
        """
        Returns the value of the `domain` property.
        """
        return self._domain

    @domain.setter
    def domain(self, value):
        """
        Sets the value of the `domain` property.
        """
        self._domain = value

    @property
    def ui_language(self):
        """
        Returns the value of the `ui_language` property.
        """
        return self._ui_language

    @ui_language.setter
    def ui_language(self, value):
        """
        Sets the value of the `ui_language` property.
        """
        self._ui_language = value

    @property
    def windows_license_key(self):
        """
        Returns the value of the `windows_license_key` property.
        """
        return self._windows_license_key

    @windows_license_key.setter
    def windows_license_key(self, value):
        """
        Sets the value of the `windows_license_key` property.
        """
        self._windows_license_key = value

    @property
    def input_locale(self):
        """
        Returns the value of the `input_locale` property.
        """
        return self._input_locale

    @input_locale.setter
    def input_locale(self, value):
        """
        Sets the value of the `input_locale` property.
        """
        self._input_locale = value

    @property
    def nic_configurations(self):
        """
        Returns the value of the `nic_configurations` property.
        """
        return self._nic_configurations

    @nic_configurations.setter
    def nic_configurations(self, value):
        """
        Sets the value of the `nic_configurations` property.
        """
        self._nic_configurations = value

    @property
    def dns_servers(self):
        """
        Returns the value of the `dns_servers` property.
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, value):
        """
        Sets the value of the `dns_servers` property.
        """
        self._dns_servers = value

    @property
    def cloud_init(self):
        """
        Returns the value of the `cloud_init` property.
        """
        return self._cloud_init

    @cloud_init.setter
    def cloud_init(self, value):
        """
        Sets the value of the `cloud_init` property.
        """
        Struct._check_type('cloud_init', value, CloudInit)
        self._cloud_init = value

    @property
    def custom_script(self):
        """
        Returns the value of the `custom_script` property.
        """
        return self._custom_script

    @custom_script.setter
    def custom_script(self, value):
        """
        Sets the value of the `custom_script` property.
        """
        self._custom_script = value

    @property
    def user_name(self):
        """
        Returns the value of the `user_name` property.
        """
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """
        Sets the value of the `user_name` property.
        """
        self._user_name = value

    @property
    def regenerate_ids(self):
        """
        Returns the value of the `regenerate_ids` property.
        """
        return self._regenerate_ids

    @regenerate_ids.setter
    def regenerate_ids(self, value):
        """
        Sets the value of the `regenerate_ids` property.
        """
        self._regenerate_ids = value

    @property
    def root_password(self):
        """
        Returns the value of the `root_password` property.
        """
        return self._root_password

    @root_password.setter
    def root_password(self, value):
        """
        Sets the value of the `root_password` property.
        """
        self._root_password = value


class Io(Struct):

    def __init__(
        self,
        threads=None,
    ):
        super(Io, self).__init__(
        )
        self.threads = threads

    @property
    def threads(self):
        """
        Returns the value of the `threads` property.
        """
        return self._threads

    @threads.setter
    def threads(self, value):
        """
        Sets the value of the `threads` property.
        """
        self._threads = value


class Ip(Struct):

    def __init__(
        self,
        address=None,
        gateway=None,
        netmask=None,
        version=None,
    ):
        super(Ip, self).__init__(
        )
        self.address = address
        self.gateway = gateway
        self.netmask = netmask
        self.version = version

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, IpVersion)
        self._version = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def netmask(self):
        """
        Returns the value of the `netmask` property.
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """
        Sets the value of the `netmask` property.
        """
        self._netmask = value

    @property
    def gateway(self):
        """
        Returns the value of the `gateway` property.
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """
        Sets the value of the `gateway` property.
        """
        self._gateway = value


class IpAddressAssignment(Struct):

    def __init__(
        self,
        assignment_method=None,
        ip=None,
    ):
        super(IpAddressAssignment, self).__init__(
        )
        self.assignment_method = assignment_method
        self.ip = ip

    @property
    def ip(self):
        """
        Returns the value of the `ip` property.
        """
        return self._ip

    @ip.setter
    def ip(self, value):
        """
        Sets the value of the `ip` property.
        """
        Struct._check_type('ip', value, Ip)
        self._ip = value

    @property
    def assignment_method(self):
        """
        Returns the value of the `assignment_method` property.
        """
        return self._assignment_method

    @assignment_method.setter
    def assignment_method(self, value):
        """
        Sets the value of the `assignment_method` property.
        """
        Struct._check_type('assignment_method', value, BootProtocol)
        self._assignment_method = value


class IscsiBond(Identified):

    def __init__(
        self,
        comment=None,
        data_center=None,
        description=None,
        id=None,
        name=None,
        networks=None,
        storage_connections=None,
    ):
        super(IscsiBond, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.data_center = data_center
        self.networks = networks
        self.storage_connections = storage_connections

    @property
    def storage_connections(self):
        """
        Returns the value of the `storage_connections` property.
        """
        return self._storage_connections

    @storage_connections.setter
    def storage_connections(self, value):
        """
        Sets the value of the `storage_connections` property.
        """
        self._storage_connections = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def networks(self):
        """
        Returns the value of the `networks` property.
        """
        return self._networks

    @networks.setter
    def networks(self, value):
        """
        Sets the value of the `networks` property.
        """
        self._networks = value


class IscsiDetails(Struct):

    def __init__(
        self,
        address=None,
        disk_id=None,
        initiator=None,
        lun_mapping=None,
        password=None,
        paths=None,
        port=None,
        portal=None,
        product_id=None,
        serial=None,
        size=None,
        status=None,
        storage_domain_id=None,
        target=None,
        username=None,
        vendor_id=None,
        volume_group_id=None,
    ):
        super(IscsiDetails, self).__init__(
        )
        self.address = address
        self.disk_id = disk_id
        self.initiator = initiator
        self.lun_mapping = lun_mapping
        self.password = password
        self.paths = paths
        self.port = port
        self.portal = portal
        self.product_id = product_id
        self.serial = serial
        self.size = size
        self.status = status
        self.storage_domain_id = storage_domain_id
        self.target = target
        self.username = username
        self.vendor_id = vendor_id
        self.volume_group_id = volume_group_id

    @property
    def storage_domain_id(self):
        """
        Returns the value of the `storage_domain_id` property.
        """
        return self._storage_domain_id

    @storage_domain_id.setter
    def storage_domain_id(self, value):
        """
        Sets the value of the `storage_domain_id` property.
        """
        self._storage_domain_id = value

    @property
    def vendor_id(self):
        """
        Returns the value of the `vendor_id` property.
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, value):
        """
        Sets the value of the `vendor_id` property.
        """
        self._vendor_id = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def initiator(self):
        """
        Returns the value of the `initiator` property.
        """
        return self._initiator

    @initiator.setter
    def initiator(self, value):
        """
        Sets the value of the `initiator` property.
        """
        self._initiator = value

    @property
    def product_id(self):
        """
        Returns the value of the `product_id` property.
        """
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        """
        Sets the value of the `product_id` property.
        """
        self._product_id = value

    @property
    def disk_id(self):
        """
        Returns the value of the `disk_id` property.
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, value):
        """
        Sets the value of the `disk_id` property.
        """
        self._disk_id = value

    @property
    def target(self):
        """
        Returns the value of the `target` property.
        """
        return self._target

    @target.setter
    def target(self, value):
        """
        Sets the value of the `target` property.
        """
        self._target = value

    @property
    def serial(self):
        """
        Returns the value of the `serial` property.
        """
        return self._serial

    @serial.setter
    def serial(self, value):
        """
        Sets the value of the `serial` property.
        """
        self._serial = value

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def lun_mapping(self):
        """
        Returns the value of the `lun_mapping` property.
        """
        return self._lun_mapping

    @lun_mapping.setter
    def lun_mapping(self, value):
        """
        Sets the value of the `lun_mapping` property.
        """
        self._lun_mapping = value

    @property
    def size(self):
        """
        Returns the value of the `size` property.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the value of the `size` property.
        """
        self._size = value

    @property
    def paths(self):
        """
        Returns the value of the `paths` property.
        """
        return self._paths

    @paths.setter
    def paths(self, value):
        """
        Sets the value of the `paths` property.
        """
        self._paths = value

    @property
    def portal(self):
        """
        Returns the value of the `portal` property.
        """
        return self._portal

    @portal.setter
    def portal(self, value):
        """
        Sets the value of the `portal` property.
        """
        self._portal = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        self._status = value

    @property
    def volume_group_id(self):
        """
        Returns the value of the `volume_group_id` property.
        """
        return self._volume_group_id

    @volume_group_id.setter
    def volume_group_id(self, value):
        """
        Sets the value of the `volume_group_id` property.
        """
        self._volume_group_id = value


class Job(Identified):

    def __init__(
        self,
        auto_cleared=None,
        comment=None,
        description=None,
        end_time=None,
        external=None,
        id=None,
        last_updated=None,
        name=None,
        owner=None,
        start_time=None,
        status=None,
        steps=None,
    ):
        super(Job, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.auto_cleared = auto_cleared
        self.end_time = end_time
        self.external = external
        self.last_updated = last_updated
        self.owner = owner
        self.start_time = start_time
        self.status = status
        self.steps = steps

    @property
    def last_updated(self):
        """
        Returns the value of the `last_updated` property.
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, value):
        """
        Sets the value of the `last_updated` property.
        """
        self._last_updated = value

    @property
    def auto_cleared(self):
        """
        Returns the value of the `auto_cleared` property.
        """
        return self._auto_cleared

    @auto_cleared.setter
    def auto_cleared(self, value):
        """
        Sets the value of the `auto_cleared` property.
        """
        self._auto_cleared = value

    @property
    def owner(self):
        """
        Returns the value of the `owner` property.
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """
        Sets the value of the `owner` property.
        """
        Struct._check_type('owner', value, User)
        self._owner = value

    @property
    def external(self):
        """
        Returns the value of the `external` property.
        """
        return self._external

    @external.setter
    def external(self, value):
        """
        Sets the value of the `external` property.
        """
        self._external = value

    @property
    def end_time(self):
        """
        Returns the value of the `end_time` property.
        """
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        """
        Sets the value of the `end_time` property.
        """
        self._end_time = value

    @property
    def start_time(self):
        """
        Returns the value of the `start_time` property.
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """
        Sets the value of the `start_time` property.
        """
        self._start_time = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, JobStatus)
        self._status = value

    @property
    def steps(self):
        """
        Returns the value of the `steps` property.
        """
        return self._steps

    @steps.setter
    def steps(self, value):
        """
        Sets the value of the `steps` property.
        """
        self._steps = value


class KatelloErratum(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        host=None,
        id=None,
        issued=None,
        name=None,
        packages=None,
        severity=None,
        solution=None,
        summary=None,
        title=None,
        type=None,
        vm=None,
    ):
        super(KatelloErratum, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.host = host
        self.issued = issued
        self.packages = packages
        self.severity = severity
        self.solution = solution
        self.summary = summary
        self.title = title
        self.type = type
        self.vm = vm

    @property
    def severity(self):
        """
        Returns the value of the `severity` property.
        """
        return self._severity

    @severity.setter
    def severity(self, value):
        """
        Sets the value of the `severity` property.
        """
        self._severity = value

    @property
    def title(self):
        """
        Returns the value of the `title` property.
        """
        return self._title

    @title.setter
    def title(self, value):
        """
        Sets the value of the `title` property.
        """
        self._title = value

    @property
    def summary(self):
        """
        Returns the value of the `summary` property.
        """
        return self._summary

    @summary.setter
    def summary(self, value):
        """
        Sets the value of the `summary` property.
        """
        self._summary = value

    @property
    def solution(self):
        """
        Returns the value of the `solution` property.
        """
        return self._solution

    @solution.setter
    def solution(self, value):
        """
        Sets the value of the `solution` property.
        """
        self._solution = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def issued(self):
        """
        Returns the value of the `issued` property.
        """
        return self._issued

    @issued.setter
    def issued(self, value):
        """
        Sets the value of the `issued` property.
        """
        self._issued = value

    @property
    def packages(self):
        """
        Returns the value of the `packages` property.
        """
        return self._packages

    @packages.setter
    def packages(self, value):
        """
        Sets the value of the `packages` property.
        """
        self._packages = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value


class Kernel(Struct):

    def __init__(
        self,
        version=None,
    ):
        super(Kernel, self).__init__(
        )
        self.version = version

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, Version)
        self._version = value


class Ksm(Struct):

    def __init__(
        self,
        enabled=None,
        merge_across_nodes=None,
    ):
        super(Ksm, self).__init__(
        )
        self.enabled = enabled
        self.merge_across_nodes = merge_across_nodes

    @property
    def merge_across_nodes(self):
        """
        Returns the value of the `merge_across_nodes` property.
        """
        return self._merge_across_nodes

    @merge_across_nodes.setter
    def merge_across_nodes(self, value):
        """
        Sets the value of the `merge_across_nodes` property.
        """
        self._merge_across_nodes = value

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class LinkLayerDiscoveryProtocolElement(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        oui=None,
        properties=None,
        subtype=None,
        type=None,
    ):
        super(LinkLayerDiscoveryProtocolElement, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.oui = oui
        self.properties = properties
        self.subtype = subtype
        self.type = type

    @property
    def oui(self):
        """
        Returns the value of the `oui` property.
        """
        return self._oui

    @oui.setter
    def oui(self, value):
        """
        Sets the value of the `oui` property.
        """
        self._oui = value

    @property
    def subtype(self):
        """
        Returns the value of the `subtype` property.
        """
        return self._subtype

    @subtype.setter
    def subtype(self, value):
        """
        Sets the value of the `subtype` property.
        """
        self._subtype = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value

    @property
    def properties(self):
        """
        Returns the value of the `properties` property.
        """
        return self._properties

    @properties.setter
    def properties(self, value):
        """
        Sets the value of the `properties` property.
        """
        self._properties = value


class LogicalUnit(Struct):

    def __init__(
        self,
        address=None,
        discard_max_size=None,
        discard_zeroes_data=None,
        disk_id=None,
        id=None,
        lun_mapping=None,
        password=None,
        paths=None,
        port=None,
        portal=None,
        product_id=None,
        serial=None,
        size=None,
        status=None,
        storage_domain_id=None,
        target=None,
        username=None,
        vendor_id=None,
        volume_group_id=None,
    ):
        super(LogicalUnit, self).__init__(
        )
        self.address = address
        self.discard_max_size = discard_max_size
        self.discard_zeroes_data = discard_zeroes_data
        self.disk_id = disk_id
        self.id = id
        self.lun_mapping = lun_mapping
        self.password = password
        self.paths = paths
        self.port = port
        self.portal = portal
        self.product_id = product_id
        self.serial = serial
        self.size = size
        self.status = status
        self.storage_domain_id = storage_domain_id
        self.target = target
        self.username = username
        self.vendor_id = vendor_id
        self.volume_group_id = volume_group_id

    @property
    def storage_domain_id(self):
        """
        Returns the value of the `storage_domain_id` property.
        """
        return self._storage_domain_id

    @storage_domain_id.setter
    def storage_domain_id(self, value):
        """
        Sets the value of the `storage_domain_id` property.
        """
        self._storage_domain_id = value

    @property
    def vendor_id(self):
        """
        Returns the value of the `vendor_id` property.
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, value):
        """
        Sets the value of the `vendor_id` property.
        """
        self._vendor_id = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def product_id(self):
        """
        Returns the value of the `product_id` property.
        """
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        """
        Sets the value of the `product_id` property.
        """
        self._product_id = value

    @property
    def discard_zeroes_data(self):
        """
        Returns the value of the `discard_zeroes_data` property.
        """
        return self._discard_zeroes_data

    @discard_zeroes_data.setter
    def discard_zeroes_data(self, value):
        """
        Sets the value of the `discard_zeroes_data` property.
        """
        self._discard_zeroes_data = value

    @property
    def disk_id(self):
        """
        Returns the value of the `disk_id` property.
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, value):
        """
        Sets the value of the `disk_id` property.
        """
        self._disk_id = value

    @property
    def target(self):
        """
        Returns the value of the `target` property.
        """
        return self._target

    @target.setter
    def target(self, value):
        """
        Sets the value of the `target` property.
        """
        self._target = value

    @property
    def serial(self):
        """
        Returns the value of the `serial` property.
        """
        return self._serial

    @serial.setter
    def serial(self, value):
        """
        Sets the value of the `serial` property.
        """
        self._serial = value

    @property
    def discard_max_size(self):
        """
        Returns the value of the `discard_max_size` property.
        """
        return self._discard_max_size

    @discard_max_size.setter
    def discard_max_size(self, value):
        """
        Sets the value of the `discard_max_size` property.
        """
        self._discard_max_size = value

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def lun_mapping(self):
        """
        Returns the value of the `lun_mapping` property.
        """
        return self._lun_mapping

    @lun_mapping.setter
    def lun_mapping(self, value):
        """
        Sets the value of the `lun_mapping` property.
        """
        self._lun_mapping = value

    @property
    def size(self):
        """
        Returns the value of the `size` property.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the value of the `size` property.
        """
        self._size = value

    @property
    def paths(self):
        """
        Returns the value of the `paths` property.
        """
        return self._paths

    @paths.setter
    def paths(self, value):
        """
        Sets the value of the `paths` property.
        """
        self._paths = value

    @property
    def id(self):
        """
        Returns the value of the `id` property.
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        Sets the value of the `id` property.
        """
        self._id = value

    @property
    def portal(self):
        """
        Returns the value of the `portal` property.
        """
        return self._portal

    @portal.setter
    def portal(self, value):
        """
        Sets the value of the `portal` property.
        """
        self._portal = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, LunStatus)
        self._status = value

    @property
    def volume_group_id(self):
        """
        Returns the value of the `volume_group_id` property.
        """
        return self._volume_group_id

    @volume_group_id.setter
    def volume_group_id(self, value):
        """
        Sets the value of the `volume_group_id` property.
        """
        self._volume_group_id = value


class MDevType(Struct):

    def __init__(
        self,
        available_instances=None,
        description=None,
        human_readable_name=None,
        name=None,
    ):
        super(MDevType, self).__init__(
        )
        self.available_instances = available_instances
        self.description = description
        self.human_readable_name = human_readable_name
        self.name = name

    @property
    def human_readable_name(self):
        """
        Returns the value of the `human_readable_name` property.
        """
        return self._human_readable_name

    @human_readable_name.setter
    def human_readable_name(self, value):
        """
        Sets the value of the `human_readable_name` property.
        """
        self._human_readable_name = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def available_instances(self):
        """
        Returns the value of the `available_instances` property.
        """
        return self._available_instances

    @available_instances.setter
    def available_instances(self, value):
        """
        Sets the value of the `available_instances` property.
        """
        self._available_instances = value

    @property
    def description(self):
        """
        Returns the value of the `description` property.
        """
        return self._description

    @description.setter
    def description(self, value):
        """
        Sets the value of the `description` property.
        """
        self._description = value


class Mac(Struct):

    def __init__(
        self,
        address=None,
    ):
        super(Mac, self).__init__(
        )
        self.address = address

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value


class MacPool(Identified):

    def __init__(
        self,
        allow_duplicates=None,
        comment=None,
        default_pool=None,
        description=None,
        id=None,
        name=None,
        permissions=None,
        ranges=None,
    ):
        super(MacPool, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.allow_duplicates = allow_duplicates
        self.default_pool = default_pool
        self.permissions = permissions
        self.ranges = ranges

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def allow_duplicates(self):
        """
        Returns the value of the `allow_duplicates` property.
        """
        return self._allow_duplicates

    @allow_duplicates.setter
    def allow_duplicates(self, value):
        """
        Sets the value of the `allow_duplicates` property.
        """
        self._allow_duplicates = value

    @property
    def default_pool(self):
        """
        Returns the value of the `default_pool` property.
        """
        return self._default_pool

    @default_pool.setter
    def default_pool(self, value):
        """
        Sets the value of the `default_pool` property.
        """
        self._default_pool = value

    @property
    def ranges(self):
        """
        Returns the value of the `ranges` property.
        """
        return self._ranges

    @ranges.setter
    def ranges(self, value):
        """
        Sets the value of the `ranges` property.
        """
        self._ranges = value


class MemoryOverCommit(Struct):

    def __init__(
        self,
        percent=None,
    ):
        super(MemoryOverCommit, self).__init__(
        )
        self.percent = percent

    @property
    def percent(self):
        """
        Returns the value of the `percent` property.
        """
        return self._percent

    @percent.setter
    def percent(self, value):
        """
        Sets the value of the `percent` property.
        """
        self._percent = value


class MemoryPolicy(Struct):

    def __init__(
        self,
        ballooning=None,
        guaranteed=None,
        max=None,
        over_commit=None,
        transparent_huge_pages=None,
    ):
        super(MemoryPolicy, self).__init__(
        )
        self.ballooning = ballooning
        self.guaranteed = guaranteed
        self.max = max
        self.over_commit = over_commit
        self.transparent_huge_pages = transparent_huge_pages

    @property
    def max(self):
        """
        Returns the value of the `max` property.
        """
        return self._max

    @max.setter
    def max(self, value):
        """
        Sets the value of the `max` property.
        """
        self._max = value

    @property
    def over_commit(self):
        """
        Returns the value of the `over_commit` property.
        """
        return self._over_commit

    @over_commit.setter
    def over_commit(self, value):
        """
        Sets the value of the `over_commit` property.
        """
        Struct._check_type('over_commit', value, MemoryOverCommit)
        self._over_commit = value

    @property
    def ballooning(self):
        """
        Returns the value of the `ballooning` property.
        """
        return self._ballooning

    @ballooning.setter
    def ballooning(self, value):
        """
        Sets the value of the `ballooning` property.
        """
        self._ballooning = value

    @property
    def transparent_huge_pages(self):
        """
        Returns the value of the `transparent_huge_pages` property.
        """
        return self._transparent_huge_pages

    @transparent_huge_pages.setter
    def transparent_huge_pages(self, value):
        """
        Sets the value of the `transparent_huge_pages` property.
        """
        Struct._check_type('transparent_huge_pages', value, TransparentHugePages)
        self._transparent_huge_pages = value

    @property
    def guaranteed(self):
        """
        Returns the value of the `guaranteed` property.
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, value):
        """
        Sets the value of the `guaranteed` property.
        """
        self._guaranteed = value


class Method(Struct):

    def __init__(
        self,
        id=None,
    ):
        super(Method, self).__init__(
        )
        self.id = id

    @property
    def id(self):
        """
        Returns the value of the `id` property.
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        Sets the value of the `id` property.
        """
        Struct._check_type('id', value, SsoMethod)
        self._id = value


class MigrationBandwidth(Struct):

    def __init__(
        self,
        assignment_method=None,
        custom_value=None,
    ):
        super(MigrationBandwidth, self).__init__(
        )
        self.assignment_method = assignment_method
        self.custom_value = custom_value

    @property
    def custom_value(self):
        """
        Returns the value of the `custom_value` property.
        """
        return self._custom_value

    @custom_value.setter
    def custom_value(self, value):
        """
        Sets the value of the `custom_value` property.
        """
        self._custom_value = value

    @property
    def assignment_method(self):
        """
        Returns the value of the `assignment_method` property.
        """
        return self._assignment_method

    @assignment_method.setter
    def assignment_method(self, value):
        """
        Sets the value of the `assignment_method` property.
        """
        Struct._check_type('assignment_method', value, MigrationBandwidthAssignmentMethod)
        self._assignment_method = value


class MigrationOptions(Struct):

    def __init__(
        self,
        auto_converge=None,
        bandwidth=None,
        compressed=None,
        encrypted=None,
        policy=None,
    ):
        super(MigrationOptions, self).__init__(
        )
        self.auto_converge = auto_converge
        self.bandwidth = bandwidth
        self.compressed = compressed
        self.encrypted = encrypted
        self.policy = policy

    @property
    def encrypted(self):
        """
        Returns the value of the `encrypted` property.
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, value):
        """
        Sets the value of the `encrypted` property.
        """
        Struct._check_type('encrypted', value, InheritableBoolean)
        self._encrypted = value

    @property
    def bandwidth(self):
        """
        Returns the value of the `bandwidth` property.
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, value):
        """
        Sets the value of the `bandwidth` property.
        """
        Struct._check_type('bandwidth', value, MigrationBandwidth)
        self._bandwidth = value

    @property
    def auto_converge(self):
        """
        Returns the value of the `auto_converge` property.
        """
        return self._auto_converge

    @auto_converge.setter
    def auto_converge(self, value):
        """
        Sets the value of the `auto_converge` property.
        """
        Struct._check_type('auto_converge', value, InheritableBoolean)
        self._auto_converge = value

    @property
    def compressed(self):
        """
        Returns the value of the `compressed` property.
        """
        return self._compressed

    @compressed.setter
    def compressed(self, value):
        """
        Sets the value of the `compressed` property.
        """
        Struct._check_type('compressed', value, InheritableBoolean)
        self._compressed = value

    @property
    def policy(self):
        """
        Returns the value of the `policy` property.
        """
        return self._policy

    @policy.setter
    def policy(self, value):
        """
        Sets the value of the `policy` property.
        """
        Struct._check_type('policy', value, MigrationPolicy)
        self._policy = value


class MigrationPolicy(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
    ):
        super(MigrationPolicy, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        pass


class Network(Identified):

    def __init__(
        self,
        cluster=None,
        comment=None,
        data_center=None,
        description=None,
        display=None,
        dns_resolver_configuration=None,
        external_provider=None,
        external_provider_physical_network=None,
        id=None,
        ip=None,
        mtu=None,
        name=None,
        network_labels=None,
        permissions=None,
        port_isolation=None,
        profile_required=None,
        qos=None,
        required=None,
        status=None,
        stp=None,
        usages=None,
        vdsm_name=None,
        vlan=None,
        vnic_profiles=None,
    ):
        super(Network, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cluster = cluster
        self.data_center = data_center
        self.display = display
        self.dns_resolver_configuration = dns_resolver_configuration
        self.external_provider = external_provider
        self.external_provider_physical_network = external_provider_physical_network
        self.ip = ip
        self.mtu = mtu
        self.network_labels = network_labels
        self.permissions = permissions
        self.port_isolation = port_isolation
        self.profile_required = profile_required
        self.qos = qos
        self.required = required
        self.status = status
        self.stp = stp
        self.usages = usages
        self.vdsm_name = vdsm_name
        self.vlan = vlan
        self.vnic_profiles = vnic_profiles

    @property
    def dns_resolver_configuration(self):
        """
        Returns the value of the `dns_resolver_configuration` property.
        """
        return self._dns_resolver_configuration

    @dns_resolver_configuration.setter
    def dns_resolver_configuration(self, value):
        """
        Sets the value of the `dns_resolver_configuration` property.
        """
        Struct._check_type('dns_resolver_configuration', value, DnsResolverConfiguration)
        self._dns_resolver_configuration = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def external_provider_physical_network(self):
        """
        Returns the value of the `external_provider_physical_network` property.
        """
        return self._external_provider_physical_network

    @external_provider_physical_network.setter
    def external_provider_physical_network(self, value):
        """
        Sets the value of the `external_provider_physical_network` property.
        """
        Struct._check_type('external_provider_physical_network', value, Network)
        self._external_provider_physical_network = value

    @property
    def display(self):
        """
        Returns the value of the `display` property.
        """
        return self._display

    @display.setter
    def display(self, value):
        """
        Sets the value of the `display` property.
        """
        self._display = value

    @property
    def profile_required(self):
        """
        Returns the value of the `profile_required` property.
        """
        return self._profile_required

    @profile_required.setter
    def profile_required(self, value):
        """
        Sets the value of the `profile_required` property.
        """
        self._profile_required = value

    @property
    def vdsm_name(self):
        """
        Returns the value of the `vdsm_name` property.
        """
        return self._vdsm_name

    @vdsm_name.setter
    def vdsm_name(self, value):
        """
        Sets the value of the `vdsm_name` property.
        """
        self._vdsm_name = value

    @property
    def ip(self):
        """
        Returns the value of the `ip` property.
        """
        return self._ip

    @ip.setter
    def ip(self, value):
        """
        Sets the value of the `ip` property.
        """
        Struct._check_type('ip', value, Ip)
        self._ip = value

    @property
    def network_labels(self):
        """
        Returns the value of the `network_labels` property.
        """
        return self._network_labels

    @network_labels.setter
    def network_labels(self, value):
        """
        Sets the value of the `network_labels` property.
        """
        self._network_labels = value

    @property
    def mtu(self):
        """
        Returns the value of the `mtu` property.
        """
        return self._mtu

    @mtu.setter
    def mtu(self, value):
        """
        Sets the value of the `mtu` property.
        """
        self._mtu = value

    @property
    def vnic_profiles(self):
        """
        Returns the value of the `vnic_profiles` property.
        """
        return self._vnic_profiles

    @vnic_profiles.setter
    def vnic_profiles(self, value):
        """
        Sets the value of the `vnic_profiles` property.
        """
        self._vnic_profiles = value

    @property
    def port_isolation(self):
        """
        Returns the value of the `port_isolation` property.
        """
        return self._port_isolation

    @port_isolation.setter
    def port_isolation(self, value):
        """
        Sets the value of the `port_isolation` property.
        """
        self._port_isolation = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def stp(self):
        """
        Returns the value of the `stp` property.
        """
        return self._stp

    @stp.setter
    def stp(self, value):
        """
        Sets the value of the `stp` property.
        """
        self._stp = value

    @property
    def required(self):
        """
        Returns the value of the `required` property.
        """
        return self._required

    @required.setter
    def required(self, value):
        """
        Sets the value of the `required` property.
        """
        self._required = value

    @property
    def external_provider(self):
        """
        Returns the value of the `external_provider` property.
        """
        return self._external_provider

    @external_provider.setter
    def external_provider(self, value):
        """
        Sets the value of the `external_provider` property.
        """
        Struct._check_type('external_provider', value, OpenStackNetworkProvider)
        self._external_provider = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def vlan(self):
        """
        Returns the value of the `vlan` property.
        """
        return self._vlan

    @vlan.setter
    def vlan(self, value):
        """
        Sets the value of the `vlan` property.
        """
        Struct._check_type('vlan', value, Vlan)
        self._vlan = value

    @property
    def qos(self):
        """
        Returns the value of the `qos` property.
        """
        return self._qos

    @qos.setter
    def qos(self, value):
        """
        Sets the value of the `qos` property.
        """
        Struct._check_type('qos', value, Qos)
        self._qos = value

    @property
    def usages(self):
        """
        Returns the value of the `usages` property.
        """
        return self._usages

    @usages.setter
    def usages(self, value):
        """
        Sets the value of the `usages` property.
        """
        self._usages = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, NetworkStatus)
        self._status = value


class NetworkAttachment(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        dns_resolver_configuration=None,
        host=None,
        host_nic=None,
        id=None,
        in_sync=None,
        ip_address_assignments=None,
        name=None,
        network=None,
        properties=None,
        qos=None,
        reported_configurations=None,
    ):
        super(NetworkAttachment, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.dns_resolver_configuration = dns_resolver_configuration
        self.host = host
        self.host_nic = host_nic
        self.in_sync = in_sync
        self.ip_address_assignments = ip_address_assignments
        self.network = network
        self.properties = properties
        self.qos = qos
        self.reported_configurations = reported_configurations

    @property
    def in_sync(self):
        """
        Returns the value of the `in_sync` property.
        """
        return self._in_sync

    @in_sync.setter
    def in_sync(self, value):
        """
        Sets the value of the `in_sync` property.
        """
        self._in_sync = value

    @property
    def reported_configurations(self):
        """
        Returns the value of the `reported_configurations` property.
        """
        return self._reported_configurations

    @reported_configurations.setter
    def reported_configurations(self, value):
        """
        Sets the value of the `reported_configurations` property.
        """
        self._reported_configurations = value

    @property
    def dns_resolver_configuration(self):
        """
        Returns the value of the `dns_resolver_configuration` property.
        """
        return self._dns_resolver_configuration

    @dns_resolver_configuration.setter
    def dns_resolver_configuration(self, value):
        """
        Sets the value of the `dns_resolver_configuration` property.
        """
        Struct._check_type('dns_resolver_configuration', value, DnsResolverConfiguration)
        self._dns_resolver_configuration = value

    @property
    def qos(self):
        """
        Returns the value of the `qos` property.
        """
        return self._qos

    @qos.setter
    def qos(self, value):
        """
        Sets the value of the `qos` property.
        """
        Struct._check_type('qos', value, Qos)
        self._qos = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def ip_address_assignments(self):
        """
        Returns the value of the `ip_address_assignments` property.
        """
        return self._ip_address_assignments

    @ip_address_assignments.setter
    def ip_address_assignments(self, value):
        """
        Sets the value of the `ip_address_assignments` property.
        """
        self._ip_address_assignments = value

    @property
    def network(self):
        """
        Returns the value of the `network` property.
        """
        return self._network

    @network.setter
    def network(self, value):
        """
        Sets the value of the `network` property.
        """
        Struct._check_type('network', value, Network)
        self._network = value

    @property
    def host_nic(self):
        """
        Returns the value of the `host_nic` property.
        """
        return self._host_nic

    @host_nic.setter
    def host_nic(self, value):
        """
        Sets the value of the `host_nic` property.
        """
        Struct._check_type('host_nic', value, HostNic)
        self._host_nic = value

    @property
    def properties(self):
        """
        Returns the value of the `properties` property.
        """
        return self._properties

    @properties.setter
    def properties(self, value):
        """
        Sets the value of the `properties` property.
        """
        self._properties = value


class NetworkConfiguration(Struct):

    def __init__(
        self,
        dns=None,
        nics=None,
    ):
        super(NetworkConfiguration, self).__init__(
        )
        self.dns = dns
        self.nics = nics

    @property
    def nics(self):
        """
        Returns the value of the `nics` property.
        """
        return self._nics

    @nics.setter
    def nics(self, value):
        """
        Sets the value of the `nics` property.
        """
        self._nics = value

    @property
    def dns(self):
        """
        Returns the value of the `dns` property.
        """
        return self._dns

    @dns.setter
    def dns(self, value):
        """
        Sets the value of the `dns` property.
        """
        Struct._check_type('dns', value, Dns)
        self._dns = value


class NetworkFilter(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        version=None,
    ):
        super(NetworkFilter, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.version = version

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, Version)
        self._version = value


class NetworkFilterParameter(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        nic=None,
        value=None,
    ):
        super(NetworkFilterParameter, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.nic = nic
        self.value = value

    @property
    def nic(self):
        """
        Returns the value of the `nic` property.
        """
        return self._nic

    @nic.setter
    def nic(self, value):
        """
        Sets the value of the `nic` property.
        """
        Struct._check_type('nic', value, Nic)
        self._nic = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class NetworkLabel(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        host_nic=None,
        id=None,
        name=None,
        network=None,
    ):
        super(NetworkLabel, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.host_nic = host_nic
        self.network = network

    @property
    def network(self):
        """
        Returns the value of the `network` property.
        """
        return self._network

    @network.setter
    def network(self, value):
        """
        Sets the value of the `network` property.
        """
        Struct._check_type('network', value, Network)
        self._network = value

    @property
    def host_nic(self):
        """
        Returns the value of the `host_nic` property.
        """
        return self._host_nic

    @host_nic.setter
    def host_nic(self, value):
        """
        Sets the value of the `host_nic` property.
        """
        Struct._check_type('host_nic', value, HostNic)
        self._host_nic = value


class NfsProfileDetail(EntityProfileDetail):

    def __init__(
        self,
        nfs_server_ip=None,
        profile_details=None,
    ):
        super(NfsProfileDetail, self).__init__(
            profile_details=profile_details,
        )
        self.nfs_server_ip = nfs_server_ip

    @property
    def nfs_server_ip(self):
        """
        Returns the value of the `nfs_server_ip` property.
        """
        return self._nfs_server_ip

    @nfs_server_ip.setter
    def nfs_server_ip(self, value):
        """
        Sets the value of the `nfs_server_ip` property.
        """
        self._nfs_server_ip = value


class NicConfiguration(Struct):

    def __init__(
        self,
        boot_protocol=None,
        ip=None,
        ipv6=None,
        ipv6_boot_protocol=None,
        name=None,
        on_boot=None,
    ):
        super(NicConfiguration, self).__init__(
        )
        self.boot_protocol = boot_protocol
        self.ip = ip
        self.ipv6 = ipv6
        self.ipv6_boot_protocol = ipv6_boot_protocol
        self.name = name
        self.on_boot = on_boot

    @property
    def boot_protocol(self):
        """
        Returns the value of the `boot_protocol` property.
        """
        return self._boot_protocol

    @boot_protocol.setter
    def boot_protocol(self, value):
        """
        Sets the value of the `boot_protocol` property.
        """
        Struct._check_type('boot_protocol', value, BootProtocol)
        self._boot_protocol = value

    @property
    def ip(self):
        """
        Returns the value of the `ip` property.
        """
        return self._ip

    @ip.setter
    def ip(self, value):
        """
        Sets the value of the `ip` property.
        """
        Struct._check_type('ip', value, Ip)
        self._ip = value

    @property
    def ipv6(self):
        """
        Returns the value of the `ipv6` property.
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, value):
        """
        Sets the value of the `ipv6` property.
        """
        Struct._check_type('ipv6', value, Ip)
        self._ipv6 = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def on_boot(self):
        """
        Returns the value of the `on_boot` property.
        """
        return self._on_boot

    @on_boot.setter
    def on_boot(self, value):
        """
        Sets the value of the `on_boot` property.
        """
        self._on_boot = value

    @property
    def ipv6_boot_protocol(self):
        """
        Returns the value of the `ipv6_boot_protocol` property.
        """
        return self._ipv6_boot_protocol

    @ipv6_boot_protocol.setter
    def ipv6_boot_protocol(self, value):
        """
        Sets the value of the `ipv6_boot_protocol` property.
        """
        Struct._check_type('ipv6_boot_protocol', value, BootProtocol)
        self._ipv6_boot_protocol = value


class NumaNode(Identified):

    def __init__(
        self,
        comment=None,
        cpu=None,
        description=None,
        host=None,
        id=None,
        index=None,
        memory=None,
        name=None,
        node_distance=None,
        statistics=None,
    ):
        super(NumaNode, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cpu = cpu
        self.host = host
        self.index = index
        self.memory = memory
        self.node_distance = node_distance
        self.statistics = statistics

    @property
    def memory(self):
        """
        Returns the value of the `memory` property.
        """
        return self._memory

    @memory.setter
    def memory(self, value):
        """
        Sets the value of the `memory` property.
        """
        self._memory = value

    @property
    def cpu(self):
        """
        Returns the value of the `cpu` property.
        """
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        """
        Sets the value of the `cpu` property.
        """
        Struct._check_type('cpu', value, Cpu)
        self._cpu = value

    @property
    def node_distance(self):
        """
        Returns the value of the `node_distance` property.
        """
        return self._node_distance

    @node_distance.setter
    def node_distance(self, value):
        """
        Sets the value of the `node_distance` property.
        """
        self._node_distance = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def index(self):
        """
        Returns the value of the `index` property.
        """
        return self._index

    @index.setter
    def index(self, value):
        """
        Sets the value of the `index` property.
        """
        self._index = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value


class NumaNodePin(Struct):

    def __init__(
        self,
        host_numa_node=None,
        index=None,
        pinned=None,
    ):
        super(NumaNodePin, self).__init__(
        )
        self.host_numa_node = host_numa_node
        self.index = index
        self.pinned = pinned

    @property
    def index(self):
        """
        Returns the value of the `index` property.
        """
        return self._index

    @index.setter
    def index(self, value):
        """
        Sets the value of the `index` property.
        """
        self._index = value

    @property
    def host_numa_node(self):
        """
        Returns the value of the `host_numa_node` property.
        """
        return self._host_numa_node

    @host_numa_node.setter
    def host_numa_node(self, value):
        """
        Sets the value of the `host_numa_node` property.
        """
        Struct._check_type('host_numa_node', value, NumaNode)
        self._host_numa_node = value

    @property
    def pinned(self):
        """
        Returns the value of the `pinned` property.
        """
        return self._pinned

    @pinned.setter
    def pinned(self, value):
        """
        Sets the value of the `pinned` property.
        """
        self._pinned = value


class OpenStackImage(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        openstack_image_provider=None,
    ):
        super(OpenStackImage, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.openstack_image_provider = openstack_image_provider

    @property
    def openstack_image_provider(self):
        """
        Returns the value of the `openstack_image_provider` property.
        """
        return self._openstack_image_provider

    @openstack_image_provider.setter
    def openstack_image_provider(self, value):
        """
        Sets the value of the `openstack_image_provider` property.
        """
        Struct._check_type('openstack_image_provider', value, OpenStackImageProvider)
        self._openstack_image_provider = value


class OpenStackNetwork(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        openstack_network_provider=None,
    ):
        super(OpenStackNetwork, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.openstack_network_provider = openstack_network_provider

    @property
    def openstack_network_provider(self):
        """
        Returns the value of the `openstack_network_provider` property.
        """
        return self._openstack_network_provider

    @openstack_network_provider.setter
    def openstack_network_provider(self, value):
        """
        Sets the value of the `openstack_network_provider` property.
        """
        Struct._check_type('openstack_network_provider', value, OpenStackNetworkProvider)
        self._openstack_network_provider = value


class OpenStackSubnet(Identified):

    def __init__(
        self,
        cidr=None,
        comment=None,
        description=None,
        dns_servers=None,
        gateway=None,
        id=None,
        ip_version=None,
        name=None,
        openstack_network=None,
    ):
        super(OpenStackSubnet, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cidr = cidr
        self.dns_servers = dns_servers
        self.gateway = gateway
        self.ip_version = ip_version
        self.openstack_network = openstack_network

    @property
    def ip_version(self):
        """
        Returns the value of the `ip_version` property.
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, value):
        """
        Sets the value of the `ip_version` property.
        """
        self._ip_version = value

    @property
    def gateway(self):
        """
        Returns the value of the `gateway` property.
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """
        Sets the value of the `gateway` property.
        """
        self._gateway = value

    @property
    def dns_servers(self):
        """
        Returns the value of the `dns_servers` property.
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, value):
        """
        Sets the value of the `dns_servers` property.
        """
        self._dns_servers = value

    @property
    def openstack_network(self):
        """
        Returns the value of the `openstack_network` property.
        """
        return self._openstack_network

    @openstack_network.setter
    def openstack_network(self, value):
        """
        Sets the value of the `openstack_network` property.
        """
        Struct._check_type('openstack_network', value, OpenStackNetwork)
        self._openstack_network = value

    @property
    def cidr(self):
        """
        Returns the value of the `cidr` property.
        """
        return self._cidr

    @cidr.setter
    def cidr(self, value):
        """
        Sets the value of the `cidr` property.
        """
        self._cidr = value


class OpenStackVolumeType(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        openstack_volume_provider=None,
        properties=None,
    ):
        super(OpenStackVolumeType, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.openstack_volume_provider = openstack_volume_provider
        self.properties = properties

    @property
    def openstack_volume_provider(self):
        """
        Returns the value of the `openstack_volume_provider` property.
        """
        return self._openstack_volume_provider

    @openstack_volume_provider.setter
    def openstack_volume_provider(self, value):
        """
        Sets the value of the `openstack_volume_provider` property.
        """
        Struct._check_type('openstack_volume_provider', value, OpenStackVolumeProvider)
        self._openstack_volume_provider = value

    @property
    def properties(self):
        """
        Returns the value of the `properties` property.
        """
        return self._properties

    @properties.setter
    def properties(self, value):
        """
        Sets the value of the `properties` property.
        """
        self._properties = value


class OpenstackVolumeAuthenticationKey(Identified):

    def __init__(
        self,
        comment=None,
        creation_date=None,
        description=None,
        id=None,
        name=None,
        openstack_volume_provider=None,
        usage_type=None,
        uuid=None,
        value=None,
    ):
        super(OpenstackVolumeAuthenticationKey, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.creation_date = creation_date
        self.openstack_volume_provider = openstack_volume_provider
        self.usage_type = usage_type
        self.uuid = uuid
        self.value = value

    @property
    def openstack_volume_provider(self):
        """
        Returns the value of the `openstack_volume_provider` property.
        """
        return self._openstack_volume_provider

    @openstack_volume_provider.setter
    def openstack_volume_provider(self, value):
        """
        Sets the value of the `openstack_volume_provider` property.
        """
        Struct._check_type('openstack_volume_provider', value, OpenStackVolumeProvider)
        self._openstack_volume_provider = value

    @property
    def usage_type(self):
        """
        Returns the value of the `usage_type` property.
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        """
        Sets the value of the `usage_type` property.
        """
        Struct._check_type('usage_type', value, OpenstackVolumeAuthenticationKeyUsageType)
        self._usage_type = value

    @property
    def creation_date(self):
        """
        Returns the value of the `creation_date` property.
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """
        Sets the value of the `creation_date` property.
        """
        self._creation_date = value

    @property
    def uuid(self):
        """
        Returns the value of the `uuid` property.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """
        Sets the value of the `uuid` property.
        """
        self._uuid = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class OperatingSystem(Struct):

    def __init__(
        self,
        boot=None,
        cmdline=None,
        custom_kernel_cmdline=None,
        initrd=None,
        kernel=None,
        reported_kernel_cmdline=None,
        type=None,
        version=None,
    ):
        super(OperatingSystem, self).__init__(
        )
        self.boot = boot
        self.cmdline = cmdline
        self.custom_kernel_cmdline = custom_kernel_cmdline
        self.initrd = initrd
        self.kernel = kernel
        self.reported_kernel_cmdline = reported_kernel_cmdline
        self.type = type
        self.version = version

    @property
    def cmdline(self):
        """
        Returns the value of the `cmdline` property.
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, value):
        """
        Sets the value of the `cmdline` property.
        """
        self._cmdline = value

    @property
    def reported_kernel_cmdline(self):
        """
        Returns the value of the `reported_kernel_cmdline` property.
        """
        return self._reported_kernel_cmdline

    @reported_kernel_cmdline.setter
    def reported_kernel_cmdline(self, value):
        """
        Sets the value of the `reported_kernel_cmdline` property.
        """
        self._reported_kernel_cmdline = value

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, Version)
        self._version = value

    @property
    def kernel(self):
        """
        Returns the value of the `kernel` property.
        """
        return self._kernel

    @kernel.setter
    def kernel(self, value):
        """
        Sets the value of the `kernel` property.
        """
        self._kernel = value

    @property
    def custom_kernel_cmdline(self):
        """
        Returns the value of the `custom_kernel_cmdline` property.
        """
        return self._custom_kernel_cmdline

    @custom_kernel_cmdline.setter
    def custom_kernel_cmdline(self, value):
        """
        Sets the value of the `custom_kernel_cmdline` property.
        """
        self._custom_kernel_cmdline = value

    @property
    def initrd(self):
        """
        Returns the value of the `initrd` property.
        """
        return self._initrd

    @initrd.setter
    def initrd(self, value):
        """
        Sets the value of the `initrd` property.
        """
        self._initrd = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value

    @property
    def boot(self):
        """
        Returns the value of the `boot` property.
        """
        return self._boot

    @boot.setter
    def boot(self, value):
        """
        Sets the value of the `boot` property.
        """
        Struct._check_type('boot', value, Boot)
        self._boot = value


class OperatingSystemInfo(Identified):

    def __init__(
        self,
        architecture=None,
        comment=None,
        description=None,
        id=None,
        large_icon=None,
        name=None,
        small_icon=None,
    ):
        super(OperatingSystemInfo, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.architecture = architecture
        self.large_icon = large_icon
        self.small_icon = small_icon

    @property
    def large_icon(self):
        """
        Returns the value of the `large_icon` property.
        """
        return self._large_icon

    @large_icon.setter
    def large_icon(self, value):
        """
        Sets the value of the `large_icon` property.
        """
        Struct._check_type('large_icon', value, Icon)
        self._large_icon = value

    @property
    def architecture(self):
        """
        Returns the value of the `architecture` property.
        """
        return self._architecture

    @architecture.setter
    def architecture(self, value):
        """
        Sets the value of the `architecture` property.
        """
        Struct._check_type('architecture', value, Architecture)
        self._architecture = value

    @property
    def small_icon(self):
        """
        Returns the value of the `small_icon` property.
        """
        return self._small_icon

    @small_icon.setter
    def small_icon(self, value):
        """
        Sets the value of the `small_icon` property.
        """
        Struct._check_type('small_icon', value, Icon)
        self._small_icon = value


class Option(Struct):

    def __init__(
        self,
        name=None,
        type=None,
        value=None,
    ):
        super(Option, self).__init__(
        )
        self.name = name
        self.type = type
        self.value = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value


class Package(Struct):

    def __init__(
        self,
        name=None,
    ):
        super(Package, self).__init__(
        )
        self.name = name

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value


class Payload(Struct):

    def __init__(
        self,
        files=None,
        type=None,
        volume_id=None,
    ):
        super(Payload, self).__init__(
        )
        self.files = files
        self.type = type
        self.volume_id = volume_id

    @property
    def volume_id(self):
        """
        Returns the value of the `volume_id` property.
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, value):
        """
        Sets the value of the `volume_id` property.
        """
        self._volume_id = value

    @property
    def files(self):
        """
        Returns the value of the `files` property.
        """
        return self._files

    @files.setter
    def files(self, value):
        """
        Sets the value of the `files` property.
        """
        self._files = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, VmDeviceType)
        self._type = value


class Permission(Identified):

    def __init__(
        self,
        cluster=None,
        comment=None,
        data_center=None,
        description=None,
        disk=None,
        group=None,
        host=None,
        id=None,
        name=None,
        role=None,
        storage_domain=None,
        template=None,
        user=None,
        vm=None,
        vm_pool=None,
    ):
        super(Permission, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cluster = cluster
        self.data_center = data_center
        self.disk = disk
        self.group = group
        self.host = host
        self.role = role
        self.storage_domain = storage_domain
        self.template = template
        self.user = user
        self.vm = vm
        self.vm_pool = vm_pool

    @property
    def role(self):
        """
        Returns the value of the `role` property.
        """
        return self._role

    @role.setter
    def role(self, value):
        """
        Sets the value of the `role` property.
        """
        Struct._check_type('role', value, Role)
        self._role = value

    @property
    def vm_pool(self):
        """
        Returns the value of the `vm_pool` property.
        """
        return self._vm_pool

    @vm_pool.setter
    def vm_pool(self, value):
        """
        Sets the value of the `vm_pool` property.
        """
        Struct._check_type('vm_pool', value, VmPool)
        self._vm_pool = value

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def disk(self):
        """
        Returns the value of the `disk` property.
        """
        return self._disk

    @disk.setter
    def disk(self, value):
        """
        Sets the value of the `disk` property.
        """
        Struct._check_type('disk', value, Disk)
        self._disk = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def group(self):
        """
        Returns the value of the `group` property.
        """
        return self._group

    @group.setter
    def group(self, value):
        """
        Sets the value of the `group` property.
        """
        Struct._check_type('group', value, Group)
        self._group = value


class Permit(Identified):

    def __init__(
        self,
        administrative=None,
        comment=None,
        description=None,
        id=None,
        name=None,
        role=None,
    ):
        super(Permit, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.administrative = administrative
        self.role = role

    @property
    def role(self):
        """
        Returns the value of the `role` property.
        """
        return self._role

    @role.setter
    def role(self, value):
        """
        Sets the value of the `role` property.
        """
        Struct._check_type('role', value, Role)
        self._role = value

    @property
    def administrative(self):
        """
        Returns the value of the `administrative` property.
        """
        return self._administrative

    @administrative.setter
    def administrative(self, value):
        """
        Sets the value of the `administrative` property.
        """
        self._administrative = value


class PmProxy(Struct):

    def __init__(
        self,
        type=None,
    ):
        super(PmProxy, self).__init__(
        )
        self.type = type

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, PmProxyType)
        self._type = value


class PortMirroring(Struct):

    def __init__(
        self,
    ):
        super(PortMirroring, self).__init__(
        )
        pass


class PowerManagement(Struct):

    def __init__(
        self,
        address=None,
        agents=None,
        automatic_pm_enabled=None,
        enabled=None,
        kdump_detection=None,
        options=None,
        password=None,
        pm_proxies=None,
        status=None,
        type=None,
        username=None,
    ):
        super(PowerManagement, self).__init__(
        )
        self.address = address
        self.agents = agents
        self.automatic_pm_enabled = automatic_pm_enabled
        self.enabled = enabled
        self.kdump_detection = kdump_detection
        self.options = options
        self.password = password
        self.pm_proxies = pm_proxies
        self.status = status
        self.type = type
        self.username = username

    @property
    def kdump_detection(self):
        """
        Returns the value of the `kdump_detection` property.
        """
        return self._kdump_detection

    @kdump_detection.setter
    def kdump_detection(self, value):
        """
        Sets the value of the `kdump_detection` property.
        """
        self._kdump_detection = value

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def pm_proxies(self):
        """
        Returns the value of the `pm_proxies` property.
        """
        return self._pm_proxies

    @pm_proxies.setter
    def pm_proxies(self, value):
        """
        Sets the value of the `pm_proxies` property.
        """
        self._pm_proxies = value

    @property
    def options(self):
        """
        Returns the value of the `options` property.
        """
        return self._options

    @options.setter
    def options(self, value):
        """
        Sets the value of the `options` property.
        """
        self._options = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, PowerManagementStatus)
        self._status = value

    @property
    def agents(self):
        """
        Returns the value of the `agents` property.
        """
        return self._agents

    @agents.setter
    def agents(self, value):
        """
        Sets the value of the `agents` property.
        """
        self._agents = value

    @property
    def automatic_pm_enabled(self):
        """
        Returns the value of the `automatic_pm_enabled` property.
        """
        return self._automatic_pm_enabled

    @automatic_pm_enabled.setter
    def automatic_pm_enabled(self, value):
        """
        Sets the value of the `automatic_pm_enabled` property.
        """
        self._automatic_pm_enabled = value

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value


class Product(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
    ):
        super(Product, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        pass


class ProductInfo(Struct):

    def __init__(
        self,
        instance_id=None,
        name=None,
        vendor=None,
        version=None,
    ):
        super(ProductInfo, self).__init__(
        )
        self.instance_id = instance_id
        self.name = name
        self.vendor = vendor
        self.version = version

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, Version)
        self._version = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def vendor(self):
        """
        Returns the value of the `vendor` property.
        """
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        """
        Sets the value of the `vendor` property.
        """
        self._vendor = value

    @property
    def instance_id(self):
        """
        Returns the value of the `instance_id` property.
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        """
        Sets the value of the `instance_id` property.
        """
        self._instance_id = value


class ProfileDetail(Struct):

    def __init__(
        self,
        block_statistics=None,
        duration=None,
        fop_statistics=None,
        profile_type=None,
        statistics=None,
    ):
        super(ProfileDetail, self).__init__(
        )
        self.block_statistics = block_statistics
        self.duration = duration
        self.fop_statistics = fop_statistics
        self.profile_type = profile_type
        self.statistics = statistics

    @property
    def fop_statistics(self):
        """
        Returns the value of the `fop_statistics` property.
        """
        return self._fop_statistics

    @fop_statistics.setter
    def fop_statistics(self, value):
        """
        Sets the value of the `fop_statistics` property.
        """
        self._fop_statistics = value

    @property
    def duration(self):
        """
        Returns the value of the `duration` property.
        """
        return self._duration

    @duration.setter
    def duration(self, value):
        """
        Sets the value of the `duration` property.
        """
        self._duration = value

    @property
    def block_statistics(self):
        """
        Returns the value of the `block_statistics` property.
        """
        return self._block_statistics

    @block_statistics.setter
    def block_statistics(self, value):
        """
        Sets the value of the `block_statistics` property.
        """
        self._block_statistics = value

    @property
    def profile_type(self):
        """
        Returns the value of the `profile_type` property.
        """
        return self._profile_type

    @profile_type.setter
    def profile_type(self, value):
        """
        Sets the value of the `profile_type` property.
        """
        self._profile_type = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value


class Property(Struct):

    def __init__(
        self,
        name=None,
        value=None,
    ):
        super(Property, self).__init__(
        )
        self.name = name
        self.value = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class ProxyTicket(Struct):

    def __init__(
        self,
        value=None,
    ):
        super(ProxyTicket, self).__init__(
        )
        self.value = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class Qos(Identified):

    def __init__(
        self,
        comment=None,
        cpu_limit=None,
        data_center=None,
        description=None,
        id=None,
        inbound_average=None,
        inbound_burst=None,
        inbound_peak=None,
        max_iops=None,
        max_read_iops=None,
        max_read_throughput=None,
        max_throughput=None,
        max_write_iops=None,
        max_write_throughput=None,
        name=None,
        outbound_average=None,
        outbound_average_linkshare=None,
        outbound_average_realtime=None,
        outbound_average_upperlimit=None,
        outbound_burst=None,
        outbound_peak=None,
        type=None,
    ):
        super(Qos, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cpu_limit = cpu_limit
        self.data_center = data_center
        self.inbound_average = inbound_average
        self.inbound_burst = inbound_burst
        self.inbound_peak = inbound_peak
        self.max_iops = max_iops
        self.max_read_iops = max_read_iops
        self.max_read_throughput = max_read_throughput
        self.max_throughput = max_throughput
        self.max_write_iops = max_write_iops
        self.max_write_throughput = max_write_throughput
        self.outbound_average = outbound_average
        self.outbound_average_linkshare = outbound_average_linkshare
        self.outbound_average_realtime = outbound_average_realtime
        self.outbound_average_upperlimit = outbound_average_upperlimit
        self.outbound_burst = outbound_burst
        self.outbound_peak = outbound_peak
        self.type = type

    @property
    def max_read_throughput(self):
        """
        Returns the value of the `max_read_throughput` property.
        """
        return self._max_read_throughput

    @max_read_throughput.setter
    def max_read_throughput(self, value):
        """
        Sets the value of the `max_read_throughput` property.
        """
        self._max_read_throughput = value

    @property
    def max_iops(self):
        """
        Returns the value of the `max_iops` property.
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, value):
        """
        Sets the value of the `max_iops` property.
        """
        self._max_iops = value

    @property
    def max_throughput(self):
        """
        Returns the value of the `max_throughput` property.
        """
        return self._max_throughput

    @max_throughput.setter
    def max_throughput(self, value):
        """
        Sets the value of the `max_throughput` property.
        """
        self._max_throughput = value

    @property
    def max_read_iops(self):
        """
        Returns the value of the `max_read_iops` property.
        """
        return self._max_read_iops

    @max_read_iops.setter
    def max_read_iops(self, value):
        """
        Sets the value of the `max_read_iops` property.
        """
        self._max_read_iops = value

    @property
    def outbound_burst(self):
        """
        Returns the value of the `outbound_burst` property.
        """
        return self._outbound_burst

    @outbound_burst.setter
    def outbound_burst(self, value):
        """
        Sets the value of the `outbound_burst` property.
        """
        self._outbound_burst = value

    @property
    def max_write_iops(self):
        """
        Returns the value of the `max_write_iops` property.
        """
        return self._max_write_iops

    @max_write_iops.setter
    def max_write_iops(self, value):
        """
        Sets the value of the `max_write_iops` property.
        """
        self._max_write_iops = value

    @property
    def max_write_throughput(self):
        """
        Returns the value of the `max_write_throughput` property.
        """
        return self._max_write_throughput

    @max_write_throughput.setter
    def max_write_throughput(self, value):
        """
        Sets the value of the `max_write_throughput` property.
        """
        self._max_write_throughput = value

    @property
    def cpu_limit(self):
        """
        Returns the value of the `cpu_limit` property.
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, value):
        """
        Sets the value of the `cpu_limit` property.
        """
        self._cpu_limit = value

    @property
    def inbound_peak(self):
        """
        Returns the value of the `inbound_peak` property.
        """
        return self._inbound_peak

    @inbound_peak.setter
    def inbound_peak(self, value):
        """
        Sets the value of the `inbound_peak` property.
        """
        self._inbound_peak = value

    @property
    def outbound_average_linkshare(self):
        """
        Returns the value of the `outbound_average_linkshare` property.
        """
        return self._outbound_average_linkshare

    @outbound_average_linkshare.setter
    def outbound_average_linkshare(self, value):
        """
        Sets the value of the `outbound_average_linkshare` property.
        """
        self._outbound_average_linkshare = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, QosType)
        self._type = value

    @property
    def inbound_average(self):
        """
        Returns the value of the `inbound_average` property.
        """
        return self._inbound_average

    @inbound_average.setter
    def inbound_average(self, value):
        """
        Sets the value of the `inbound_average` property.
        """
        self._inbound_average = value

    @property
    def outbound_average_upperlimit(self):
        """
        Returns the value of the `outbound_average_upperlimit` property.
        """
        return self._outbound_average_upperlimit

    @outbound_average_upperlimit.setter
    def outbound_average_upperlimit(self, value):
        """
        Sets the value of the `outbound_average_upperlimit` property.
        """
        self._outbound_average_upperlimit = value

    @property
    def inbound_burst(self):
        """
        Returns the value of the `inbound_burst` property.
        """
        return self._inbound_burst

    @inbound_burst.setter
    def inbound_burst(self, value):
        """
        Sets the value of the `inbound_burst` property.
        """
        self._inbound_burst = value

    @property
    def outbound_peak(self):
        """
        Returns the value of the `outbound_peak` property.
        """
        return self._outbound_peak

    @outbound_peak.setter
    def outbound_peak(self, value):
        """
        Sets the value of the `outbound_peak` property.
        """
        self._outbound_peak = value

    @property
    def outbound_average(self):
        """
        Returns the value of the `outbound_average` property.
        """
        return self._outbound_average

    @outbound_average.setter
    def outbound_average(self, value):
        """
        Sets the value of the `outbound_average` property.
        """
        self._outbound_average = value

    @property
    def outbound_average_realtime(self):
        """
        Returns the value of the `outbound_average_realtime` property.
        """
        return self._outbound_average_realtime

    @outbound_average_realtime.setter
    def outbound_average_realtime(self, value):
        """
        Sets the value of the `outbound_average_realtime` property.
        """
        self._outbound_average_realtime = value


class Quota(Identified):

    def __init__(
        self,
        cluster_hard_limit_pct=None,
        cluster_soft_limit_pct=None,
        comment=None,
        data_center=None,
        description=None,
        disks=None,
        id=None,
        name=None,
        permissions=None,
        quota_cluster_limits=None,
        quota_storage_limits=None,
        storage_hard_limit_pct=None,
        storage_soft_limit_pct=None,
        users=None,
        vms=None,
    ):
        super(Quota, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cluster_hard_limit_pct = cluster_hard_limit_pct
        self.cluster_soft_limit_pct = cluster_soft_limit_pct
        self.data_center = data_center
        self.disks = disks
        self.permissions = permissions
        self.quota_cluster_limits = quota_cluster_limits
        self.quota_storage_limits = quota_storage_limits
        self.storage_hard_limit_pct = storage_hard_limit_pct
        self.storage_soft_limit_pct = storage_soft_limit_pct
        self.users = users
        self.vms = vms

    @property
    def users(self):
        """
        Returns the value of the `users` property.
        """
        return self._users

    @users.setter
    def users(self, value):
        """
        Sets the value of the `users` property.
        """
        self._users = value

    @property
    def storage_soft_limit_pct(self):
        """
        Returns the value of the `storage_soft_limit_pct` property.
        """
        return self._storage_soft_limit_pct

    @storage_soft_limit_pct.setter
    def storage_soft_limit_pct(self, value):
        """
        Sets the value of the `storage_soft_limit_pct` property.
        """
        self._storage_soft_limit_pct = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def quota_cluster_limits(self):
        """
        Returns the value of the `quota_cluster_limits` property.
        """
        return self._quota_cluster_limits

    @quota_cluster_limits.setter
    def quota_cluster_limits(self, value):
        """
        Sets the value of the `quota_cluster_limits` property.
        """
        self._quota_cluster_limits = value

    @property
    def cluster_hard_limit_pct(self):
        """
        Returns the value of the `cluster_hard_limit_pct` property.
        """
        return self._cluster_hard_limit_pct

    @cluster_hard_limit_pct.setter
    def cluster_hard_limit_pct(self, value):
        """
        Sets the value of the `cluster_hard_limit_pct` property.
        """
        self._cluster_hard_limit_pct = value

    @property
    def storage_hard_limit_pct(self):
        """
        Returns the value of the `storage_hard_limit_pct` property.
        """
        return self._storage_hard_limit_pct

    @storage_hard_limit_pct.setter
    def storage_hard_limit_pct(self, value):
        """
        Sets the value of the `storage_hard_limit_pct` property.
        """
        self._storage_hard_limit_pct = value

    @property
    def disks(self):
        """
        Returns the value of the `disks` property.
        """
        return self._disks

    @disks.setter
    def disks(self, value):
        """
        Sets the value of the `disks` property.
        """
        self._disks = value

    @property
    def cluster_soft_limit_pct(self):
        """
        Returns the value of the `cluster_soft_limit_pct` property.
        """
        return self._cluster_soft_limit_pct

    @cluster_soft_limit_pct.setter
    def cluster_soft_limit_pct(self, value):
        """
        Sets the value of the `cluster_soft_limit_pct` property.
        """
        self._cluster_soft_limit_pct = value

    @property
    def vms(self):
        """
        Returns the value of the `vms` property.
        """
        return self._vms

    @vms.setter
    def vms(self, value):
        """
        Sets the value of the `vms` property.
        """
        self._vms = value

    @property
    def quota_storage_limits(self):
        """
        Returns the value of the `quota_storage_limits` property.
        """
        return self._quota_storage_limits

    @quota_storage_limits.setter
    def quota_storage_limits(self, value):
        """
        Sets the value of the `quota_storage_limits` property.
        """
        self._quota_storage_limits = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value


class QuotaClusterLimit(Identified):

    def __init__(
        self,
        cluster=None,
        comment=None,
        description=None,
        id=None,
        memory_limit=None,
        memory_usage=None,
        name=None,
        quota=None,
        vcpu_limit=None,
        vcpu_usage=None,
    ):
        super(QuotaClusterLimit, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cluster = cluster
        self.memory_limit = memory_limit
        self.memory_usage = memory_usage
        self.quota = quota
        self.vcpu_limit = vcpu_limit
        self.vcpu_usage = vcpu_usage

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def memory_limit(self):
        """
        Returns the value of the `memory_limit` property.
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, value):
        """
        Sets the value of the `memory_limit` property.
        """
        self._memory_limit = value

    @property
    def vcpu_usage(self):
        """
        Returns the value of the `vcpu_usage` property.
        """
        return self._vcpu_usage

    @vcpu_usage.setter
    def vcpu_usage(self, value):
        """
        Sets the value of the `vcpu_usage` property.
        """
        self._vcpu_usage = value

    @property
    def quota(self):
        """
        Returns the value of the `quota` property.
        """
        return self._quota

    @quota.setter
    def quota(self, value):
        """
        Sets the value of the `quota` property.
        """
        Struct._check_type('quota', value, Quota)
        self._quota = value

    @property
    def vcpu_limit(self):
        """
        Returns the value of the `vcpu_limit` property.
        """
        return self._vcpu_limit

    @vcpu_limit.setter
    def vcpu_limit(self, value):
        """
        Sets the value of the `vcpu_limit` property.
        """
        self._vcpu_limit = value

    @property
    def memory_usage(self):
        """
        Returns the value of the `memory_usage` property.
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, value):
        """
        Sets the value of the `memory_usage` property.
        """
        self._memory_usage = value


class QuotaStorageLimit(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        limit=None,
        name=None,
        quota=None,
        storage_domain=None,
        usage=None,
    ):
        super(QuotaStorageLimit, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.limit = limit
        self.quota = quota
        self.storage_domain = storage_domain
        self.usage = usage

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def usage(self):
        """
        Returns the value of the `usage` property.
        """
        return self._usage

    @usage.setter
    def usage(self, value):
        """
        Sets the value of the `usage` property.
        """
        self._usage = value

    @property
    def quota(self):
        """
        Returns the value of the `quota` property.
        """
        return self._quota

    @quota.setter
    def quota(self, value):
        """
        Sets the value of the `quota` property.
        """
        Struct._check_type('quota', value, Quota)
        self._quota = value

    @property
    def limit(self):
        """
        Returns the value of the `limit` property.
        """
        return self._limit

    @limit.setter
    def limit(self, value):
        """
        Sets the value of the `limit` property.
        """
        self._limit = value


class Range(Struct):

    def __init__(
        self,
        from_=None,
        to=None,
    ):
        super(Range, self).__init__(
        )
        self.from_ = from_
        self.to = to

    @property
    def from_(self):
        """
        Returns the value of the `from_` property.
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        """
        Sets the value of the `from_` property.
        """
        self._from_ = value

    @property
    def to(self):
        """
        Returns the value of the `to` property.
        """
        return self._to

    @to.setter
    def to(self, value):
        """
        Sets the value of the `to` property.
        """
        self._to = value


class Rate(Struct):

    def __init__(
        self,
        bytes=None,
        period=None,
    ):
        super(Rate, self).__init__(
        )
        self.bytes = bytes
        self.period = period

    @property
    def period(self):
        """
        Returns the value of the `period` property.
        """
        return self._period

    @period.setter
    def period(self, value):
        """
        Sets the value of the `period` property.
        """
        self._period = value

    @property
    def bytes(self):
        """
        Returns the value of the `bytes` property.
        """
        return self._bytes

    @bytes.setter
    def bytes(self, value):
        """
        Sets the value of the `bytes` property.
        """
        self._bytes = value


class RegistrationAffinityGroupMapping(Struct):

    def __init__(
        self,
        from_=None,
        to=None,
    ):
        super(RegistrationAffinityGroupMapping, self).__init__(
        )
        self.from_ = from_
        self.to = to

    @property
    def from_(self):
        """
        Returns the value of the `from_` property.
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        """
        Sets the value of the `from_` property.
        """
        Struct._check_type('from_', value, AffinityGroup)
        self._from_ = value

    @property
    def to(self):
        """
        Returns the value of the `to` property.
        """
        return self._to

    @to.setter
    def to(self, value):
        """
        Sets the value of the `to` property.
        """
        Struct._check_type('to', value, AffinityGroup)
        self._to = value


class RegistrationAffinityLabelMapping(Struct):

    def __init__(
        self,
        from_=None,
        to=None,
    ):
        super(RegistrationAffinityLabelMapping, self).__init__(
        )
        self.from_ = from_
        self.to = to

    @property
    def from_(self):
        """
        Returns the value of the `from_` property.
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        """
        Sets the value of the `from_` property.
        """
        Struct._check_type('from_', value, AffinityLabel)
        self._from_ = value

    @property
    def to(self):
        """
        Returns the value of the `to` property.
        """
        return self._to

    @to.setter
    def to(self, value):
        """
        Sets the value of the `to` property.
        """
        Struct._check_type('to', value, AffinityLabel)
        self._to = value


class RegistrationClusterMapping(Struct):

    def __init__(
        self,
        from_=None,
        to=None,
    ):
        super(RegistrationClusterMapping, self).__init__(
        )
        self.from_ = from_
        self.to = to

    @property
    def from_(self):
        """
        Returns the value of the `from_` property.
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        """
        Sets the value of the `from_` property.
        """
        Struct._check_type('from_', value, Cluster)
        self._from_ = value

    @property
    def to(self):
        """
        Returns the value of the `to` property.
        """
        return self._to

    @to.setter
    def to(self, value):
        """
        Sets the value of the `to` property.
        """
        Struct._check_type('to', value, Cluster)
        self._to = value


class RegistrationConfiguration(Struct):

    def __init__(
        self,
        affinity_group_mappings=None,
        affinity_label_mappings=None,
        cluster_mappings=None,
        domain_mappings=None,
        lun_mappings=None,
        role_mappings=None,
        vnic_profile_mappings=None,
    ):
        super(RegistrationConfiguration, self).__init__(
        )
        self.affinity_group_mappings = affinity_group_mappings
        self.affinity_label_mappings = affinity_label_mappings
        self.cluster_mappings = cluster_mappings
        self.domain_mappings = domain_mappings
        self.lun_mappings = lun_mappings
        self.role_mappings = role_mappings
        self.vnic_profile_mappings = vnic_profile_mappings

    @property
    def role_mappings(self):
        """
        Returns the value of the `role_mappings` property.
        """
        return self._role_mappings

    @role_mappings.setter
    def role_mappings(self, value):
        """
        Sets the value of the `role_mappings` property.
        """
        self._role_mappings = value

    @property
    def affinity_label_mappings(self):
        """
        Returns the value of the `affinity_label_mappings` property.
        """
        return self._affinity_label_mappings

    @affinity_label_mappings.setter
    def affinity_label_mappings(self, value):
        """
        Sets the value of the `affinity_label_mappings` property.
        """
        self._affinity_label_mappings = value

    @property
    def cluster_mappings(self):
        """
        Returns the value of the `cluster_mappings` property.
        """
        return self._cluster_mappings

    @cluster_mappings.setter
    def cluster_mappings(self, value):
        """
        Sets the value of the `cluster_mappings` property.
        """
        self._cluster_mappings = value

    @property
    def lun_mappings(self):
        """
        Returns the value of the `lun_mappings` property.
        """
        return self._lun_mappings

    @lun_mappings.setter
    def lun_mappings(self, value):
        """
        Sets the value of the `lun_mappings` property.
        """
        self._lun_mappings = value

    @property
    def vnic_profile_mappings(self):
        """
        Returns the value of the `vnic_profile_mappings` property.
        """
        return self._vnic_profile_mappings

    @vnic_profile_mappings.setter
    def vnic_profile_mappings(self, value):
        """
        Sets the value of the `vnic_profile_mappings` property.
        """
        self._vnic_profile_mappings = value

    @property
    def affinity_group_mappings(self):
        """
        Returns the value of the `affinity_group_mappings` property.
        """
        return self._affinity_group_mappings

    @affinity_group_mappings.setter
    def affinity_group_mappings(self, value):
        """
        Sets the value of the `affinity_group_mappings` property.
        """
        self._affinity_group_mappings = value

    @property
    def domain_mappings(self):
        """
        Returns the value of the `domain_mappings` property.
        """
        return self._domain_mappings

    @domain_mappings.setter
    def domain_mappings(self, value):
        """
        Sets the value of the `domain_mappings` property.
        """
        self._domain_mappings = value


class RegistrationDomainMapping(Struct):

    def __init__(
        self,
        from_=None,
        to=None,
    ):
        super(RegistrationDomainMapping, self).__init__(
        )
        self.from_ = from_
        self.to = to

    @property
    def from_(self):
        """
        Returns the value of the `from_` property.
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        """
        Sets the value of the `from_` property.
        """
        Struct._check_type('from_', value, Domain)
        self._from_ = value

    @property
    def to(self):
        """
        Returns the value of the `to` property.
        """
        return self._to

    @to.setter
    def to(self, value):
        """
        Sets the value of the `to` property.
        """
        Struct._check_type('to', value, Domain)
        self._to = value


class RegistrationLunMapping(Struct):

    def __init__(
        self,
        from_=None,
        to=None,
    ):
        super(RegistrationLunMapping, self).__init__(
        )
        self.from_ = from_
        self.to = to

    @property
    def from_(self):
        """
        Returns the value of the `from_` property.
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        """
        Sets the value of the `from_` property.
        """
        Struct._check_type('from_', value, Disk)
        self._from_ = value

    @property
    def to(self):
        """
        Returns the value of the `to` property.
        """
        return self._to

    @to.setter
    def to(self, value):
        """
        Sets the value of the `to` property.
        """
        Struct._check_type('to', value, Disk)
        self._to = value


class RegistrationRoleMapping(Struct):

    def __init__(
        self,
        from_=None,
        to=None,
    ):
        super(RegistrationRoleMapping, self).__init__(
        )
        self.from_ = from_
        self.to = to

    @property
    def from_(self):
        """
        Returns the value of the `from_` property.
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        """
        Sets the value of the `from_` property.
        """
        Struct._check_type('from_', value, Role)
        self._from_ = value

    @property
    def to(self):
        """
        Returns the value of the `to` property.
        """
        return self._to

    @to.setter
    def to(self, value):
        """
        Sets the value of the `to` property.
        """
        Struct._check_type('to', value, Role)
        self._to = value


class RegistrationVnicProfileMapping(Struct):

    def __init__(
        self,
        from_=None,
        to=None,
    ):
        super(RegistrationVnicProfileMapping, self).__init__(
        )
        self.from_ = from_
        self.to = to

    @property
    def from_(self):
        """
        Returns the value of the `from_` property.
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        """
        Sets the value of the `from_` property.
        """
        Struct._check_type('from_', value, VnicProfile)
        self._from_ = value

    @property
    def to(self):
        """
        Returns the value of the `to` property.
        """
        return self._to

    @to.setter
    def to(self, value):
        """
        Sets the value of the `to` property.
        """
        Struct._check_type('to', value, VnicProfile)
        self._to = value


class ReportedConfiguration(Struct):

    def __init__(
        self,
        actual_value=None,
        expected_value=None,
        in_sync=None,
        name=None,
    ):
        super(ReportedConfiguration, self).__init__(
        )
        self.actual_value = actual_value
        self.expected_value = expected_value
        self.in_sync = in_sync
        self.name = name

    @property
    def in_sync(self):
        """
        Returns the value of the `in_sync` property.
        """
        return self._in_sync

    @in_sync.setter
    def in_sync(self, value):
        """
        Sets the value of the `in_sync` property.
        """
        self._in_sync = value

    @property
    def actual_value(self):
        """
        Returns the value of the `actual_value` property.
        """
        return self._actual_value

    @actual_value.setter
    def actual_value(self, value):
        """
        Sets the value of the `actual_value` property.
        """
        self._actual_value = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def expected_value(self):
        """
        Returns the value of the `expected_value` property.
        """
        return self._expected_value

    @expected_value.setter
    def expected_value(self, value):
        """
        Sets the value of the `expected_value` property.
        """
        self._expected_value = value


class ReportedDevice(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        ips=None,
        mac=None,
        name=None,
        type=None,
        vm=None,
    ):
        super(ReportedDevice, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.ips = ips
        self.mac = mac
        self.type = type
        self.vm = vm

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def ips(self):
        """
        Returns the value of the `ips` property.
        """
        return self._ips

    @ips.setter
    def ips(self, value):
        """
        Sets the value of the `ips` property.
        """
        self._ips = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, ReportedDeviceType)
        self._type = value

    @property
    def mac(self):
        """
        Returns the value of the `mac` property.
        """
        return self._mac

    @mac.setter
    def mac(self, value):
        """
        Sets the value of the `mac` property.
        """
        Struct._check_type('mac', value, Mac)
        self._mac = value


class RngDevice(Struct):

    def __init__(
        self,
        rate=None,
        source=None,
    ):
        super(RngDevice, self).__init__(
        )
        self.rate = rate
        self.source = source

    @property
    def rate(self):
        """
        Returns the value of the `rate` property.
        """
        return self._rate

    @rate.setter
    def rate(self, value):
        """
        Sets the value of the `rate` property.
        """
        Struct._check_type('rate', value, Rate)
        self._rate = value

    @property
    def source(self):
        """
        Returns the value of the `source` property.
        """
        return self._source

    @source.setter
    def source(self, value):
        """
        Sets the value of the `source` property.
        """
        Struct._check_type('source', value, RngSource)
        self._source = value


class Role(Identified):

    def __init__(
        self,
        administrative=None,
        comment=None,
        description=None,
        id=None,
        mutable=None,
        name=None,
        permits=None,
        user=None,
    ):
        super(Role, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.administrative = administrative
        self.mutable = mutable
        self.permits = permits
        self.user = user

    @property
    def administrative(self):
        """
        Returns the value of the `administrative` property.
        """
        return self._administrative

    @administrative.setter
    def administrative(self, value):
        """
        Sets the value of the `administrative` property.
        """
        self._administrative = value

    @property
    def mutable(self):
        """
        Returns the value of the `mutable` property.
        """
        return self._mutable

    @mutable.setter
    def mutable(self, value):
        """
        Sets the value of the `mutable` property.
        """
        self._mutable = value

    @property
    def permits(self):
        """
        Returns the value of the `permits` property.
        """
        return self._permits

    @permits.setter
    def permits(self, value):
        """
        Sets the value of the `permits` property.
        """
        self._permits = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value


class SchedulingPolicy(Identified):

    def __init__(
        self,
        balances=None,
        comment=None,
        default_policy=None,
        description=None,
        filters=None,
        id=None,
        locked=None,
        name=None,
        properties=None,
        weight=None,
    ):
        super(SchedulingPolicy, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.balances = balances
        self.default_policy = default_policy
        self.filters = filters
        self.locked = locked
        self.properties = properties
        self.weight = weight

    @property
    def balances(self):
        """
        Returns the value of the `balances` property.
        """
        return self._balances

    @balances.setter
    def balances(self, value):
        """
        Sets the value of the `balances` property.
        """
        self._balances = value

    @property
    def default_policy(self):
        """
        Returns the value of the `default_policy` property.
        """
        return self._default_policy

    @default_policy.setter
    def default_policy(self, value):
        """
        Sets the value of the `default_policy` property.
        """
        self._default_policy = value

    @property
    def weight(self):
        """
        Returns the value of the `weight` property.
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        """
        Sets the value of the `weight` property.
        """
        self._weight = value

    @property
    def filters(self):
        """
        Returns the value of the `filters` property.
        """
        return self._filters

    @filters.setter
    def filters(self, value):
        """
        Sets the value of the `filters` property.
        """
        self._filters = value

    @property
    def locked(self):
        """
        Returns the value of the `locked` property.
        """
        return self._locked

    @locked.setter
    def locked(self, value):
        """
        Sets the value of the `locked` property.
        """
        self._locked = value

    @property
    def properties(self):
        """
        Returns the value of the `properties` property.
        """
        return self._properties

    @properties.setter
    def properties(self, value):
        """
        Sets the value of the `properties` property.
        """
        self._properties = value


class SchedulingPolicyUnit(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        enabled=None,
        id=None,
        internal=None,
        name=None,
        properties=None,
        type=None,
    ):
        super(SchedulingPolicyUnit, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.enabled = enabled
        self.internal = internal
        self.properties = properties
        self.type = type

    @property
    def internal(self):
        """
        Returns the value of the `internal` property.
        """
        return self._internal

    @internal.setter
    def internal(self, value):
        """
        Sets the value of the `internal` property.
        """
        self._internal = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, PolicyUnitType)
        self._type = value

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value

    @property
    def properties(self):
        """
        Returns the value of the `properties` property.
        """
        return self._properties

    @properties.setter
    def properties(self, value):
        """
        Sets the value of the `properties` property.
        """
        self._properties = value


class SeLinux(Struct):

    def __init__(
        self,
        mode=None,
    ):
        super(SeLinux, self).__init__(
        )
        self.mode = mode

    @property
    def mode(self):
        """
        Returns the value of the `mode` property.
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """
        Sets the value of the `mode` property.
        """
        Struct._check_type('mode', value, SeLinuxMode)
        self._mode = value


class SerialNumber(Struct):

    def __init__(
        self,
        policy=None,
        value=None,
    ):
        super(SerialNumber, self).__init__(
        )
        self.policy = policy
        self.value = value

    @property
    def policy(self):
        """
        Returns the value of the `policy` property.
        """
        return self._policy

    @policy.setter
    def policy(self, value):
        """
        Sets the value of the `policy` property.
        """
        Struct._check_type('policy', value, SerialNumberPolicy)
        self._policy = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class Session(Identified):

    def __init__(
        self,
        comment=None,
        console_user=None,
        description=None,
        id=None,
        ip=None,
        name=None,
        protocol=None,
        user=None,
        vm=None,
    ):
        super(Session, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.console_user = console_user
        self.ip = ip
        self.protocol = protocol
        self.user = user
        self.vm = vm

    @property
    def ip(self):
        """
        Returns the value of the `ip` property.
        """
        return self._ip

    @ip.setter
    def ip(self, value):
        """
        Sets the value of the `ip` property.
        """
        Struct._check_type('ip', value, Ip)
        self._ip = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def console_user(self):
        """
        Returns the value of the `console_user` property.
        """
        return self._console_user

    @console_user.setter
    def console_user(self, value):
        """
        Sets the value of the `console_user` property.
        """
        self._console_user = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def protocol(self):
        """
        Returns the value of the `protocol` property.
        """
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        """
        Sets the value of the `protocol` property.
        """
        self._protocol = value


class SkipIfConnectivityBroken(Struct):

    def __init__(
        self,
        enabled=None,
        threshold=None,
    ):
        super(SkipIfConnectivityBroken, self).__init__(
        )
        self.enabled = enabled
        self.threshold = threshold

    @property
    def threshold(self):
        """
        Returns the value of the `threshold` property.
        """
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        """
        Sets the value of the `threshold` property.
        """
        self._threshold = value

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class SkipIfSdActive(Struct):

    def __init__(
        self,
        enabled=None,
    ):
        super(SkipIfSdActive, self).__init__(
        )
        self.enabled = enabled

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class SpecialObjects(Struct):

    def __init__(
        self,
        blank_template=None,
        root_tag=None,
    ):
        super(SpecialObjects, self).__init__(
        )
        self.blank_template = blank_template
        self.root_tag = root_tag

    @property
    def blank_template(self):
        """
        Returns the value of the `blank_template` property.
        """
        return self._blank_template

    @blank_template.setter
    def blank_template(self, value):
        """
        Sets the value of the `blank_template` property.
        """
        Struct._check_type('blank_template', value, Template)
        self._blank_template = value

    @property
    def root_tag(self):
        """
        Returns the value of the `root_tag` property.
        """
        return self._root_tag

    @root_tag.setter
    def root_tag(self, value):
        """
        Sets the value of the `root_tag` property.
        """
        Struct._check_type('root_tag', value, Tag)
        self._root_tag = value


class Spm(Struct):

    def __init__(
        self,
        priority=None,
        status=None,
    ):
        super(Spm, self).__init__(
        )
        self.priority = priority
        self.status = status

    @property
    def priority(self):
        """
        Returns the value of the `priority` property.
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """
        Sets the value of the `priority` property.
        """
        self._priority = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, SpmStatus)
        self._status = value


class Ssh(Identified):

    def __init__(
        self,
        authentication_method=None,
        comment=None,
        description=None,
        fingerprint=None,
        id=None,
        name=None,
        port=None,
        public_key=None,
        user=None,
    ):
        super(Ssh, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.authentication_method = authentication_method
        self.fingerprint = fingerprint
        self.port = port
        self.public_key = public_key
        self.user = user

    @property
    def authentication_method(self):
        """
        Returns the value of the `authentication_method` property.
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, value):
        """
        Sets the value of the `authentication_method` property.
        """
        Struct._check_type('authentication_method', value, SshAuthenticationMethod)
        self._authentication_method = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def public_key(self):
        """
        Returns the value of the `public_key` property.
        """
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        """
        Sets the value of the `public_key` property.
        """
        self._public_key = value

    @property
    def fingerprint(self):
        """
        Returns the value of the `fingerprint` property.
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, value):
        """
        Sets the value of the `fingerprint` property.
        """
        self._fingerprint = value


class SshPublicKey(Identified):

    def __init__(
        self,
        comment=None,
        content=None,
        description=None,
        id=None,
        name=None,
        user=None,
    ):
        super(SshPublicKey, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.content = content
        self.user = user

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def content(self):
        """
        Returns the value of the `content` property.
        """
        return self._content

    @content.setter
    def content(self, value):
        """
        Sets the value of the `content` property.
        """
        self._content = value


class Sso(Struct):

    def __init__(
        self,
        methods=None,
    ):
        super(Sso, self).__init__(
        )
        self.methods = methods

    @property
    def methods(self):
        """
        Returns the value of the `methods` property.
        """
        return self._methods

    @methods.setter
    def methods(self, value):
        """
        Sets the value of the `methods` property.
        """
        self._methods = value


class Statistic(Identified):

    def __init__(
        self,
        brick=None,
        comment=None,
        description=None,
        disk=None,
        gluster_volume=None,
        host=None,
        host_nic=None,
        host_numa_node=None,
        id=None,
        kind=None,
        name=None,
        nic=None,
        step=None,
        type=None,
        unit=None,
        values=None,
        vm=None,
    ):
        super(Statistic, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.brick = brick
        self.disk = disk
        self.gluster_volume = gluster_volume
        self.host = host
        self.host_nic = host_nic
        self.host_numa_node = host_numa_node
        self.kind = kind
        self.nic = nic
        self.step = step
        self.type = type
        self.unit = unit
        self.values = values
        self.vm = vm

    @property
    def kind(self):
        """
        Returns the value of the `kind` property.
        """
        return self._kind

    @kind.setter
    def kind(self, value):
        """
        Sets the value of the `kind` property.
        """
        Struct._check_type('kind', value, StatisticKind)
        self._kind = value

    @property
    def values(self):
        """
        Returns the value of the `values` property.
        """
        return self._values

    @values.setter
    def values(self, value):
        """
        Sets the value of the `values` property.
        """
        self._values = value

    @property
    def nic(self):
        """
        Returns the value of the `nic` property.
        """
        return self._nic

    @nic.setter
    def nic(self, value):
        """
        Sets the value of the `nic` property.
        """
        Struct._check_type('nic', value, Nic)
        self._nic = value

    @property
    def gluster_volume(self):
        """
        Returns the value of the `gluster_volume` property.
        """
        return self._gluster_volume

    @gluster_volume.setter
    def gluster_volume(self, value):
        """
        Sets the value of the `gluster_volume` property.
        """
        Struct._check_type('gluster_volume', value, GlusterVolume)
        self._gluster_volume = value

    @property
    def host_numa_node(self):
        """
        Returns the value of the `host_numa_node` property.
        """
        return self._host_numa_node

    @host_numa_node.setter
    def host_numa_node(self, value):
        """
        Sets the value of the `host_numa_node` property.
        """
        Struct._check_type('host_numa_node', value, NumaNode)
        self._host_numa_node = value

    @property
    def host_nic(self):
        """
        Returns the value of the `host_nic` property.
        """
        return self._host_nic

    @host_nic.setter
    def host_nic(self, value):
        """
        Sets the value of the `host_nic` property.
        """
        Struct._check_type('host_nic', value, HostNic)
        self._host_nic = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, ValueType)
        self._type = value

    @property
    def disk(self):
        """
        Returns the value of the `disk` property.
        """
        return self._disk

    @disk.setter
    def disk(self, value):
        """
        Sets the value of the `disk` property.
        """
        Struct._check_type('disk', value, Disk)
        self._disk = value

    @property
    def unit(self):
        """
        Returns the value of the `unit` property.
        """
        return self._unit

    @unit.setter
    def unit(self, value):
        """
        Sets the value of the `unit` property.
        """
        Struct._check_type('unit', value, StatisticUnit)
        self._unit = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def brick(self):
        """
        Returns the value of the `brick` property.
        """
        return self._brick

    @brick.setter
    def brick(self, value):
        """
        Sets the value of the `brick` property.
        """
        Struct._check_type('brick', value, GlusterBrick)
        self._brick = value

    @property
    def step(self):
        """
        Returns the value of the `step` property.
        """
        return self._step

    @step.setter
    def step(self, value):
        """
        Sets the value of the `step` property.
        """
        Struct._check_type('step', value, Step)
        self._step = value


class Step(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        end_time=None,
        execution_host=None,
        external=None,
        external_type=None,
        id=None,
        job=None,
        name=None,
        number=None,
        parent_step=None,
        progress=None,
        start_time=None,
        statistics=None,
        status=None,
        type=None,
    ):
        super(Step, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.end_time = end_time
        self.execution_host = execution_host
        self.external = external
        self.external_type = external_type
        self.job = job
        self.number = number
        self.parent_step = parent_step
        self.progress = progress
        self.start_time = start_time
        self.statistics = statistics
        self.status = status
        self.type = type

    @property
    def number(self):
        """
        Returns the value of the `number` property.
        """
        return self._number

    @number.setter
    def number(self, value):
        """
        Sets the value of the `number` property.
        """
        self._number = value

    @property
    def external(self):
        """
        Returns the value of the `external` property.
        """
        return self._external

    @external.setter
    def external(self, value):
        """
        Sets the value of the `external` property.
        """
        self._external = value

    @property
    def end_time(self):
        """
        Returns the value of the `end_time` property.
        """
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        """
        Sets the value of the `end_time` property.
        """
        self._end_time = value

    @property
    def start_time(self):
        """
        Returns the value of the `start_time` property.
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """
        Sets the value of the `start_time` property.
        """
        self._start_time = value

    @property
    def progress(self):
        """
        Returns the value of the `progress` property.
        """
        return self._progress

    @progress.setter
    def progress(self, value):
        """
        Sets the value of the `progress` property.
        """
        self._progress = value

    @property
    def execution_host(self):
        """
        Returns the value of the `execution_host` property.
        """
        return self._execution_host

    @execution_host.setter
    def execution_host(self, value):
        """
        Sets the value of the `execution_host` property.
        """
        Struct._check_type('execution_host', value, Host)
        self._execution_host = value

    @property
    def external_type(self):
        """
        Returns the value of the `external_type` property.
        """
        return self._external_type

    @external_type.setter
    def external_type(self, value):
        """
        Sets the value of the `external_type` property.
        """
        Struct._check_type('external_type', value, ExternalSystemType)
        self._external_type = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, StepStatus)
        self._status = value

    @property
    def job(self):
        """
        Returns the value of the `job` property.
        """
        return self._job

    @job.setter
    def job(self, value):
        """
        Sets the value of the `job` property.
        """
        Struct._check_type('job', value, Job)
        self._job = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, StepEnum)
        self._type = value

    @property
    def parent_step(self):
        """
        Returns the value of the `parent_step` property.
        """
        return self._parent_step

    @parent_step.setter
    def parent_step(self, value):
        """
        Sets the value of the `parent_step` property.
        """
        Struct._check_type('parent_step', value, Step)
        self._parent_step = value


class StorageConnection(Identified):

    def __init__(
        self,
        address=None,
        comment=None,
        description=None,
        gluster_volume=None,
        host=None,
        id=None,
        mount_options=None,
        name=None,
        nfs_retrans=None,
        nfs_timeo=None,
        nfs_version=None,
        password=None,
        path=None,
        port=None,
        portal=None,
        target=None,
        type=None,
        username=None,
        vfs_type=None,
    ):
        super(StorageConnection, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.address = address
        self.gluster_volume = gluster_volume
        self.host = host
        self.mount_options = mount_options
        self.nfs_retrans = nfs_retrans
        self.nfs_timeo = nfs_timeo
        self.nfs_version = nfs_version
        self.password = password
        self.path = path
        self.port = port
        self.portal = portal
        self.target = target
        self.type = type
        self.username = username
        self.vfs_type = vfs_type

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def gluster_volume(self):
        """
        Returns the value of the `gluster_volume` property.
        """
        return self._gluster_volume

    @gluster_volume.setter
    def gluster_volume(self, value):
        """
        Sets the value of the `gluster_volume` property.
        """
        Struct._check_type('gluster_volume', value, GlusterVolume)
        self._gluster_volume = value

    @property
    def target(self):
        """
        Returns the value of the `target` property.
        """
        return self._target

    @target.setter
    def target(self, value):
        """
        Sets the value of the `target` property.
        """
        self._target = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, StorageType)
        self._type = value

    @property
    def nfs_timeo(self):
        """
        Returns the value of the `nfs_timeo` property.
        """
        return self._nfs_timeo

    @nfs_timeo.setter
    def nfs_timeo(self, value):
        """
        Sets the value of the `nfs_timeo` property.
        """
        self._nfs_timeo = value

    @property
    def path(self):
        """
        Returns the value of the `path` property.
        """
        return self._path

    @path.setter
    def path(self, value):
        """
        Sets the value of the `path` property.
        """
        self._path = value

    @property
    def nfs_retrans(self):
        """
        Returns the value of the `nfs_retrans` property.
        """
        return self._nfs_retrans

    @nfs_retrans.setter
    def nfs_retrans(self, value):
        """
        Sets the value of the `nfs_retrans` property.
        """
        self._nfs_retrans = value

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def vfs_type(self):
        """
        Returns the value of the `vfs_type` property.
        """
        return self._vfs_type

    @vfs_type.setter
    def vfs_type(self, value):
        """
        Sets the value of the `vfs_type` property.
        """
        self._vfs_type = value

    @property
    def nfs_version(self):
        """
        Returns the value of the `nfs_version` property.
        """
        return self._nfs_version

    @nfs_version.setter
    def nfs_version(self, value):
        """
        Sets the value of the `nfs_version` property.
        """
        Struct._check_type('nfs_version', value, NfsVersion)
        self._nfs_version = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def portal(self):
        """
        Returns the value of the `portal` property.
        """
        return self._portal

    @portal.setter
    def portal(self, value):
        """
        Sets the value of the `portal` property.
        """
        self._portal = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def mount_options(self):
        """
        Returns the value of the `mount_options` property.
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, value):
        """
        Sets the value of the `mount_options` property.
        """
        self._mount_options = value


class StorageConnectionExtension(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        host=None,
        id=None,
        name=None,
        password=None,
        target=None,
        username=None,
    ):
        super(StorageConnectionExtension, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.host = host
        self.password = password
        self.target = target
        self.username = username

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def target(self):
        """
        Returns the value of the `target` property.
        """
        return self._target

    @target.setter
    def target(self, value):
        """
        Sets the value of the `target` property.
        """
        self._target = value


class StorageDomain(Identified):

    def __init__(
        self,
        available=None,
        backup=None,
        block_size=None,
        comment=None,
        committed=None,
        critical_space_action_blocker=None,
        data_center=None,
        data_centers=None,
        description=None,
        discard_after_delete=None,
        disk_profiles=None,
        disk_snapshots=None,
        disks=None,
        external_status=None,
        files=None,
        host=None,
        id=None,
        images=None,
        import_=None,
        master=None,
        name=None,
        permissions=None,
        status=None,
        storage=None,
        storage_connections=None,
        storage_format=None,
        supports_discard=None,
        supports_discard_zeroes_data=None,
        templates=None,
        type=None,
        used=None,
        vms=None,
        warning_low_space_indicator=None,
        wipe_after_delete=None,
    ):
        super(StorageDomain, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.available = available
        self.backup = backup
        self.block_size = block_size
        self.committed = committed
        self.critical_space_action_blocker = critical_space_action_blocker
        self.data_center = data_center
        self.data_centers = data_centers
        self.discard_after_delete = discard_after_delete
        self.disk_profiles = disk_profiles
        self.disk_snapshots = disk_snapshots
        self.disks = disks
        self.external_status = external_status
        self.files = files
        self.host = host
        self.images = images
        self.import_ = import_
        self.master = master
        self.permissions = permissions
        self.status = status
        self.storage = storage
        self.storage_connections = storage_connections
        self.storage_format = storage_format
        self.supports_discard = supports_discard
        self.supports_discard_zeroes_data = supports_discard_zeroes_data
        self.templates = templates
        self.type = type
        self.used = used
        self.vms = vms
        self.warning_low_space_indicator = warning_low_space_indicator
        self.wipe_after_delete = wipe_after_delete

    @property
    def data_centers(self):
        """
        Returns the value of the `data_centers` property.
        """
        return self._data_centers

    @data_centers.setter
    def data_centers(self, value):
        """
        Sets the value of the `data_centers` property.
        """
        self._data_centers = value

    @property
    def block_size(self):
        """
        Returns the value of the `block_size` property.
        """
        return self._block_size

    @block_size.setter
    def block_size(self, value):
        """
        Sets the value of the `block_size` property.
        """
        self._block_size = value

    @property
    def committed(self):
        """
        Returns the value of the `committed` property.
        """
        return self._committed

    @committed.setter
    def committed(self, value):
        """
        Sets the value of the `committed` property.
        """
        self._committed = value

    @property
    def warning_low_space_indicator(self):
        """
        Returns the value of the `warning_low_space_indicator` property.
        """
        return self._warning_low_space_indicator

    @warning_low_space_indicator.setter
    def warning_low_space_indicator(self, value):
        """
        Sets the value of the `warning_low_space_indicator` property.
        """
        self._warning_low_space_indicator = value

    @property
    def templates(self):
        """
        Returns the value of the `templates` property.
        """
        return self._templates

    @templates.setter
    def templates(self, value):
        """
        Sets the value of the `templates` property.
        """
        self._templates = value

    @property
    def external_status(self):
        """
        Returns the value of the `external_status` property.
        """
        return self._external_status

    @external_status.setter
    def external_status(self, value):
        """
        Sets the value of the `external_status` property.
        """
        Struct._check_type('external_status', value, ExternalStatus)
        self._external_status = value

    @property
    def master(self):
        """
        Returns the value of the `master` property.
        """
        return self._master

    @master.setter
    def master(self, value):
        """
        Sets the value of the `master` property.
        """
        self._master = value

    @property
    def discard_after_delete(self):
        """
        Returns the value of the `discard_after_delete` property.
        """
        return self._discard_after_delete

    @discard_after_delete.setter
    def discard_after_delete(self, value):
        """
        Sets the value of the `discard_after_delete` property.
        """
        self._discard_after_delete = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def images(self):
        """
        Returns the value of the `images` property.
        """
        return self._images

    @images.setter
    def images(self, value):
        """
        Sets the value of the `images` property.
        """
        self._images = value

    @property
    def supports_discard_zeroes_data(self):
        """
        Returns the value of the `supports_discard_zeroes_data` property.
        """
        return self._supports_discard_zeroes_data

    @supports_discard_zeroes_data.setter
    def supports_discard_zeroes_data(self, value):
        """
        Sets the value of the `supports_discard_zeroes_data` property.
        """
        self._supports_discard_zeroes_data = value

    @property
    def files(self):
        """
        Returns the value of the `files` property.
        """
        return self._files

    @files.setter
    def files(self, value):
        """
        Sets the value of the `files` property.
        """
        self._files = value

    @property
    def storage_connections(self):
        """
        Returns the value of the `storage_connections` property.
        """
        return self._storage_connections

    @storage_connections.setter
    def storage_connections(self, value):
        """
        Sets the value of the `storage_connections` property.
        """
        self._storage_connections = value

    @property
    def disk_profiles(self):
        """
        Returns the value of the `disk_profiles` property.
        """
        return self._disk_profiles

    @disk_profiles.setter
    def disk_profiles(self, value):
        """
        Sets the value of the `disk_profiles` property.
        """
        self._disk_profiles = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, StorageDomainStatus)
        self._status = value

    @property
    def backup(self):
        """
        Returns the value of the `backup` property.
        """
        return self._backup

    @backup.setter
    def backup(self, value):
        """
        Sets the value of the `backup` property.
        """
        self._backup = value

    @property
    def disk_snapshots(self):
        """
        Returns the value of the `disk_snapshots` property.
        """
        return self._disk_snapshots

    @disk_snapshots.setter
    def disk_snapshots(self, value):
        """
        Sets the value of the `disk_snapshots` property.
        """
        self._disk_snapshots = value

    @property
    def storage_format(self):
        """
        Returns the value of the `storage_format` property.
        """
        return self._storage_format

    @storage_format.setter
    def storage_format(self, value):
        """
        Sets the value of the `storage_format` property.
        """
        Struct._check_type('storage_format', value, StorageFormat)
        self._storage_format = value

    @property
    def import_(self):
        """
        Returns the value of the `import_` property.
        """
        return self._import_

    @import_.setter
    def import_(self, value):
        """
        Sets the value of the `import_` property.
        """
        self._import_ = value

    @property
    def disks(self):
        """
        Returns the value of the `disks` property.
        """
        return self._disks

    @disks.setter
    def disks(self, value):
        """
        Sets the value of the `disks` property.
        """
        self._disks = value

    @property
    def available(self):
        """
        Returns the value of the `available` property.
        """
        return self._available

    @available.setter
    def available(self, value):
        """
        Sets the value of the `available` property.
        """
        self._available = value

    @property
    def storage(self):
        """
        Returns the value of the `storage` property.
        """
        return self._storage

    @storage.setter
    def storage(self, value):
        """
        Sets the value of the `storage` property.
        """
        Struct._check_type('storage', value, HostStorage)
        self._storage = value

    @property
    def used(self):
        """
        Returns the value of the `used` property.
        """
        return self._used

    @used.setter
    def used(self, value):
        """
        Sets the value of the `used` property.
        """
        self._used = value

    @property
    def supports_discard(self):
        """
        Returns the value of the `supports_discard` property.
        """
        return self._supports_discard

    @supports_discard.setter
    def supports_discard(self, value):
        """
        Sets the value of the `supports_discard` property.
        """
        self._supports_discard = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, StorageDomainType)
        self._type = value

    @property
    def critical_space_action_blocker(self):
        """
        Returns the value of the `critical_space_action_blocker` property.
        """
        return self._critical_space_action_blocker

    @critical_space_action_blocker.setter
    def critical_space_action_blocker(self, value):
        """
        Sets the value of the `critical_space_action_blocker` property.
        """
        self._critical_space_action_blocker = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def wipe_after_delete(self):
        """
        Returns the value of the `wipe_after_delete` property.
        """
        return self._wipe_after_delete

    @wipe_after_delete.setter
    def wipe_after_delete(self, value):
        """
        Sets the value of the `wipe_after_delete` property.
        """
        self._wipe_after_delete = value

    @property
    def vms(self):
        """
        Returns the value of the `vms` property.
        """
        return self._vms

    @vms.setter
    def vms(self, value):
        """
        Sets the value of the `vms` property.
        """
        self._vms = value


class StorageDomainLease(Struct):

    def __init__(
        self,
        storage_domain=None,
    ):
        super(StorageDomainLease, self).__init__(
        )
        self.storage_domain = storage_domain

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value


class SystemOption(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        values=None,
    ):
        super(SystemOption, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.values = values

    @property
    def values(self):
        """
        Returns the value of the `values` property.
        """
        return self._values

    @values.setter
    def values(self, value):
        """
        Sets the value of the `values` property.
        """
        self._values = value


class SystemOptionValue(Struct):

    def __init__(
        self,
        value=None,
        version=None,
    ):
        super(SystemOptionValue, self).__init__(
        )
        self.value = value
        self.version = version

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        self._version = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class Tag(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        group=None,
        host=None,
        id=None,
        name=None,
        parent=None,
        template=None,
        user=None,
        vm=None,
    ):
        super(Tag, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.group = group
        self.host = host
        self.parent = parent
        self.template = template
        self.user = user
        self.vm = vm

    @property
    def parent(self):
        """
        Returns the value of the `parent` property.
        """
        return self._parent

    @parent.setter
    def parent(self, value):
        """
        Sets the value of the `parent` property.
        """
        Struct._check_type('parent', value, Tag)
        self._parent = value

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def group(self):
        """
        Returns the value of the `group` property.
        """
        return self._group

    @group.setter
    def group(self, value):
        """
        Sets the value of the `group` property.
        """
        Struct._check_type('group', value, Group)
        self._group = value


class TemplateVersion(Struct):

    def __init__(
        self,
        base_template=None,
        version_name=None,
        version_number=None,
    ):
        super(TemplateVersion, self).__init__(
        )
        self.base_template = base_template
        self.version_name = version_name
        self.version_number = version_number

    @property
    def version_number(self):
        """
        Returns the value of the `version_number` property.
        """
        return self._version_number

    @version_number.setter
    def version_number(self, value):
        """
        Sets the value of the `version_number` property.
        """
        self._version_number = value

    @property
    def version_name(self):
        """
        Returns the value of the `version_name` property.
        """
        return self._version_name

    @version_name.setter
    def version_name(self, value):
        """
        Sets the value of the `version_name` property.
        """
        self._version_name = value

    @property
    def base_template(self):
        """
        Returns the value of the `base_template` property.
        """
        return self._base_template

    @base_template.setter
    def base_template(self, value):
        """
        Sets the value of the `base_template` property.
        """
        Struct._check_type('base_template', value, Template)
        self._base_template = value


class Ticket(Struct):

    def __init__(
        self,
        expiry=None,
        value=None,
    ):
        super(Ticket, self).__init__(
        )
        self.expiry = expiry
        self.value = value

    @property
    def expiry(self):
        """
        Returns the value of the `expiry` property.
        """
        return self._expiry

    @expiry.setter
    def expiry(self, value):
        """
        Sets the value of the `expiry` property.
        """
        self._expiry = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class TimeZone(Struct):

    def __init__(
        self,
        name=None,
        utc_offset=None,
    ):
        super(TimeZone, self).__init__(
        )
        self.name = name
        self.utc_offset = utc_offset

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def utc_offset(self):
        """
        Returns the value of the `utc_offset` property.
        """
        return self._utc_offset

    @utc_offset.setter
    def utc_offset(self, value):
        """
        Sets the value of the `utc_offset` property.
        """
        self._utc_offset = value


class TransparentHugePages(Struct):

    def __init__(
        self,
        enabled=None,
    ):
        super(TransparentHugePages, self).__init__(
        )
        self.enabled = enabled

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class UnmanagedNetwork(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        host=None,
        host_nic=None,
        id=None,
        name=None,
    ):
        super(UnmanagedNetwork, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.host = host
        self.host_nic = host_nic

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def host_nic(self):
        """
        Returns the value of the `host_nic` property.
        """
        return self._host_nic

    @host_nic.setter
    def host_nic(self, value):
        """
        Sets the value of the `host_nic` property.
        """
        Struct._check_type('host_nic', value, HostNic)
        self._host_nic = value


class Usb(Struct):

    def __init__(
        self,
        enabled=None,
        type=None,
    ):
        super(Usb, self).__init__(
        )
        self.enabled = enabled
        self.type = type

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, UsbType)
        self._type = value


class User(Identified):

    def __init__(
        self,
        comment=None,
        department=None,
        description=None,
        domain=None,
        domain_entry_id=None,
        email=None,
        groups=None,
        id=None,
        last_name=None,
        logged_in=None,
        name=None,
        namespace=None,
        options=None,
        password=None,
        permissions=None,
        principal=None,
        roles=None,
        ssh_public_keys=None,
        tags=None,
        user_name=None,
        user_options=None,
    ):
        super(User, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.department = department
        self.domain = domain
        self.domain_entry_id = domain_entry_id
        self.email = email
        self.groups = groups
        self.last_name = last_name
        self.logged_in = logged_in
        self.namespace = namespace
        self.options = options
        self.password = password
        self.permissions = permissions
        self.principal = principal
        self.roles = roles
        self.ssh_public_keys = ssh_public_keys
        self.tags = tags
        self.user_name = user_name
        self.user_options = user_options

    @property
    def logged_in(self):
        """
        Returns the value of the `logged_in` property.
        """
        return self._logged_in

    @logged_in.setter
    def logged_in(self, value):
        """
        Sets the value of the `logged_in` property.
        """
        self._logged_in = value

    @property
    def last_name(self):
        """
        Returns the value of the `last_name` property.
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Sets the value of the `last_name` property.
        """
        self._last_name = value

    @property
    def roles(self):
        """
        Returns the value of the `roles` property.
        """
        return self._roles

    @roles.setter
    def roles(self, value):
        """
        Sets the value of the `roles` property.
        """
        self._roles = value

    @property
    def ssh_public_keys(self):
        """
        Returns the value of the `ssh_public_keys` property.
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, value):
        """
        Sets the value of the `ssh_public_keys` property.
        """
        self._ssh_public_keys = value

    @property
    def groups(self):
        """
        Returns the value of the `groups` property.
        """
        return self._groups

    @groups.setter
    def groups(self, value):
        """
        Sets the value of the `groups` property.
        """
        self._groups = value

    @property
    def tags(self):
        """
        Returns the value of the `tags` property.
        """
        return self._tags

    @tags.setter
    def tags(self, value):
        """
        Sets the value of the `tags` property.
        """
        self._tags = value

    @property
    def domain(self):
        """
        Returns the value of the `domain` property.
        """
        return self._domain

    @domain.setter
    def domain(self, value):
        """
        Sets the value of the `domain` property.
        """
        Struct._check_type('domain', value, Domain)
        self._domain = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def principal(self):
        """
        Returns the value of the `principal` property.
        """
        return self._principal

    @principal.setter
    def principal(self, value):
        """
        Sets the value of the `principal` property.
        """
        self._principal = value

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def namespace(self):
        """
        Returns the value of the `namespace` property.
        """
        return self._namespace

    @namespace.setter
    def namespace(self, value):
        """
        Sets the value of the `namespace` property.
        """
        self._namespace = value

    @property
    def email(self):
        """
        Returns the value of the `email` property.
        """
        return self._email

    @email.setter
    def email(self, value):
        """
        Sets the value of the `email` property.
        """
        self._email = value

    @property
    def user_options(self):
        """
        Returns the value of the `user_options` property.
        """
        return self._user_options

    @user_options.setter
    def user_options(self, value):
        """
        Sets the value of the `user_options` property.
        """
        self._user_options = value

    @property
    def user_name(self):
        """
        Returns the value of the `user_name` property.
        """
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """
        Sets the value of the `user_name` property.
        """
        self._user_name = value

    @property
    def options(self):
        """
        Returns the value of the `options` property.
        """
        return self._options

    @options.setter
    def options(self, value):
        """
        Sets the value of the `options` property.
        """
        self._options = value

    @property
    def domain_entry_id(self):
        """
        Returns the value of the `domain_entry_id` property.
        """
        return self._domain_entry_id

    @domain_entry_id.setter
    def domain_entry_id(self, value):
        """
        Sets the value of the `domain_entry_id` property.
        """
        self._domain_entry_id = value

    @property
    def department(self):
        """
        Returns the value of the `department` property.
        """
        return self._department

    @department.setter
    def department(self, value):
        """
        Sets the value of the `department` property.
        """
        self._department = value


class UserOption(Identified):

    def __init__(
        self,
        comment=None,
        content=None,
        description=None,
        id=None,
        name=None,
        user=None,
    ):
        super(UserOption, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.content = content
        self.user = user

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def content(self):
        """
        Returns the value of the `content` property.
        """
        return self._content

    @content.setter
    def content(self, value):
        """
        Sets the value of the `content` property.
        """
        self._content = value


class Value(Struct):

    def __init__(
        self,
        datum=None,
        detail=None,
    ):
        super(Value, self).__init__(
        )
        self.datum = datum
        self.detail = detail

    @property
    def datum(self):
        """
        Returns the value of the `datum` property.
        """
        return self._datum

    @datum.setter
    def datum(self, value):
        """
        Sets the value of the `datum` property.
        """
        self._datum = value

    @property
    def detail(self):
        """
        Returns the value of the `detail` property.
        """
        return self._detail

    @detail.setter
    def detail(self, value):
        """
        Sets the value of the `detail` property.
        """
        self._detail = value


class VcpuPin(Struct):

    def __init__(
        self,
        cpu_set=None,
        vcpu=None,
    ):
        super(VcpuPin, self).__init__(
        )
        self.cpu_set = cpu_set
        self.vcpu = vcpu

    @property
    def vcpu(self):
        """
        Returns the value of the `vcpu` property.
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, value):
        """
        Sets the value of the `vcpu` property.
        """
        self._vcpu = value

    @property
    def cpu_set(self):
        """
        Returns the value of the `cpu_set` property.
        """
        return self._cpu_set

    @cpu_set.setter
    def cpu_set(self, value):
        """
        Sets the value of the `cpu_set` property.
        """
        self._cpu_set = value


class Vendor(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
    ):
        super(Vendor, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        pass


class Version(Identified):

    def __init__(
        self,
        build=None,
        comment=None,
        description=None,
        full_version=None,
        id=None,
        major=None,
        minor=None,
        name=None,
        revision=None,
    ):
        super(Version, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.build = build
        self.full_version = full_version
        self.major = major
        self.minor = minor
        self.revision = revision

    @property
    def full_version(self):
        """
        Returns the value of the `full_version` property.
        """
        return self._full_version

    @full_version.setter
    def full_version(self, value):
        """
        Sets the value of the `full_version` property.
        """
        self._full_version = value

    @property
    def major(self):
        """
        Returns the value of the `major` property.
        """
        return self._major

    @major.setter
    def major(self, value):
        """
        Sets the value of the `major` property.
        """
        self._major = value

    @property
    def minor(self):
        """
        Returns the value of the `minor` property.
        """
        return self._minor

    @minor.setter
    def minor(self, value):
        """
        Sets the value of the `minor` property.
        """
        self._minor = value

    @property
    def build(self):
        """
        Returns the value of the `build` property.
        """
        return self._build

    @build.setter
    def build(self, value):
        """
        Sets the value of the `build` property.
        """
        self._build = value

    @property
    def revision(self):
        """
        Returns the value of the `revision` property.
        """
        return self._revision

    @revision.setter
    def revision(self, value):
        """
        Sets the value of the `revision` property.
        """
        self._revision = value


class VirtioScsi(Struct):

    def __init__(
        self,
        enabled=None,
    ):
        super(VirtioScsi, self).__init__(
        )
        self.enabled = enabled

    @property
    def enabled(self):
        """
        Returns the value of the `enabled` property.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Sets the value of the `enabled` property.
        """
        self._enabled = value


class VirtualNumaNode(NumaNode):

    def __init__(
        self,
        comment=None,
        cpu=None,
        description=None,
        host=None,
        id=None,
        index=None,
        memory=None,
        name=None,
        node_distance=None,
        numa_node_pins=None,
        numa_tune_mode=None,
        statistics=None,
        vm=None,
    ):
        super(VirtualNumaNode, self).__init__(
            comment=comment,
            cpu=cpu,
            description=description,
            host=host,
            id=id,
            index=index,
            memory=memory,
            name=name,
            node_distance=node_distance,
            statistics=statistics,
        )
        self.numa_node_pins = numa_node_pins
        self.numa_tune_mode = numa_tune_mode
        self.vm = vm

    @property
    def numa_tune_mode(self):
        """
        Returns the value of the `numa_tune_mode` property.
        """
        return self._numa_tune_mode

    @numa_tune_mode.setter
    def numa_tune_mode(self, value):
        """
        Sets the value of the `numa_tune_mode` property.
        """
        Struct._check_type('numa_tune_mode', value, NumaTuneMode)
        self._numa_tune_mode = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def numa_node_pins(self):
        """
        Returns the value of the `numa_node_pins` property.
        """
        return self._numa_node_pins

    @numa_node_pins.setter
    def numa_node_pins(self, value):
        """
        Sets the value of the `numa_node_pins` property.
        """
        self._numa_node_pins = value


class Vlan(Struct):

    def __init__(
        self,
        id=None,
    ):
        super(Vlan, self).__init__(
        )
        self.id = id

    @property
    def id(self):
        """
        Returns the value of the `id` property.
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        Sets the value of the `id` property.
        """
        self._id = value


class VmBase(Identified):

    def __init__(
        self,
        auto_pinning_policy=None,
        bios=None,
        cluster=None,
        comment=None,
        console=None,
        cpu=None,
        cpu_profile=None,
        cpu_shares=None,
        creation_time=None,
        custom_compatibility_version=None,
        custom_cpu_model=None,
        custom_emulated_machine=None,
        custom_properties=None,
        delete_protected=None,
        description=None,
        display=None,
        domain=None,
        high_availability=None,
        id=None,
        initialization=None,
        io=None,
        large_icon=None,
        lease=None,
        memory=None,
        memory_policy=None,
        migration=None,
        migration_downtime=None,
        multi_queues_enabled=None,
        name=None,
        origin=None,
        os=None,
        placement_policy=None,
        quota=None,
        rng_device=None,
        serial_number=None,
        small_icon=None,
        soundcard_enabled=None,
        sso=None,
        start_paused=None,
        stateless=None,
        storage_domain=None,
        storage_error_resume_behaviour=None,
        time_zone=None,
        tpm_enabled=None,
        tunnel_migration=None,
        type=None,
        usb=None,
        virtio_scsi=None,
        virtio_scsi_multi_queues=None,
        virtio_scsi_multi_queues_enabled=None,
    ):
        super(VmBase, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.auto_pinning_policy = auto_pinning_policy
        self.bios = bios
        self.cluster = cluster
        self.console = console
        self.cpu = cpu
        self.cpu_profile = cpu_profile
        self.cpu_shares = cpu_shares
        self.creation_time = creation_time
        self.custom_compatibility_version = custom_compatibility_version
        self.custom_cpu_model = custom_cpu_model
        self.custom_emulated_machine = custom_emulated_machine
        self.custom_properties = custom_properties
        self.delete_protected = delete_protected
        self.display = display
        self.domain = domain
        self.high_availability = high_availability
        self.initialization = initialization
        self.io = io
        self.large_icon = large_icon
        self.lease = lease
        self.memory = memory
        self.memory_policy = memory_policy
        self.migration = migration
        self.migration_downtime = migration_downtime
        self.multi_queues_enabled = multi_queues_enabled
        self.origin = origin
        self.os = os
        self.placement_policy = placement_policy
        self.quota = quota
        self.rng_device = rng_device
        self.serial_number = serial_number
        self.small_icon = small_icon
        self.soundcard_enabled = soundcard_enabled
        self.sso = sso
        self.start_paused = start_paused
        self.stateless = stateless
        self.storage_domain = storage_domain
        self.storage_error_resume_behaviour = storage_error_resume_behaviour
        self.time_zone = time_zone
        self.tpm_enabled = tpm_enabled
        self.tunnel_migration = tunnel_migration
        self.type = type
        self.usb = usb
        self.virtio_scsi = virtio_scsi
        self.virtio_scsi_multi_queues = virtio_scsi_multi_queues
        self.virtio_scsi_multi_queues_enabled = virtio_scsi_multi_queues_enabled

    @property
    def delete_protected(self):
        """
        Returns the value of the `delete_protected` property.
        """
        return self._delete_protected

    @delete_protected.setter
    def delete_protected(self, value):
        """
        Sets the value of the `delete_protected` property.
        """
        self._delete_protected = value

    @property
    def high_availability(self):
        """
        Returns the value of the `high_availability` property.
        """
        return self._high_availability

    @high_availability.setter
    def high_availability(self, value):
        """
        Sets the value of the `high_availability` property.
        """
        Struct._check_type('high_availability', value, HighAvailability)
        self._high_availability = value

    @property
    def console(self):
        """
        Returns the value of the `console` property.
        """
        return self._console

    @console.setter
    def console(self, value):
        """
        Sets the value of the `console` property.
        """
        Struct._check_type('console', value, Console)
        self._console = value

    @property
    def serial_number(self):
        """
        Returns the value of the `serial_number` property.
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """
        Sets the value of the `serial_number` property.
        """
        Struct._check_type('serial_number', value, SerialNumber)
        self._serial_number = value

    @property
    def os(self):
        """
        Returns the value of the `os` property.
        """
        return self._os

    @os.setter
    def os(self, value):
        """
        Sets the value of the `os` property.
        """
        Struct._check_type('os', value, OperatingSystem)
        self._os = value

    @property
    def display(self):
        """
        Returns the value of the `display` property.
        """
        return self._display

    @display.setter
    def display(self, value):
        """
        Sets the value of the `display` property.
        """
        Struct._check_type('display', value, Display)
        self._display = value

    @property
    def io(self):
        """
        Returns the value of the `io` property.
        """
        return self._io

    @io.setter
    def io(self, value):
        """
        Sets the value of the `io` property.
        """
        Struct._check_type('io', value, Io)
        self._io = value

    @property
    def cpu(self):
        """
        Returns the value of the `cpu` property.
        """
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        """
        Sets the value of the `cpu` property.
        """
        Struct._check_type('cpu', value, Cpu)
        self._cpu = value

    @property
    def initialization(self):
        """
        Returns the value of the `initialization` property.
        """
        return self._initialization

    @initialization.setter
    def initialization(self, value):
        """
        Sets the value of the `initialization` property.
        """
        Struct._check_type('initialization', value, Initialization)
        self._initialization = value

    @property
    def migration_downtime(self):
        """
        Returns the value of the `migration_downtime` property.
        """
        return self._migration_downtime

    @migration_downtime.setter
    def migration_downtime(self, value):
        """
        Sets the value of the `migration_downtime` property.
        """
        self._migration_downtime = value

    @property
    def time_zone(self):
        """
        Returns the value of the `time_zone` property.
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        """
        Sets the value of the `time_zone` property.
        """
        Struct._check_type('time_zone', value, TimeZone)
        self._time_zone = value

    @property
    def small_icon(self):
        """
        Returns the value of the `small_icon` property.
        """
        return self._small_icon

    @small_icon.setter
    def small_icon(self, value):
        """
        Sets the value of the `small_icon` property.
        """
        Struct._check_type('small_icon', value, Icon)
        self._small_icon = value

    @property
    def domain(self):
        """
        Returns the value of the `domain` property.
        """
        return self._domain

    @domain.setter
    def domain(self, value):
        """
        Sets the value of the `domain` property.
        """
        Struct._check_type('domain', value, Domain)
        self._domain = value

    @property
    def memory_policy(self):
        """
        Returns the value of the `memory_policy` property.
        """
        return self._memory_policy

    @memory_policy.setter
    def memory_policy(self, value):
        """
        Sets the value of the `memory_policy` property.
        """
        Struct._check_type('memory_policy', value, MemoryPolicy)
        self._memory_policy = value

    @property
    def virtio_scsi(self):
        """
        Returns the value of the `virtio_scsi` property.
        """
        return self._virtio_scsi

    @virtio_scsi.setter
    def virtio_scsi(self, value):
        """
        Sets the value of the `virtio_scsi` property.
        """
        Struct._check_type('virtio_scsi', value, VirtioScsi)
        self._virtio_scsi = value

    @property
    def custom_cpu_model(self):
        """
        Returns the value of the `custom_cpu_model` property.
        """
        return self._custom_cpu_model

    @custom_cpu_model.setter
    def custom_cpu_model(self, value):
        """
        Sets the value of the `custom_cpu_model` property.
        """
        self._custom_cpu_model = value

    @property
    def soundcard_enabled(self):
        """
        Returns the value of the `soundcard_enabled` property.
        """
        return self._soundcard_enabled

    @soundcard_enabled.setter
    def soundcard_enabled(self, value):
        """
        Sets the value of the `soundcard_enabled` property.
        """
        self._soundcard_enabled = value

    @property
    def tunnel_migration(self):
        """
        Returns the value of the `tunnel_migration` property.
        """
        return self._tunnel_migration

    @tunnel_migration.setter
    def tunnel_migration(self, value):
        """
        Sets the value of the `tunnel_migration` property.
        """
        self._tunnel_migration = value

    @property
    def auto_pinning_policy(self):
        """
        Returns the value of the `auto_pinning_policy` property.
        """
        return self._auto_pinning_policy

    @auto_pinning_policy.setter
    def auto_pinning_policy(self, value):
        """
        Sets the value of the `auto_pinning_policy` property.
        """
        Struct._check_type('auto_pinning_policy', value, AutoPinningPolicy)
        self._auto_pinning_policy = value

    @property
    def large_icon(self):
        """
        Returns the value of the `large_icon` property.
        """
        return self._large_icon

    @large_icon.setter
    def large_icon(self, value):
        """
        Sets the value of the `large_icon` property.
        """
        Struct._check_type('large_icon', value, Icon)
        self._large_icon = value

    @property
    def lease(self):
        """
        Returns the value of the `lease` property.
        """
        return self._lease

    @lease.setter
    def lease(self, value):
        """
        Sets the value of the `lease` property.
        """
        Struct._check_type('lease', value, StorageDomainLease)
        self._lease = value

    @property
    def virtio_scsi_multi_queues_enabled(self):
        """
        Returns the value of the `virtio_scsi_multi_queues_enabled` property.
        """
        return self._virtio_scsi_multi_queues_enabled

    @virtio_scsi_multi_queues_enabled.setter
    def virtio_scsi_multi_queues_enabled(self, value):
        """
        Sets the value of the `virtio_scsi_multi_queues_enabled` property.
        """
        self._virtio_scsi_multi_queues_enabled = value

    @property
    def migration(self):
        """
        Returns the value of the `migration` property.
        """
        return self._migration

    @migration.setter
    def migration(self, value):
        """
        Sets the value of the `migration` property.
        """
        Struct._check_type('migration', value, MigrationOptions)
        self._migration = value

    @property
    def cpu_shares(self):
        """
        Returns the value of the `cpu_shares` property.
        """
        return self._cpu_shares

    @cpu_shares.setter
    def cpu_shares(self, value):
        """
        Sets the value of the `cpu_shares` property.
        """
        self._cpu_shares = value

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def memory(self):
        """
        Returns the value of the `memory` property.
        """
        return self._memory

    @memory.setter
    def memory(self, value):
        """
        Sets the value of the `memory` property.
        """
        self._memory = value

    @property
    def usb(self):
        """
        Returns the value of the `usb` property.
        """
        return self._usb

    @usb.setter
    def usb(self, value):
        """
        Sets the value of the `usb` property.
        """
        Struct._check_type('usb', value, Usb)
        self._usb = value

    @property
    def custom_emulated_machine(self):
        """
        Returns the value of the `custom_emulated_machine` property.
        """
        return self._custom_emulated_machine

    @custom_emulated_machine.setter
    def custom_emulated_machine(self, value):
        """
        Sets the value of the `custom_emulated_machine` property.
        """
        self._custom_emulated_machine = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def bios(self):
        """
        Returns the value of the `bios` property.
        """
        return self._bios

    @bios.setter
    def bios(self, value):
        """
        Sets the value of the `bios` property.
        """
        Struct._check_type('bios', value, Bios)
        self._bios = value

    @property
    def origin(self):
        """
        Returns the value of the `origin` property.
        """
        return self._origin

    @origin.setter
    def origin(self, value):
        """
        Sets the value of the `origin` property.
        """
        self._origin = value

    @property
    def multi_queues_enabled(self):
        """
        Returns the value of the `multi_queues_enabled` property.
        """
        return self._multi_queues_enabled

    @multi_queues_enabled.setter
    def multi_queues_enabled(self, value):
        """
        Sets the value of the `multi_queues_enabled` property.
        """
        self._multi_queues_enabled = value

    @property
    def custom_properties(self):
        """
        Returns the value of the `custom_properties` property.
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, value):
        """
        Sets the value of the `custom_properties` property.
        """
        self._custom_properties = value

    @property
    def rng_device(self):
        """
        Returns the value of the `rng_device` property.
        """
        return self._rng_device

    @rng_device.setter
    def rng_device(self, value):
        """
        Sets the value of the `rng_device` property.
        """
        Struct._check_type('rng_device', value, RngDevice)
        self._rng_device = value

    @property
    def creation_time(self):
        """
        Returns the value of the `creation_time` property.
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value):
        """
        Sets the value of the `creation_time` property.
        """
        self._creation_time = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, VmType)
        self._type = value

    @property
    def sso(self):
        """
        Returns the value of the `sso` property.
        """
        return self._sso

    @sso.setter
    def sso(self, value):
        """
        Sets the value of the `sso` property.
        """
        Struct._check_type('sso', value, Sso)
        self._sso = value

    @property
    def virtio_scsi_multi_queues(self):
        """
        Returns the value of the `virtio_scsi_multi_queues` property.
        """
        return self._virtio_scsi_multi_queues

    @virtio_scsi_multi_queues.setter
    def virtio_scsi_multi_queues(self, value):
        """
        Sets the value of the `virtio_scsi_multi_queues` property.
        """
        self._virtio_scsi_multi_queues = value

    @property
    def tpm_enabled(self):
        """
        Returns the value of the `tpm_enabled` property.
        """
        return self._tpm_enabled

    @tpm_enabled.setter
    def tpm_enabled(self, value):
        """
        Sets the value of the `tpm_enabled` property.
        """
        self._tpm_enabled = value

    @property
    def start_paused(self):
        """
        Returns the value of the `start_paused` property.
        """
        return self._start_paused

    @start_paused.setter
    def start_paused(self, value):
        """
        Sets the value of the `start_paused` property.
        """
        self._start_paused = value

    @property
    def quota(self):
        """
        Returns the value of the `quota` property.
        """
        return self._quota

    @quota.setter
    def quota(self, value):
        """
        Sets the value of the `quota` property.
        """
        Struct._check_type('quota', value, Quota)
        self._quota = value

    @property
    def custom_compatibility_version(self):
        """
        Returns the value of the `custom_compatibility_version` property.
        """
        return self._custom_compatibility_version

    @custom_compatibility_version.setter
    def custom_compatibility_version(self, value):
        """
        Sets the value of the `custom_compatibility_version` property.
        """
        Struct._check_type('custom_compatibility_version', value, Version)
        self._custom_compatibility_version = value

    @property
    def stateless(self):
        """
        Returns the value of the `stateless` property.
        """
        return self._stateless

    @stateless.setter
    def stateless(self, value):
        """
        Sets the value of the `stateless` property.
        """
        self._stateless = value

    @property
    def storage_error_resume_behaviour(self):
        """
        Returns the value of the `storage_error_resume_behaviour` property.
        """
        return self._storage_error_resume_behaviour

    @storage_error_resume_behaviour.setter
    def storage_error_resume_behaviour(self, value):
        """
        Sets the value of the `storage_error_resume_behaviour` property.
        """
        Struct._check_type('storage_error_resume_behaviour', value, VmStorageErrorResumeBehaviour)
        self._storage_error_resume_behaviour = value

    @property
    def placement_policy(self):
        """
        Returns the value of the `placement_policy` property.
        """
        return self._placement_policy

    @placement_policy.setter
    def placement_policy(self, value):
        """
        Sets the value of the `placement_policy` property.
        """
        Struct._check_type('placement_policy', value, VmPlacementPolicy)
        self._placement_policy = value

    @property
    def cpu_profile(self):
        """
        Returns the value of the `cpu_profile` property.
        """
        return self._cpu_profile

    @cpu_profile.setter
    def cpu_profile(self, value):
        """
        Sets the value of the `cpu_profile` property.
        """
        Struct._check_type('cpu_profile', value, CpuProfile)
        self._cpu_profile = value


class VmPlacementPolicy(Struct):

    def __init__(
        self,
        affinity=None,
        hosts=None,
    ):
        super(VmPlacementPolicy, self).__init__(
        )
        self.affinity = affinity
        self.hosts = hosts

    @property
    def affinity(self):
        """
        Returns the value of the `affinity` property.
        """
        return self._affinity

    @affinity.setter
    def affinity(self, value):
        """
        Sets the value of the `affinity` property.
        """
        Struct._check_type('affinity', value, VmAffinity)
        self._affinity = value

    @property
    def hosts(self):
        """
        Returns the value of the `hosts` property.
        """
        return self._hosts

    @hosts.setter
    def hosts(self, value):
        """
        Sets the value of the `hosts` property.
        """
        self._hosts = value


class VmPool(Identified):

    def __init__(
        self,
        auto_storage_select=None,
        cluster=None,
        comment=None,
        description=None,
        display=None,
        id=None,
        instance_type=None,
        max_user_vms=None,
        name=None,
        permissions=None,
        prestarted_vms=None,
        rng_device=None,
        size=None,
        soundcard_enabled=None,
        stateful=None,
        template=None,
        tpm_enabled=None,
        type=None,
        use_latest_template_version=None,
        vm=None,
    ):
        super(VmPool, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.auto_storage_select = auto_storage_select
        self.cluster = cluster
        self.display = display
        self.instance_type = instance_type
        self.max_user_vms = max_user_vms
        self.permissions = permissions
        self.prestarted_vms = prestarted_vms
        self.rng_device = rng_device
        self.size = size
        self.soundcard_enabled = soundcard_enabled
        self.stateful = stateful
        self.template = template
        self.tpm_enabled = tpm_enabled
        self.type = type
        self.use_latest_template_version = use_latest_template_version
        self.vm = vm

    @property
    def use_latest_template_version(self):
        """
        Returns the value of the `use_latest_template_version` property.
        """
        return self._use_latest_template_version

    @use_latest_template_version.setter
    def use_latest_template_version(self, value):
        """
        Sets the value of the `use_latest_template_version` property.
        """
        self._use_latest_template_version = value

    @property
    def max_user_vms(self):
        """
        Returns the value of the `max_user_vms` property.
        """
        return self._max_user_vms

    @max_user_vms.setter
    def max_user_vms(self, value):
        """
        Sets the value of the `max_user_vms` property.
        """
        self._max_user_vms = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def display(self):
        """
        Returns the value of the `display` property.
        """
        return self._display

    @display.setter
    def display(self, value):
        """
        Sets the value of the `display` property.
        """
        Struct._check_type('display', value, Display)
        self._display = value

    @property
    def auto_storage_select(self):
        """
        Returns the value of the `auto_storage_select` property.
        """
        return self._auto_storage_select

    @auto_storage_select.setter
    def auto_storage_select(self, value):
        """
        Sets the value of the `auto_storage_select` property.
        """
        self._auto_storage_select = value

    @property
    def rng_device(self):
        """
        Returns the value of the `rng_device` property.
        """
        return self._rng_device

    @rng_device.setter
    def rng_device(self, value):
        """
        Sets the value of the `rng_device` property.
        """
        Struct._check_type('rng_device', value, RngDevice)
        self._rng_device = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, VmPoolType)
        self._type = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def tpm_enabled(self):
        """
        Returns the value of the `tpm_enabled` property.
        """
        return self._tpm_enabled

    @tpm_enabled.setter
    def tpm_enabled(self, value):
        """
        Sets the value of the `tpm_enabled` property.
        """
        self._tpm_enabled = value

    @property
    def instance_type(self):
        """
        Returns the value of the `instance_type` property.
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, value):
        """
        Sets the value of the `instance_type` property.
        """
        Struct._check_type('instance_type', value, InstanceType)
        self._instance_type = value

    @property
    def size(self):
        """
        Returns the value of the `size` property.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the value of the `size` property.
        """
        self._size = value

    @property
    def soundcard_enabled(self):
        """
        Returns the value of the `soundcard_enabled` property.
        """
        return self._soundcard_enabled

    @soundcard_enabled.setter
    def soundcard_enabled(self, value):
        """
        Sets the value of the `soundcard_enabled` property.
        """
        self._soundcard_enabled = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def stateful(self):
        """
        Returns the value of the `stateful` property.
        """
        return self._stateful

    @stateful.setter
    def stateful(self, value):
        """
        Sets the value of the `stateful` property.
        """
        self._stateful = value

    @property
    def prestarted_vms(self):
        """
        Returns the value of the `prestarted_vms` property.
        """
        return self._prestarted_vms

    @prestarted_vms.setter
    def prestarted_vms(self, value):
        """
        Sets the value of the `prestarted_vms` property.
        """
        self._prestarted_vms = value


class VmSummary(Struct):

    def __init__(
        self,
        active=None,
        migrating=None,
        total=None,
    ):
        super(VmSummary, self).__init__(
        )
        self.active = active
        self.migrating = migrating
        self.total = total

    @property
    def migrating(self):
        """
        Returns the value of the `migrating` property.
        """
        return self._migrating

    @migrating.setter
    def migrating(self, value):
        """
        Sets the value of the `migrating` property.
        """
        self._migrating = value

    @property
    def total(self):
        """
        Returns the value of the `total` property.
        """
        return self._total

    @total.setter
    def total(self, value):
        """
        Sets the value of the `total` property.
        """
        self._total = value

    @property
    def active(self):
        """
        Returns the value of the `active` property.
        """
        return self._active

    @active.setter
    def active(self, value):
        """
        Sets the value of the `active` property.
        """
        self._active = value


class VnicPassThrough(Struct):

    def __init__(
        self,
        mode=None,
    ):
        super(VnicPassThrough, self).__init__(
        )
        self.mode = mode

    @property
    def mode(self):
        """
        Returns the value of the `mode` property.
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """
        Sets the value of the `mode` property.
        """
        Struct._check_type('mode', value, VnicPassThroughMode)
        self._mode = value


class VnicProfile(Identified):

    def __init__(
        self,
        comment=None,
        custom_properties=None,
        description=None,
        failover=None,
        id=None,
        migratable=None,
        name=None,
        network=None,
        network_filter=None,
        pass_through=None,
        permissions=None,
        port_mirroring=None,
        qos=None,
    ):
        super(VnicProfile, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.custom_properties = custom_properties
        self.failover = failover
        self.migratable = migratable
        self.network = network
        self.network_filter = network_filter
        self.pass_through = pass_through
        self.permissions = permissions
        self.port_mirroring = port_mirroring
        self.qos = qos

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def qos(self):
        """
        Returns the value of the `qos` property.
        """
        return self._qos

    @qos.setter
    def qos(self, value):
        """
        Sets the value of the `qos` property.
        """
        Struct._check_type('qos', value, Qos)
        self._qos = value

    @property
    def failover(self):
        """
        Returns the value of the `failover` property.
        """
        return self._failover

    @failover.setter
    def failover(self, value):
        """
        Sets the value of the `failover` property.
        """
        Struct._check_type('failover', value, VnicProfile)
        self._failover = value

    @property
    def pass_through(self):
        """
        Returns the value of the `pass_through` property.
        """
        return self._pass_through

    @pass_through.setter
    def pass_through(self, value):
        """
        Sets the value of the `pass_through` property.
        """
        Struct._check_type('pass_through', value, VnicPassThrough)
        self._pass_through = value

    @property
    def network_filter(self):
        """
        Returns the value of the `network_filter` property.
        """
        return self._network_filter

    @network_filter.setter
    def network_filter(self, value):
        """
        Sets the value of the `network_filter` property.
        """
        Struct._check_type('network_filter', value, NetworkFilter)
        self._network_filter = value

    @property
    def custom_properties(self):
        """
        Returns the value of the `custom_properties` property.
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, value):
        """
        Sets the value of the `custom_properties` property.
        """
        self._custom_properties = value

    @property
    def network(self):
        """
        Returns the value of the `network` property.
        """
        return self._network

    @network.setter
    def network(self, value):
        """
        Sets the value of the `network` property.
        """
        Struct._check_type('network', value, Network)
        self._network = value

    @property
    def port_mirroring(self):
        """
        Returns the value of the `port_mirroring` property.
        """
        return self._port_mirroring

    @port_mirroring.setter
    def port_mirroring(self, value):
        """
        Sets the value of the `port_mirroring` property.
        """
        self._port_mirroring = value

    @property
    def migratable(self):
        """
        Returns the value of the `migratable` property.
        """
        return self._migratable

    @migratable.setter
    def migratable(self, value):
        """
        Sets the value of the `migratable` property.
        """
        self._migratable = value


class VnicProfileMapping(Struct):

    def __init__(
        self,
        source_network_name=None,
        source_network_profile_name=None,
        target_vnic_profile=None,
    ):
        super(VnicProfileMapping, self).__init__(
        )
        self.source_network_name = source_network_name
        self.source_network_profile_name = source_network_profile_name
        self.target_vnic_profile = target_vnic_profile

    @property
    def source_network_name(self):
        """
        Returns the value of the `source_network_name` property.
        """
        return self._source_network_name

    @source_network_name.setter
    def source_network_name(self, value):
        """
        Sets the value of the `source_network_name` property.
        """
        self._source_network_name = value

    @property
    def source_network_profile_name(self):
        """
        Returns the value of the `source_network_profile_name` property.
        """
        return self._source_network_profile_name

    @source_network_profile_name.setter
    def source_network_profile_name(self, value):
        """
        Sets the value of the `source_network_profile_name` property.
        """
        self._source_network_profile_name = value

    @property
    def target_vnic_profile(self):
        """
        Returns the value of the `target_vnic_profile` property.
        """
        return self._target_vnic_profile

    @target_vnic_profile.setter
    def target_vnic_profile(self, value):
        """
        Sets the value of the `target_vnic_profile` property.
        """
        Struct._check_type('target_vnic_profile', value, VnicProfile)
        self._target_vnic_profile = value


class VolumeGroup(Struct):

    def __init__(
        self,
        id=None,
        logical_units=None,
        name=None,
    ):
        super(VolumeGroup, self).__init__(
        )
        self.id = id
        self.logical_units = logical_units
        self.name = name

    @property
    def logical_units(self):
        """
        Returns the value of the `logical_units` property.
        """
        return self._logical_units

    @logical_units.setter
    def logical_units(self, value):
        """
        Sets the value of the `logical_units` property.
        """
        self._logical_units = value

    @property
    def name(self):
        """
        Returns the value of the `name` property.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the value of the `name` property.
        """
        self._name = value

    @property
    def id(self):
        """
        Returns the value of the `id` property.
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        Sets the value of the `id` property.
        """
        self._id = value


class Weight(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        factor=None,
        id=None,
        name=None,
        scheduling_policy=None,
        scheduling_policy_unit=None,
    ):
        super(Weight, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.factor = factor
        self.scheduling_policy = scheduling_policy
        self.scheduling_policy_unit = scheduling_policy_unit

    @property
    def scheduling_policy(self):
        """
        Returns the value of the `scheduling_policy` property.
        """
        return self._scheduling_policy

    @scheduling_policy.setter
    def scheduling_policy(self, value):
        """
        Sets the value of the `scheduling_policy` property.
        """
        Struct._check_type('scheduling_policy', value, SchedulingPolicy)
        self._scheduling_policy = value

    @property
    def scheduling_policy_unit(self):
        """
        Returns the value of the `scheduling_policy_unit` property.
        """
        return self._scheduling_policy_unit

    @scheduling_policy_unit.setter
    def scheduling_policy_unit(self, value):
        """
        Sets the value of the `scheduling_policy_unit` property.
        """
        Struct._check_type('scheduling_policy_unit', value, SchedulingPolicyUnit)
        self._scheduling_policy_unit = value

    @property
    def factor(self):
        """
        Returns the value of the `factor` property.
        """
        return self._factor

    @factor.setter
    def factor(self, value):
        """
        Sets the value of the `factor` property.
        """
        self._factor = value


class Action(Identified):

    def __init__(
        self,
        activate=None,
        allow_partial_import=None,
        async_=None,
        attachment=None,
        authorized_key=None,
        auto_pinning_policy=None,
        bricks=None,
        certificates=None,
        check_connectivity=None,
        clone=None,
        clone_permissions=None,
        cluster=None,
        collapse_snapshots=None,
        comment=None,
        commit_on_success=None,
        connection=None,
        connectivity_timeout=None,
        data_center=None,
        deploy_hosted_engine=None,
        description=None,
        details=None,
        directory=None,
        discard_snapshots=None,
        discovered_targets=None,
        disk=None,
        disk_profile=None,
        disks=None,
        exclusive=None,
        fault=None,
        fence_type=None,
        filename=None,
        filter=None,
        fix_layout=None,
        force=None,
        grace_period=None,
        host=None,
        id=None,
        image=None,
        image_transfer=None,
        import_as_template=None,
        is_attached=None,
        iscsi=None,
        iscsi_targets=None,
        job=None,
        lease=None,
        logical_units=None,
        maintenance_after_restart=None,
        maintenance_enabled=None,
        migrate_vms_in_affinity_closure=None,
        modified_bonds=None,
        modified_labels=None,
        modified_network_attachments=None,
        name=None,
        optimize_cpu_settings=None,
        option=None,
        pause=None,
        permission=None,
        power_management=None,
        proxy_ticket=None,
        quota=None,
        reason=None,
        reassign_bad_macs=None,
        reboot=None,
        registration_configuration=None,
        remote_viewer_connection_file=None,
        removed_bonds=None,
        removed_labels=None,
        removed_network_attachments=None,
        resolution_type=None,
        restore_memory=None,
        root_password=None,
        seal=None,
        snapshot=None,
        source_host=None,
        ssh=None,
        status=None,
        stop_gluster_service=None,
        storage_domain=None,
        storage_domains=None,
        succeeded=None,
        synchronized_network_attachments=None,
        template=None,
        ticket=None,
        timeout=None,
        undeploy_hosted_engine=None,
        upgrade_action=None,
        use_cloud_init=None,
        use_ignition=None,
        use_initialization=None,
        use_sysprep=None,
        virtual_functions_configuration=None,
        vm=None,
        vnic_profile_mappings=None,
        volatile=None,
    ):
        super(Action, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.activate = activate
        self.allow_partial_import = allow_partial_import
        self.async_ = async_
        self.attachment = attachment
        self.authorized_key = authorized_key
        self.auto_pinning_policy = auto_pinning_policy
        self.bricks = bricks
        self.certificates = certificates
        self.check_connectivity = check_connectivity
        self.clone = clone
        self.clone_permissions = clone_permissions
        self.cluster = cluster
        self.collapse_snapshots = collapse_snapshots
        self.commit_on_success = commit_on_success
        self.connection = connection
        self.connectivity_timeout = connectivity_timeout
        self.data_center = data_center
        self.deploy_hosted_engine = deploy_hosted_engine
        self.details = details
        self.directory = directory
        self.discard_snapshots = discard_snapshots
        self.discovered_targets = discovered_targets
        self.disk = disk
        self.disk_profile = disk_profile
        self.disks = disks
        self.exclusive = exclusive
        self.fault = fault
        self.fence_type = fence_type
        self.filename = filename
        self.filter = filter
        self.fix_layout = fix_layout
        self.force = force
        self.grace_period = grace_period
        self.host = host
        self.image = image
        self.image_transfer = image_transfer
        self.import_as_template = import_as_template
        self.is_attached = is_attached
        self.iscsi = iscsi
        self.iscsi_targets = iscsi_targets
        self.job = job
        self.lease = lease
        self.logical_units = logical_units
        self.maintenance_after_restart = maintenance_after_restart
        self.maintenance_enabled = maintenance_enabled
        self.migrate_vms_in_affinity_closure = migrate_vms_in_affinity_closure
        self.modified_bonds = modified_bonds
        self.modified_labels = modified_labels
        self.modified_network_attachments = modified_network_attachments
        self.optimize_cpu_settings = optimize_cpu_settings
        self.option = option
        self.pause = pause
        self.permission = permission
        self.power_management = power_management
        self.proxy_ticket = proxy_ticket
        self.quota = quota
        self.reason = reason
        self.reassign_bad_macs = reassign_bad_macs
        self.reboot = reboot
        self.registration_configuration = registration_configuration
        self.remote_viewer_connection_file = remote_viewer_connection_file
        self.removed_bonds = removed_bonds
        self.removed_labels = removed_labels
        self.removed_network_attachments = removed_network_attachments
        self.resolution_type = resolution_type
        self.restore_memory = restore_memory
        self.root_password = root_password
        self.seal = seal
        self.snapshot = snapshot
        self.source_host = source_host
        self.ssh = ssh
        self.status = status
        self.stop_gluster_service = stop_gluster_service
        self.storage_domain = storage_domain
        self.storage_domains = storage_domains
        self.succeeded = succeeded
        self.synchronized_network_attachments = synchronized_network_attachments
        self.template = template
        self.ticket = ticket
        self.timeout = timeout
        self.undeploy_hosted_engine = undeploy_hosted_engine
        self.upgrade_action = upgrade_action
        self.use_cloud_init = use_cloud_init
        self.use_ignition = use_ignition
        self.use_initialization = use_initialization
        self.use_sysprep = use_sysprep
        self.virtual_functions_configuration = virtual_functions_configuration
        self.vm = vm
        self.vnic_profile_mappings = vnic_profile_mappings
        self.volatile = volatile

    @property
    def image(self):
        """
        Returns the value of the `image` property.
        """
        return self._image

    @image.setter
    def image(self, value):
        """
        Sets the value of the `image` property.
        """
        self._image = value

    @property
    def reboot(self):
        """
        Returns the value of the `reboot` property.
        """
        return self._reboot

    @reboot.setter
    def reboot(self, value):
        """
        Sets the value of the `reboot` property.
        """
        self._reboot = value

    @property
    def image_transfer(self):
        """
        Returns the value of the `image_transfer` property.
        """
        return self._image_transfer

    @image_transfer.setter
    def image_transfer(self, value):
        """
        Sets the value of the `image_transfer` property.
        """
        Struct._check_type('image_transfer', value, ImageTransfer)
        self._image_transfer = value

    @property
    def source_host(self):
        """
        Returns the value of the `source_host` property.
        """
        return self._source_host

    @source_host.setter
    def source_host(self, value):
        """
        Sets the value of the `source_host` property.
        """
        Struct._check_type('source_host', value, Host)
        self._source_host = value

    @property
    def optimize_cpu_settings(self):
        """
        Returns the value of the `optimize_cpu_settings` property.
        """
        return self._optimize_cpu_settings

    @optimize_cpu_settings.setter
    def optimize_cpu_settings(self, value):
        """
        Sets the value of the `optimize_cpu_settings` property.
        """
        self._optimize_cpu_settings = value

    @property
    def fault(self):
        """
        Returns the value of the `fault` property.
        """
        return self._fault

    @fault.setter
    def fault(self, value):
        """
        Sets the value of the `fault` property.
        """
        Struct._check_type('fault', value, Fault)
        self._fault = value

    @property
    def use_initialization(self):
        """
        Returns the value of the `use_initialization` property.
        """
        return self._use_initialization

    @use_initialization.setter
    def use_initialization(self, value):
        """
        Sets the value of the `use_initialization` property.
        """
        self._use_initialization = value

    @property
    def commit_on_success(self):
        """
        Returns the value of the `commit_on_success` property.
        """
        return self._commit_on_success

    @commit_on_success.setter
    def commit_on_success(self, value):
        """
        Sets the value of the `commit_on_success` property.
        """
        self._commit_on_success = value

    @property
    def resolution_type(self):
        """
        Returns the value of the `resolution_type` property.
        """
        return self._resolution_type

    @resolution_type.setter
    def resolution_type(self, value):
        """
        Sets the value of the `resolution_type` property.
        """
        self._resolution_type = value

    @property
    def storage_domains(self):
        """
        Returns the value of the `storage_domains` property.
        """
        return self._storage_domains

    @storage_domains.setter
    def storage_domains(self, value):
        """
        Sets the value of the `storage_domains` property.
        """
        self._storage_domains = value

    @property
    def check_connectivity(self):
        """
        Returns the value of the `check_connectivity` property.
        """
        return self._check_connectivity

    @check_connectivity.setter
    def check_connectivity(self, value):
        """
        Sets the value of the `check_connectivity` property.
        """
        self._check_connectivity = value

    @property
    def collapse_snapshots(self):
        """
        Returns the value of the `collapse_snapshots` property.
        """
        return self._collapse_snapshots

    @collapse_snapshots.setter
    def collapse_snapshots(self, value):
        """
        Sets the value of the `collapse_snapshots` property.
        """
        self._collapse_snapshots = value

    @property
    def filename(self):
        """
        Returns the value of the `filename` property.
        """
        return self._filename

    @filename.setter
    def filename(self, value):
        """
        Sets the value of the `filename` property.
        """
        self._filename = value

    @property
    def disk(self):
        """
        Returns the value of the `disk` property.
        """
        return self._disk

    @disk.setter
    def disk(self, value):
        """
        Sets the value of the `disk` property.
        """
        Struct._check_type('disk', value, Disk)
        self._disk = value

    @property
    def async_(self):
        """
        Returns the value of the `async_` property.
        """
        return self._async_

    @async_.setter
    def async_(self, value):
        """
        Sets the value of the `async_` property.
        """
        self._async_ = value

    @property
    def virtual_functions_configuration(self):
        """
        Returns the value of the `virtual_functions_configuration` property.
        """
        return self._virtual_functions_configuration

    @virtual_functions_configuration.setter
    def virtual_functions_configuration(self, value):
        """
        Sets the value of the `virtual_functions_configuration` property.
        """
        Struct._check_type('virtual_functions_configuration', value, HostNicVirtualFunctionsConfiguration)
        self._virtual_functions_configuration = value

    @property
    def modified_labels(self):
        """
        Returns the value of the `modified_labels` property.
        """
        return self._modified_labels

    @modified_labels.setter
    def modified_labels(self, value):
        """
        Sets the value of the `modified_labels` property.
        """
        self._modified_labels = value

    @property
    def snapshot(self):
        """
        Returns the value of the `snapshot` property.
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value):
        """
        Sets the value of the `snapshot` property.
        """
        Struct._check_type('snapshot', value, Snapshot)
        self._snapshot = value

    @property
    def proxy_ticket(self):
        """
        Returns the value of the `proxy_ticket` property.
        """
        return self._proxy_ticket

    @proxy_ticket.setter
    def proxy_ticket(self, value):
        """
        Sets the value of the `proxy_ticket` property.
        """
        Struct._check_type('proxy_ticket', value, ProxyTicket)
        self._proxy_ticket = value

    @property
    def filter(self):
        """
        Returns the value of the `filter` property.
        """
        return self._filter

    @filter.setter
    def filter(self, value):
        """
        Sets the value of the `filter` property.
        """
        self._filter = value

    @property
    def clone_permissions(self):
        """
        Returns the value of the `clone_permissions` property.
        """
        return self._clone_permissions

    @clone_permissions.setter
    def clone_permissions(self, value):
        """
        Sets the value of the `clone_permissions` property.
        """
        self._clone_permissions = value

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def maintenance_after_restart(self):
        """
        Returns the value of the `maintenance_after_restart` property.
        """
        return self._maintenance_after_restart

    @maintenance_after_restart.setter
    def maintenance_after_restart(self, value):
        """
        Sets the value of the `maintenance_after_restart` property.
        """
        self._maintenance_after_restart = value

    @property
    def reason(self):
        """
        Returns the value of the `reason` property.
        """
        return self._reason

    @reason.setter
    def reason(self, value):
        """
        Sets the value of the `reason` property.
        """
        self._reason = value

    @property
    def ssh(self):
        """
        Returns the value of the `ssh` property.
        """
        return self._ssh

    @ssh.setter
    def ssh(self, value):
        """
        Sets the value of the `ssh` property.
        """
        Struct._check_type('ssh', value, Ssh)
        self._ssh = value

    @property
    def disks(self):
        """
        Returns the value of the `disks` property.
        """
        return self._disks

    @disks.setter
    def disks(self, value):
        """
        Sets the value of the `disks` property.
        """
        self._disks = value

    @property
    def seal(self):
        """
        Returns the value of the `seal` property.
        """
        return self._seal

    @seal.setter
    def seal(self, value):
        """
        Sets the value of the `seal` property.
        """
        self._seal = value

    @property
    def directory(self):
        """
        Returns the value of the `directory` property.
        """
        return self._directory

    @directory.setter
    def directory(self, value):
        """
        Sets the value of the `directory` property.
        """
        self._directory = value

    @property
    def disk_profile(self):
        """
        Returns the value of the `disk_profile` property.
        """
        return self._disk_profile

    @disk_profile.setter
    def disk_profile(self, value):
        """
        Sets the value of the `disk_profile` property.
        """
        Struct._check_type('disk_profile', value, DiskProfile)
        self._disk_profile = value

    @property
    def removed_network_attachments(self):
        """
        Returns the value of the `removed_network_attachments` property.
        """
        return self._removed_network_attachments

    @removed_network_attachments.setter
    def removed_network_attachments(self, value):
        """
        Sets the value of the `removed_network_attachments` property.
        """
        self._removed_network_attachments = value

    @property
    def timeout(self):
        """
        Returns the value of the `timeout` property.
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        """
        Sets the value of the `timeout` property.
        """
        self._timeout = value

    @property
    def maintenance_enabled(self):
        """
        Returns the value of the `maintenance_enabled` property.
        """
        return self._maintenance_enabled

    @maintenance_enabled.setter
    def maintenance_enabled(self, value):
        """
        Sets the value of the `maintenance_enabled` property.
        """
        self._maintenance_enabled = value

    @property
    def connectivity_timeout(self):
        """
        Returns the value of the `connectivity_timeout` property.
        """
        return self._connectivity_timeout

    @connectivity_timeout.setter
    def connectivity_timeout(self, value):
        """
        Sets the value of the `connectivity_timeout` property.
        """
        self._connectivity_timeout = value

    @property
    def modified_network_attachments(self):
        """
        Returns the value of the `modified_network_attachments` property.
        """
        return self._modified_network_attachments

    @modified_network_attachments.setter
    def modified_network_attachments(self, value):
        """
        Sets the value of the `modified_network_attachments` property.
        """
        self._modified_network_attachments = value

    @property
    def registration_configuration(self):
        """
        Returns the value of the `registration_configuration` property.
        """
        return self._registration_configuration

    @registration_configuration.setter
    def registration_configuration(self, value):
        """
        Sets the value of the `registration_configuration` property.
        """
        Struct._check_type('registration_configuration', value, RegistrationConfiguration)
        self._registration_configuration = value

    @property
    def discard_snapshots(self):
        """
        Returns the value of the `discard_snapshots` property.
        """
        return self._discard_snapshots

    @discard_snapshots.setter
    def discard_snapshots(self, value):
        """
        Sets the value of the `discard_snapshots` property.
        """
        self._discard_snapshots = value

    @property
    def synchronized_network_attachments(self):
        """
        Returns the value of the `synchronized_network_attachments` property.
        """
        return self._synchronized_network_attachments

    @synchronized_network_attachments.setter
    def synchronized_network_attachments(self, value):
        """
        Sets the value of the `synchronized_network_attachments` property.
        """
        self._synchronized_network_attachments = value

    @property
    def use_sysprep(self):
        """
        Returns the value of the `use_sysprep` property.
        """
        return self._use_sysprep

    @use_sysprep.setter
    def use_sysprep(self, value):
        """
        Sets the value of the `use_sysprep` property.
        """
        self._use_sysprep = value

    @property
    def attachment(self):
        """
        Returns the value of the `attachment` property.
        """
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        """
        Sets the value of the `attachment` property.
        """
        Struct._check_type('attachment', value, DiskAttachment)
        self._attachment = value

    @property
    def power_management(self):
        """
        Returns the value of the `power_management` property.
        """
        return self._power_management

    @power_management.setter
    def power_management(self, value):
        """
        Sets the value of the `power_management` property.
        """
        Struct._check_type('power_management', value, PowerManagement)
        self._power_management = value

    @property
    def connection(self):
        """
        Returns the value of the `connection` property.
        """
        return self._connection

    @connection.setter
    def connection(self, value):
        """
        Sets the value of the `connection` property.
        """
        Struct._check_type('connection', value, StorageConnection)
        self._connection = value

    @property
    def details(self):
        """
        Returns the value of the `details` property.
        """
        return self._details

    @details.setter
    def details(self, value):
        """
        Sets the value of the `details` property.
        """
        Struct._check_type('details', value, GlusterVolumeProfileDetails)
        self._details = value

    @property
    def exclusive(self):
        """
        Returns the value of the `exclusive` property.
        """
        return self._exclusive

    @exclusive.setter
    def exclusive(self, value):
        """
        Sets the value of the `exclusive` property.
        """
        self._exclusive = value

    @property
    def root_password(self):
        """
        Returns the value of the `root_password` property.
        """
        return self._root_password

    @root_password.setter
    def root_password(self, value):
        """
        Sets the value of the `root_password` property.
        """
        self._root_password = value

    @property
    def allow_partial_import(self):
        """
        Returns the value of the `allow_partial_import` property.
        """
        return self._allow_partial_import

    @allow_partial_import.setter
    def allow_partial_import(self, value):
        """
        Sets the value of the `allow_partial_import` property.
        """
        self._allow_partial_import = value

    @property
    def remote_viewer_connection_file(self):
        """
        Returns the value of the `remote_viewer_connection_file` property.
        """
        return self._remote_viewer_connection_file

    @remote_viewer_connection_file.setter
    def remote_viewer_connection_file(self, value):
        """
        Sets the value of the `remote_viewer_connection_file` property.
        """
        self._remote_viewer_connection_file = value

    @property
    def bricks(self):
        """
        Returns the value of the `bricks` property.
        """
        return self._bricks

    @bricks.setter
    def bricks(self, value):
        """
        Sets the value of the `bricks` property.
        """
        self._bricks = value

    @property
    def import_as_template(self):
        """
        Returns the value of the `import_as_template` property.
        """
        return self._import_as_template

    @import_as_template.setter
    def import_as_template(self, value):
        """
        Sets the value of the `import_as_template` property.
        """
        self._import_as_template = value

    @property
    def ticket(self):
        """
        Returns the value of the `ticket` property.
        """
        return self._ticket

    @ticket.setter
    def ticket(self, value):
        """
        Sets the value of the `ticket` property.
        """
        Struct._check_type('ticket', value, Ticket)
        self._ticket = value

    @property
    def deploy_hosted_engine(self):
        """
        Returns the value of the `deploy_hosted_engine` property.
        """
        return self._deploy_hosted_engine

    @deploy_hosted_engine.setter
    def deploy_hosted_engine(self, value):
        """
        Sets the value of the `deploy_hosted_engine` property.
        """
        self._deploy_hosted_engine = value

    @property
    def restore_memory(self):
        """
        Returns the value of the `restore_memory` property.
        """
        return self._restore_memory

    @restore_memory.setter
    def restore_memory(self, value):
        """
        Sets the value of the `restore_memory` property.
        """
        self._restore_memory = value

    @property
    def permission(self):
        """
        Returns the value of the `permission` property.
        """
        return self._permission

    @permission.setter
    def permission(self, value):
        """
        Sets the value of the `permission` property.
        """
        Struct._check_type('permission', value, Permission)
        self._permission = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def pause(self):
        """
        Returns the value of the `pause` property.
        """
        return self._pause

    @pause.setter
    def pause(self, value):
        """
        Sets the value of the `pause` property.
        """
        self._pause = value

    @property
    def volatile(self):
        """
        Returns the value of the `volatile` property.
        """
        return self._volatile

    @volatile.setter
    def volatile(self, value):
        """
        Sets the value of the `volatile` property.
        """
        self._volatile = value

    @property
    def use_cloud_init(self):
        """
        Returns the value of the `use_cloud_init` property.
        """
        return self._use_cloud_init

    @use_cloud_init.setter
    def use_cloud_init(self, value):
        """
        Sets the value of the `use_cloud_init` property.
        """
        self._use_cloud_init = value

    @property
    def grace_period(self):
        """
        Returns the value of the `grace_period` property.
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, value):
        """
        Sets the value of the `grace_period` property.
        """
        Struct._check_type('grace_period', value, GracePeriod)
        self._grace_period = value

    @property
    def migrate_vms_in_affinity_closure(self):
        """
        Returns the value of the `migrate_vms_in_affinity_closure` property.
        """
        return self._migrate_vms_in_affinity_closure

    @migrate_vms_in_affinity_closure.setter
    def migrate_vms_in_affinity_closure(self, value):
        """
        Sets the value of the `migrate_vms_in_affinity_closure` property.
        """
        self._migrate_vms_in_affinity_closure = value

    @property
    def upgrade_action(self):
        """
        Returns the value of the `upgrade_action` property.
        """
        return self._upgrade_action

    @upgrade_action.setter
    def upgrade_action(self, value):
        """
        Sets the value of the `upgrade_action` property.
        """
        Struct._check_type('upgrade_action', value, ClusterUpgradeAction)
        self._upgrade_action = value

    @property
    def certificates(self):
        """
        Returns the value of the `certificates` property.
        """
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        """
        Sets the value of the `certificates` property.
        """
        self._certificates = value

    @property
    def iscsi(self):
        """
        Returns the value of the `iscsi` property.
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, value):
        """
        Sets the value of the `iscsi` property.
        """
        Struct._check_type('iscsi', value, IscsiDetails)
        self._iscsi = value

    @property
    def auto_pinning_policy(self):
        """
        Returns the value of the `auto_pinning_policy` property.
        """
        return self._auto_pinning_policy

    @auto_pinning_policy.setter
    def auto_pinning_policy(self, value):
        """
        Sets the value of the `auto_pinning_policy` property.
        """
        Struct._check_type('auto_pinning_policy', value, AutoPinningPolicy)
        self._auto_pinning_policy = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def lease(self):
        """
        Returns the value of the `lease` property.
        """
        return self._lease

    @lease.setter
    def lease(self, value):
        """
        Sets the value of the `lease` property.
        """
        Struct._check_type('lease', value, StorageDomainLease)
        self._lease = value

    @property
    def activate(self):
        """
        Returns the value of the `activate` property.
        """
        return self._activate

    @activate.setter
    def activate(self, value):
        """
        Sets the value of the `activate` property.
        """
        self._activate = value

    @property
    def clone(self):
        """
        Returns the value of the `clone` property.
        """
        return self._clone

    @clone.setter
    def clone(self, value):
        """
        Sets the value of the `clone` property.
        """
        self._clone = value

    @property
    def force(self):
        """
        Returns the value of the `force` property.
        """
        return self._force

    @force.setter
    def force(self, value):
        """
        Sets the value of the `force` property.
        """
        self._force = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        self._status = value

    @property
    def stop_gluster_service(self):
        """
        Returns the value of the `stop_gluster_service` property.
        """
        return self._stop_gluster_service

    @stop_gluster_service.setter
    def stop_gluster_service(self, value):
        """
        Sets the value of the `stop_gluster_service` property.
        """
        self._stop_gluster_service = value

    @property
    def job(self):
        """
        Returns the value of the `job` property.
        """
        return self._job

    @job.setter
    def job(self, value):
        """
        Sets the value of the `job` property.
        """
        Struct._check_type('job', value, Job)
        self._job = value

    @property
    def option(self):
        """
        Returns the value of the `option` property.
        """
        return self._option

    @option.setter
    def option(self, value):
        """
        Sets the value of the `option` property.
        """
        Struct._check_type('option', value, Option)
        self._option = value

    @property
    def succeeded(self):
        """
        Returns the value of the `succeeded` property.
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, value):
        """
        Sets the value of the `succeeded` property.
        """
        self._succeeded = value

    @property
    def removed_labels(self):
        """
        Returns the value of the `removed_labels` property.
        """
        return self._removed_labels

    @removed_labels.setter
    def removed_labels(self, value):
        """
        Sets the value of the `removed_labels` property.
        """
        self._removed_labels = value

    @property
    def use_ignition(self):
        """
        Returns the value of the `use_ignition` property.
        """
        return self._use_ignition

    @use_ignition.setter
    def use_ignition(self, value):
        """
        Sets the value of the `use_ignition` property.
        """
        self._use_ignition = value

    @property
    def modified_bonds(self):
        """
        Returns the value of the `modified_bonds` property.
        """
        return self._modified_bonds

    @modified_bonds.setter
    def modified_bonds(self, value):
        """
        Sets the value of the `modified_bonds` property.
        """
        self._modified_bonds = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def is_attached(self):
        """
        Returns the value of the `is_attached` property.
        """
        return self._is_attached

    @is_attached.setter
    def is_attached(self, value):
        """
        Sets the value of the `is_attached` property.
        """
        self._is_attached = value

    @property
    def undeploy_hosted_engine(self):
        """
        Returns the value of the `undeploy_hosted_engine` property.
        """
        return self._undeploy_hosted_engine

    @undeploy_hosted_engine.setter
    def undeploy_hosted_engine(self, value):
        """
        Sets the value of the `undeploy_hosted_engine` property.
        """
        self._undeploy_hosted_engine = value

    @property
    def reassign_bad_macs(self):
        """
        Returns the value of the `reassign_bad_macs` property.
        """
        return self._reassign_bad_macs

    @reassign_bad_macs.setter
    def reassign_bad_macs(self, value):
        """
        Sets the value of the `reassign_bad_macs` property.
        """
        self._reassign_bad_macs = value

    @property
    def iscsi_targets(self):
        """
        Returns the value of the `iscsi_targets` property.
        """
        return self._iscsi_targets

    @iscsi_targets.setter
    def iscsi_targets(self, value):
        """
        Sets the value of the `iscsi_targets` property.
        """
        self._iscsi_targets = value

    @property
    def fence_type(self):
        """
        Returns the value of the `fence_type` property.
        """
        return self._fence_type

    @fence_type.setter
    def fence_type(self, value):
        """
        Sets the value of the `fence_type` property.
        """
        self._fence_type = value

    @property
    def discovered_targets(self):
        """
        Returns the value of the `discovered_targets` property.
        """
        return self._discovered_targets

    @discovered_targets.setter
    def discovered_targets(self, value):
        """
        Sets the value of the `discovered_targets` property.
        """
        self._discovered_targets = value

    @property
    def authorized_key(self):
        """
        Returns the value of the `authorized_key` property.
        """
        return self._authorized_key

    @authorized_key.setter
    def authorized_key(self, value):
        """
        Sets the value of the `authorized_key` property.
        """
        Struct._check_type('authorized_key', value, AuthorizedKey)
        self._authorized_key = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def logical_units(self):
        """
        Returns the value of the `logical_units` property.
        """
        return self._logical_units

    @logical_units.setter
    def logical_units(self, value):
        """
        Sets the value of the `logical_units` property.
        """
        self._logical_units = value

    @property
    def quota(self):
        """
        Returns the value of the `quota` property.
        """
        return self._quota

    @quota.setter
    def quota(self, value):
        """
        Sets the value of the `quota` property.
        """
        Struct._check_type('quota', value, Quota)
        self._quota = value

    @property
    def vnic_profile_mappings(self):
        """
        Returns the value of the `vnic_profile_mappings` property.
        """
        return self._vnic_profile_mappings

    @vnic_profile_mappings.setter
    def vnic_profile_mappings(self, value):
        """
        Sets the value of the `vnic_profile_mappings` property.
        """
        self._vnic_profile_mappings = value

    @property
    def removed_bonds(self):
        """
        Returns the value of the `removed_bonds` property.
        """
        return self._removed_bonds

    @removed_bonds.setter
    def removed_bonds(self, value):
        """
        Sets the value of the `removed_bonds` property.
        """
        self._removed_bonds = value

    @property
    def fix_layout(self):
        """
        Returns the value of the `fix_layout` property.
        """
        return self._fix_layout

    @fix_layout.setter
    def fix_layout(self, value):
        """
        Sets the value of the `fix_layout` property.
        """
        self._fix_layout = value


class AffinityGroup(Identified):

    def __init__(
        self,
        broken=None,
        cluster=None,
        comment=None,
        description=None,
        enforcing=None,
        host_labels=None,
        hosts=None,
        hosts_rule=None,
        id=None,
        name=None,
        positive=None,
        priority=None,
        vm_labels=None,
        vms=None,
        vms_rule=None,
    ):
        super(AffinityGroup, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.broken = broken
        self.cluster = cluster
        self.enforcing = enforcing
        self.host_labels = host_labels
        self.hosts = hosts
        self.hosts_rule = hosts_rule
        self.positive = positive
        self.priority = priority
        self.vm_labels = vm_labels
        self.vms = vms
        self.vms_rule = vms_rule

    @property
    def broken(self):
        """
        Returns the value of the `broken` property.
        """
        return self._broken

    @broken.setter
    def broken(self, value):
        """
        Sets the value of the `broken` property.
        """
        self._broken = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def enforcing(self):
        """
        Returns the value of the `enforcing` property.
        """
        return self._enforcing

    @enforcing.setter
    def enforcing(self, value):
        """
        Sets the value of the `enforcing` property.
        """
        self._enforcing = value

    @property
    def host_labels(self):
        """
        Returns the value of the `host_labels` property.
        """
        return self._host_labels

    @host_labels.setter
    def host_labels(self, value):
        """
        Sets the value of the `host_labels` property.
        """
        self._host_labels = value

    @property
    def hosts(self):
        """
        Returns the value of the `hosts` property.
        """
        return self._hosts

    @hosts.setter
    def hosts(self, value):
        """
        Sets the value of the `hosts` property.
        """
        self._hosts = value

    @property
    def positive(self):
        """
        Returns the value of the `positive` property.
        """
        return self._positive

    @positive.setter
    def positive(self, value):
        """
        Sets the value of the `positive` property.
        """
        self._positive = value

    @property
    def vms(self):
        """
        Returns the value of the `vms` property.
        """
        return self._vms

    @vms.setter
    def vms(self, value):
        """
        Sets the value of the `vms` property.
        """
        self._vms = value

    @property
    def priority(self):
        """
        Returns the value of the `priority` property.
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """
        Sets the value of the `priority` property.
        """
        self._priority = value

    @property
    def vm_labels(self):
        """
        Returns the value of the `vm_labels` property.
        """
        return self._vm_labels

    @vm_labels.setter
    def vm_labels(self, value):
        """
        Sets the value of the `vm_labels` property.
        """
        self._vm_labels = value

    @property
    def vms_rule(self):
        """
        Returns the value of the `vms_rule` property.
        """
        return self._vms_rule

    @vms_rule.setter
    def vms_rule(self, value):
        """
        Sets the value of the `vms_rule` property.
        """
        Struct._check_type('vms_rule', value, AffinityRule)
        self._vms_rule = value

    @property
    def hosts_rule(self):
        """
        Returns the value of the `hosts_rule` property.
        """
        return self._hosts_rule

    @hosts_rule.setter
    def hosts_rule(self, value):
        """
        Sets the value of the `hosts_rule` property.
        """
        Struct._check_type('hosts_rule', value, AffinityRule)
        self._hosts_rule = value


class AffinityLabel(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        has_implicit_affinity_group=None,
        hosts=None,
        id=None,
        name=None,
        read_only=None,
        vms=None,
    ):
        super(AffinityLabel, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.has_implicit_affinity_group = has_implicit_affinity_group
        self.hosts = hosts
        self.read_only = read_only
        self.vms = vms

    @property
    def hosts(self):
        """
        Returns the value of the `hosts` property.
        """
        return self._hosts

    @hosts.setter
    def hosts(self, value):
        """
        Sets the value of the `hosts` property.
        """
        self._hosts = value

    @property
    def vms(self):
        """
        Returns the value of the `vms` property.
        """
        return self._vms

    @vms.setter
    def vms(self, value):
        """
        Sets the value of the `vms` property.
        """
        self._vms = value

    @property
    def has_implicit_affinity_group(self):
        """
        Returns the value of the `has_implicit_affinity_group` property.
        """
        return self._has_implicit_affinity_group

    @has_implicit_affinity_group.setter
    def has_implicit_affinity_group(self, value):
        """
        Sets the value of the `has_implicit_affinity_group` property.
        """
        self._has_implicit_affinity_group = value

    @property
    def read_only(self):
        """
        Returns the value of the `read_only` property.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """
        Sets the value of the `read_only` property.
        """
        self._read_only = value


class Agent(Identified):

    def __init__(
        self,
        address=None,
        comment=None,
        concurrent=None,
        description=None,
        encrypt_options=None,
        host=None,
        id=None,
        name=None,
        options=None,
        order=None,
        password=None,
        port=None,
        type=None,
        username=None,
    ):
        super(Agent, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.address = address
        self.concurrent = concurrent
        self.encrypt_options = encrypt_options
        self.host = host
        self.options = options
        self.order = order
        self.password = password
        self.port = port
        self.type = type
        self.username = username

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def encrypt_options(self):
        """
        Returns the value of the `encrypt_options` property.
        """
        return self._encrypt_options

    @encrypt_options.setter
    def encrypt_options(self, value):
        """
        Sets the value of the `encrypt_options` property.
        """
        self._encrypt_options = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def concurrent(self):
        """
        Returns the value of the `concurrent` property.
        """
        return self._concurrent

    @concurrent.setter
    def concurrent(self, value):
        """
        Sets the value of the `concurrent` property.
        """
        self._concurrent = value

    @property
    def options(self):
        """
        Returns the value of the `options` property.
        """
        return self._options

    @options.setter
    def options(self, value):
        """
        Sets the value of the `options` property.
        """
        self._options = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def order(self):
        """
        Returns the value of the `order` property.
        """
        return self._order

    @order.setter
    def order(self, value):
        """
        Sets the value of the `order` property.
        """
        self._order = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value


class Application(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        vm=None,
    ):
        super(Application, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.vm = vm

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value


class AuthorizedKey(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        key=None,
        name=None,
        user=None,
    ):
        super(AuthorizedKey, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.key = key
        self.user = user

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def key(self):
        """
        Returns the value of the `key` property.
        """
        return self._key

    @key.setter
    def key(self, value):
        """
        Sets the value of the `key` property.
        """
        self._key = value


class Backup(Identified):

    def __init__(
        self,
        comment=None,
        creation_date=None,
        description=None,
        disks=None,
        from_checkpoint_id=None,
        host=None,
        id=None,
        modification_date=None,
        name=None,
        phase=None,
        to_checkpoint_id=None,
        vm=None,
    ):
        super(Backup, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.creation_date = creation_date
        self.disks = disks
        self.from_checkpoint_id = from_checkpoint_id
        self.host = host
        self.modification_date = modification_date
        self.phase = phase
        self.to_checkpoint_id = to_checkpoint_id
        self.vm = vm

    @property
    def phase(self):
        """
        Returns the value of the `phase` property.
        """
        return self._phase

    @phase.setter
    def phase(self, value):
        """
        Sets the value of the `phase` property.
        """
        Struct._check_type('phase', value, BackupPhase)
        self._phase = value

    @property
    def to_checkpoint_id(self):
        """
        Returns the value of the `to_checkpoint_id` property.
        """
        return self._to_checkpoint_id

    @to_checkpoint_id.setter
    def to_checkpoint_id(self, value):
        """
        Sets the value of the `to_checkpoint_id` property.
        """
        self._to_checkpoint_id = value

    @property
    def modification_date(self):
        """
        Returns the value of the `modification_date` property.
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, value):
        """
        Sets the value of the `modification_date` property.
        """
        self._modification_date = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def from_checkpoint_id(self):
        """
        Returns the value of the `from_checkpoint_id` property.
        """
        return self._from_checkpoint_id

    @from_checkpoint_id.setter
    def from_checkpoint_id(self, value):
        """
        Sets the value of the `from_checkpoint_id` property.
        """
        self._from_checkpoint_id = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def disks(self):
        """
        Returns the value of the `disks` property.
        """
        return self._disks

    @disks.setter
    def disks(self, value):
        """
        Sets the value of the `disks` property.
        """
        self._disks = value

    @property
    def creation_date(self):
        """
        Returns the value of the `creation_date` property.
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """
        Sets the value of the `creation_date` property.
        """
        self._creation_date = value


class Balance(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        scheduling_policy=None,
        scheduling_policy_unit=None,
    ):
        super(Balance, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.scheduling_policy = scheduling_policy
        self.scheduling_policy_unit = scheduling_policy_unit

    @property
    def scheduling_policy(self):
        """
        Returns the value of the `scheduling_policy` property.
        """
        return self._scheduling_policy

    @scheduling_policy.setter
    def scheduling_policy(self, value):
        """
        Sets the value of the `scheduling_policy` property.
        """
        Struct._check_type('scheduling_policy', value, SchedulingPolicy)
        self._scheduling_policy = value

    @property
    def scheduling_policy_unit(self):
        """
        Returns the value of the `scheduling_policy_unit` property.
        """
        return self._scheduling_policy_unit

    @scheduling_policy_unit.setter
    def scheduling_policy_unit(self, value):
        """
        Sets the value of the `scheduling_policy_unit` property.
        """
        Struct._check_type('scheduling_policy_unit', value, SchedulingPolicyUnit)
        self._scheduling_policy_unit = value


class Bookmark(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        value=None,
    ):
        super(Bookmark, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.value = value

    @property
    def value(self):
        """
        Returns the value of the `value` property.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of the `value` property.
        """
        self._value = value


class BrickProfileDetail(EntityProfileDetail):

    def __init__(
        self,
        brick=None,
        profile_details=None,
    ):
        super(BrickProfileDetail, self).__init__(
            profile_details=profile_details,
        )
        self.brick = brick

    @property
    def brick(self):
        """
        Returns the value of the `brick` property.
        """
        return self._brick

    @brick.setter
    def brick(self, value):
        """
        Sets the value of the `brick` property.
        """
        Struct._check_type('brick', value, GlusterBrick)
        self._brick = value


class Certificate(Identified):

    def __init__(
        self,
        comment=None,
        content=None,
        description=None,
        id=None,
        name=None,
        organization=None,
        subject=None,
    ):
        super(Certificate, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.content = content
        self.organization = organization
        self.subject = subject

    @property
    def subject(self):
        """
        Returns the value of the `subject` property.
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        """
        Sets the value of the `subject` property.
        """
        self._subject = value

    @property
    def organization(self):
        """
        Returns the value of the `organization` property.
        """
        return self._organization

    @organization.setter
    def organization(self, value):
        """
        Sets the value of the `organization` property.
        """
        self._organization = value

    @property
    def content(self):
        """
        Returns the value of the `content` property.
        """
        return self._content

    @content.setter
    def content(self, value):
        """
        Sets the value of the `content` property.
        """
        self._content = value


class Checkpoint(Identified):

    def __init__(
        self,
        comment=None,
        creation_date=None,
        description=None,
        disks=None,
        id=None,
        name=None,
        parent_id=None,
        state=None,
        vm=None,
    ):
        super(Checkpoint, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.creation_date = creation_date
        self.disks = disks
        self.parent_id = parent_id
        self.state = state
        self.vm = vm

    @property
    def parent_id(self):
        """
        Returns the value of the `parent_id` property.
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        """
        Sets the value of the `parent_id` property.
        """
        self._parent_id = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def disks(self):
        """
        Returns the value of the `disks` property.
        """
        return self._disks

    @disks.setter
    def disks(self, value):
        """
        Sets the value of the `disks` property.
        """
        self._disks = value

    @property
    def state(self):
        """
        Returns the value of the `state` property.
        """
        return self._state

    @state.setter
    def state(self, value):
        """
        Sets the value of the `state` property.
        """
        Struct._check_type('state', value, CheckpointState)
        self._state = value

    @property
    def creation_date(self):
        """
        Returns the value of the `creation_date` property.
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """
        Sets the value of the `creation_date` property.
        """
        self._creation_date = value


class Cluster(Identified):

    def __init__(
        self,
        affinity_groups=None,
        ballooning_enabled=None,
        bios_type=None,
        comment=None,
        cpu=None,
        cpu_profiles=None,
        custom_scheduling_policy_properties=None,
        data_center=None,
        description=None,
        display=None,
        enabled_features=None,
        error_handling=None,
        external_network_providers=None,
        fencing_policy=None,
        fips_mode=None,
        firewall_type=None,
        gluster_hooks=None,
        gluster_service=None,
        gluster_tuned_profile=None,
        gluster_volumes=None,
        ha_reservation=None,
        id=None,
        ksm=None,
        log_max_memory_used_threshold=None,
        log_max_memory_used_threshold_type=None,
        mac_pool=None,
        maintenance_reason_required=None,
        management_network=None,
        memory_policy=None,
        migration=None,
        name=None,
        network_filters=None,
        networks=None,
        optional_reason=None,
        permissions=None,
        required_rng_sources=None,
        scheduling_policy=None,
        serial_number=None,
        supported_versions=None,
        switch_type=None,
        threads_as_cores=None,
        trusted_service=None,
        tunnel_migration=None,
        version=None,
        virt_service=None,
        vnc_encryption=None,
    ):
        super(Cluster, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.affinity_groups = affinity_groups
        self.ballooning_enabled = ballooning_enabled
        self.bios_type = bios_type
        self.cpu = cpu
        self.cpu_profiles = cpu_profiles
        self.custom_scheduling_policy_properties = custom_scheduling_policy_properties
        self.data_center = data_center
        self.display = display
        self.enabled_features = enabled_features
        self.error_handling = error_handling
        self.external_network_providers = external_network_providers
        self.fencing_policy = fencing_policy
        self.fips_mode = fips_mode
        self.firewall_type = firewall_type
        self.gluster_hooks = gluster_hooks
        self.gluster_service = gluster_service
        self.gluster_tuned_profile = gluster_tuned_profile
        self.gluster_volumes = gluster_volumes
        self.ha_reservation = ha_reservation
        self.ksm = ksm
        self.log_max_memory_used_threshold = log_max_memory_used_threshold
        self.log_max_memory_used_threshold_type = log_max_memory_used_threshold_type
        self.mac_pool = mac_pool
        self.maintenance_reason_required = maintenance_reason_required
        self.management_network = management_network
        self.memory_policy = memory_policy
        self.migration = migration
        self.network_filters = network_filters
        self.networks = networks
        self.optional_reason = optional_reason
        self.permissions = permissions
        self.required_rng_sources = required_rng_sources
        self.scheduling_policy = scheduling_policy
        self.serial_number = serial_number
        self.supported_versions = supported_versions
        self.switch_type = switch_type
        self.threads_as_cores = threads_as_cores
        self.trusted_service = trusted_service
        self.tunnel_migration = tunnel_migration
        self.version = version
        self.virt_service = virt_service
        self.vnc_encryption = vnc_encryption

    @property
    def serial_number(self):
        """
        Returns the value of the `serial_number` property.
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """
        Sets the value of the `serial_number` property.
        """
        Struct._check_type('serial_number', value, SerialNumber)
        self._serial_number = value

    @property
    def threads_as_cores(self):
        """
        Returns the value of the `threads_as_cores` property.
        """
        return self._threads_as_cores

    @threads_as_cores.setter
    def threads_as_cores(self, value):
        """
        Sets the value of the `threads_as_cores` property.
        """
        self._threads_as_cores = value

    @property
    def gluster_volumes(self):
        """
        Returns the value of the `gluster_volumes` property.
        """
        return self._gluster_volumes

    @gluster_volumes.setter
    def gluster_volumes(self, value):
        """
        Sets the value of the `gluster_volumes` property.
        """
        self._gluster_volumes = value

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, Version)
        self._version = value

    @property
    def display(self):
        """
        Returns the value of the `display` property.
        """
        return self._display

    @display.setter
    def display(self, value):
        """
        Sets the value of the `display` property.
        """
        Struct._check_type('display', value, Display)
        self._display = value

    @property
    def ballooning_enabled(self):
        """
        Returns the value of the `ballooning_enabled` property.
        """
        return self._ballooning_enabled

    @ballooning_enabled.setter
    def ballooning_enabled(self, value):
        """
        Sets the value of the `ballooning_enabled` property.
        """
        self._ballooning_enabled = value

    @property
    def cpu(self):
        """
        Returns the value of the `cpu` property.
        """
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        """
        Sets the value of the `cpu` property.
        """
        Struct._check_type('cpu', value, Cpu)
        self._cpu = value

    @property
    def log_max_memory_used_threshold(self):
        """
        Returns the value of the `log_max_memory_used_threshold` property.
        """
        return self._log_max_memory_used_threshold

    @log_max_memory_used_threshold.setter
    def log_max_memory_used_threshold(self, value):
        """
        Sets the value of the `log_max_memory_used_threshold` property.
        """
        self._log_max_memory_used_threshold = value

    @property
    def external_network_providers(self):
        """
        Returns the value of the `external_network_providers` property.
        """
        return self._external_network_providers

    @external_network_providers.setter
    def external_network_providers(self, value):
        """
        Sets the value of the `external_network_providers` property.
        """
        self._external_network_providers = value

    @property
    def mac_pool(self):
        """
        Returns the value of the `mac_pool` property.
        """
        return self._mac_pool

    @mac_pool.setter
    def mac_pool(self, value):
        """
        Sets the value of the `mac_pool` property.
        """
        Struct._check_type('mac_pool', value, MacPool)
        self._mac_pool = value

    @property
    def firewall_type(self):
        """
        Returns the value of the `firewall_type` property.
        """
        return self._firewall_type

    @firewall_type.setter
    def firewall_type(self, value):
        """
        Sets the value of the `firewall_type` property.
        """
        Struct._check_type('firewall_type', value, FirewallType)
        self._firewall_type = value

    @property
    def required_rng_sources(self):
        """
        Returns the value of the `required_rng_sources` property.
        """
        return self._required_rng_sources

    @required_rng_sources.setter
    def required_rng_sources(self, value):
        """
        Sets the value of the `required_rng_sources` property.
        """
        self._required_rng_sources = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def memory_policy(self):
        """
        Returns the value of the `memory_policy` property.
        """
        return self._memory_policy

    @memory_policy.setter
    def memory_policy(self, value):
        """
        Sets the value of the `memory_policy` property.
        """
        Struct._check_type('memory_policy', value, MemoryPolicy)
        self._memory_policy = value

    @property
    def fencing_policy(self):
        """
        Returns the value of the `fencing_policy` property.
        """
        return self._fencing_policy

    @fencing_policy.setter
    def fencing_policy(self, value):
        """
        Sets the value of the `fencing_policy` property.
        """
        Struct._check_type('fencing_policy', value, FencingPolicy)
        self._fencing_policy = value

    @property
    def enabled_features(self):
        """
        Returns the value of the `enabled_features` property.
        """
        return self._enabled_features

    @enabled_features.setter
    def enabled_features(self, value):
        """
        Sets the value of the `enabled_features` property.
        """
        self._enabled_features = value

    @property
    def network_filters(self):
        """
        Returns the value of the `network_filters` property.
        """
        return self._network_filters

    @network_filters.setter
    def network_filters(self, value):
        """
        Sets the value of the `network_filters` property.
        """
        self._network_filters = value

    @property
    def virt_service(self):
        """
        Returns the value of the `virt_service` property.
        """
        return self._virt_service

    @virt_service.setter
    def virt_service(self, value):
        """
        Sets the value of the `virt_service` property.
        """
        self._virt_service = value

    @property
    def tunnel_migration(self):
        """
        Returns the value of the `tunnel_migration` property.
        """
        return self._tunnel_migration

    @tunnel_migration.setter
    def tunnel_migration(self, value):
        """
        Sets the value of the `tunnel_migration` property.
        """
        self._tunnel_migration = value

    @property
    def gluster_service(self):
        """
        Returns the value of the `gluster_service` property.
        """
        return self._gluster_service

    @gluster_service.setter
    def gluster_service(self, value):
        """
        Sets the value of the `gluster_service` property.
        """
        self._gluster_service = value

    @property
    def trusted_service(self):
        """
        Returns the value of the `trusted_service` property.
        """
        return self._trusted_service

    @trusted_service.setter
    def trusted_service(self, value):
        """
        Sets the value of the `trusted_service` property.
        """
        self._trusted_service = value

    @property
    def migration(self):
        """
        Returns the value of the `migration` property.
        """
        return self._migration

    @migration.setter
    def migration(self, value):
        """
        Sets the value of the `migration` property.
        """
        Struct._check_type('migration', value, MigrationOptions)
        self._migration = value

    @property
    def fips_mode(self):
        """
        Returns the value of the `fips_mode` property.
        """
        return self._fips_mode

    @fips_mode.setter
    def fips_mode(self, value):
        """
        Sets the value of the `fips_mode` property.
        """
        Struct._check_type('fips_mode', value, FipsMode)
        self._fips_mode = value

    @property
    def optional_reason(self):
        """
        Returns the value of the `optional_reason` property.
        """
        return self._optional_reason

    @optional_reason.setter
    def optional_reason(self, value):
        """
        Sets the value of the `optional_reason` property.
        """
        self._optional_reason = value

    @property
    def ha_reservation(self):
        """
        Returns the value of the `ha_reservation` property.
        """
        return self._ha_reservation

    @ha_reservation.setter
    def ha_reservation(self, value):
        """
        Sets the value of the `ha_reservation` property.
        """
        self._ha_reservation = value

    @property
    def ksm(self):
        """
        Returns the value of the `ksm` property.
        """
        return self._ksm

    @ksm.setter
    def ksm(self, value):
        """
        Sets the value of the `ksm` property.
        """
        Struct._check_type('ksm', value, Ksm)
        self._ksm = value

    @property
    def log_max_memory_used_threshold_type(self):
        """
        Returns the value of the `log_max_memory_used_threshold_type` property.
        """
        return self._log_max_memory_used_threshold_type

    @log_max_memory_used_threshold_type.setter
    def log_max_memory_used_threshold_type(self, value):
        """
        Sets the value of the `log_max_memory_used_threshold_type` property.
        """
        Struct._check_type('log_max_memory_used_threshold_type', value, LogMaxMemoryUsedThresholdType)
        self._log_max_memory_used_threshold_type = value

    @property
    def affinity_groups(self):
        """
        Returns the value of the `affinity_groups` property.
        """
        return self._affinity_groups

    @affinity_groups.setter
    def affinity_groups(self, value):
        """
        Sets the value of the `affinity_groups` property.
        """
        self._affinity_groups = value

    @property
    def gluster_hooks(self):
        """
        Returns the value of the `gluster_hooks` property.
        """
        return self._gluster_hooks

    @gluster_hooks.setter
    def gluster_hooks(self, value):
        """
        Sets the value of the `gluster_hooks` property.
        """
        self._gluster_hooks = value

    @property
    def error_handling(self):
        """
        Returns the value of the `error_handling` property.
        """
        return self._error_handling

    @error_handling.setter
    def error_handling(self, value):
        """
        Sets the value of the `error_handling` property.
        """
        Struct._check_type('error_handling', value, ErrorHandling)
        self._error_handling = value

    @property
    def networks(self):
        """
        Returns the value of the `networks` property.
        """
        return self._networks

    @networks.setter
    def networks(self, value):
        """
        Sets the value of the `networks` property.
        """
        self._networks = value

    @property
    def gluster_tuned_profile(self):
        """
        Returns the value of the `gluster_tuned_profile` property.
        """
        return self._gluster_tuned_profile

    @gluster_tuned_profile.setter
    def gluster_tuned_profile(self, value):
        """
        Sets the value of the `gluster_tuned_profile` property.
        """
        self._gluster_tuned_profile = value

    @property
    def maintenance_reason_required(self):
        """
        Returns the value of the `maintenance_reason_required` property.
        """
        return self._maintenance_reason_required

    @maintenance_reason_required.setter
    def maintenance_reason_required(self, value):
        """
        Sets the value of the `maintenance_reason_required` property.
        """
        self._maintenance_reason_required = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def scheduling_policy(self):
        """
        Returns the value of the `scheduling_policy` property.
        """
        return self._scheduling_policy

    @scheduling_policy.setter
    def scheduling_policy(self, value):
        """
        Sets the value of the `scheduling_policy` property.
        """
        Struct._check_type('scheduling_policy', value, SchedulingPolicy)
        self._scheduling_policy = value

    @property
    def cpu_profiles(self):
        """
        Returns the value of the `cpu_profiles` property.
        """
        return self._cpu_profiles

    @cpu_profiles.setter
    def cpu_profiles(self, value):
        """
        Sets the value of the `cpu_profiles` property.
        """
        self._cpu_profiles = value

    @property
    def management_network(self):
        """
        Returns the value of the `management_network` property.
        """
        return self._management_network

    @management_network.setter
    def management_network(self, value):
        """
        Sets the value of the `management_network` property.
        """
        Struct._check_type('management_network', value, Network)
        self._management_network = value

    @property
    def switch_type(self):
        """
        Returns the value of the `switch_type` property.
        """
        return self._switch_type

    @switch_type.setter
    def switch_type(self, value):
        """
        Sets the value of the `switch_type` property.
        """
        Struct._check_type('switch_type', value, SwitchType)
        self._switch_type = value

    @property
    def vnc_encryption(self):
        """
        Returns the value of the `vnc_encryption` property.
        """
        return self._vnc_encryption

    @vnc_encryption.setter
    def vnc_encryption(self, value):
        """
        Sets the value of the `vnc_encryption` property.
        """
        self._vnc_encryption = value

    @property
    def supported_versions(self):
        """
        Returns the value of the `supported_versions` property.
        """
        return self._supported_versions

    @supported_versions.setter
    def supported_versions(self, value):
        """
        Sets the value of the `supported_versions` property.
        """
        self._supported_versions = value

    @property
    def bios_type(self):
        """
        Returns the value of the `bios_type` property.
        """
        return self._bios_type

    @bios_type.setter
    def bios_type(self, value):
        """
        Sets the value of the `bios_type` property.
        """
        Struct._check_type('bios_type', value, BiosType)
        self._bios_type = value

    @property
    def custom_scheduling_policy_properties(self):
        """
        Returns the value of the `custom_scheduling_policy_properties` property.
        """
        return self._custom_scheduling_policy_properties

    @custom_scheduling_policy_properties.setter
    def custom_scheduling_policy_properties(self, value):
        """
        Sets the value of the `custom_scheduling_policy_properties` property.
        """
        self._custom_scheduling_policy_properties = value


class ClusterFeature(Identified):

    def __init__(
        self,
        cluster_level=None,
        comment=None,
        description=None,
        id=None,
        name=None,
    ):
        super(ClusterFeature, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cluster_level = cluster_level

    @property
    def cluster_level(self):
        """
        Returns the value of the `cluster_level` property.
        """
        return self._cluster_level

    @cluster_level.setter
    def cluster_level(self, value):
        """
        Sets the value of the `cluster_level` property.
        """
        Struct._check_type('cluster_level', value, ClusterLevel)
        self._cluster_level = value


class ClusterLevel(Identified):

    def __init__(
        self,
        cluster_features=None,
        comment=None,
        cpu_types=None,
        description=None,
        id=None,
        name=None,
        permits=None,
    ):
        super(ClusterLevel, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cluster_features = cluster_features
        self.cpu_types = cpu_types
        self.permits = permits

    @property
    def cluster_features(self):
        """
        Returns the value of the `cluster_features` property.
        """
        return self._cluster_features

    @cluster_features.setter
    def cluster_features(self, value):
        """
        Sets the value of the `cluster_features` property.
        """
        self._cluster_features = value

    @property
    def cpu_types(self):
        """
        Returns the value of the `cpu_types` property.
        """
        return self._cpu_types

    @cpu_types.setter
    def cpu_types(self, value):
        """
        Sets the value of the `cpu_types` property.
        """
        self._cpu_types = value

    @property
    def permits(self):
        """
        Returns the value of the `permits` property.
        """
        return self._permits

    @permits.setter
    def permits(self, value):
        """
        Sets the value of the `permits` property.
        """
        self._permits = value


class CpuProfile(Identified):

    def __init__(
        self,
        cluster=None,
        comment=None,
        description=None,
        id=None,
        name=None,
        permissions=None,
        qos=None,
    ):
        super(CpuProfile, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cluster = cluster
        self.permissions = permissions
        self.qos = qos

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def qos(self):
        """
        Returns the value of the `qos` property.
        """
        return self._qos

    @qos.setter
    def qos(self, value):
        """
        Sets the value of the `qos` property.
        """
        Struct._check_type('qos', value, Qos)
        self._qos = value


class DataCenter(Identified):

    def __init__(
        self,
        clusters=None,
        comment=None,
        description=None,
        id=None,
        iscsi_bonds=None,
        local=None,
        mac_pool=None,
        name=None,
        networks=None,
        permissions=None,
        qoss=None,
        quota_mode=None,
        quotas=None,
        status=None,
        storage_domains=None,
        storage_format=None,
        supported_versions=None,
        version=None,
    ):
        super(DataCenter, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.clusters = clusters
        self.iscsi_bonds = iscsi_bonds
        self.local = local
        self.mac_pool = mac_pool
        self.networks = networks
        self.permissions = permissions
        self.qoss = qoss
        self.quota_mode = quota_mode
        self.quotas = quotas
        self.status = status
        self.storage_domains = storage_domains
        self.storage_format = storage_format
        self.supported_versions = supported_versions
        self.version = version

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, Version)
        self._version = value

    @property
    def quotas(self):
        """
        Returns the value of the `quotas` property.
        """
        return self._quotas

    @quotas.setter
    def quotas(self, value):
        """
        Sets the value of the `quotas` property.
        """
        self._quotas = value

    @property
    def storage_format(self):
        """
        Returns the value of the `storage_format` property.
        """
        return self._storage_format

    @storage_format.setter
    def storage_format(self, value):
        """
        Sets the value of the `storage_format` property.
        """
        Struct._check_type('storage_format', value, StorageFormat)
        self._storage_format = value

    @property
    def quota_mode(self):
        """
        Returns the value of the `quota_mode` property.
        """
        return self._quota_mode

    @quota_mode.setter
    def quota_mode(self, value):
        """
        Sets the value of the `quota_mode` property.
        """
        Struct._check_type('quota_mode', value, QuotaModeType)
        self._quota_mode = value

    @property
    def qoss(self):
        """
        Returns the value of the `qoss` property.
        """
        return self._qoss

    @qoss.setter
    def qoss(self, value):
        """
        Sets the value of the `qoss` property.
        """
        self._qoss = value

    @property
    def mac_pool(self):
        """
        Returns the value of the `mac_pool` property.
        """
        return self._mac_pool

    @mac_pool.setter
    def mac_pool(self, value):
        """
        Sets the value of the `mac_pool` property.
        """
        Struct._check_type('mac_pool', value, MacPool)
        self._mac_pool = value

    @property
    def storage_domains(self):
        """
        Returns the value of the `storage_domains` property.
        """
        return self._storage_domains

    @storage_domains.setter
    def storage_domains(self, value):
        """
        Sets the value of the `storage_domains` property.
        """
        self._storage_domains = value

    @property
    def iscsi_bonds(self):
        """
        Returns the value of the `iscsi_bonds` property.
        """
        return self._iscsi_bonds

    @iscsi_bonds.setter
    def iscsi_bonds(self, value):
        """
        Sets the value of the `iscsi_bonds` property.
        """
        self._iscsi_bonds = value

    @property
    def networks(self):
        """
        Returns the value of the `networks` property.
        """
        return self._networks

    @networks.setter
    def networks(self, value):
        """
        Sets the value of the `networks` property.
        """
        self._networks = value

    @property
    def local(self):
        """
        Returns the value of the `local` property.
        """
        return self._local

    @local.setter
    def local(self, value):
        """
        Sets the value of the `local` property.
        """
        self._local = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def supported_versions(self):
        """
        Returns the value of the `supported_versions` property.
        """
        return self._supported_versions

    @supported_versions.setter
    def supported_versions(self, value):
        """
        Sets the value of the `supported_versions` property.
        """
        self._supported_versions = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, DataCenterStatus)
        self._status = value

    @property
    def clusters(self):
        """
        Returns the value of the `clusters` property.
        """
        return self._clusters

    @clusters.setter
    def clusters(self, value):
        """
        Sets the value of the `clusters` property.
        """
        self._clusters = value


class Device(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        instance_type=None,
        name=None,
        template=None,
        vm=None,
        vms=None,
    ):
        super(Device, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.instance_type = instance_type
        self.template = template
        self.vm = vm
        self.vms = vms

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def instance_type(self):
        """
        Returns the value of the `instance_type` property.
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, value):
        """
        Sets the value of the `instance_type` property.
        """
        Struct._check_type('instance_type', value, InstanceType)
        self._instance_type = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def vms(self):
        """
        Returns the value of the `vms` property.
        """
        return self._vms

    @vms.setter
    def vms(self, value):
        """
        Sets the value of the `vms` property.
        """
        self._vms = value


class Disk(Device):

    def __init__(
        self,
        active=None,
        actual_size=None,
        alias=None,
        backup=None,
        backup_mode=None,
        bootable=None,
        comment=None,
        content_type=None,
        description=None,
        disk_profile=None,
        disk_snapshots=None,
        external_disk=None,
        format=None,
        id=None,
        image_id=None,
        initial_size=None,
        instance_type=None,
        interface=None,
        logical_name=None,
        lun_storage=None,
        name=None,
        openstack_volume_type=None,
        permissions=None,
        propagate_errors=None,
        provisioned_size=None,
        qcow_version=None,
        quota=None,
        read_only=None,
        sgio=None,
        shareable=None,
        snapshot=None,
        sparse=None,
        statistics=None,
        status=None,
        storage_domain=None,
        storage_domains=None,
        storage_type=None,
        template=None,
        total_size=None,
        uses_scsi_reservation=None,
        vm=None,
        vms=None,
        wipe_after_delete=None,
    ):
        super(Disk, self).__init__(
            comment=comment,
            description=description,
            id=id,
            instance_type=instance_type,
            name=name,
            template=template,
            vm=vm,
            vms=vms,
        )
        self.active = active
        self.actual_size = actual_size
        self.alias = alias
        self.backup = backup
        self.backup_mode = backup_mode
        self.bootable = bootable
        self.content_type = content_type
        self.disk_profile = disk_profile
        self.disk_snapshots = disk_snapshots
        self.external_disk = external_disk
        self.format = format
        self.image_id = image_id
        self.initial_size = initial_size
        self.interface = interface
        self.logical_name = logical_name
        self.lun_storage = lun_storage
        self.openstack_volume_type = openstack_volume_type
        self.permissions = permissions
        self.propagate_errors = propagate_errors
        self.provisioned_size = provisioned_size
        self.qcow_version = qcow_version
        self.quota = quota
        self.read_only = read_only
        self.sgio = sgio
        self.shareable = shareable
        self.snapshot = snapshot
        self.sparse = sparse
        self.statistics = statistics
        self.status = status
        self.storage_domain = storage_domain
        self.storage_domains = storage_domains
        self.storage_type = storage_type
        self.total_size = total_size
        self.uses_scsi_reservation = uses_scsi_reservation
        self.wipe_after_delete = wipe_after_delete

    @property
    def initial_size(self):
        """
        Returns the value of the `initial_size` property.
        """
        return self._initial_size

    @initial_size.setter
    def initial_size(self, value):
        """
        Sets the value of the `initial_size` property.
        """
        self._initial_size = value

    @property
    def qcow_version(self):
        """
        Returns the value of the `qcow_version` property.
        """
        return self._qcow_version

    @qcow_version.setter
    def qcow_version(self, value):
        """
        Sets the value of the `qcow_version` property.
        """
        Struct._check_type('qcow_version', value, QcowVersion)
        self._qcow_version = value

    @property
    def total_size(self):
        """
        Returns the value of the `total_size` property.
        """
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        """
        Sets the value of the `total_size` property.
        """
        self._total_size = value

    @property
    def content_type(self):
        """
        Returns the value of the `content_type` property.
        """
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """
        Sets the value of the `content_type` property.
        """
        Struct._check_type('content_type', value, DiskContentType)
        self._content_type = value

    @property
    def format(self):
        """
        Returns the value of the `format` property.
        """
        return self._format

    @format.setter
    def format(self, value):
        """
        Sets the value of the `format` property.
        """
        Struct._check_type('format', value, DiskFormat)
        self._format = value

    @property
    def active(self):
        """
        Returns the value of the `active` property.
        """
        return self._active

    @active.setter
    def active(self, value):
        """
        Sets the value of the `active` property.
        """
        self._active = value

    @property
    def storage_domains(self):
        """
        Returns the value of the `storage_domains` property.
        """
        return self._storage_domains

    @storage_domains.setter
    def storage_domains(self, value):
        """
        Sets the value of the `storage_domains` property.
        """
        self._storage_domains = value

    @property
    def actual_size(self):
        """
        Returns the value of the `actual_size` property.
        """
        return self._actual_size

    @actual_size.setter
    def actual_size(self, value):
        """
        Sets the value of the `actual_size` property.
        """
        self._actual_size = value

    @property
    def propagate_errors(self):
        """
        Returns the value of the `propagate_errors` property.
        """
        return self._propagate_errors

    @propagate_errors.setter
    def propagate_errors(self, value):
        """
        Sets the value of the `propagate_errors` property.
        """
        self._propagate_errors = value

    @property
    def external_disk(self):
        """
        Returns the value of the `external_disk` property.
        """
        return self._external_disk

    @external_disk.setter
    def external_disk(self, value):
        """
        Sets the value of the `external_disk` property.
        """
        self._external_disk = value

    @property
    def uses_scsi_reservation(self):
        """
        Returns the value of the `uses_scsi_reservation` property.
        """
        return self._uses_scsi_reservation

    @uses_scsi_reservation.setter
    def uses_scsi_reservation(self, value):
        """
        Sets the value of the `uses_scsi_reservation` property.
        """
        self._uses_scsi_reservation = value

    @property
    def snapshot(self):
        """
        Returns the value of the `snapshot` property.
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value):
        """
        Sets the value of the `snapshot` property.
        """
        Struct._check_type('snapshot', value, Snapshot)
        self._snapshot = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, DiskStatus)
        self._status = value

    @property
    def logical_name(self):
        """
        Returns the value of the `logical_name` property.
        """
        return self._logical_name

    @logical_name.setter
    def logical_name(self, value):
        """
        Sets the value of the `logical_name` property.
        """
        self._logical_name = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value

    @property
    def shareable(self):
        """
        Returns the value of the `shareable` property.
        """
        return self._shareable

    @shareable.setter
    def shareable(self, value):
        """
        Sets the value of the `shareable` property.
        """
        self._shareable = value

    @property
    def backup(self):
        """
        Returns the value of the `backup` property.
        """
        return self._backup

    @backup.setter
    def backup(self, value):
        """
        Sets the value of the `backup` property.
        """
        Struct._check_type('backup', value, DiskBackup)
        self._backup = value

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def disk_snapshots(self):
        """
        Returns the value of the `disk_snapshots` property.
        """
        return self._disk_snapshots

    @disk_snapshots.setter
    def disk_snapshots(self, value):
        """
        Sets the value of the `disk_snapshots` property.
        """
        self._disk_snapshots = value

    @property
    def provisioned_size(self):
        """
        Returns the value of the `provisioned_size` property.
        """
        return self._provisioned_size

    @provisioned_size.setter
    def provisioned_size(self, value):
        """
        Sets the value of the `provisioned_size` property.
        """
        self._provisioned_size = value

    @property
    def backup_mode(self):
        """
        Returns the value of the `backup_mode` property.
        """
        return self._backup_mode

    @backup_mode.setter
    def backup_mode(self, value):
        """
        Sets the value of the `backup_mode` property.
        """
        Struct._check_type('backup_mode', value, DiskBackupMode)
        self._backup_mode = value

    @property
    def openstack_volume_type(self):
        """
        Returns the value of the `openstack_volume_type` property.
        """
        return self._openstack_volume_type

    @openstack_volume_type.setter
    def openstack_volume_type(self, value):
        """
        Sets the value of the `openstack_volume_type` property.
        """
        Struct._check_type('openstack_volume_type', value, OpenStackVolumeType)
        self._openstack_volume_type = value

    @property
    def alias(self):
        """
        Returns the value of the `alias` property.
        """
        return self._alias

    @alias.setter
    def alias(self, value):
        """
        Sets the value of the `alias` property.
        """
        self._alias = value

    @property
    def sparse(self):
        """
        Returns the value of the `sparse` property.
        """
        return self._sparse

    @sparse.setter
    def sparse(self, value):
        """
        Sets the value of the `sparse` property.
        """
        self._sparse = value

    @property
    def bootable(self):
        """
        Returns the value of the `bootable` property.
        """
        return self._bootable

    @bootable.setter
    def bootable(self, value):
        """
        Sets the value of the `bootable` property.
        """
        self._bootable = value

    @property
    def sgio(self):
        """
        Returns the value of the `sgio` property.
        """
        return self._sgio

    @sgio.setter
    def sgio(self, value):
        """
        Sets the value of the `sgio` property.
        """
        Struct._check_type('sgio', value, ScsiGenericIO)
        self._sgio = value

    @property
    def disk_profile(self):
        """
        Returns the value of the `disk_profile` property.
        """
        return self._disk_profile

    @disk_profile.setter
    def disk_profile(self, value):
        """
        Sets the value of the `disk_profile` property.
        """
        Struct._check_type('disk_profile', value, DiskProfile)
        self._disk_profile = value

    @property
    def interface(self):
        """
        Returns the value of the `interface` property.
        """
        return self._interface

    @interface.setter
    def interface(self, value):
        """
        Sets the value of the `interface` property.
        """
        Struct._check_type('interface', value, DiskInterface)
        self._interface = value

    @property
    def storage_type(self):
        """
        Returns the value of the `storage_type` property.
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, value):
        """
        Sets the value of the `storage_type` property.
        """
        Struct._check_type('storage_type', value, DiskStorageType)
        self._storage_type = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def lun_storage(self):
        """
        Returns the value of the `lun_storage` property.
        """
        return self._lun_storage

    @lun_storage.setter
    def lun_storage(self, value):
        """
        Sets the value of the `lun_storage` property.
        """
        Struct._check_type('lun_storage', value, HostStorage)
        self._lun_storage = value

    @property
    def wipe_after_delete(self):
        """
        Returns the value of the `wipe_after_delete` property.
        """
        return self._wipe_after_delete

    @wipe_after_delete.setter
    def wipe_after_delete(self, value):
        """
        Sets the value of the `wipe_after_delete` property.
        """
        self._wipe_after_delete = value

    @property
    def quota(self):
        """
        Returns the value of the `quota` property.
        """
        return self._quota

    @quota.setter
    def quota(self, value):
        """
        Sets the value of the `quota` property.
        """
        Struct._check_type('quota', value, Quota)
        self._quota = value

    @property
    def image_id(self):
        """
        Returns the value of the `image_id` property.
        """
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        """
        Sets the value of the `image_id` property.
        """
        self._image_id = value

    @property
    def read_only(self):
        """
        Returns the value of the `read_only` property.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """
        Sets the value of the `read_only` property.
        """
        self._read_only = value


class DiskAttachment(Identified):

    def __init__(
        self,
        active=None,
        bootable=None,
        comment=None,
        description=None,
        disk=None,
        id=None,
        interface=None,
        logical_name=None,
        name=None,
        pass_discard=None,
        read_only=None,
        template=None,
        uses_scsi_reservation=None,
        vm=None,
    ):
        super(DiskAttachment, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.active = active
        self.bootable = bootable
        self.disk = disk
        self.interface = interface
        self.logical_name = logical_name
        self.pass_discard = pass_discard
        self.read_only = read_only
        self.template = template
        self.uses_scsi_reservation = uses_scsi_reservation
        self.vm = vm

    @property
    def disk(self):
        """
        Returns the value of the `disk` property.
        """
        return self._disk

    @disk.setter
    def disk(self, value):
        """
        Sets the value of the `disk` property.
        """
        Struct._check_type('disk', value, Disk)
        self._disk = value

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def uses_scsi_reservation(self):
        """
        Returns the value of the `uses_scsi_reservation` property.
        """
        return self._uses_scsi_reservation

    @uses_scsi_reservation.setter
    def uses_scsi_reservation(self, value):
        """
        Sets the value of the `uses_scsi_reservation` property.
        """
        self._uses_scsi_reservation = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def pass_discard(self):
        """
        Returns the value of the `pass_discard` property.
        """
        return self._pass_discard

    @pass_discard.setter
    def pass_discard(self, value):
        """
        Sets the value of the `pass_discard` property.
        """
        self._pass_discard = value

    @property
    def bootable(self):
        """
        Returns the value of the `bootable` property.
        """
        return self._bootable

    @bootable.setter
    def bootable(self, value):
        """
        Sets the value of the `bootable` property.
        """
        self._bootable = value

    @property
    def active(self):
        """
        Returns the value of the `active` property.
        """
        return self._active

    @active.setter
    def active(self, value):
        """
        Sets the value of the `active` property.
        """
        self._active = value

    @property
    def logical_name(self):
        """
        Returns the value of the `logical_name` property.
        """
        return self._logical_name

    @logical_name.setter
    def logical_name(self, value):
        """
        Sets the value of the `logical_name` property.
        """
        self._logical_name = value

    @property
    def interface(self):
        """
        Returns the value of the `interface` property.
        """
        return self._interface

    @interface.setter
    def interface(self, value):
        """
        Sets the value of the `interface` property.
        """
        Struct._check_type('interface', value, DiskInterface)
        self._interface = value

    @property
    def read_only(self):
        """
        Returns the value of the `read_only` property.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """
        Sets the value of the `read_only` property.
        """
        self._read_only = value


class DiskProfile(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        permissions=None,
        qos=None,
        storage_domain=None,
    ):
        super(DiskProfile, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.permissions = permissions
        self.qos = qos
        self.storage_domain = storage_domain

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def qos(self):
        """
        Returns the value of the `qos` property.
        """
        return self._qos

    @qos.setter
    def qos(self, value):
        """
        Sets the value of the `qos` property.
        """
        Struct._check_type('qos', value, Qos)
        self._qos = value


class DiskSnapshot(Disk):

    def __init__(
        self,
        active=None,
        actual_size=None,
        alias=None,
        backup=None,
        backup_mode=None,
        bootable=None,
        comment=None,
        content_type=None,
        description=None,
        disk=None,
        disk_profile=None,
        disk_snapshots=None,
        external_disk=None,
        format=None,
        id=None,
        image_id=None,
        initial_size=None,
        instance_type=None,
        interface=None,
        logical_name=None,
        lun_storage=None,
        name=None,
        openstack_volume_type=None,
        parent=None,
        permissions=None,
        propagate_errors=None,
        provisioned_size=None,
        qcow_version=None,
        quota=None,
        read_only=None,
        sgio=None,
        shareable=None,
        snapshot=None,
        sparse=None,
        statistics=None,
        status=None,
        storage_domain=None,
        storage_domains=None,
        storage_type=None,
        template=None,
        total_size=None,
        uses_scsi_reservation=None,
        vm=None,
        vms=None,
        wipe_after_delete=None,
    ):
        super(DiskSnapshot, self).__init__(
            active=active,
            actual_size=actual_size,
            alias=alias,
            backup=backup,
            backup_mode=backup_mode,
            bootable=bootable,
            comment=comment,
            content_type=content_type,
            description=description,
            disk_profile=disk_profile,
            disk_snapshots=disk_snapshots,
            external_disk=external_disk,
            format=format,
            id=id,
            image_id=image_id,
            initial_size=initial_size,
            instance_type=instance_type,
            interface=interface,
            logical_name=logical_name,
            lun_storage=lun_storage,
            name=name,
            openstack_volume_type=openstack_volume_type,
            permissions=permissions,
            propagate_errors=propagate_errors,
            provisioned_size=provisioned_size,
            qcow_version=qcow_version,
            quota=quota,
            read_only=read_only,
            sgio=sgio,
            shareable=shareable,
            snapshot=snapshot,
            sparse=sparse,
            statistics=statistics,
            status=status,
            storage_domain=storage_domain,
            storage_domains=storage_domains,
            storage_type=storage_type,
            template=template,
            total_size=total_size,
            uses_scsi_reservation=uses_scsi_reservation,
            vm=vm,
            vms=vms,
            wipe_after_delete=wipe_after_delete,
        )
        self.disk = disk
        self.parent = parent

    @property
    def parent(self):
        """
        Returns the value of the `parent` property.
        """
        return self._parent

    @parent.setter
    def parent(self, value):
        """
        Sets the value of the `parent` property.
        """
        Struct._check_type('parent', value, DiskSnapshot)
        self._parent = value

    @property
    def disk(self):
        """
        Returns the value of the `disk` property.
        """
        return self._disk

    @disk.setter
    def disk(self, value):
        """
        Sets the value of the `disk` property.
        """
        Struct._check_type('disk', value, Disk)
        self._disk = value


class Domain(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        groups=None,
        id=None,
        name=None,
        user=None,
        users=None,
    ):
        super(Domain, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.groups = groups
        self.user = user
        self.users = users

    @property
    def users(self):
        """
        Returns the value of the `users` property.
        """
        return self._users

    @users.setter
    def users(self, value):
        """
        Sets the value of the `users` property.
        """
        self._users = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def groups(self):
        """
        Returns the value of the `groups` property.
        """
        return self._groups

    @groups.setter
    def groups(self, value):
        """
        Sets the value of the `groups` property.
        """
        self._groups = value


class Event(Identified):

    def __init__(
        self,
        cluster=None,
        code=None,
        comment=None,
        correlation_id=None,
        custom_data=None,
        custom_id=None,
        data_center=None,
        description=None,
        flood_rate=None,
        host=None,
        id=None,
        index=None,
        log_on_host=None,
        name=None,
        origin=None,
        severity=None,
        storage_domain=None,
        template=None,
        time=None,
        user=None,
        vm=None,
    ):
        super(Event, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.cluster = cluster
        self.code = code
        self.correlation_id = correlation_id
        self.custom_data = custom_data
        self.custom_id = custom_id
        self.data_center = data_center
        self.flood_rate = flood_rate
        self.host = host
        self.index = index
        self.log_on_host = log_on_host
        self.origin = origin
        self.severity = severity
        self.storage_domain = storage_domain
        self.template = template
        self.time = time
        self.user = user
        self.vm = vm

    @property
    def severity(self):
        """
        Returns the value of the `severity` property.
        """
        return self._severity

    @severity.setter
    def severity(self, value):
        """
        Sets the value of the `severity` property.
        """
        Struct._check_type('severity', value, LogSeverity)
        self._severity = value

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def code(self):
        """
        Returns the value of the `code` property.
        """
        return self._code

    @code.setter
    def code(self, value):
        """
        Sets the value of the `code` property.
        """
        self._code = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def origin(self):
        """
        Returns the value of the `origin` property.
        """
        return self._origin

    @origin.setter
    def origin(self, value):
        """
        Sets the value of the `origin` property.
        """
        self._origin = value

    @property
    def correlation_id(self):
        """
        Returns the value of the `correlation_id` property.
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, value):
        """
        Sets the value of the `correlation_id` property.
        """
        self._correlation_id = value

    @property
    def index(self):
        """
        Returns the value of the `index` property.
        """
        return self._index

    @index.setter
    def index(self, value):
        """
        Sets the value of the `index` property.
        """
        self._index = value

    @property
    def flood_rate(self):
        """
        Returns the value of the `flood_rate` property.
        """
        return self._flood_rate

    @flood_rate.setter
    def flood_rate(self, value):
        """
        Sets the value of the `flood_rate` property.
        """
        self._flood_rate = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def custom_id(self):
        """
        Returns the value of the `custom_id` property.
        """
        return self._custom_id

    @custom_id.setter
    def custom_id(self, value):
        """
        Sets the value of the `custom_id` property.
        """
        self._custom_id = value

    @property
    def custom_data(self):
        """
        Returns the value of the `custom_data` property.
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, value):
        """
        Sets the value of the `custom_data` property.
        """
        self._custom_data = value

    @property
    def log_on_host(self):
        """
        Returns the value of the `log_on_host` property.
        """
        return self._log_on_host

    @log_on_host.setter
    def log_on_host(self, value):
        """
        Sets the value of the `log_on_host` property.
        """
        self._log_on_host = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def time(self):
        """
        Returns the value of the `time` property.
        """
        return self._time

    @time.setter
    def time(self, value):
        """
        Sets the value of the `time` property.
        """
        self._time = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value


class EventSubscription(Identified):

    def __init__(
        self,
        address=None,
        comment=None,
        description=None,
        event=None,
        id=None,
        name=None,
        notification_method=None,
        user=None,
    ):
        super(EventSubscription, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.address = address
        self.event = event
        self.notification_method = notification_method
        self.user = user

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def notification_method(self):
        """
        Returns the value of the `notification_method` property.
        """
        return self._notification_method

    @notification_method.setter
    def notification_method(self, value):
        """
        Sets the value of the `notification_method` property.
        """
        Struct._check_type('notification_method', value, NotificationMethod)
        self._notification_method = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        Struct._check_type('user', value, User)
        self._user = value

    @property
    def event(self):
        """
        Returns the value of the `event` property.
        """
        return self._event

    @event.setter
    def event(self, value):
        """
        Sets the value of the `event` property.
        """
        Struct._check_type('event', value, NotifiableEvent)
        self._event = value


class ExternalComputeResource(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        external_host_provider=None,
        id=None,
        name=None,
        provider=None,
        url=None,
        user=None,
    ):
        super(ExternalComputeResource, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.external_host_provider = external_host_provider
        self.provider = provider
        self.url = url
        self.user = user

    @property
    def external_host_provider(self):
        """
        Returns the value of the `external_host_provider` property.
        """
        return self._external_host_provider

    @external_host_provider.setter
    def external_host_provider(self, value):
        """
        Sets the value of the `external_host_provider` property.
        """
        Struct._check_type('external_host_provider', value, ExternalHostProvider)
        self._external_host_provider = value

    @property
    def provider(self):
        """
        Returns the value of the `provider` property.
        """
        return self._provider

    @provider.setter
    def provider(self, value):
        """
        Sets the value of the `provider` property.
        """
        self._provider = value

    @property
    def user(self):
        """
        Returns the value of the `user` property.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the value of the `user` property.
        """
        self._user = value

    @property
    def url(self):
        """
        Returns the value of the `url` property.
        """
        return self._url

    @url.setter
    def url(self, value):
        """
        Sets the value of the `url` property.
        """
        self._url = value


class ExternalDiscoveredHost(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        external_host_provider=None,
        id=None,
        ip=None,
        last_report=None,
        mac=None,
        name=None,
        subnet_name=None,
    ):
        super(ExternalDiscoveredHost, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.external_host_provider = external_host_provider
        self.ip = ip
        self.last_report = last_report
        self.mac = mac
        self.subnet_name = subnet_name

    @property
    def subnet_name(self):
        """
        Returns the value of the `subnet_name` property.
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, value):
        """
        Sets the value of the `subnet_name` property.
        """
        self._subnet_name = value

    @property
    def external_host_provider(self):
        """
        Returns the value of the `external_host_provider` property.
        """
        return self._external_host_provider

    @external_host_provider.setter
    def external_host_provider(self, value):
        """
        Sets the value of the `external_host_provider` property.
        """
        Struct._check_type('external_host_provider', value, ExternalHostProvider)
        self._external_host_provider = value

    @property
    def last_report(self):
        """
        Returns the value of the `last_report` property.
        """
        return self._last_report

    @last_report.setter
    def last_report(self, value):
        """
        Sets the value of the `last_report` property.
        """
        self._last_report = value

    @property
    def ip(self):
        """
        Returns the value of the `ip` property.
        """
        return self._ip

    @ip.setter
    def ip(self, value):
        """
        Sets the value of the `ip` property.
        """
        self._ip = value

    @property
    def mac(self):
        """
        Returns the value of the `mac` property.
        """
        return self._mac

    @mac.setter
    def mac(self, value):
        """
        Sets the value of the `mac` property.
        """
        self._mac = value


class ExternalHost(Identified):

    def __init__(
        self,
        address=None,
        comment=None,
        description=None,
        external_host_provider=None,
        id=None,
        name=None,
    ):
        super(ExternalHost, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.address = address
        self.external_host_provider = external_host_provider

    @property
    def external_host_provider(self):
        """
        Returns the value of the `external_host_provider` property.
        """
        return self._external_host_provider

    @external_host_provider.setter
    def external_host_provider(self, value):
        """
        Sets the value of the `external_host_provider` property.
        """
        Struct._check_type('external_host_provider', value, ExternalHostProvider)
        self._external_host_provider = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value


class ExternalHostGroup(Identified):

    def __init__(
        self,
        architecture_name=None,
        comment=None,
        description=None,
        domain_name=None,
        external_host_provider=None,
        id=None,
        name=None,
        operating_system_name=None,
        subnet_name=None,
    ):
        super(ExternalHostGroup, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.architecture_name = architecture_name
        self.domain_name = domain_name
        self.external_host_provider = external_host_provider
        self.operating_system_name = operating_system_name
        self.subnet_name = subnet_name

    @property
    def subnet_name(self):
        """
        Returns the value of the `subnet_name` property.
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, value):
        """
        Sets the value of the `subnet_name` property.
        """
        self._subnet_name = value

    @property
    def domain_name(self):
        """
        Returns the value of the `domain_name` property.
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        """
        Sets the value of the `domain_name` property.
        """
        self._domain_name = value

    @property
    def external_host_provider(self):
        """
        Returns the value of the `external_host_provider` property.
        """
        return self._external_host_provider

    @external_host_provider.setter
    def external_host_provider(self, value):
        """
        Sets the value of the `external_host_provider` property.
        """
        Struct._check_type('external_host_provider', value, ExternalHostProvider)
        self._external_host_provider = value

    @property
    def operating_system_name(self):
        """
        Returns the value of the `operating_system_name` property.
        """
        return self._operating_system_name

    @operating_system_name.setter
    def operating_system_name(self, value):
        """
        Sets the value of the `operating_system_name` property.
        """
        self._operating_system_name = value

    @property
    def architecture_name(self):
        """
        Returns the value of the `architecture_name` property.
        """
        return self._architecture_name

    @architecture_name.setter
    def architecture_name(self, value):
        """
        Sets the value of the `architecture_name` property.
        """
        self._architecture_name = value


class ExternalNetworkProviderConfiguration(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        external_network_provider=None,
        host=None,
        id=None,
        name=None,
    ):
        super(ExternalNetworkProviderConfiguration, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.external_network_provider = external_network_provider
        self.host = host

    @property
    def external_network_provider(self):
        """
        Returns the value of the `external_network_provider` property.
        """
        return self._external_network_provider

    @external_network_provider.setter
    def external_network_provider(self, value):
        """
        Sets the value of the `external_network_provider` property.
        """
        Struct._check_type('external_network_provider', value, ExternalProvider)
        self._external_network_provider = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value


class ExternalProvider(Identified):

    def __init__(
        self,
        authentication_url=None,
        comment=None,
        description=None,
        id=None,
        name=None,
        password=None,
        properties=None,
        requires_authentication=None,
        url=None,
        username=None,
    ):
        super(ExternalProvider, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.authentication_url = authentication_url
        self.password = password
        self.properties = properties
        self.requires_authentication = requires_authentication
        self.url = url
        self.username = username

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def requires_authentication(self):
        """
        Returns the value of the `requires_authentication` property.
        """
        return self._requires_authentication

    @requires_authentication.setter
    def requires_authentication(self, value):
        """
        Sets the value of the `requires_authentication` property.
        """
        self._requires_authentication = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def authentication_url(self):
        """
        Returns the value of the `authentication_url` property.
        """
        return self._authentication_url

    @authentication_url.setter
    def authentication_url(self, value):
        """
        Sets the value of the `authentication_url` property.
        """
        self._authentication_url = value

    @property
    def url(self):
        """
        Returns the value of the `url` property.
        """
        return self._url

    @url.setter
    def url(self, value):
        """
        Sets the value of the `url` property.
        """
        self._url = value

    @property
    def properties(self):
        """
        Returns the value of the `properties` property.
        """
        return self._properties

    @properties.setter
    def properties(self, value):
        """
        Sets the value of the `properties` property.
        """
        self._properties = value


class File(Identified):

    def __init__(
        self,
        comment=None,
        content=None,
        description=None,
        id=None,
        name=None,
        storage_domain=None,
        type=None,
    ):
        super(File, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.content = content
        self.storage_domain = storage_domain
        self.type = type

    @property
    def storage_domain(self):
        """
        Returns the value of the `storage_domain` property.
        """
        return self._storage_domain

    @storage_domain.setter
    def storage_domain(self, value):
        """
        Sets the value of the `storage_domain` property.
        """
        Struct._check_type('storage_domain', value, StorageDomain)
        self._storage_domain = value

    @property
    def content(self):
        """
        Returns the value of the `content` property.
        """
        return self._content

    @content.setter
    def content(self, value):
        """
        Sets the value of the `content` property.
        """
        self._content = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value


class Filter(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        id=None,
        name=None,
        position=None,
        scheduling_policy_unit=None,
    ):
        super(Filter, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.position = position
        self.scheduling_policy_unit = scheduling_policy_unit

    @property
    def scheduling_policy_unit(self):
        """
        Returns the value of the `scheduling_policy_unit` property.
        """
        return self._scheduling_policy_unit

    @scheduling_policy_unit.setter
    def scheduling_policy_unit(self, value):
        """
        Sets the value of the `scheduling_policy_unit` property.
        """
        Struct._check_type('scheduling_policy_unit', value, SchedulingPolicyUnit)
        self._scheduling_policy_unit = value

    @property
    def position(self):
        """
        Returns the value of the `position` property.
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Sets the value of the `position` property.
        """
        self._position = value


class Floppy(Device):

    def __init__(
        self,
        comment=None,
        description=None,
        file=None,
        id=None,
        instance_type=None,
        name=None,
        template=None,
        vm=None,
        vms=None,
    ):
        super(Floppy, self).__init__(
            comment=comment,
            description=description,
            id=id,
            instance_type=instance_type,
            name=name,
            template=template,
            vm=vm,
            vms=vms,
        )
        self.file = file

    @property
    def file(self):
        """
        Returns the value of the `file` property.
        """
        return self._file

    @file.setter
    def file(self, value):
        """
        Sets the value of the `file` property.
        """
        Struct._check_type('file', value, File)
        self._file = value


class GlusterBrickAdvancedDetails(Device):

    def __init__(
        self,
        comment=None,
        description=None,
        device=None,
        fs_name=None,
        gluster_clients=None,
        id=None,
        instance_type=None,
        memory_pools=None,
        mnt_options=None,
        name=None,
        pid=None,
        port=None,
        template=None,
        vm=None,
        vms=None,
    ):
        super(GlusterBrickAdvancedDetails, self).__init__(
            comment=comment,
            description=description,
            id=id,
            instance_type=instance_type,
            name=name,
            template=template,
            vm=vm,
            vms=vms,
        )
        self.device = device
        self.fs_name = fs_name
        self.gluster_clients = gluster_clients
        self.memory_pools = memory_pools
        self.mnt_options = mnt_options
        self.pid = pid
        self.port = port

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def memory_pools(self):
        """
        Returns the value of the `memory_pools` property.
        """
        return self._memory_pools

    @memory_pools.setter
    def memory_pools(self, value):
        """
        Sets the value of the `memory_pools` property.
        """
        self._memory_pools = value

    @property
    def mnt_options(self):
        """
        Returns the value of the `mnt_options` property.
        """
        return self._mnt_options

    @mnt_options.setter
    def mnt_options(self, value):
        """
        Sets the value of the `mnt_options` property.
        """
        self._mnt_options = value

    @property
    def fs_name(self):
        """
        Returns the value of the `fs_name` property.
        """
        return self._fs_name

    @fs_name.setter
    def fs_name(self, value):
        """
        Sets the value of the `fs_name` property.
        """
        self._fs_name = value

    @property
    def pid(self):
        """
        Returns the value of the `pid` property.
        """
        return self._pid

    @pid.setter
    def pid(self, value):
        """
        Sets the value of the `pid` property.
        """
        self._pid = value

    @property
    def gluster_clients(self):
        """
        Returns the value of the `gluster_clients` property.
        """
        return self._gluster_clients

    @gluster_clients.setter
    def gluster_clients(self, value):
        """
        Sets the value of the `gluster_clients` property.
        """
        self._gluster_clients = value

    @property
    def device(self):
        """
        Returns the value of the `device` property.
        """
        return self._device

    @device.setter
    def device(self, value):
        """
        Sets the value of the `device` property.
        """
        self._device = value


class GlusterHook(Identified):

    def __init__(
        self,
        checksum=None,
        cluster=None,
        comment=None,
        conflict_status=None,
        conflicts=None,
        content=None,
        content_type=None,
        description=None,
        gluster_command=None,
        id=None,
        name=None,
        server_hooks=None,
        stage=None,
        status=None,
    ):
        super(GlusterHook, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.checksum = checksum
        self.cluster = cluster
        self.conflict_status = conflict_status
        self.conflicts = conflicts
        self.content = content
        self.content_type = content_type
        self.gluster_command = gluster_command
        self.server_hooks = server_hooks
        self.stage = stage
        self.status = status

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def stage(self):
        """
        Returns the value of the `stage` property.
        """
        return self._stage

    @stage.setter
    def stage(self, value):
        """
        Sets the value of the `stage` property.
        """
        Struct._check_type('stage', value, HookStage)
        self._stage = value

    @property
    def content_type(self):
        """
        Returns the value of the `content_type` property.
        """
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """
        Sets the value of the `content_type` property.
        """
        Struct._check_type('content_type', value, HookContentType)
        self._content_type = value

    @property
    def conflict_status(self):
        """
        Returns the value of the `conflict_status` property.
        """
        return self._conflict_status

    @conflict_status.setter
    def conflict_status(self, value):
        """
        Sets the value of the `conflict_status` property.
        """
        self._conflict_status = value

    @property
    def conflicts(self):
        """
        Returns the value of the `conflicts` property.
        """
        return self._conflicts

    @conflicts.setter
    def conflicts(self, value):
        """
        Sets the value of the `conflicts` property.
        """
        self._conflicts = value

    @property
    def checksum(self):
        """
        Returns the value of the `checksum` property.
        """
        return self._checksum

    @checksum.setter
    def checksum(self, value):
        """
        Sets the value of the `checksum` property.
        """
        self._checksum = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, GlusterHookStatus)
        self._status = value

    @property
    def gluster_command(self):
        """
        Returns the value of the `gluster_command` property.
        """
        return self._gluster_command

    @gluster_command.setter
    def gluster_command(self, value):
        """
        Sets the value of the `gluster_command` property.
        """
        self._gluster_command = value

    @property
    def content(self):
        """
        Returns the value of the `content` property.
        """
        return self._content

    @content.setter
    def content(self, value):
        """
        Sets the value of the `content` property.
        """
        self._content = value

    @property
    def server_hooks(self):
        """
        Returns the value of the `server_hooks` property.
        """
        return self._server_hooks

    @server_hooks.setter
    def server_hooks(self, value):
        """
        Sets the value of the `server_hooks` property.
        """
        self._server_hooks = value


class GlusterMemoryPool(Identified):

    def __init__(
        self,
        alloc_count=None,
        cold_count=None,
        comment=None,
        description=None,
        hot_count=None,
        id=None,
        max_alloc=None,
        max_stdalloc=None,
        name=None,
        padded_size=None,
        pool_misses=None,
        type=None,
    ):
        super(GlusterMemoryPool, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.alloc_count = alloc_count
        self.cold_count = cold_count
        self.hot_count = hot_count
        self.max_alloc = max_alloc
        self.max_stdalloc = max_stdalloc
        self.padded_size = padded_size
        self.pool_misses = pool_misses
        self.type = type

    @property
    def cold_count(self):
        """
        Returns the value of the `cold_count` property.
        """
        return self._cold_count

    @cold_count.setter
    def cold_count(self, value):
        """
        Sets the value of the `cold_count` property.
        """
        self._cold_count = value

    @property
    def pool_misses(self):
        """
        Returns the value of the `pool_misses` property.
        """
        return self._pool_misses

    @pool_misses.setter
    def pool_misses(self, value):
        """
        Sets the value of the `pool_misses` property.
        """
        self._pool_misses = value

    @property
    def padded_size(self):
        """
        Returns the value of the `padded_size` property.
        """
        return self._padded_size

    @padded_size.setter
    def padded_size(self, value):
        """
        Sets the value of the `padded_size` property.
        """
        self._padded_size = value

    @property
    def max_stdalloc(self):
        """
        Returns the value of the `max_stdalloc` property.
        """
        return self._max_stdalloc

    @max_stdalloc.setter
    def max_stdalloc(self, value):
        """
        Sets the value of the `max_stdalloc` property.
        """
        self._max_stdalloc = value

    @property
    def alloc_count(self):
        """
        Returns the value of the `alloc_count` property.
        """
        return self._alloc_count

    @alloc_count.setter
    def alloc_count(self, value):
        """
        Sets the value of the `alloc_count` property.
        """
        self._alloc_count = value

    @property
    def hot_count(self):
        """
        Returns the value of the `hot_count` property.
        """
        return self._hot_count

    @hot_count.setter
    def hot_count(self, value):
        """
        Sets the value of the `hot_count` property.
        """
        self._hot_count = value

    @property
    def max_alloc(self):
        """
        Returns the value of the `max_alloc` property.
        """
        return self._max_alloc

    @max_alloc.setter
    def max_alloc(self, value):
        """
        Sets the value of the `max_alloc` property.
        """
        self._max_alloc = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        self._type = value


class GlusterServerHook(Identified):

    def __init__(
        self,
        checksum=None,
        comment=None,
        content_type=None,
        description=None,
        host=None,
        id=None,
        name=None,
        status=None,
    ):
        super(GlusterServerHook, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.checksum = checksum
        self.content_type = content_type
        self.host = host
        self.status = status

    @property
    def content_type(self):
        """
        Returns the value of the `content_type` property.
        """
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """
        Sets the value of the `content_type` property.
        """
        Struct._check_type('content_type', value, HookContentType)
        self._content_type = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def checksum(self):
        """
        Returns the value of the `checksum` property.
        """
        return self._checksum

    @checksum.setter
    def checksum(self, value):
        """
        Sets the value of the `checksum` property.
        """
        self._checksum = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, GlusterHookStatus)
        self._status = value


class GlusterVolume(Identified):

    def __init__(
        self,
        bricks=None,
        cluster=None,
        comment=None,
        description=None,
        disperse_count=None,
        id=None,
        name=None,
        options=None,
        redundancy_count=None,
        replica_count=None,
        statistics=None,
        status=None,
        stripe_count=None,
        transport_types=None,
        volume_type=None,
    ):
        super(GlusterVolume, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.bricks = bricks
        self.cluster = cluster
        self.disperse_count = disperse_count
        self.options = options
        self.redundancy_count = redundancy_count
        self.replica_count = replica_count
        self.statistics = statistics
        self.status = status
        self.stripe_count = stripe_count
        self.transport_types = transport_types
        self.volume_type = volume_type

    @property
    def disperse_count(self):
        """
        Returns the value of the `disperse_count` property.
        """
        return self._disperse_count

    @disperse_count.setter
    def disperse_count(self, value):
        """
        Sets the value of the `disperse_count` property.
        """
        self._disperse_count = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def bricks(self):
        """
        Returns the value of the `bricks` property.
        """
        return self._bricks

    @bricks.setter
    def bricks(self, value):
        """
        Sets the value of the `bricks` property.
        """
        self._bricks = value

    @property
    def transport_types(self):
        """
        Returns the value of the `transport_types` property.
        """
        return self._transport_types

    @transport_types.setter
    def transport_types(self, value):
        """
        Sets the value of the `transport_types` property.
        """
        self._transport_types = value

    @property
    def volume_type(self):
        """
        Returns the value of the `volume_type` property.
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, value):
        """
        Sets the value of the `volume_type` property.
        """
        Struct._check_type('volume_type', value, GlusterVolumeType)
        self._volume_type = value

    @property
    def redundancy_count(self):
        """
        Returns the value of the `redundancy_count` property.
        """
        return self._redundancy_count

    @redundancy_count.setter
    def redundancy_count(self, value):
        """
        Sets the value of the `redundancy_count` property.
        """
        self._redundancy_count = value

    @property
    def options(self):
        """
        Returns the value of the `options` property.
        """
        return self._options

    @options.setter
    def options(self, value):
        """
        Sets the value of the `options` property.
        """
        self._options = value

    @property
    def replica_count(self):
        """
        Returns the value of the `replica_count` property.
        """
        return self._replica_count

    @replica_count.setter
    def replica_count(self, value):
        """
        Sets the value of the `replica_count` property.
        """
        self._replica_count = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, GlusterVolumeStatus)
        self._status = value

    @property
    def stripe_count(self):
        """
        Returns the value of the `stripe_count` property.
        """
        return self._stripe_count

    @stripe_count.setter
    def stripe_count(self, value):
        """
        Sets the value of the `stripe_count` property.
        """
        self._stripe_count = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value


class GlusterVolumeProfileDetails(Identified):

    def __init__(
        self,
        brick_profile_details=None,
        comment=None,
        description=None,
        id=None,
        name=None,
        nfs_profile_details=None,
    ):
        super(GlusterVolumeProfileDetails, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.brick_profile_details = brick_profile_details
        self.nfs_profile_details = nfs_profile_details

    @property
    def brick_profile_details(self):
        """
        Returns the value of the `brick_profile_details` property.
        """
        return self._brick_profile_details

    @brick_profile_details.setter
    def brick_profile_details(self, value):
        """
        Sets the value of the `brick_profile_details` property.
        """
        self._brick_profile_details = value

    @property
    def nfs_profile_details(self):
        """
        Returns the value of the `nfs_profile_details` property.
        """
        return self._nfs_profile_details

    @nfs_profile_details.setter
    def nfs_profile_details(self, value):
        """
        Sets the value of the `nfs_profile_details` property.
        """
        self._nfs_profile_details = value


class GraphicsConsole(Identified):

    def __init__(
        self,
        address=None,
        comment=None,
        description=None,
        id=None,
        instance_type=None,
        name=None,
        port=None,
        protocol=None,
        template=None,
        tls_port=None,
        vm=None,
    ):
        super(GraphicsConsole, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.address = address
        self.instance_type = instance_type
        self.port = port
        self.protocol = protocol
        self.template = template
        self.tls_port = tls_port
        self.vm = vm

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def instance_type(self):
        """
        Returns the value of the `instance_type` property.
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, value):
        """
        Sets the value of the `instance_type` property.
        """
        Struct._check_type('instance_type', value, InstanceType)
        self._instance_type = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def protocol(self):
        """
        Returns the value of the `protocol` property.
        """
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        """
        Sets the value of the `protocol` property.
        """
        Struct._check_type('protocol', value, GraphicsType)
        self._protocol = value

    @property
    def tls_port(self):
        """
        Returns the value of the `tls_port` property.
        """
        return self._tls_port

    @tls_port.setter
    def tls_port(self, value):
        """
        Sets the value of the `tls_port` property.
        """
        self._tls_port = value


class Group(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        domain=None,
        domain_entry_id=None,
        id=None,
        name=None,
        namespace=None,
        permissions=None,
        roles=None,
        tags=None,
    ):
        super(Group, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.domain = domain
        self.domain_entry_id = domain_entry_id
        self.namespace = namespace
        self.permissions = permissions
        self.roles = roles
        self.tags = tags

    @property
    def domain(self):
        """
        Returns the value of the `domain` property.
        """
        return self._domain

    @domain.setter
    def domain(self, value):
        """
        Sets the value of the `domain` property.
        """
        Struct._check_type('domain', value, Domain)
        self._domain = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def roles(self):
        """
        Returns the value of the `roles` property.
        """
        return self._roles

    @roles.setter
    def roles(self, value):
        """
        Sets the value of the `roles` property.
        """
        self._roles = value

    @property
    def namespace(self):
        """
        Returns the value of the `namespace` property.
        """
        return self._namespace

    @namespace.setter
    def namespace(self, value):
        """
        Sets the value of the `namespace` property.
        """
        self._namespace = value

    @property
    def domain_entry_id(self):
        """
        Returns the value of the `domain_entry_id` property.
        """
        return self._domain_entry_id

    @domain_entry_id.setter
    def domain_entry_id(self, value):
        """
        Sets the value of the `domain_entry_id` property.
        """
        self._domain_entry_id = value

    @property
    def tags(self):
        """
        Returns the value of the `tags` property.
        """
        return self._tags

    @tags.setter
    def tags(self, value):
        """
        Sets the value of the `tags` property.
        """
        self._tags = value


class Hook(Identified):

    def __init__(
        self,
        comment=None,
        description=None,
        event_name=None,
        host=None,
        id=None,
        md5=None,
        name=None,
    ):
        super(Hook, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.event_name = event_name
        self.host = host
        self.md5 = md5

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def event_name(self):
        """
        Returns the value of the `event_name` property.
        """
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        """
        Sets the value of the `event_name` property.
        """
        self._event_name = value

    @property
    def md5(self):
        """
        Returns the value of the `md5` property.
        """
        return self._md5

    @md5.setter
    def md5(self, value):
        """
        Sets the value of the `md5` property.
        """
        self._md5 = value


class Host(Identified):

    def __init__(
        self,
        address=None,
        affinity_labels=None,
        agents=None,
        auto_numa_status=None,
        certificate=None,
        cluster=None,
        comment=None,
        cpu=None,
        description=None,
        device_passthrough=None,
        devices=None,
        display=None,
        external_host_provider=None,
        external_network_provider_configurations=None,
        external_status=None,
        hardware_information=None,
        hooks=None,
        hosted_engine=None,
        id=None,
        iscsi=None,
        katello_errata=None,
        kdump_status=None,
        ksm=None,
        libvirt_version=None,
        max_scheduling_memory=None,
        memory=None,
        name=None,
        network_attachments=None,
        network_operation_in_progress=None,
        nics=None,
        numa_nodes=None,
        numa_supported=None,
        os=None,
        override_iptables=None,
        ovn_configured=None,
        permissions=None,
        port=None,
        power_management=None,
        protocol=None,
        reinstallation_required=None,
        root_password=None,
        se_linux=None,
        spm=None,
        ssh=None,
        statistics=None,
        status=None,
        status_detail=None,
        storage_connection_extensions=None,
        storages=None,
        summary=None,
        tags=None,
        transparent_huge_pages=None,
        type=None,
        unmanaged_networks=None,
        update_available=None,
        version=None,
        vgpu_placement=None,
    ):
        super(Host, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.address = address
        self.affinity_labels = affinity_labels
        self.agents = agents
        self.auto_numa_status = auto_numa_status
        self.certificate = certificate
        self.cluster = cluster
        self.cpu = cpu
        self.device_passthrough = device_passthrough
        self.devices = devices
        self.display = display
        self.external_host_provider = external_host_provider
        self.external_network_provider_configurations = external_network_provider_configurations
        self.external_status = external_status
        self.hardware_information = hardware_information
        self.hooks = hooks
        self.hosted_engine = hosted_engine
        self.iscsi = iscsi
        self.katello_errata = katello_errata
        self.kdump_status = kdump_status
        self.ksm = ksm
        self.libvirt_version = libvirt_version
        self.max_scheduling_memory = max_scheduling_memory
        self.memory = memory
        self.network_attachments = network_attachments
        self.network_operation_in_progress = network_operation_in_progress
        self.nics = nics
        self.numa_nodes = numa_nodes
        self.numa_supported = numa_supported
        self.os = os
        self.override_iptables = override_iptables
        self.ovn_configured = ovn_configured
        self.permissions = permissions
        self.port = port
        self.power_management = power_management
        self.protocol = protocol
        self.reinstallation_required = reinstallation_required
        self.root_password = root_password
        self.se_linux = se_linux
        self.spm = spm
        self.ssh = ssh
        self.statistics = statistics
        self.status = status
        self.status_detail = status_detail
        self.storage_connection_extensions = storage_connection_extensions
        self.storages = storages
        self.summary = summary
        self.tags = tags
        self.transparent_huge_pages = transparent_huge_pages
        self.type = type
        self.unmanaged_networks = unmanaged_networks
        self.update_available = update_available
        self.version = version
        self.vgpu_placement = vgpu_placement

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, Version)
        self._version = value

    @property
    def summary(self):
        """
        Returns the value of the `summary` property.
        """
        return self._summary

    @summary.setter
    def summary(self, value):
        """
        Sets the value of the `summary` property.
        """
        Struct._check_type('summary', value, VmSummary)
        self._summary = value

    @property
    def os(self):
        """
        Returns the value of the `os` property.
        """
        return self._os

    @os.setter
    def os(self, value):
        """
        Sets the value of the `os` property.
        """
        Struct._check_type('os', value, OperatingSystem)
        self._os = value

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def devices(self):
        """
        Returns the value of the `devices` property.
        """
        return self._devices

    @devices.setter
    def devices(self, value):
        """
        Sets the value of the `devices` property.
        """
        self._devices = value

    @property
    def se_linux(self):
        """
        Returns the value of the `se_linux` property.
        """
        return self._se_linux

    @se_linux.setter
    def se_linux(self, value):
        """
        Sets the value of the `se_linux` property.
        """
        Struct._check_type('se_linux', value, SeLinux)
        self._se_linux = value

    @property
    def affinity_labels(self):
        """
        Returns the value of the `affinity_labels` property.
        """
        return self._affinity_labels

    @affinity_labels.setter
    def affinity_labels(self, value):
        """
        Sets the value of the `affinity_labels` property.
        """
        self._affinity_labels = value

    @property
    def hosted_engine(self):
        """
        Returns the value of the `hosted_engine` property.
        """
        return self._hosted_engine

    @hosted_engine.setter
    def hosted_engine(self, value):
        """
        Sets the value of the `hosted_engine` property.
        """
        Struct._check_type('hosted_engine', value, HostedEngine)
        self._hosted_engine = value

    @property
    def storage_connection_extensions(self):
        """
        Returns the value of the `storage_connection_extensions` property.
        """
        return self._storage_connection_extensions

    @storage_connection_extensions.setter
    def storage_connection_extensions(self, value):
        """
        Sets the value of the `storage_connection_extensions` property.
        """
        self._storage_connection_extensions = value

    @property
    def tags(self):
        """
        Returns the value of the `tags` property.
        """
        return self._tags

    @tags.setter
    def tags(self, value):
        """
        Sets the value of the `tags` property.
        """
        self._tags = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def reinstallation_required(self):
        """
        Returns the value of the `reinstallation_required` property.
        """
        return self._reinstallation_required

    @reinstallation_required.setter
    def reinstallation_required(self, value):
        """
        Sets the value of the `reinstallation_required` property.
        """
        self._reinstallation_required = value

    @property
    def override_iptables(self):
        """
        Returns the value of the `override_iptables` property.
        """
        return self._override_iptables

    @override_iptables.setter
    def override_iptables(self, value):
        """
        Sets the value of the `override_iptables` property.
        """
        self._override_iptables = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value

    @property
    def numa_supported(self):
        """
        Returns the value of the `numa_supported` property.
        """
        return self._numa_supported

    @numa_supported.setter
    def numa_supported(self, value):
        """
        Sets the value of the `numa_supported` property.
        """
        self._numa_supported = value

    @property
    def hooks(self):
        """
        Returns the value of the `hooks` property.
        """
        return self._hooks

    @hooks.setter
    def hooks(self, value):
        """
        Sets the value of the `hooks` property.
        """
        self._hooks = value

    @property
    def ksm(self):
        """
        Returns the value of the `ksm` property.
        """
        return self._ksm

    @ksm.setter
    def ksm(self, value):
        """
        Sets the value of the `ksm` property.
        """
        Struct._check_type('ksm', value, Ksm)
        self._ksm = value

    @property
    def ssh(self):
        """
        Returns the value of the `ssh` property.
        """
        return self._ssh

    @ssh.setter
    def ssh(self, value):
        """
        Sets the value of the `ssh` property.
        """
        Struct._check_type('ssh', value, Ssh)
        self._ssh = value

    @property
    def kdump_status(self):
        """
        Returns the value of the `kdump_status` property.
        """
        return self._kdump_status

    @kdump_status.setter
    def kdump_status(self, value):
        """
        Sets the value of the `kdump_status` property.
        """
        Struct._check_type('kdump_status', value, KdumpStatus)
        self._kdump_status = value

    @property
    def update_available(self):
        """
        Returns the value of the `update_available` property.
        """
        return self._update_available

    @update_available.setter
    def update_available(self, value):
        """
        Sets the value of the `update_available` property.
        """
        self._update_available = value

    @property
    def ovn_configured(self):
        """
        Returns the value of the `ovn_configured` property.
        """
        return self._ovn_configured

    @ovn_configured.setter
    def ovn_configured(self, value):
        """
        Sets the value of the `ovn_configured` property.
        """
        self._ovn_configured = value

    @property
    def external_network_provider_configurations(self):
        """
        Returns the value of the `external_network_provider_configurations` property.
        """
        return self._external_network_provider_configurations

    @external_network_provider_configurations.setter
    def external_network_provider_configurations(self, value):
        """
        Sets the value of the `external_network_provider_configurations` property.
        """
        self._external_network_provider_configurations = value

    @property
    def storages(self):
        """
        Returns the value of the `storages` property.
        """
        return self._storages

    @storages.setter
    def storages(self, value):
        """
        Sets the value of the `storages` property.
        """
        self._storages = value

    @property
    def numa_nodes(self):
        """
        Returns the value of the `numa_nodes` property.
        """
        return self._numa_nodes

    @numa_nodes.setter
    def numa_nodes(self, value):
        """
        Sets the value of the `numa_nodes` property.
        """
        self._numa_nodes = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def status_detail(self):
        """
        Returns the value of the `status_detail` property.
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, value):
        """
        Sets the value of the `status_detail` property.
        """
        self._status_detail = value

    @property
    def power_management(self):
        """
        Returns the value of the `power_management` property.
        """
        return self._power_management

    @power_management.setter
    def power_management(self, value):
        """
        Sets the value of the `power_management` property.
        """
        Struct._check_type('power_management', value, PowerManagement)
        self._power_management = value

    @property
    def nics(self):
        """
        Returns the value of the `nics` property.
        """
        return self._nics

    @nics.setter
    def nics(self, value):
        """
        Sets the value of the `nics` property.
        """
        self._nics = value

    @property
    def device_passthrough(self):
        """
        Returns the value of the `device_passthrough` property.
        """
        return self._device_passthrough

    @device_passthrough.setter
    def device_passthrough(self, value):
        """
        Sets the value of the `device_passthrough` property.
        """
        Struct._check_type('device_passthrough', value, HostDevicePassthrough)
        self._device_passthrough = value

    @property
    def unmanaged_networks(self):
        """
        Returns the value of the `unmanaged_networks` property.
        """
        return self._unmanaged_networks

    @unmanaged_networks.setter
    def unmanaged_networks(self, value):
        """
        Sets the value of the `unmanaged_networks` property.
        """
        self._unmanaged_networks = value

    @property
    def protocol(self):
        """
        Returns the value of the `protocol` property.
        """
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        """
        Sets the value of the `protocol` property.
        """
        Struct._check_type('protocol', value, HostProtocol)
        self._protocol = value

    @property
    def root_password(self):
        """
        Returns the value of the `root_password` property.
        """
        return self._root_password

    @root_password.setter
    def root_password(self, value):
        """
        Sets the value of the `root_password` property.
        """
        self._root_password = value

    @property
    def network_attachments(self):
        """
        Returns the value of the `network_attachments` property.
        """
        return self._network_attachments

    @network_attachments.setter
    def network_attachments(self, value):
        """
        Sets the value of the `network_attachments` property.
        """
        self._network_attachments = value

    @property
    def max_scheduling_memory(self):
        """
        Returns the value of the `max_scheduling_memory` property.
        """
        return self._max_scheduling_memory

    @max_scheduling_memory.setter
    def max_scheduling_memory(self, value):
        """
        Sets the value of the `max_scheduling_memory` property.
        """
        self._max_scheduling_memory = value

    @property
    def display(self):
        """
        Returns the value of the `display` property.
        """
        return self._display

    @display.setter
    def display(self, value):
        """
        Sets the value of the `display` property.
        """
        Struct._check_type('display', value, Display)
        self._display = value

    @property
    def auto_numa_status(self):
        """
        Returns the value of the `auto_numa_status` property.
        """
        return self._auto_numa_status

    @auto_numa_status.setter
    def auto_numa_status(self, value):
        """
        Sets the value of the `auto_numa_status` property.
        """
        Struct._check_type('auto_numa_status', value, AutoNumaStatus)
        self._auto_numa_status = value

    @property
    def cpu(self):
        """
        Returns the value of the `cpu` property.
        """
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        """
        Sets the value of the `cpu` property.
        """
        Struct._check_type('cpu', value, Cpu)
        self._cpu = value

    @property
    def external_status(self):
        """
        Returns the value of the `external_status` property.
        """
        return self._external_status

    @external_status.setter
    def external_status(self, value):
        """
        Sets the value of the `external_status` property.
        """
        Struct._check_type('external_status', value, ExternalStatus)
        self._external_status = value

    @property
    def agents(self):
        """
        Returns the value of the `agents` property.
        """
        return self._agents

    @agents.setter
    def agents(self, value):
        """
        Sets the value of the `agents` property.
        """
        self._agents = value

    @property
    def spm(self):
        """
        Returns the value of the `spm` property.
        """
        return self._spm

    @spm.setter
    def spm(self, value):
        """
        Sets the value of the `spm` property.
        """
        Struct._check_type('spm', value, Spm)
        self._spm = value

    @property
    def libvirt_version(self):
        """
        Returns the value of the `libvirt_version` property.
        """
        return self._libvirt_version

    @libvirt_version.setter
    def libvirt_version(self, value):
        """
        Sets the value of the `libvirt_version` property.
        """
        Struct._check_type('libvirt_version', value, Version)
        self._libvirt_version = value

    @property
    def iscsi(self):
        """
        Returns the value of the `iscsi` property.
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, value):
        """
        Sets the value of the `iscsi` property.
        """
        Struct._check_type('iscsi', value, IscsiDetails)
        self._iscsi = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, HostStatus)
        self._status = value

    @property
    def hardware_information(self):
        """
        Returns the value of the `hardware_information` property.
        """
        return self._hardware_information

    @hardware_information.setter
    def hardware_information(self, value):
        """
        Sets the value of the `hardware_information` property.
        """
        Struct._check_type('hardware_information', value, HardwareInformation)
        self._hardware_information = value

    @property
    def katello_errata(self):
        """
        Returns the value of the `katello_errata` property.
        """
        return self._katello_errata

    @katello_errata.setter
    def katello_errata(self, value):
        """
        Sets the value of the `katello_errata` property.
        """
        self._katello_errata = value

    @property
    def memory(self):
        """
        Returns the value of the `memory` property.
        """
        return self._memory

    @memory.setter
    def memory(self, value):
        """
        Sets the value of the `memory` property.
        """
        self._memory = value

    @property
    def cluster(self):
        """
        Returns the value of the `cluster` property.
        """
        return self._cluster

    @cluster.setter
    def cluster(self, value):
        """
        Sets the value of the `cluster` property.
        """
        Struct._check_type('cluster', value, Cluster)
        self._cluster = value

    @property
    def transparent_huge_pages(self):
        """
        Returns the value of the `transparent_huge_pages` property.
        """
        return self._transparent_huge_pages

    @transparent_huge_pages.setter
    def transparent_huge_pages(self, value):
        """
        Sets the value of the `transparent_huge_pages` property.
        """
        Struct._check_type('transparent_huge_pages', value, TransparentHugePages)
        self._transparent_huge_pages = value

    @property
    def certificate(self):
        """
        Returns the value of the `certificate` property.
        """
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        """
        Sets the value of the `certificate` property.
        """
        Struct._check_type('certificate', value, Certificate)
        self._certificate = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, HostType)
        self._type = value

    @property
    def external_host_provider(self):
        """
        Returns the value of the `external_host_provider` property.
        """
        return self._external_host_provider

    @external_host_provider.setter
    def external_host_provider(self, value):
        """
        Sets the value of the `external_host_provider` property.
        """
        Struct._check_type('external_host_provider', value, ExternalHostProvider)
        self._external_host_provider = value

    @property
    def vgpu_placement(self):
        """
        Returns the value of the `vgpu_placement` property.
        """
        return self._vgpu_placement

    @vgpu_placement.setter
    def vgpu_placement(self, value):
        """
        Sets the value of the `vgpu_placement` property.
        """
        Struct._check_type('vgpu_placement', value, VgpuPlacement)
        self._vgpu_placement = value

    @property
    def network_operation_in_progress(self):
        """
        Returns the value of the `network_operation_in_progress` property.
        """
        return self._network_operation_in_progress

    @network_operation_in_progress.setter
    def network_operation_in_progress(self, value):
        """
        Sets the value of the `network_operation_in_progress` property.
        """
        self._network_operation_in_progress = value


class HostDevice(Identified):

    def __init__(
        self,
        capability=None,
        comment=None,
        description=None,
        driver=None,
        host=None,
        id=None,
        iommu_group=None,
        m_dev_types=None,
        name=None,
        parent_device=None,
        physical_function=None,
        placeholder=None,
        product=None,
        vendor=None,
        virtual_functions=None,
        vm=None,
    ):
        super(HostDevice, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.capability = capability
        self.driver = driver
        self.host = host
        self.iommu_group = iommu_group
        self.m_dev_types = m_dev_types
        self.parent_device = parent_device
        self.physical_function = physical_function
        self.placeholder = placeholder
        self.product = product
        self.vendor = vendor
        self.virtual_functions = virtual_functions
        self.vm = vm

    @property
    def product(self):
        """
        Returns the value of the `product` property.
        """
        return self._product

    @product.setter
    def product(self, value):
        """
        Sets the value of the `product` property.
        """
        Struct._check_type('product', value, Product)
        self._product = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def virtual_functions(self):
        """
        Returns the value of the `virtual_functions` property.
        """
        return self._virtual_functions

    @virtual_functions.setter
    def virtual_functions(self, value):
        """
        Sets the value of the `virtual_functions` property.
        """
        self._virtual_functions = value

    @property
    def vendor(self):
        """
        Returns the value of the `vendor` property.
        """
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        """
        Sets the value of the `vendor` property.
        """
        Struct._check_type('vendor', value, Vendor)
        self._vendor = value

    @property
    def placeholder(self):
        """
        Returns the value of the `placeholder` property.
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, value):
        """
        Sets the value of the `placeholder` property.
        """
        self._placeholder = value

    @property
    def driver(self):
        """
        Returns the value of the `driver` property.
        """
        return self._driver

    @driver.setter
    def driver(self, value):
        """
        Sets the value of the `driver` property.
        """
        self._driver = value

    @property
    def iommu_group(self):
        """
        Returns the value of the `iommu_group` property.
        """
        return self._iommu_group

    @iommu_group.setter
    def iommu_group(self, value):
        """
        Sets the value of the `iommu_group` property.
        """
        self._iommu_group = value

    @property
    def m_dev_types(self):
        """
        Returns the value of the `m_dev_types` property.
        """
        return self._m_dev_types

    @m_dev_types.setter
    def m_dev_types(self, value):
        """
        Sets the value of the `m_dev_types` property.
        """
        self._m_dev_types = value

    @property
    def parent_device(self):
        """
        Returns the value of the `parent_device` property.
        """
        return self._parent_device

    @parent_device.setter
    def parent_device(self, value):
        """
        Sets the value of the `parent_device` property.
        """
        Struct._check_type('parent_device', value, HostDevice)
        self._parent_device = value

    @property
    def capability(self):
        """
        Returns the value of the `capability` property.
        """
        return self._capability

    @capability.setter
    def capability(self, value):
        """
        Sets the value of the `capability` property.
        """
        self._capability = value

    @property
    def physical_function(self):
        """
        Returns the value of the `physical_function` property.
        """
        return self._physical_function

    @physical_function.setter
    def physical_function(self, value):
        """
        Sets the value of the `physical_function` property.
        """
        Struct._check_type('physical_function', value, HostDevice)
        self._physical_function = value


class HostNic(Identified):

    def __init__(
        self,
        ad_aggregator_id=None,
        base_interface=None,
        bonding=None,
        boot_protocol=None,
        bridged=None,
        check_connectivity=None,
        comment=None,
        custom_configuration=None,
        description=None,
        host=None,
        id=None,
        ip=None,
        ipv6=None,
        ipv6_boot_protocol=None,
        mac=None,
        mtu=None,
        name=None,
        network=None,
        network_labels=None,
        override_configuration=None,
        physical_function=None,
        properties=None,
        qos=None,
        speed=None,
        statistics=None,
        status=None,
        virtual_functions_configuration=None,
        vlan=None,
    ):
        super(HostNic, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.ad_aggregator_id = ad_aggregator_id
        self.base_interface = base_interface
        self.bonding = bonding
        self.boot_protocol = boot_protocol
        self.bridged = bridged
        self.check_connectivity = check_connectivity
        self.custom_configuration = custom_configuration
        self.host = host
        self.ip = ip
        self.ipv6 = ipv6
        self.ipv6_boot_protocol = ipv6_boot_protocol
        self.mac = mac
        self.mtu = mtu
        self.network = network
        self.network_labels = network_labels
        self.override_configuration = override_configuration
        self.physical_function = physical_function
        self.properties = properties
        self.qos = qos
        self.speed = speed
        self.statistics = statistics
        self.status = status
        self.virtual_functions_configuration = virtual_functions_configuration
        self.vlan = vlan

    @property
    def base_interface(self):
        """
        Returns the value of the `base_interface` property.
        """
        return self._base_interface

    @base_interface.setter
    def base_interface(self, value):
        """
        Sets the value of the `base_interface` property.
        """
        self._base_interface = value

    @property
    def ad_aggregator_id(self):
        """
        Returns the value of the `ad_aggregator_id` property.
        """
        return self._ad_aggregator_id

    @ad_aggregator_id.setter
    def ad_aggregator_id(self, value):
        """
        Sets the value of the `ad_aggregator_id` property.
        """
        self._ad_aggregator_id = value

    @property
    def boot_protocol(self):
        """
        Returns the value of the `boot_protocol` property.
        """
        return self._boot_protocol

    @boot_protocol.setter
    def boot_protocol(self, value):
        """
        Sets the value of the `boot_protocol` property.
        """
        Struct._check_type('boot_protocol', value, BootProtocol)
        self._boot_protocol = value

    @property
    def ip(self):
        """
        Returns the value of the `ip` property.
        """
        return self._ip

    @ip.setter
    def ip(self, value):
        """
        Sets the value of the `ip` property.
        """
        Struct._check_type('ip', value, Ip)
        self._ip = value

    @property
    def custom_configuration(self):
        """
        Returns the value of the `custom_configuration` property.
        """
        return self._custom_configuration

    @custom_configuration.setter
    def custom_configuration(self, value):
        """
        Sets the value of the `custom_configuration` property.
        """
        self._custom_configuration = value

    @property
    def network_labels(self):
        """
        Returns the value of the `network_labels` property.
        """
        return self._network_labels

    @network_labels.setter
    def network_labels(self, value):
        """
        Sets the value of the `network_labels` property.
        """
        self._network_labels = value

    @property
    def check_connectivity(self):
        """
        Returns the value of the `check_connectivity` property.
        """
        return self._check_connectivity

    @check_connectivity.setter
    def check_connectivity(self, value):
        """
        Sets the value of the `check_connectivity` property.
        """
        self._check_connectivity = value

    @property
    def mtu(self):
        """
        Returns the value of the `mtu` property.
        """
        return self._mtu

    @mtu.setter
    def mtu(self, value):
        """
        Sets the value of the `mtu` property.
        """
        self._mtu = value

    @property
    def network(self):
        """
        Returns the value of the `network` property.
        """
        return self._network

    @network.setter
    def network(self, value):
        """
        Sets the value of the `network` property.
        """
        Struct._check_type('network', value, Network)
        self._network = value

    @property
    def mac(self):
        """
        Returns the value of the `mac` property.
        """
        return self._mac

    @mac.setter
    def mac(self, value):
        """
        Sets the value of the `mac` property.
        """
        Struct._check_type('mac', value, Mac)
        self._mac = value

    @property
    def speed(self):
        """
        Returns the value of the `speed` property.
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        """
        Sets the value of the `speed` property.
        """
        self._speed = value

    @property
    def override_configuration(self):
        """
        Returns the value of the `override_configuration` property.
        """
        return self._override_configuration

    @override_configuration.setter
    def override_configuration(self, value):
        """
        Sets the value of the `override_configuration` property.
        """
        self._override_configuration = value

    @property
    def vlan(self):
        """
        Returns the value of the `vlan` property.
        """
        return self._vlan

    @vlan.setter
    def vlan(self, value):
        """
        Sets the value of the `vlan` property.
        """
        Struct._check_type('vlan', value, Vlan)
        self._vlan = value

    @property
    def qos(self):
        """
        Returns the value of the `qos` property.
        """
        return self._qos

    @qos.setter
    def qos(self, value):
        """
        Sets the value of the `qos` property.
        """
        Struct._check_type('qos', value, Qos)
        self._qos = value

    @property
    def virtual_functions_configuration(self):
        """
        Returns the value of the `virtual_functions_configuration` property.
        """
        return self._virtual_functions_configuration

    @virtual_functions_configuration.setter
    def virtual_functions_configuration(self, value):
        """
        Sets the value of the `virtual_functions_configuration` property.
        """
        Struct._check_type('virtual_functions_configuration', value, HostNicVirtualFunctionsConfiguration)
        self._virtual_functions_configuration = value

    @property
    def ipv6(self):
        """
        Returns the value of the `ipv6` property.
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, value):
        """
        Sets the value of the `ipv6` property.
        """
        Struct._check_type('ipv6', value, Ip)
        self._ipv6 = value

    @property
    def bonding(self):
        """
        Returns the value of the `bonding` property.
        """
        return self._bonding

    @bonding.setter
    def bonding(self, value):
        """
        Sets the value of the `bonding` property.
        """
        Struct._check_type('bonding', value, Bonding)
        self._bonding = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def bridged(self):
        """
        Returns the value of the `bridged` property.
        """
        return self._bridged

    @bridged.setter
    def bridged(self, value):
        """
        Sets the value of the `bridged` property.
        """
        self._bridged = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, NicStatus)
        self._status = value

    @property
    def ipv6_boot_protocol(self):
        """
        Returns the value of the `ipv6_boot_protocol` property.
        """
        return self._ipv6_boot_protocol

    @ipv6_boot_protocol.setter
    def ipv6_boot_protocol(self, value):
        """
        Sets the value of the `ipv6_boot_protocol` property.
        """
        Struct._check_type('ipv6_boot_protocol', value, BootProtocol)
        self._ipv6_boot_protocol = value

    @property
    def physical_function(self):
        """
        Returns the value of the `physical_function` property.
        """
        return self._physical_function

    @physical_function.setter
    def physical_function(self, value):
        """
        Sets the value of the `physical_function` property.
        """
        Struct._check_type('physical_function', value, HostNic)
        self._physical_function = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value

    @property
    def properties(self):
        """
        Returns the value of the `properties` property.
        """
        return self._properties

    @properties.setter
    def properties(self, value):
        """
        Sets the value of the `properties` property.
        """
        self._properties = value


class HostStorage(Identified):

    def __init__(
        self,
        address=None,
        comment=None,
        description=None,
        driver_options=None,
        driver_sensitive_options=None,
        host=None,
        id=None,
        logical_units=None,
        mount_options=None,
        name=None,
        nfs_retrans=None,
        nfs_timeo=None,
        nfs_version=None,
        override_luns=None,
        password=None,
        path=None,
        port=None,
        portal=None,
        target=None,
        type=None,
        username=None,
        vfs_type=None,
        volume_group=None,
    ):
        super(HostStorage, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.address = address
        self.driver_options = driver_options
        self.driver_sensitive_options = driver_sensitive_options
        self.host = host
        self.logical_units = logical_units
        self.mount_options = mount_options
        self.nfs_retrans = nfs_retrans
        self.nfs_timeo = nfs_timeo
        self.nfs_version = nfs_version
        self.override_luns = override_luns
        self.password = password
        self.path = path
        self.port = port
        self.portal = portal
        self.target = target
        self.type = type
        self.username = username
        self.vfs_type = vfs_type
        self.volume_group = volume_group

    @property
    def address(self):
        """
        Returns the value of the `address` property.
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the `address` property.
        """
        self._address = value

    @property
    def driver_sensitive_options(self):
        """
        Returns the value of the `driver_sensitive_options` property.
        """
        return self._driver_sensitive_options

    @driver_sensitive_options.setter
    def driver_sensitive_options(self, value):
        """
        Sets the value of the `driver_sensitive_options` property.
        """
        self._driver_sensitive_options = value

    @property
    def driver_options(self):
        """
        Returns the value of the `driver_options` property.
        """
        return self._driver_options

    @driver_options.setter
    def driver_options(self, value):
        """
        Sets the value of the `driver_options` property.
        """
        self._driver_options = value

    @property
    def target(self):
        """
        Returns the value of the `target` property.
        """
        return self._target

    @target.setter
    def target(self, value):
        """
        Sets the value of the `target` property.
        """
        self._target = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, StorageType)
        self._type = value

    @property
    def nfs_timeo(self):
        """
        Returns the value of the `nfs_timeo` property.
        """
        return self._nfs_timeo

    @nfs_timeo.setter
    def nfs_timeo(self, value):
        """
        Sets the value of the `nfs_timeo` property.
        """
        self._nfs_timeo = value

    @property
    def path(self):
        """
        Returns the value of the `path` property.
        """
        return self._path

    @path.setter
    def path(self, value):
        """
        Sets the value of the `path` property.
        """
        self._path = value

    @property
    def nfs_retrans(self):
        """
        Returns the value of the `nfs_retrans` property.
        """
        return self._nfs_retrans

    @nfs_retrans.setter
    def nfs_retrans(self, value):
        """
        Sets the value of the `nfs_retrans` property.
        """
        self._nfs_retrans = value

    @property
    def password(self):
        """
        Returns the value of the `password` property.
        """
        return self._password

    @password.setter
    def password(self, value):
        """
        Sets the value of the `password` property.
        """
        self._password = value

    @property
    def port(self):
        """
        Returns the value of the `port` property.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Sets the value of the `port` property.
        """
        self._port = value

    @property
    def volume_group(self):
        """
        Returns the value of the `volume_group` property.
        """
        return self._volume_group

    @volume_group.setter
    def volume_group(self, value):
        """
        Sets the value of the `volume_group` property.
        """
        Struct._check_type('volume_group', value, VolumeGroup)
        self._volume_group = value

    @property
    def vfs_type(self):
        """
        Returns the value of the `vfs_type` property.
        """
        return self._vfs_type

    @vfs_type.setter
    def vfs_type(self, value):
        """
        Sets the value of the `vfs_type` property.
        """
        self._vfs_type = value

    @property
    def nfs_version(self):
        """
        Returns the value of the `nfs_version` property.
        """
        return self._nfs_version

    @nfs_version.setter
    def nfs_version(self, value):
        """
        Sets the value of the `nfs_version` property.
        """
        Struct._check_type('nfs_version', value, NfsVersion)
        self._nfs_version = value

    @property
    def logical_units(self):
        """
        Returns the value of the `logical_units` property.
        """
        return self._logical_units

    @logical_units.setter
    def logical_units(self, value):
        """
        Sets the value of the `logical_units` property.
        """
        self._logical_units = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def portal(self):
        """
        Returns the value of the `portal` property.
        """
        return self._portal

    @portal.setter
    def portal(self, value):
        """
        Sets the value of the `portal` property.
        """
        self._portal = value

    @property
    def username(self):
        """
        Returns the value of the `username` property.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the value of the `username` property.
        """
        self._username = value

    @property
    def override_luns(self):
        """
        Returns the value of the `override_luns` property.
        """
        return self._override_luns

    @override_luns.setter
    def override_luns(self, value):
        """
        Sets the value of the `override_luns` property.
        """
        self._override_luns = value

    @property
    def mount_options(self):
        """
        Returns the value of the `mount_options` property.
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, value):
        """
        Sets the value of the `mount_options` property.
        """
        self._mount_options = value


class Icon(Identified):

    def __init__(
        self,
        comment=None,
        data=None,
        description=None,
        id=None,
        media_type=None,
        name=None,
    ):
        super(Icon, self).__init__(
            comment=comment,
            description=description,
            id=id,
            name=name,
        )
        self.data = data
        self.media_type = media_type

    @property
    def media_type(self):
        """
        Returns the value of the `media_type` property.
        """
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        """
        Sets the value of the `media_type` property.
        """
        self._media_type = value

    @property
    def data(self):
        """
        Returns the value of the `data` property.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the value of the `data` property.
        """
        self._data = value


class Nic(Device):

    def __init__(
        self,
        boot_protocol=None,
        comment=None,
        description=None,
        id=None,
        instance_type=None,
        interface=None,
        linked=None,
        mac=None,
        name=None,
        network=None,
        network_attachments=None,
        network_filter_parameters=None,
        network_labels=None,
        on_boot=None,
        plugged=None,
        reported_devices=None,
        statistics=None,
        synced=None,
        template=None,
        virtual_function_allowed_labels=None,
        virtual_function_allowed_networks=None,
        vm=None,
        vms=None,
        vnic_profile=None,
    ):
        super(Nic, self).__init__(
            comment=comment,
            description=description,
            id=id,
            instance_type=instance_type,
            name=name,
            template=template,
            vm=vm,
            vms=vms,
        )
        self.boot_protocol = boot_protocol
        self.interface = interface
        self.linked = linked
        self.mac = mac
        self.network = network
        self.network_attachments = network_attachments
        self.network_filter_parameters = network_filter_parameters
        self.network_labels = network_labels
        self.on_boot = on_boot
        self.plugged = plugged
        self.reported_devices = reported_devices
        self.statistics = statistics
        self.synced = synced
        self.virtual_function_allowed_labels = virtual_function_allowed_labels
        self.virtual_function_allowed_networks = virtual_function_allowed_networks
        self.vnic_profile = vnic_profile

    @property
    def synced(self):
        """
        Returns the value of the `synced` property.
        """
        return self._synced

    @synced.setter
    def synced(self, value):
        """
        Sets the value of the `synced` property.
        """
        self._synced = value

    @property
    def reported_devices(self):
        """
        Returns the value of the `reported_devices` property.
        """
        return self._reported_devices

    @reported_devices.setter
    def reported_devices(self, value):
        """
        Sets the value of the `reported_devices` property.
        """
        self._reported_devices = value

    @property
    def virtual_function_allowed_labels(self):
        """
        Returns the value of the `virtual_function_allowed_labels` property.
        """
        return self._virtual_function_allowed_labels

    @virtual_function_allowed_labels.setter
    def virtual_function_allowed_labels(self, value):
        """
        Sets the value of the `virtual_function_allowed_labels` property.
        """
        self._virtual_function_allowed_labels = value

    @property
    def network_filter_parameters(self):
        """
        Returns the value of the `network_filter_parameters` property.
        """
        return self._network_filter_parameters

    @network_filter_parameters.setter
    def network_filter_parameters(self, value):
        """
        Sets the value of the `network_filter_parameters` property.
        """
        self._network_filter_parameters = value

    @property
    def boot_protocol(self):
        """
        Returns the value of the `boot_protocol` property.
        """
        return self._boot_protocol

    @boot_protocol.setter
    def boot_protocol(self, value):
        """
        Sets the value of the `boot_protocol` property.
        """
        Struct._check_type('boot_protocol', value, BootProtocol)
        self._boot_protocol = value

    @property
    def network_labels(self):
        """
        Returns the value of the `network_labels` property.
        """
        return self._network_labels

    @network_labels.setter
    def network_labels(self, value):
        """
        Sets the value of the `network_labels` property.
        """
        self._network_labels = value

    @property
    def network(self):
        """
        Returns the value of the `network` property.
        """
        return self._network

    @network.setter
    def network(self, value):
        """
        Sets the value of the `network` property.
        """
        Struct._check_type('network', value, Network)
        self._network = value

    @property
    def interface(self):
        """
        Returns the value of the `interface` property.
        """
        return self._interface

    @interface.setter
    def interface(self, value):
        """
        Sets the value of the `interface` property.
        """
        Struct._check_type('interface', value, NicInterface)
        self._interface = value

    @property
    def mac(self):
        """
        Returns the value of the `mac` property.
        """
        return self._mac

    @mac.setter
    def mac(self, value):
        """
        Sets the value of the `mac` property.
        """
        Struct._check_type('mac', value, Mac)
        self._mac = value

    @property
    def plugged(self):
        """
        Returns the value of the `plugged` property.
        """
        return self._plugged

    @plugged.setter
    def plugged(self, value):
        """
        Sets the value of the `plugged` property.
        """
        self._plugged = value

    @property
    def virtual_function_allowed_networks(self):
        """
        Returns the value of the `virtual_function_allowed_networks` property.
        """
        return self._virtual_function_allowed_networks

    @virtual_function_allowed_networks.setter
    def virtual_function_allowed_networks(self, value):
        """
        Sets the value of the `virtual_function_allowed_networks` property.
        """
        self._virtual_function_allowed_networks = value

    @property
    def vnic_profile(self):
        """
        Returns the value of the `vnic_profile` property.
        """
        return self._vnic_profile

    @vnic_profile.setter
    def vnic_profile(self, value):
        """
        Sets the value of the `vnic_profile` property.
        """
        Struct._check_type('vnic_profile', value, VnicProfile)
        self._vnic_profile = value

    @property
    def on_boot(self):
        """
        Returns the value of the `on_boot` property.
        """
        return self._on_boot

    @on_boot.setter
    def on_boot(self, value):
        """
        Sets the value of the `on_boot` property.
        """
        self._on_boot = value

    @property
    def linked(self):
        """
        Returns the value of the `linked` property.
        """
        return self._linked

    @linked.setter
    def linked(self, value):
        """
        Sets the value of the `linked` property.
        """
        self._linked = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value

    @property
    def network_attachments(self):
        """
        Returns the value of the `network_attachments` property.
        """
        return self._network_attachments

    @network_attachments.setter
    def network_attachments(self, value):
        """
        Sets the value of the `network_attachments` property.
        """
        self._network_attachments = value


class OpenStackProvider(ExternalProvider):

    def __init__(
        self,
        authentication_url=None,
        comment=None,
        description=None,
        id=None,
        name=None,
        password=None,
        properties=None,
        requires_authentication=None,
        tenant_name=None,
        url=None,
        username=None,
    ):
        super(OpenStackProvider, self).__init__(
            authentication_url=authentication_url,
            comment=comment,
            description=description,
            id=id,
            name=name,
            password=password,
            properties=properties,
            requires_authentication=requires_authentication,
            url=url,
            username=username,
        )
        self.tenant_name = tenant_name

    @property
    def tenant_name(self):
        """
        Returns the value of the `tenant_name` property.
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, value):
        """
        Sets the value of the `tenant_name` property.
        """
        self._tenant_name = value


class OpenStackVolumeProvider(OpenStackProvider):

    def __init__(
        self,
        authentication_keys=None,
        authentication_url=None,
        certificates=None,
        comment=None,
        data_center=None,
        description=None,
        id=None,
        name=None,
        password=None,
        properties=None,
        requires_authentication=None,
        tenant_name=None,
        url=None,
        username=None,
        volume_types=None,
    ):
        super(OpenStackVolumeProvider, self).__init__(
            authentication_url=authentication_url,
            comment=comment,
            description=description,
            id=id,
            name=name,
            password=password,
            properties=properties,
            requires_authentication=requires_authentication,
            tenant_name=tenant_name,
            url=url,
            username=username,
        )
        self.authentication_keys = authentication_keys
        self.certificates = certificates
        self.data_center = data_center
        self.volume_types = volume_types

    @property
    def certificates(self):
        """
        Returns the value of the `certificates` property.
        """
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        """
        Sets the value of the `certificates` property.
        """
        self._certificates = value

    @property
    def authentication_keys(self):
        """
        Returns the value of the `authentication_keys` property.
        """
        return self._authentication_keys

    @authentication_keys.setter
    def authentication_keys(self, value):
        """
        Sets the value of the `authentication_keys` property.
        """
        self._authentication_keys = value

    @property
    def data_center(self):
        """
        Returns the value of the `data_center` property.
        """
        return self._data_center

    @data_center.setter
    def data_center(self, value):
        """
        Sets the value of the `data_center` property.
        """
        Struct._check_type('data_center', value, DataCenter)
        self._data_center = value

    @property
    def volume_types(self):
        """
        Returns the value of the `volume_types` property.
        """
        return self._volume_types

    @volume_types.setter
    def volume_types(self, value):
        """
        Sets the value of the `volume_types` property.
        """
        self._volume_types = value


class Template(VmBase):

    def __init__(
        self,
        auto_pinning_policy=None,
        bios=None,
        cdroms=None,
        cluster=None,
        comment=None,
        console=None,
        cpu=None,
        cpu_profile=None,
        cpu_shares=None,
        creation_time=None,
        custom_compatibility_version=None,
        custom_cpu_model=None,
        custom_emulated_machine=None,
        custom_properties=None,
        delete_protected=None,
        description=None,
        disk_attachments=None,
        display=None,
        domain=None,
        graphics_consoles=None,
        high_availability=None,
        id=None,
        initialization=None,
        io=None,
        large_icon=None,
        lease=None,
        memory=None,
        memory_policy=None,
        migration=None,
        migration_downtime=None,
        multi_queues_enabled=None,
        name=None,
        nics=None,
        origin=None,
        os=None,
        permissions=None,
        placement_policy=None,
        quota=None,
        rng_device=None,
        serial_number=None,
        small_icon=None,
        soundcard_enabled=None,
        sso=None,
        start_paused=None,
        stateless=None,
        status=None,
        storage_domain=None,
        storage_error_resume_behaviour=None,
        tags=None,
        time_zone=None,
        tpm_enabled=None,
        tunnel_migration=None,
        type=None,
        usb=None,
        version=None,
        virtio_scsi=None,
        virtio_scsi_multi_queues=None,
        virtio_scsi_multi_queues_enabled=None,
        vm=None,
        watchdogs=None,
    ):
        super(Template, self).__init__(
            auto_pinning_policy=auto_pinning_policy,
            bios=bios,
            cluster=cluster,
            comment=comment,
            console=console,
            cpu=cpu,
            cpu_profile=cpu_profile,
            cpu_shares=cpu_shares,
            creation_time=creation_time,
            custom_compatibility_version=custom_compatibility_version,
            custom_cpu_model=custom_cpu_model,
            custom_emulated_machine=custom_emulated_machine,
            custom_properties=custom_properties,
            delete_protected=delete_protected,
            description=description,
            display=display,
            domain=domain,
            high_availability=high_availability,
            id=id,
            initialization=initialization,
            io=io,
            large_icon=large_icon,
            lease=lease,
            memory=memory,
            memory_policy=memory_policy,
            migration=migration,
            migration_downtime=migration_downtime,
            multi_queues_enabled=multi_queues_enabled,
            name=name,
            origin=origin,
            os=os,
            placement_policy=placement_policy,
            quota=quota,
            rng_device=rng_device,
            serial_number=serial_number,
            small_icon=small_icon,
            soundcard_enabled=soundcard_enabled,
            sso=sso,
            start_paused=start_paused,
            stateless=stateless,
            storage_domain=storage_domain,
            storage_error_resume_behaviour=storage_error_resume_behaviour,
            time_zone=time_zone,
            tpm_enabled=tpm_enabled,
            tunnel_migration=tunnel_migration,
            type=type,
            usb=usb,
            virtio_scsi=virtio_scsi,
            virtio_scsi_multi_queues=virtio_scsi_multi_queues,
            virtio_scsi_multi_queues_enabled=virtio_scsi_multi_queues_enabled,
        )
        self.cdroms = cdroms
        self.disk_attachments = disk_attachments
        self.graphics_consoles = graphics_consoles
        self.nics = nics
        self.permissions = permissions
        self.status = status
        self.tags = tags
        self.version = version
        self.vm = vm
        self.watchdogs = watchdogs

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def version(self):
        """
        Returns the value of the `version` property.
        """
        return self._version

    @version.setter
    def version(self, value):
        """
        Sets the value of the `version` property.
        """
        Struct._check_type('version', value, TemplateVersion)
        self._version = value

    @property
    def disk_attachments(self):
        """
        Returns the value of the `disk_attachments` property.
        """
        return self._disk_attachments

    @disk_attachments.setter
    def disk_attachments(self, value):
        """
        Sets the value of the `disk_attachments` property.
        """
        self._disk_attachments = value

    @property
    def cdroms(self):
        """
        Returns the value of the `cdroms` property.
        """
        return self._cdroms

    @cdroms.setter
    def cdroms(self, value):
        """
        Sets the value of the `cdroms` property.
        """
        self._cdroms = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def graphics_consoles(self):
        """
        Returns the value of the `graphics_consoles` property.
        """
        return self._graphics_consoles

    @graphics_consoles.setter
    def graphics_consoles(self, value):
        """
        Sets the value of the `graphics_consoles` property.
        """
        self._graphics_consoles = value

    @property
    def nics(self):
        """
        Returns the value of the `nics` property.
        """
        return self._nics

    @nics.setter
    def nics(self, value):
        """
        Sets the value of the `nics` property.
        """
        self._nics = value

    @property
    def watchdogs(self):
        """
        Returns the value of the `watchdogs` property.
        """
        return self._watchdogs

    @watchdogs.setter
    def watchdogs(self, value):
        """
        Sets the value of the `watchdogs` property.
        """
        self._watchdogs = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, TemplateStatus)
        self._status = value

    @property
    def tags(self):
        """
        Returns the value of the `tags` property.
        """
        return self._tags

    @tags.setter
    def tags(self, value):
        """
        Sets the value of the `tags` property.
        """
        self._tags = value


class Vm(VmBase):

    def __init__(
        self,
        affinity_labels=None,
        applications=None,
        auto_pinning_policy=None,
        bios=None,
        cdroms=None,
        cluster=None,
        comment=None,
        console=None,
        cpu=None,
        cpu_profile=None,
        cpu_shares=None,
        creation_time=None,
        custom_compatibility_version=None,
        custom_cpu_model=None,
        custom_emulated_machine=None,
        custom_properties=None,
        delete_protected=None,
        description=None,
        disk_attachments=None,
        display=None,
        domain=None,
        external_host_provider=None,
        floppies=None,
        fqdn=None,
        graphics_consoles=None,
        guest_operating_system=None,
        guest_time_zone=None,
        has_illegal_images=None,
        high_availability=None,
        host=None,
        host_devices=None,
        id=None,
        initialization=None,
        instance_type=None,
        io=None,
        katello_errata=None,
        large_icon=None,
        lease=None,
        memory=None,
        memory_policy=None,
        migration=None,
        migration_downtime=None,
        multi_queues_enabled=None,
        name=None,
        next_run_configuration_exists=None,
        nics=None,
        numa_nodes=None,
        numa_tune_mode=None,
        origin=None,
        original_template=None,
        os=None,
        payloads=None,
        permissions=None,
        placement_policy=None,
        quota=None,
        reported_devices=None,
        rng_device=None,
        run_once=None,
        serial_number=None,
        sessions=None,
        small_icon=None,
        snapshots=None,
        soundcard_enabled=None,
        sso=None,
        start_paused=None,
        start_time=None,
        stateless=None,
        statistics=None,
        status=None,
        status_detail=None,
        stop_reason=None,
        stop_time=None,
        storage_domain=None,
        storage_error_resume_behaviour=None,
        tags=None,
        template=None,
        time_zone=None,
        tpm_enabled=None,
        tunnel_migration=None,
        type=None,
        usb=None,
        use_latest_template_version=None,
        virtio_scsi=None,
        virtio_scsi_multi_queues=None,
        virtio_scsi_multi_queues_enabled=None,
        vm_pool=None,
        watchdogs=None,
    ):
        super(Vm, self).__init__(
            auto_pinning_policy=auto_pinning_policy,
            bios=bios,
            cluster=cluster,
            comment=comment,
            console=console,
            cpu=cpu,
            cpu_profile=cpu_profile,
            cpu_shares=cpu_shares,
            creation_time=creation_time,
            custom_compatibility_version=custom_compatibility_version,
            custom_cpu_model=custom_cpu_model,
            custom_emulated_machine=custom_emulated_machine,
            custom_properties=custom_properties,
            delete_protected=delete_protected,
            description=description,
            display=display,
            domain=domain,
            high_availability=high_availability,
            id=id,
            initialization=initialization,
            io=io,
            large_icon=large_icon,
            lease=lease,
            memory=memory,
            memory_policy=memory_policy,
            migration=migration,
            migration_downtime=migration_downtime,
            multi_queues_enabled=multi_queues_enabled,
            name=name,
            origin=origin,
            os=os,
            placement_policy=placement_policy,
            quota=quota,
            rng_device=rng_device,
            serial_number=serial_number,
            small_icon=small_icon,
            soundcard_enabled=soundcard_enabled,
            sso=sso,
            start_paused=start_paused,
            stateless=stateless,
            storage_domain=storage_domain,
            storage_error_resume_behaviour=storage_error_resume_behaviour,
            time_zone=time_zone,
            tpm_enabled=tpm_enabled,
            tunnel_migration=tunnel_migration,
            type=type,
            usb=usb,
            virtio_scsi=virtio_scsi,
            virtio_scsi_multi_queues=virtio_scsi_multi_queues,
            virtio_scsi_multi_queues_enabled=virtio_scsi_multi_queues_enabled,
        )
        self.affinity_labels = affinity_labels
        self.applications = applications
        self.cdroms = cdroms
        self.disk_attachments = disk_attachments
        self.external_host_provider = external_host_provider
        self.floppies = floppies
        self.fqdn = fqdn
        self.graphics_consoles = graphics_consoles
        self.guest_operating_system = guest_operating_system
        self.guest_time_zone = guest_time_zone
        self.has_illegal_images = has_illegal_images
        self.host = host
        self.host_devices = host_devices
        self.instance_type = instance_type
        self.katello_errata = katello_errata
        self.next_run_configuration_exists = next_run_configuration_exists
        self.nics = nics
        self.numa_nodes = numa_nodes
        self.numa_tune_mode = numa_tune_mode
        self.original_template = original_template
        self.payloads = payloads
        self.permissions = permissions
        self.reported_devices = reported_devices
        self.run_once = run_once
        self.sessions = sessions
        self.snapshots = snapshots
        self.start_time = start_time
        self.statistics = statistics
        self.status = status
        self.status_detail = status_detail
        self.stop_reason = stop_reason
        self.stop_time = stop_time
        self.tags = tags
        self.template = template
        self.use_latest_template_version = use_latest_template_version
        self.vm_pool = vm_pool
        self.watchdogs = watchdogs

    @property
    def numa_tune_mode(self):
        """
        Returns the value of the `numa_tune_mode` property.
        """
        return self._numa_tune_mode

    @numa_tune_mode.setter
    def numa_tune_mode(self, value):
        """
        Sets the value of the `numa_tune_mode` property.
        """
        Struct._check_type('numa_tune_mode', value, NumaTuneMode)
        self._numa_tune_mode = value

    @property
    def use_latest_template_version(self):
        """
        Returns the value of the `use_latest_template_version` property.
        """
        return self._use_latest_template_version

    @use_latest_template_version.setter
    def use_latest_template_version(self, value):
        """
        Sets the value of the `use_latest_template_version` property.
        """
        self._use_latest_template_version = value

    @property
    def reported_devices(self):
        """
        Returns the value of the `reported_devices` property.
        """
        return self._reported_devices

    @reported_devices.setter
    def reported_devices(self, value):
        """
        Sets the value of the `reported_devices` property.
        """
        self._reported_devices = value

    @property
    def sessions(self):
        """
        Returns the value of the `sessions` property.
        """
        return self._sessions

    @sessions.setter
    def sessions(self, value):
        """
        Sets the value of the `sessions` property.
        """
        self._sessions = value

    @property
    def fqdn(self):
        """
        Returns the value of the `fqdn` property.
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, value):
        """
        Sets the value of the `fqdn` property.
        """
        self._fqdn = value

    @property
    def cdroms(self):
        """
        Returns the value of the `cdroms` property.
        """
        return self._cdroms

    @cdroms.setter
    def cdroms(self, value):
        """
        Sets the value of the `cdroms` property.
        """
        self._cdroms = value

    @property
    def affinity_labels(self):
        """
        Returns the value of the `affinity_labels` property.
        """
        return self._affinity_labels

    @affinity_labels.setter
    def affinity_labels(self, value):
        """
        Sets the value of the `affinity_labels` property.
        """
        self._affinity_labels = value

    @property
    def floppies(self):
        """
        Returns the value of the `floppies` property.
        """
        return self._floppies

    @floppies.setter
    def floppies(self, value):
        """
        Sets the value of the `floppies` property.
        """
        self._floppies = value

    @property
    def stop_time(self):
        """
        Returns the value of the `stop_time` property.
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, value):
        """
        Sets the value of the `stop_time` property.
        """
        self._stop_time = value

    @property
    def tags(self):
        """
        Returns the value of the `tags` property.
        """
        return self._tags

    @tags.setter
    def tags(self, value):
        """
        Sets the value of the `tags` property.
        """
        self._tags = value

    @property
    def host_devices(self):
        """
        Returns the value of the `host_devices` property.
        """
        return self._host_devices

    @host_devices.setter
    def host_devices(self, value):
        """
        Sets the value of the `host_devices` property.
        """
        self._host_devices = value

    @property
    def snapshots(self):
        """
        Returns the value of the `snapshots` property.
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, value):
        """
        Sets the value of the `snapshots` property.
        """
        self._snapshots = value

    @property
    def disk_attachments(self):
        """
        Returns the value of the `disk_attachments` property.
        """
        return self._disk_attachments

    @disk_attachments.setter
    def disk_attachments(self, value):
        """
        Sets the value of the `disk_attachments` property.
        """
        self._disk_attachments = value

    @property
    def stop_reason(self):
        """
        Returns the value of the `stop_reason` property.
        """
        return self._stop_reason

    @stop_reason.setter
    def stop_reason(self, value):
        """
        Sets the value of the `stop_reason` property.
        """
        self._stop_reason = value

    @property
    def original_template(self):
        """
        Returns the value of the `original_template` property.
        """
        return self._original_template

    @original_template.setter
    def original_template(self, value):
        """
        Sets the value of the `original_template` property.
        """
        Struct._check_type('original_template', value, Template)
        self._original_template = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, VmStatus)
        self._status = value

    @property
    def next_run_configuration_exists(self):
        """
        Returns the value of the `next_run_configuration_exists` property.
        """
        return self._next_run_configuration_exists

    @next_run_configuration_exists.setter
    def next_run_configuration_exists(self, value):
        """
        Sets the value of the `next_run_configuration_exists` property.
        """
        self._next_run_configuration_exists = value

    @property
    def applications(self):
        """
        Returns the value of the `applications` property.
        """
        return self._applications

    @applications.setter
    def applications(self, value):
        """
        Sets the value of the `applications` property.
        """
        self._applications = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value

    @property
    def katello_errata(self):
        """
        Returns the value of the `katello_errata` property.
        """
        return self._katello_errata

    @katello_errata.setter
    def katello_errata(self, value):
        """
        Sets the value of the `katello_errata` property.
        """
        self._katello_errata = value

    @property
    def template(self):
        """
        Returns the value of the `template` property.
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        Sets the value of the `template` property.
        """
        Struct._check_type('template', value, Template)
        self._template = value

    @property
    def payloads(self):
        """
        Returns the value of the `payloads` property.
        """
        return self._payloads

    @payloads.setter
    def payloads(self, value):
        """
        Sets the value of the `payloads` property.
        """
        self._payloads = value

    @property
    def start_time(self):
        """
        Returns the value of the `start_time` property.
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """
        Sets the value of the `start_time` property.
        """
        self._start_time = value

    @property
    def graphics_consoles(self):
        """
        Returns the value of the `graphics_consoles` property.
        """
        return self._graphics_consoles

    @graphics_consoles.setter
    def graphics_consoles(self, value):
        """
        Sets the value of the `graphics_consoles` property.
        """
        self._graphics_consoles = value

    @property
    def watchdogs(self):
        """
        Returns the value of the `watchdogs` property.
        """
        return self._watchdogs

    @watchdogs.setter
    def watchdogs(self, value):
        """
        Sets the value of the `watchdogs` property.
        """
        self._watchdogs = value

    @property
    def guest_time_zone(self):
        """
        Returns the value of the `guest_time_zone` property.
        """
        return self._guest_time_zone

    @guest_time_zone.setter
    def guest_time_zone(self, value):
        """
        Sets the value of the `guest_time_zone` property.
        """
        Struct._check_type('guest_time_zone', value, TimeZone)
        self._guest_time_zone = value

    @property
    def guest_operating_system(self):
        """
        Returns the value of the `guest_operating_system` property.
        """
        return self._guest_operating_system

    @guest_operating_system.setter
    def guest_operating_system(self, value):
        """
        Sets the value of the `guest_operating_system` property.
        """
        Struct._check_type('guest_operating_system', value, GuestOperatingSystem)
        self._guest_operating_system = value

    @property
    def vm_pool(self):
        """
        Returns the value of the `vm_pool` property.
        """
        return self._vm_pool

    @vm_pool.setter
    def vm_pool(self, value):
        """
        Sets the value of the `vm_pool` property.
        """
        Struct._check_type('vm_pool', value, VmPool)
        self._vm_pool = value

    @property
    def numa_nodes(self):
        """
        Returns the value of the `numa_nodes` property.
        """
        return self._numa_nodes

    @numa_nodes.setter
    def numa_nodes(self, value):
        """
        Sets the value of the `numa_nodes` property.
        """
        self._numa_nodes = value

    @property
    def permissions(self):
        """
        Returns the value of the `permissions` property.
        """
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """
        Sets the value of the `permissions` property.
        """
        self._permissions = value

    @property
    def has_illegal_images(self):
        """
        Returns the value of the `has_illegal_images` property.
        """
        return self._has_illegal_images

    @has_illegal_images.setter
    def has_illegal_images(self, value):
        """
        Sets the value of the `has_illegal_images` property.
        """
        self._has_illegal_images = value

    @property
    def external_host_provider(self):
        """
        Returns the value of the `external_host_provider` property.
        """
        return self._external_host_provider

    @external_host_provider.setter
    def external_host_provider(self, value):
        """
        Sets the value of the `external_host_provider` property.
        """
        Struct._check_type('external_host_provider', value, ExternalHostProvider)
        self._external_host_provider = value

    @property
    def instance_type(self):
        """
        Returns the value of the `instance_type` property.
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, value):
        """
        Sets the value of the `instance_type` property.
        """
        Struct._check_type('instance_type', value, InstanceType)
        self._instance_type = value

    @property
    def status_detail(self):
        """
        Returns the value of the `status_detail` property.
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, value):
        """
        Sets the value of the `status_detail` property.
        """
        self._status_detail = value

    @property
    def host(self):
        """
        Returns the value of the `host` property.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Sets the value of the `host` property.
        """
        Struct._check_type('host', value, Host)
        self._host = value

    @property
    def nics(self):
        """
        Returns the value of the `nics` property.
        """
        return self._nics

    @nics.setter
    def nics(self, value):
        """
        Sets the value of the `nics` property.
        """
        self._nics = value

    @property
    def run_once(self):
        """
        Returns the value of the `run_once` property.
        """
        return self._run_once

    @run_once.setter
    def run_once(self, value):
        """
        Sets the value of the `run_once` property.
        """
        self._run_once = value


class Watchdog(Device):

    def __init__(
        self,
        action=None,
        comment=None,
        description=None,
        id=None,
        instance_type=None,
        model=None,
        name=None,
        template=None,
        vm=None,
        vms=None,
    ):
        super(Watchdog, self).__init__(
            comment=comment,
            description=description,
            id=id,
            instance_type=instance_type,
            name=name,
            template=template,
            vm=vm,
            vms=vms,
        )
        self.action = action
        self.model = model

    @property
    def action(self):
        """
        Returns the value of the `action` property.
        """
        return self._action

    @action.setter
    def action(self, value):
        """
        Sets the value of the `action` property.
        """
        Struct._check_type('action', value, WatchdogAction)
        self._action = value

    @property
    def model(self):
        """
        Returns the value of the `model` property.
        """
        return self._model

    @model.setter
    def model(self, value):
        """
        Sets the value of the `model` property.
        """
        Struct._check_type('model', value, WatchdogModel)
        self._model = value


class Cdrom(Device):

    def __init__(
        self,
        comment=None,
        description=None,
        file=None,
        id=None,
        instance_type=None,
        name=None,
        template=None,
        vm=None,
        vms=None,
    ):
        super(Cdrom, self).__init__(
            comment=comment,
            description=description,
            id=id,
            instance_type=instance_type,
            name=name,
            template=template,
            vm=vm,
            vms=vms,
        )
        self.file = file

    @property
    def file(self):
        """
        Returns the value of the `file` property.
        """
        return self._file

    @file.setter
    def file(self, value):
        """
        Sets the value of the `file` property.
        """
        Struct._check_type('file', value, File)
        self._file = value


class ExternalHostProvider(ExternalProvider):

    def __init__(
        self,
        authentication_url=None,
        certificates=None,
        comment=None,
        compute_resources=None,
        description=None,
        discovered_hosts=None,
        host_groups=None,
        hosts=None,
        id=None,
        name=None,
        password=None,
        properties=None,
        requires_authentication=None,
        url=None,
        username=None,
    ):
        super(ExternalHostProvider, self).__init__(
            authentication_url=authentication_url,
            comment=comment,
            description=description,
            id=id,
            name=name,
            password=password,
            properties=properties,
            requires_authentication=requires_authentication,
            url=url,
            username=username,
        )
        self.certificates = certificates
        self.compute_resources = compute_resources
        self.discovered_hosts = discovered_hosts
        self.host_groups = host_groups
        self.hosts = hosts

    @property
    def certificates(self):
        """
        Returns the value of the `certificates` property.
        """
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        """
        Sets the value of the `certificates` property.
        """
        self._certificates = value

    @property
    def host_groups(self):
        """
        Returns the value of the `host_groups` property.
        """
        return self._host_groups

    @host_groups.setter
    def host_groups(self, value):
        """
        Sets the value of the `host_groups` property.
        """
        self._host_groups = value

    @property
    def hosts(self):
        """
        Returns the value of the `hosts` property.
        """
        return self._hosts

    @hosts.setter
    def hosts(self, value):
        """
        Sets the value of the `hosts` property.
        """
        self._hosts = value

    @property
    def compute_resources(self):
        """
        Returns the value of the `compute_resources` property.
        """
        return self._compute_resources

    @compute_resources.setter
    def compute_resources(self, value):
        """
        Sets the value of the `compute_resources` property.
        """
        self._compute_resources = value

    @property
    def discovered_hosts(self):
        """
        Returns the value of the `discovered_hosts` property.
        """
        return self._discovered_hosts

    @discovered_hosts.setter
    def discovered_hosts(self, value):
        """
        Sets the value of the `discovered_hosts` property.
        """
        self._discovered_hosts = value


class GlusterBrick(GlusterBrickAdvancedDetails):

    def __init__(
        self,
        brick_dir=None,
        comment=None,
        description=None,
        device=None,
        fs_name=None,
        gluster_clients=None,
        gluster_volume=None,
        id=None,
        instance_type=None,
        memory_pools=None,
        mnt_options=None,
        name=None,
        pid=None,
        port=None,
        server_id=None,
        statistics=None,
        status=None,
        template=None,
        vm=None,
        vms=None,
    ):
        super(GlusterBrick, self).__init__(
            comment=comment,
            description=description,
            device=device,
            fs_name=fs_name,
            gluster_clients=gluster_clients,
            id=id,
            instance_type=instance_type,
            memory_pools=memory_pools,
            mnt_options=mnt_options,
            name=name,
            pid=pid,
            port=port,
            template=template,
            vm=vm,
            vms=vms,
        )
        self.brick_dir = brick_dir
        self.gluster_volume = gluster_volume
        self.server_id = server_id
        self.statistics = statistics
        self.status = status

    @property
    def brick_dir(self):
        """
        Returns the value of the `brick_dir` property.
        """
        return self._brick_dir

    @brick_dir.setter
    def brick_dir(self, value):
        """
        Sets the value of the `brick_dir` property.
        """
        self._brick_dir = value

    @property
    def server_id(self):
        """
        Returns the value of the `server_id` property.
        """
        return self._server_id

    @server_id.setter
    def server_id(self, value):
        """
        Sets the value of the `server_id` property.
        """
        self._server_id = value

    @property
    def gluster_volume(self):
        """
        Returns the value of the `gluster_volume` property.
        """
        return self._gluster_volume

    @gluster_volume.setter
    def gluster_volume(self, value):
        """
        Sets the value of the `gluster_volume` property.
        """
        Struct._check_type('gluster_volume', value, GlusterVolume)
        self._gluster_volume = value

    @property
    def status(self):
        """
        Returns the value of the `status` property.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the value of the `status` property.
        """
        Struct._check_type('status', value, GlusterBrickStatus)
        self._status = value

    @property
    def statistics(self):
        """
        Returns the value of the `statistics` property.
        """
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """
        Sets the value of the `statistics` property.
        """
        self._statistics = value


class InstanceType(Template):

    def __init__(
        self,
        auto_pinning_policy=None,
        bios=None,
        cdroms=None,
        cluster=None,
        comment=None,
        console=None,
        cpu=None,
        cpu_profile=None,
        cpu_shares=None,
        creation_time=None,
        custom_compatibility_version=None,
        custom_cpu_model=None,
        custom_emulated_machine=None,
        custom_properties=None,
        delete_protected=None,
        description=None,
        disk_attachments=None,
        display=None,
        domain=None,
        graphics_consoles=None,
        high_availability=None,
        id=None,
        initialization=None,
        io=None,
        large_icon=None,
        lease=None,
        memory=None,
        memory_policy=None,
        migration=None,
        migration_downtime=None,
        multi_queues_enabled=None,
        name=None,
        nics=None,
        origin=None,
        os=None,
        permissions=None,
        placement_policy=None,
        quota=None,
        rng_device=None,
        serial_number=None,
        small_icon=None,
        soundcard_enabled=None,
        sso=None,
        start_paused=None,
        stateless=None,
        status=None,
        storage_domain=None,
        storage_error_resume_behaviour=None,
        tags=None,
        time_zone=None,
        tpm_enabled=None,
        tunnel_migration=None,
        type=None,
        usb=None,
        version=None,
        virtio_scsi=None,
        virtio_scsi_multi_queues=None,
        virtio_scsi_multi_queues_enabled=None,
        vm=None,
        watchdogs=None,
    ):
        super(InstanceType, self).__init__(
            auto_pinning_policy=auto_pinning_policy,
            bios=bios,
            cdroms=cdroms,
            cluster=cluster,
            comment=comment,
            console=console,
            cpu=cpu,
            cpu_profile=cpu_profile,
            cpu_shares=cpu_shares,
            creation_time=creation_time,
            custom_compatibility_version=custom_compatibility_version,
            custom_cpu_model=custom_cpu_model,
            custom_emulated_machine=custom_emulated_machine,
            custom_properties=custom_properties,
            delete_protected=delete_protected,
            description=description,
            disk_attachments=disk_attachments,
            display=display,
            domain=domain,
            graphics_consoles=graphics_consoles,
            high_availability=high_availability,
            id=id,
            initialization=initialization,
            io=io,
            large_icon=large_icon,
            lease=lease,
            memory=memory,
            memory_policy=memory_policy,
            migration=migration,
            migration_downtime=migration_downtime,
            multi_queues_enabled=multi_queues_enabled,
            name=name,
            nics=nics,
            origin=origin,
            os=os,
            permissions=permissions,
            placement_policy=placement_policy,
            quota=quota,
            rng_device=rng_device,
            serial_number=serial_number,
            small_icon=small_icon,
            soundcard_enabled=soundcard_enabled,
            sso=sso,
            start_paused=start_paused,
            stateless=stateless,
            status=status,
            storage_domain=storage_domain,
            storage_error_resume_behaviour=storage_error_resume_behaviour,
            tags=tags,
            time_zone=time_zone,
            tpm_enabled=tpm_enabled,
            tunnel_migration=tunnel_migration,
            type=type,
            usb=usb,
            version=version,
            virtio_scsi=virtio_scsi,
            virtio_scsi_multi_queues=virtio_scsi_multi_queues,
            virtio_scsi_multi_queues_enabled=virtio_scsi_multi_queues_enabled,
            vm=vm,
            watchdogs=watchdogs,
        )
        pass


class OpenStackImageProvider(OpenStackProvider):

    def __init__(
        self,
        authentication_url=None,
        certificates=None,
        comment=None,
        description=None,
        id=None,
        images=None,
        name=None,
        password=None,
        properties=None,
        requires_authentication=None,
        tenant_name=None,
        url=None,
        username=None,
    ):
        super(OpenStackImageProvider, self).__init__(
            authentication_url=authentication_url,
            comment=comment,
            description=description,
            id=id,
            name=name,
            password=password,
            properties=properties,
            requires_authentication=requires_authentication,
            tenant_name=tenant_name,
            url=url,
            username=username,
        )
        self.certificates = certificates
        self.images = images

    @property
    def certificates(self):
        """
        Returns the value of the `certificates` property.
        """
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        """
        Sets the value of the `certificates` property.
        """
        self._certificates = value

    @property
    def images(self):
        """
        Returns the value of the `images` property.
        """
        return self._images

    @images.setter
    def images(self, value):
        """
        Sets the value of the `images` property.
        """
        self._images = value


class OpenStackNetworkProvider(OpenStackProvider):

    def __init__(
        self,
        agent_configuration=None,
        authentication_url=None,
        auto_sync=None,
        certificates=None,
        comment=None,
        description=None,
        external_plugin_type=None,
        id=None,
        name=None,
        networks=None,
        password=None,
        plugin_type=None,
        project_domain_name=None,
        project_name=None,
        properties=None,
        read_only=None,
        requires_authentication=None,
        subnets=None,
        tenant_name=None,
        type=None,
        unmanaged=None,
        url=None,
        user_domain_name=None,
        username=None,
    ):
        super(OpenStackNetworkProvider, self).__init__(
            authentication_url=authentication_url,
            comment=comment,
            description=description,
            id=id,
            name=name,
            password=password,
            properties=properties,
            requires_authentication=requires_authentication,
            tenant_name=tenant_name,
            url=url,
            username=username,
        )
        self.agent_configuration = agent_configuration
        self.auto_sync = auto_sync
        self.certificates = certificates
        self.external_plugin_type = external_plugin_type
        self.networks = networks
        self.plugin_type = plugin_type
        self.project_domain_name = project_domain_name
        self.project_name = project_name
        self.read_only = read_only
        self.subnets = subnets
        self.type = type
        self.unmanaged = unmanaged
        self.user_domain_name = user_domain_name

    @property
    def agent_configuration(self):
        """
        Returns the value of the `agent_configuration` property.
        """
        return self._agent_configuration

    @agent_configuration.setter
    def agent_configuration(self, value):
        """
        Sets the value of the `agent_configuration` property.
        """
        Struct._check_type('agent_configuration', value, AgentConfiguration)
        self._agent_configuration = value

    @property
    def networks(self):
        """
        Returns the value of the `networks` property.
        """
        return self._networks

    @networks.setter
    def networks(self, value):
        """
        Sets the value of the `networks` property.
        """
        self._networks = value

    @property
    def auto_sync(self):
        """
        Returns the value of the `auto_sync` property.
        """
        return self._auto_sync

    @auto_sync.setter
    def auto_sync(self, value):
        """
        Sets the value of the `auto_sync` property.
        """
        self._auto_sync = value

    @property
    def type(self):
        """
        Returns the value of the `type` property.
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        Sets the value of the `type` property.
        """
        Struct._check_type('type', value, OpenStackNetworkProviderType)
        self._type = value

    @property
    def certificates(self):
        """
        Returns the value of the `certificates` property.
        """
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        """
        Sets the value of the `certificates` property.
        """
        self._certificates = value

    @property
    def unmanaged(self):
        """
        Returns the value of the `unmanaged` property.
        """
        return self._unmanaged

    @unmanaged.setter
    def unmanaged(self, value):
        """
        Sets the value of the `unmanaged` property.
        """
        self._unmanaged = value

    @property
    def user_domain_name(self):
        """
        Returns the value of the `user_domain_name` property.
        """
        return self._user_domain_name

    @user_domain_name.setter
    def user_domain_name(self, value):
        """
        Sets the value of the `user_domain_name` property.
        """
        self._user_domain_name = value

    @property
    def plugin_type(self):
        """
        Returns the value of the `plugin_type` property.
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, value):
        """
        Sets the value of the `plugin_type` property.
        """
        Struct._check_type('plugin_type', value, NetworkPluginType)
        self._plugin_type = value

    @property
    def subnets(self):
        """
        Returns the value of the `subnets` property.
        """
        return self._subnets

    @subnets.setter
    def subnets(self, value):
        """
        Sets the value of the `subnets` property.
        """
        self._subnets = value

    @property
    def project_domain_name(self):
        """
        Returns the value of the `project_domain_name` property.
        """
        return self._project_domain_name

    @project_domain_name.setter
    def project_domain_name(self, value):
        """
        Sets the value of the `project_domain_name` property.
        """
        self._project_domain_name = value

    @property
    def external_plugin_type(self):
        """
        Returns the value of the `external_plugin_type` property.
        """
        return self._external_plugin_type

    @external_plugin_type.setter
    def external_plugin_type(self, value):
        """
        Sets the value of the `external_plugin_type` property.
        """
        self._external_plugin_type = value

    @property
    def read_only(self):
        """
        Returns the value of the `read_only` property.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """
        Sets the value of the `read_only` property.
        """
        self._read_only = value

    @property
    def project_name(self):
        """
        Returns the value of the `project_name` property.
        """
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        """
        Sets the value of the `project_name` property.
        """
        self._project_name = value


class Snapshot(Vm):

    def __init__(
        self,
        affinity_labels=None,
        applications=None,
        auto_pinning_policy=None,
        bios=None,
        cdroms=None,
        cluster=None,
        comment=None,
        console=None,
        cpu=None,
        cpu_profile=None,
        cpu_shares=None,
        creation_time=None,
        custom_compatibility_version=None,
        custom_cpu_model=None,
        custom_emulated_machine=None,
        custom_properties=None,
        date=None,
        delete_protected=None,
        description=None,
        disk_attachments=None,
        disks=None,
        display=None,
        domain=None,
        external_host_provider=None,
        floppies=None,
        fqdn=None,
        graphics_consoles=None,
        guest_operating_system=None,
        guest_time_zone=None,
        has_illegal_images=None,
        high_availability=None,
        host=None,
        host_devices=None,
        id=None,
        initialization=None,
        instance_type=None,
        io=None,
        katello_errata=None,
        large_icon=None,
        lease=None,
        memory=None,
        memory_policy=None,
        migration=None,
        migration_downtime=None,
        multi_queues_enabled=None,
        name=None,
        next_run_configuration_exists=None,
        nics=None,
        numa_nodes=None,
        numa_tune_mode=None,
        origin=None,
        original_template=None,
        os=None,
        payloads=None,
        permissions=None,
        persist_memorystate=None,
        placement_policy=None,
        quota=None,
        reported_devices=None,
        rng_device=None,
        run_once=None,
        serial_number=None,
        sessions=None,
        small_icon=None,
        snapshot_status=None,
        snapshot_type=None,
        snapshots=None,
        soundcard_enabled=None,
        sso=None,
        start_paused=None,
        start_time=None,
        stateless=None,
        statistics=None,
        status=None,
        status_detail=None,
        stop_reason=None,
        stop_time=None,
        storage_domain=None,
        storage_error_resume_behaviour=None,
        tags=None,
        template=None,
        time_zone=None,
        tpm_enabled=None,
        tunnel_migration=None,
        type=None,
        usb=None,
        use_latest_template_version=None,
        virtio_scsi=None,
        virtio_scsi_multi_queues=None,
        virtio_scsi_multi_queues_enabled=None,
        vm=None,
        vm_pool=None,
        watchdogs=None,
    ):
        super(Snapshot, self).__init__(
            affinity_labels=affinity_labels,
            applications=applications,
            auto_pinning_policy=auto_pinning_policy,
            bios=bios,
            cdroms=cdroms,
            cluster=cluster,
            comment=comment,
            console=console,
            cpu=cpu,
            cpu_profile=cpu_profile,
            cpu_shares=cpu_shares,
            creation_time=creation_time,
            custom_compatibility_version=custom_compatibility_version,
            custom_cpu_model=custom_cpu_model,
            custom_emulated_machine=custom_emulated_machine,
            custom_properties=custom_properties,
            delete_protected=delete_protected,
            description=description,
            disk_attachments=disk_attachments,
            display=display,
            domain=domain,
            external_host_provider=external_host_provider,
            floppies=floppies,
            fqdn=fqdn,
            graphics_consoles=graphics_consoles,
            guest_operating_system=guest_operating_system,
            guest_time_zone=guest_time_zone,
            has_illegal_images=has_illegal_images,
            high_availability=high_availability,
            host=host,
            host_devices=host_devices,
            id=id,
            initialization=initialization,
            instance_type=instance_type,
            io=io,
            katello_errata=katello_errata,
            large_icon=large_icon,
            lease=lease,
            memory=memory,
            memory_policy=memory_policy,
            migration=migration,
            migration_downtime=migration_downtime,
            multi_queues_enabled=multi_queues_enabled,
            name=name,
            next_run_configuration_exists=next_run_configuration_exists,
            nics=nics,
            numa_nodes=numa_nodes,
            numa_tune_mode=numa_tune_mode,
            origin=origin,
            original_template=original_template,
            os=os,
            payloads=payloads,
            permissions=permissions,
            placement_policy=placement_policy,
            quota=quota,
            reported_devices=reported_devices,
            rng_device=rng_device,
            run_once=run_once,
            serial_number=serial_number,
            sessions=sessions,
            small_icon=small_icon,
            snapshots=snapshots,
            soundcard_enabled=soundcard_enabled,
            sso=sso,
            start_paused=start_paused,
            start_time=start_time,
            stateless=stateless,
            statistics=statistics,
            status=status,
            status_detail=status_detail,
            stop_reason=stop_reason,
            stop_time=stop_time,
            storage_domain=storage_domain,
            storage_error_resume_behaviour=storage_error_resume_behaviour,
            tags=tags,
            template=template,
            time_zone=time_zone,
            tpm_enabled=tpm_enabled,
            tunnel_migration=tunnel_migration,
            type=type,
            usb=usb,
            use_latest_template_version=use_latest_template_version,
            virtio_scsi=virtio_scsi,
            virtio_scsi_multi_queues=virtio_scsi_multi_queues,
            virtio_scsi_multi_queues_enabled=virtio_scsi_multi_queues_enabled,
            vm_pool=vm_pool,
            watchdogs=watchdogs,
        )
        self.date = date
        self.disks = disks
        self.persist_memorystate = persist_memorystate
        self.snapshot_status = snapshot_status
        self.snapshot_type = snapshot_type
        self.vm = vm

    @property
    def snapshot_type(self):
        """
        Returns the value of the `snapshot_type` property.
        """
        return self._snapshot_type

    @snapshot_type.setter
    def snapshot_type(self, value):
        """
        Sets the value of the `snapshot_type` property.
        """
        Struct._check_type('snapshot_type', value, SnapshotType)
        self._snapshot_type = value

    @property
    def snapshot_status(self):
        """
        Returns the value of the `snapshot_status` property.
        """
        return self._snapshot_status

    @snapshot_status.setter
    def snapshot_status(self, value):
        """
        Sets the value of the `snapshot_status` property.
        """
        Struct._check_type('snapshot_status', value, SnapshotStatus)
        self._snapshot_status = value

    @property
    def date(self):
        """
        Returns the value of the `date` property.
        """
        return self._date

    @date.setter
    def date(self, value):
        """
        Sets the value of the `date` property.
        """
        self._date = value

    @property
    def vm(self):
        """
        Returns the value of the `vm` property.
        """
        return self._vm

    @vm.setter
    def vm(self, value):
        """
        Sets the value of the `vm` property.
        """
        Struct._check_type('vm', value, Vm)
        self._vm = value

    @property
    def disks(self):
        """
        Returns the value of the `disks` property.
        """
        return self._disks

    @disks.setter
    def disks(self, value):
        """
        Sets the value of the `disks` property.
        """
        self._disks = value

    @property
    def persist_memorystate(self):
        """
        Returns the value of the `persist_memorystate` property.
        """
        return self._persist_memorystate

    @persist_memorystate.setter
    def persist_memorystate(self, value):
        """
        Sets the value of the `persist_memorystate` property.
        """
        self._persist_memorystate = value


@unique
class AccessProtocol(Enum):
    CIFS = 'cifs'
    GLUSTER = 'gluster'
    NFS = 'nfs'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class Architecture(Enum):
    PPC64 = 'ppc64'
    S390X = 's390x'
    UNDEFINED = 'undefined'
    X86_64 = 'x86_64'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class AutoNumaStatus(Enum):
    DISABLE = 'disable'
    ENABLE = 'enable'
    UNKNOWN = 'unknown'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class AutoPinningPolicy(Enum):
    ADJUST = 'adjust'
    DISABLED = 'disabled'
    EXISTING = 'existing'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class BackupPhase(Enum):
    FAILED = 'failed'
    FINALIZING = 'finalizing'
    INITIALIZING = 'initializing'
    READY = 'ready'
    STARTING = 'starting'
    SUCCEEDED = 'succeeded'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class BiosType(Enum):
    CLUSTER_DEFAULT = 'cluster_default'
    I440FX_SEA_BIOS = 'i440fx_sea_bios'
    Q35_OVMF = 'q35_ovmf'
    Q35_SEA_BIOS = 'q35_sea_bios'
    Q35_SECURE_BOOT = 'q35_secure_boot'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class BootDevice(Enum):
    CDROM = 'cdrom'
    HD = 'hd'
    NETWORK = 'network'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class BootProtocol(Enum):
    AUTOCONF = 'autoconf'
    DHCP = 'dhcp'
    NONE = 'none'
    POLY_DHCP_AUTOCONF = 'poly_dhcp_autoconf'
    STATIC = 'static'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class CheckpointState(Enum):
    CREATED = 'created'
    INVALID = 'invalid'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class CloudInitNetworkProtocol(Enum):
    ENI = 'eni'
    OPENSTACK_METADATA = 'openstack_metadata'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ClusterUpgradeAction(Enum):
    FINISH = 'finish'
    START = 'start'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ConfigurationType(Enum):
    OVA = 'ova'
    OVF = 'ovf'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class CpuMode(Enum):
    CUSTOM = 'custom'
    HOST_MODEL = 'host_model'
    HOST_PASSTHROUGH = 'host_passthrough'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class CreationStatus(Enum):
    COMPLETE = 'complete'
    FAILED = 'failed'
    IN_PROGRESS = 'in_progress'
    PENDING = 'pending'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DataCenterStatus(Enum):
    CONTEND = 'contend'
    MAINTENANCE = 'maintenance'
    NOT_OPERATIONAL = 'not_operational'
    PROBLEMATIC = 'problematic'
    UNINITIALIZED = 'uninitialized'
    UP = 'up'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DiskBackup(Enum):
    INCREMENTAL = 'incremental'
    NONE = 'none'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DiskBackupMode(Enum):
    FULL = 'full'
    INCREMENTAL = 'incremental'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DiskContentType(Enum):
    BACKUP_SCRATCH = 'backup_scratch'
    DATA = 'data'
    HOSTED_ENGINE = 'hosted_engine'
    HOSTED_ENGINE_CONFIGURATION = 'hosted_engine_configuration'
    HOSTED_ENGINE_METADATA = 'hosted_engine_metadata'
    HOSTED_ENGINE_SANLOCK = 'hosted_engine_sanlock'
    ISO = 'iso'
    MEMORY_DUMP_VOLUME = 'memory_dump_volume'
    MEMORY_METADATA_VOLUME = 'memory_metadata_volume'
    OVF_STORE = 'ovf_store'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DiskFormat(Enum):
    COW = 'cow'
    RAW = 'raw'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DiskInterface(Enum):
    IDE = 'ide'
    SATA = 'sata'
    SPAPR_VSCSI = 'spapr_vscsi'
    VIRTIO = 'virtio'
    VIRTIO_SCSI = 'virtio_scsi'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DiskStatus(Enum):
    ILLEGAL = 'illegal'
    LOCKED = 'locked'
    OK = 'ok'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DiskStorageType(Enum):
    CINDER = 'cinder'
    IMAGE = 'image'
    LUN = 'lun'
    MANAGED_BLOCK_STORAGE = 'managed_block_storage'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DiskType(Enum):
    DATA = 'data'
    SYSTEM = 'system'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class DisplayType(Enum):
    SPICE = 'spice'
    VNC = 'vnc'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class EntityExternalStatus(Enum):
    ERROR = 'error'
    FAILURE = 'failure'
    INFO = 'info'
    OK = 'ok'
    WARNING = 'warning'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ExternalStatus(Enum):
    ERROR = 'error'
    FAILURE = 'failure'
    INFO = 'info'
    OK = 'ok'
    WARNING = 'warning'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ExternalSystemType(Enum):
    GLUSTER = 'gluster'
    VDSM = 'vdsm'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ExternalVmProviderType(Enum):
    KVM = 'kvm'
    VMWARE = 'vmware'
    XEN = 'xen'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class FenceType(Enum):
    MANUAL = 'manual'
    RESTART = 'restart'
    START = 'start'
    STATUS = 'status'
    STOP = 'stop'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class FipsMode(Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    UNDEFINED = 'undefined'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class FirewallType(Enum):
    FIREWALLD = 'firewalld'
    IPTABLES = 'iptables'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class GlusterBrickStatus(Enum):
    DOWN = 'down'
    UNKNOWN = 'unknown'
    UP = 'up'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class GlusterHookStatus(Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    MISSING = 'missing'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class GlusterState(Enum):
    DOWN = 'down'
    UNKNOWN = 'unknown'
    UP = 'up'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class GlusterVolumeStatus(Enum):
    DOWN = 'down'
    UNKNOWN = 'unknown'
    UP = 'up'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class GlusterVolumeType(Enum):
    DISPERSE = 'disperse'
    DISTRIBUTE = 'distribute'
    DISTRIBUTED_DISPERSE = 'distributed_disperse'
    DISTRIBUTED_REPLICATE = 'distributed_replicate'
    DISTRIBUTED_STRIPE = 'distributed_stripe'
    DISTRIBUTED_STRIPED_REPLICATE = 'distributed_striped_replicate'
    REPLICATE = 'replicate'
    STRIPE = 'stripe'
    STRIPED_REPLICATE = 'striped_replicate'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class GraphicsType(Enum):
    SPICE = 'spice'
    VNC = 'vnc'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class HookContentType(Enum):
    BINARY = 'binary'
    TEXT = 'text'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class HookStage(Enum):
    POST = 'post'
    PRE = 'pre'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class HookStatus(Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    MISSING = 'missing'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class HostProtocol(Enum):
    STOMP = 'stomp'
    XML = 'xml'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class HostStatus(Enum):
    CONNECTING = 'connecting'
    DOWN = 'down'
    ERROR = 'error'
    INITIALIZING = 'initializing'
    INSTALL_FAILED = 'install_failed'
    INSTALLING = 'installing'
    INSTALLING_OS = 'installing_os'
    KDUMPING = 'kdumping'
    MAINTENANCE = 'maintenance'
    NON_OPERATIONAL = 'non_operational'
    NON_RESPONSIVE = 'non_responsive'
    PENDING_APPROVAL = 'pending_approval'
    PREPARING_FOR_MAINTENANCE = 'preparing_for_maintenance'
    REBOOT = 'reboot'
    UNASSIGNED = 'unassigned'
    UP = 'up'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class HostType(Enum):
    OVIRT_NODE = 'ovirt_node'
    RHEL = 'rhel'
    RHEV_H = 'rhev_h'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ImageFileType(Enum):
    DISK = 'disk'
    FLOPPY = 'floppy'
    ISO = 'iso'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ImageTransferDirection(Enum):
    DOWNLOAD = 'download'
    UPLOAD = 'upload'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ImageTransferPhase(Enum):
    CANCELLED = 'cancelled'
    CANCELLED_SYSTEM = 'cancelled_system'
    CANCELLED_USER = 'cancelled_user'
    FINALIZING_CLEANUP = 'finalizing_cleanup'
    FINALIZING_FAILURE = 'finalizing_failure'
    FINALIZING_SUCCESS = 'finalizing_success'
    FINISHED_CLEANUP = 'finished_cleanup'
    FINISHED_FAILURE = 'finished_failure'
    FINISHED_SUCCESS = 'finished_success'
    INITIALIZING = 'initializing'
    PAUSED_SYSTEM = 'paused_system'
    PAUSED_USER = 'paused_user'
    RESUMING = 'resuming'
    TRANSFERRING = 'transferring'
    UNKNOWN = 'unknown'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ImageTransferTimeoutPolicy(Enum):
    CANCEL = 'cancel'
    LEGACY = 'legacy'
    PAUSE = 'pause'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class InheritableBoolean(Enum):
    FALSE = 'false'
    INHERIT = 'inherit'
    TRUE = 'true'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class IpVersion(Enum):
    V4 = 'v4'
    V6 = 'v6'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class JobStatus(Enum):
    ABORTED = 'aborted'
    FAILED = 'failed'
    FINISHED = 'finished'
    STARTED = 'started'
    UNKNOWN = 'unknown'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class KdumpStatus(Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    UNKNOWN = 'unknown'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class LogMaxMemoryUsedThresholdType(Enum):
    ABSOLUTE_VALUE_IN_MB = 'absolute_value_in_mb'
    PERCENTAGE = 'percentage'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class LogSeverity(Enum):
    ALERT = 'alert'
    ERROR = 'error'
    NORMAL = 'normal'
    WARNING = 'warning'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class LunStatus(Enum):
    FREE = 'free'
    UNUSABLE = 'unusable'
    USED = 'used'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class MessageBrokerType(Enum):
    QPID = 'qpid'
    RABBIT_MQ = 'rabbit_mq'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class MigrateOnError(Enum):
    DO_NOT_MIGRATE = 'do_not_migrate'
    MIGRATE = 'migrate'
    MIGRATE_HIGHLY_AVAILABLE = 'migrate_highly_available'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class MigrationBandwidthAssignmentMethod(Enum):
    AUTO = 'auto'
    CUSTOM = 'custom'
    HYPERVISOR_DEFAULT = 'hypervisor_default'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NetworkPluginType(Enum):
    OPEN_VSWITCH = 'open_vswitch'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NetworkStatus(Enum):
    NON_OPERATIONAL = 'non_operational'
    OPERATIONAL = 'operational'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NetworkUsage(Enum):
    DEFAULT_ROUTE = 'default_route'
    DISPLAY = 'display'
    GLUSTER = 'gluster'
    MANAGEMENT = 'management'
    MIGRATION = 'migration'
    VM = 'vm'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NfsVersion(Enum):
    AUTO = 'auto'
    V3 = 'v3'
    V4 = 'v4'
    V4_0 = 'v4_0'
    V4_1 = 'v4_1'
    V4_2 = 'v4_2'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NicInterface(Enum):
    E1000 = 'e1000'
    PCI_PASSTHROUGH = 'pci_passthrough'
    RTL8139 = 'rtl8139'
    RTL8139_VIRTIO = 'rtl8139_virtio'
    SPAPR_VLAN = 'spapr_vlan'
    VIRTIO = 'virtio'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NicStatus(Enum):
    DOWN = 'down'
    UP = 'up'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NotifiableEvent(Enum):
    CLUSTER_ALERT_HA_RESERVATION = 'cluster_alert_ha_reservation'
    CLUSTER_ALERT_HA_RESERVATION_DOWN = 'cluster_alert_ha_reservation_down'
    DWH_ERROR = 'dwh_error'
    DWH_STOPPED = 'dwh_stopped'
    ENGINE_BACKUP_COMPLETED = 'engine_backup_completed'
    ENGINE_BACKUP_FAILED = 'engine_backup_failed'
    ENGINE_BACKUP_STARTED = 'engine_backup_started'
    ENGINE_CA_CERTIFICATION_HAS_EXPIRED = 'engine_ca_certification_has_expired'
    ENGINE_CA_CERTIFICATION_IS_ABOUT_TO_EXPIRE = 'engine_ca_certification_is_about_to_expire'
    ENGINE_CERTIFICATION_HAS_EXPIRED = 'engine_certification_has_expired'
    ENGINE_CERTIFICATION_IS_ABOUT_TO_EXPIRE = 'engine_certification_is_about_to_expire'
    ENGINE_STOP = 'engine_stop'
    FAULTY_MULTIPATHS_ON_HOST = 'faulty_multipaths_on_host'
    GLUSTER_BRICK_STATUS_CHANGED = 'gluster_brick_status_changed'
    GLUSTER_HOOK_ADD_FAILED = 'gluster_hook_add_failed'
    GLUSTER_HOOK_ADDED = 'gluster_hook_added'
    GLUSTER_HOOK_CONFLICT_DETECTED = 'gluster_hook_conflict_detected'
    GLUSTER_HOOK_DETECTED_DELETE = 'gluster_hook_detected_delete'
    GLUSTER_HOOK_DETECTED_NEW = 'gluster_hook_detected_new'
    GLUSTER_HOOK_DISABLE = 'gluster_hook_disable'
    GLUSTER_HOOK_DISABLE_FAILED = 'gluster_hook_disable_failed'
    GLUSTER_HOOK_ENABLE = 'gluster_hook_enable'
    GLUSTER_HOOK_ENABLE_FAILED = 'gluster_hook_enable_failed'
    GLUSTER_HOOK_REMOVE_FAILED = 'gluster_hook_remove_failed'
    GLUSTER_HOOK_REMOVED = 'gluster_hook_removed'
    GLUSTER_SERVER_ADD_FAILED = 'gluster_server_add_failed'
    GLUSTER_SERVER_REMOVE = 'gluster_server_remove'
    GLUSTER_SERVER_REMOVE_FAILED = 'gluster_server_remove_failed'
    GLUSTER_SERVICE_RESTART_FAILED = 'gluster_service_restart_failed'
    GLUSTER_SERVICE_RESTARTED = 'gluster_service_restarted'
    GLUSTER_SERVICE_START_FAILED = 'gluster_service_start_failed'
    GLUSTER_SERVICE_STARTED = 'gluster_service_started'
    GLUSTER_SERVICE_STOP_FAILED = 'gluster_service_stop_failed'
    GLUSTER_SERVICE_STOPPED = 'gluster_service_stopped'
    GLUSTER_VOLUME_ADD_BRICK = 'gluster_volume_add_brick'
    GLUSTER_VOLUME_ADD_BRICK_FAILED = 'gluster_volume_add_brick_failed'
    GLUSTER_VOLUME_ALL_SNAPSHOTS_DELETE_FAILED = 'gluster_volume_all_snapshots_delete_failed'
    GLUSTER_VOLUME_ALL_SNAPSHOTS_DELETED = 'gluster_volume_all_snapshots_deleted'
    GLUSTER_VOLUME_BRICK_REPLACED = 'gluster_volume_brick_replaced'
    GLUSTER_VOLUME_CONFIRMED_SPACE_LOW = 'gluster_volume_confirmed_space_low'
    GLUSTER_VOLUME_CREATE = 'gluster_volume_create'
    GLUSTER_VOLUME_CREATE_FAILED = 'gluster_volume_create_failed'
    GLUSTER_VOLUME_DELETE = 'gluster_volume_delete'
    GLUSTER_VOLUME_DELETE_FAILED = 'gluster_volume_delete_failed'
    GLUSTER_VOLUME_MIGRATE_BRICK_DATA_FINISHED = 'gluster_volume_migrate_brick_data_finished'
    GLUSTER_VOLUME_OPTION_ADDED = 'gluster_volume_option_added'
    GLUSTER_VOLUME_OPTION_MODIFIED = 'gluster_volume_option_modified'
    GLUSTER_VOLUME_OPTION_SET_FAILED = 'gluster_volume_option_set_failed'
    GLUSTER_VOLUME_OPTIONS_RESET = 'gluster_volume_options_reset'
    GLUSTER_VOLUME_OPTIONS_RESET_ALL = 'gluster_volume_options_reset_all'
    GLUSTER_VOLUME_OPTIONS_RESET_FAILED = 'gluster_volume_options_reset_failed'
    GLUSTER_VOLUME_PROFILE_START = 'gluster_volume_profile_start'
    GLUSTER_VOLUME_PROFILE_START_FAILED = 'gluster_volume_profile_start_failed'
    GLUSTER_VOLUME_PROFILE_STOP = 'gluster_volume_profile_stop'
    GLUSTER_VOLUME_PROFILE_STOP_FAILED = 'gluster_volume_profile_stop_failed'
    GLUSTER_VOLUME_REBALANCE_FINISHED = 'gluster_volume_rebalance_finished'
    GLUSTER_VOLUME_REBALANCE_NOT_FOUND_FROM_CLI = 'gluster_volume_rebalance_not_found_from_cli'
    GLUSTER_VOLUME_REBALANCE_START = 'gluster_volume_rebalance_start'
    GLUSTER_VOLUME_REBALANCE_START_DETECTED_FROM_CLI = 'gluster_volume_rebalance_start_detected_from_cli'
    GLUSTER_VOLUME_REBALANCE_START_FAILED = 'gluster_volume_rebalance_start_failed'
    GLUSTER_VOLUME_REBALANCE_STOP = 'gluster_volume_rebalance_stop'
    GLUSTER_VOLUME_REBALANCE_STOP_FAILED = 'gluster_volume_rebalance_stop_failed'
    GLUSTER_VOLUME_REMOVE_BRICKS = 'gluster_volume_remove_bricks'
    GLUSTER_VOLUME_REMOVE_BRICKS_FAILED = 'gluster_volume_remove_bricks_failed'
    GLUSTER_VOLUME_REMOVE_BRICKS_STOP = 'gluster_volume_remove_bricks_stop'
    GLUSTER_VOLUME_REMOVE_BRICKS_STOP_FAILED = 'gluster_volume_remove_bricks_stop_failed'
    GLUSTER_VOLUME_REPLACE_BRICK_FAILED = 'gluster_volume_replace_brick_failed'
    GLUSTER_VOLUME_REPLACE_BRICK_START = 'gluster_volume_replace_brick_start'
    GLUSTER_VOLUME_REPLACE_BRICK_START_FAILED = 'gluster_volume_replace_brick_start_failed'
    GLUSTER_VOLUME_SNAPSHOT_ACTIVATE_FAILED = 'gluster_volume_snapshot_activate_failed'
    GLUSTER_VOLUME_SNAPSHOT_ACTIVATED = 'gluster_volume_snapshot_activated'
    GLUSTER_VOLUME_SNAPSHOT_CREATE_FAILED = 'gluster_volume_snapshot_create_failed'
    GLUSTER_VOLUME_SNAPSHOT_CREATED = 'gluster_volume_snapshot_created'
    GLUSTER_VOLUME_SNAPSHOT_DEACTIVATE_FAILED = 'gluster_volume_snapshot_deactivate_failed'
    GLUSTER_VOLUME_SNAPSHOT_DEACTIVATED = 'gluster_volume_snapshot_deactivated'
    GLUSTER_VOLUME_SNAPSHOT_DELETE_FAILED = 'gluster_volume_snapshot_delete_failed'
    GLUSTER_VOLUME_SNAPSHOT_DELETED = 'gluster_volume_snapshot_deleted'
    GLUSTER_VOLUME_SNAPSHOT_RESTORE_FAILED = 'gluster_volume_snapshot_restore_failed'
    GLUSTER_VOLUME_SNAPSHOT_RESTORED = 'gluster_volume_snapshot_restored'
    GLUSTER_VOLUME_START = 'gluster_volume_start'
    GLUSTER_VOLUME_START_FAILED = 'gluster_volume_start_failed'
    GLUSTER_VOLUME_STOP = 'gluster_volume_stop'
    GLUSTER_VOLUME_STOP_FAILED = 'gluster_volume_stop_failed'
    HA_VM_FAILED = 'ha_vm_failed'
    HA_VM_RESTART_FAILED = 'ha_vm_restart_failed'
    HOST_ACTIVATE_FAILED = 'host_activate_failed'
    HOST_ACTIVATE_MANUAL_HA = 'host_activate_manual_ha'
    HOST_APPROVE_FAILED = 'host_approve_failed'
    HOST_BOND_SLAVE_STATE_DOWN = 'host_bond_slave_state_down'
    HOST_CERTIFICATE_HAS_INVALID_SAN = 'host_certificate_has_invalid_san'
    HOST_CERTIFICATION_HAS_EXPIRED = 'host_certification_has_expired'
    HOST_CERTIFICATION_IS_ABOUT_TO_EXPIRE = 'host_certification_is_about_to_expire'
    HOST_FAILURE = 'host_failure'
    HOST_HIGH_CPU_USE = 'host_high_cpu_use'
    HOST_HIGH_MEM_USE = 'host_high_mem_use'
    HOST_HIGH_SWAP_USE = 'host_high_swap_use'
    HOST_INITIATED_RUN_VM_FAILED = 'host_initiated_run_vm_failed'
    HOST_INSTALL_FAILED = 'host_install_failed'
    HOST_INTERFACE_HIGH_NETWORK_USE = 'host_interface_high_network_use'
    HOST_INTERFACE_STATE_DOWN = 'host_interface_state_down'
    HOST_LOW_MEM = 'host_low_mem'
    HOST_LOW_SWAP = 'host_low_swap'
    HOST_RECOVER_FAILED = 'host_recover_failed'
    HOST_SET_NONOPERATIONAL = 'host_set_nonoperational'
    HOST_SET_NONOPERATIONAL_DOMAIN = 'host_set_nonoperational_domain'
    HOST_SET_NONOPERATIONAL_IFACE_DOWN = 'host_set_nonoperational_iface_down'
    HOST_SLOW_STORAGE_RESPONSE_TIME = 'host_slow_storage_response_time'
    HOST_TIME_DRIFT_ALERT = 'host_time_drift_alert'
    HOST_UNTRUSTED = 'host_untrusted'
    HOST_UPDATES_ARE_AVAILABLE = 'host_updates_are_available'
    HOST_UPDATES_ARE_AVAILABLE_WITH_PACKAGES = 'host_updates_are_available_with_packages'
    IMPORTEXPORT_IMPORT_TEMPLATE_FROM_TRUSTED_TO_UNTRUSTED = 'importexport_import_template_from_trusted_to_untrusted'
    IMPORTEXPORT_IMPORT_TEMPLATE_FROM_UNTRUSTED_TO_TRUSTED = 'importexport_import_template_from_untrusted_to_trusted'
    IMPORTEXPORT_IMPORT_VM_FROM_TRUSTED_TO_UNTRUSTED = 'importexport_import_vm_from_trusted_to_untrusted'
    IMPORTEXPORT_IMPORT_VM_FROM_UNTRUSTED_TO_TRUSTED = 'importexport_import_vm_from_untrusted_to_trusted'
    IRS_CONFIRMED_DISK_SPACE_LOW = 'irs_confirmed_disk_space_low'
    IRS_DISK_SPACE_LOW = 'irs_disk_space_low'
    IRS_DISK_SPACE_LOW_ERROR = 'irs_disk_space_low_error'
    IRS_FAILURE = 'irs_failure'
    MAC_ADDRESS_IS_EXTERNAL = 'mac_address_is_external'
    MULTIPATH_DEVICES_WITHOUT_VALID_PATHS_ON_HOST = 'multipath_devices_without_valid_paths_on_host'
    NETWORK_UPDATE_DISPLAY_FOR_CLUSTER_WITH_ACTIVE_VM = 'network_update_display_for_cluster_with_active_vm'
    NETWORK_UPDATE_DISPLAY_FOR_HOST_WITH_ACTIVE_VM = 'network_update_display_for_host_with_active_vm'
    NO_FAULTY_MULTIPATHS_ON_HOST = 'no_faulty_multipaths_on_host'
    NUMBER_OF_LVS_ON_STORAGE_DOMAIN_EXCEEDED_THRESHOLD = 'number_of_lvs_on_storage_domain_exceeded_threshold'
    REMOVE_GLUSTER_VOLUME_BRICKS_NOT_FOUND_FROM_CLI = 'remove_gluster_volume_bricks_not_found_from_cli'
    START_REMOVING_GLUSTER_VOLUME_BRICKS = 'start_removing_gluster_volume_bricks'
    START_REMOVING_GLUSTER_VOLUME_BRICKS_DETECTED_FROM_CLI = 'start_removing_gluster_volume_bricks_detected_from_cli'
    START_REMOVING_GLUSTER_VOLUME_BRICKS_FAILED = 'start_removing_gluster_volume_bricks_failed'
    SYSTEM_CHANGE_STORAGE_POOL_STATUS_NO_HOST_FOR_SPM = 'system_change_storage_pool_status_no_host_for_spm'
    SYSTEM_DEACTIVATED_STORAGE_DOMAIN = 'system_deactivated_storage_domain'
    USER_ADD_VM_FROM_TRUSTED_TO_UNTRUSTED = 'user_add_vm_from_trusted_to_untrusted'
    USER_ADD_VM_FROM_UNTRUSTED_TO_TRUSTED = 'user_add_vm_from_untrusted_to_trusted'
    USER_ADD_VM_TEMPLATE_FROM_TRUSTED_TO_UNTRUSTED = 'user_add_vm_template_from_trusted_to_untrusted'
    USER_ADD_VM_TEMPLATE_FROM_UNTRUSTED_TO_TRUSTED = 'user_add_vm_template_from_untrusted_to_trusted'
    USER_HOST_MAINTENANCE = 'user_host_maintenance'
    USER_HOST_MAINTENANCE_MANUAL_HA = 'user_host_maintenance_manual_ha'
    USER_HOST_MAINTENANCE_MIGRATION_FAILED = 'user_host_maintenance_migration_failed'
    USER_UPDATE_VM_FROM_TRUSTED_TO_UNTRUSTED = 'user_update_vm_from_trusted_to_untrusted'
    USER_UPDATE_VM_FROM_UNTRUSTED_TO_TRUSTED = 'user_update_vm_from_untrusted_to_trusted'
    USER_UPDATE_VM_TEMPLATE_FROM_TRUSTED_TO_UNTRUSTED = 'user_update_vm_template_from_trusted_to_untrusted'
    USER_UPDATE_VM_TEMPLATE_FROM_UNTRUSTED_TO_TRUSTED = 'user_update_vm_template_from_untrusted_to_trusted'
    VM_CONSOLE_CONNECTED = 'vm_console_connected'
    VM_CONSOLE_DISCONNECTED = 'vm_console_disconnected'
    VM_DOWN_ERROR = 'vm_down_error'
    VM_FAILURE = 'vm_failure'
    VM_MIGRATION_FAILED = 'vm_migration_failed'
    VM_MIGRATION_START = 'vm_migration_start'
    VM_MIGRATION_TO_SERVER_FAILED = 'vm_migration_to_server_failed'
    VM_NOT_RESPONDING = 'vm_not_responding'
    VM_PAUSED = 'vm_paused'
    VM_PAUSED_EIO = 'vm_paused_eio'
    VM_PAUSED_ENOSPC = 'vm_paused_enospc'
    VM_PAUSED_EPERM = 'vm_paused_eperm'
    VM_PAUSED_ERROR = 'vm_paused_error'
    VM_RECOVERED_FROM_PAUSE_ERROR = 'vm_recovered_from_pause_error'
    VM_SET_TICKET = 'vm_set_ticket'
    VM_STATUS_RESTORED = 'vm_status_restored'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NotificationMethod(Enum):
    SMTP = 'smtp'
    SNMP = 'snmp'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class NumaTuneMode(Enum):
    INTERLEAVE = 'interleave'
    PREFERRED = 'preferred'
    STRICT = 'strict'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class OpenStackNetworkProviderType(Enum):
    EXTERNAL = 'external'
    NEUTRON = 'neutron'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class OpenstackVolumeAuthenticationKeyUsageType(Enum):
    CEPH = 'ceph'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class OsType(Enum):
    OTHER = 'other'
    OTHER_LINUX = 'other_linux'
    RHEL_3 = 'rhel_3'
    RHEL_3X64 = 'rhel_3x64'
    RHEL_4 = 'rhel_4'
    RHEL_4X64 = 'rhel_4x64'
    RHEL_5 = 'rhel_5'
    RHEL_5X64 = 'rhel_5x64'
    RHEL_6 = 'rhel_6'
    RHEL_6X64 = 'rhel_6x64'
    UNASSIGNED = 'unassigned'
    WINDOWS_2003 = 'windows_2003'
    WINDOWS_2003X64 = 'windows_2003x64'
    WINDOWS_2008 = 'windows_2008'
    WINDOWS_2008R2X64 = 'windows_2008r2x64'
    WINDOWS_2008X64 = 'windows_2008x64'
    WINDOWS_2012X64 = 'windows_2012x64'
    WINDOWS_7 = 'windows_7'
    WINDOWS_7X64 = 'windows_7x64'
    WINDOWS_8 = 'windows_8'
    WINDOWS_8X64 = 'windows_8x64'
    WINDOWS_XP = 'windows_xp'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class PayloadEncoding(Enum):
    BASE64 = 'base64'
    PLAINTEXT = 'plaintext'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class PmProxyType(Enum):
    CLUSTER = 'cluster'
    DC = 'dc'
    OTHER_DC = 'other_dc'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class PolicyUnitType(Enum):
    FILTER = 'filter'
    LOAD_BALANCING = 'load_balancing'
    WEIGHT = 'weight'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class PowerManagementStatus(Enum):
    OFF = 'off'
    ON = 'on'
    UNKNOWN = 'unknown'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class QcowVersion(Enum):
    QCOW2_V2 = 'qcow2_v2'
    QCOW2_V3 = 'qcow2_v3'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class QosType(Enum):
    CPU = 'cpu'
    HOSTNETWORK = 'hostnetwork'
    NETWORK = 'network'
    STORAGE = 'storage'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class QuotaModeType(Enum):
    AUDIT = 'audit'
    DISABLED = 'disabled'
    ENABLED = 'enabled'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ReportedDeviceType(Enum):
    NETWORK = 'network'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ResolutionType(Enum):
    ADD = 'add'
    COPY = 'copy'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class RngSource(Enum):
    HWRNG = 'hwrng'
    RANDOM = 'random'
    URANDOM = 'urandom'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class RoleType(Enum):
    ADMIN = 'admin'
    USER = 'user'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ScsiGenericIO(Enum):
    DISABLED = 'disabled'
    FILTERED = 'filtered'
    UNFILTERED = 'unfiltered'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class SeLinuxMode(Enum):
    DISABLED = 'disabled'
    ENFORCING = 'enforcing'
    PERMISSIVE = 'permissive'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class SerialNumberPolicy(Enum):
    CUSTOM = 'custom'
    HOST = 'host'
    NONE = 'none'
    VM = 'vm'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class SnapshotStatus(Enum):
    IN_PREVIEW = 'in_preview'
    LOCKED = 'locked'
    OK = 'ok'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class SnapshotType(Enum):
    ACTIVE = 'active'
    PREVIEW = 'preview'
    REGULAR = 'regular'
    STATELESS = 'stateless'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class SpmStatus(Enum):
    CONTENDING = 'contending'
    NONE = 'none'
    SPM = 'spm'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class SshAuthenticationMethod(Enum):
    PASSWORD = 'password'
    PUBLICKEY = 'publickey'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class SsoMethod(Enum):
    GUEST_AGENT = 'guest_agent'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class StatisticKind(Enum):
    COUNTER = 'counter'
    GAUGE = 'gauge'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class StatisticUnit(Enum):
    BITS_PER_SECOND = 'bits_per_second'
    BYTES = 'bytes'
    BYTES_PER_SECOND = 'bytes_per_second'
    COUNT_PER_SECOND = 'count_per_second'
    NONE = 'none'
    PERCENT = 'percent'
    SECONDS = 'seconds'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class StepEnum(Enum):
    EXECUTING = 'executing'
    FINALIZING = 'finalizing'
    REBALANCING_VOLUME = 'rebalancing_volume'
    REMOVING_BRICKS = 'removing_bricks'
    UNKNOWN = 'unknown'
    VALIDATING = 'validating'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class StepStatus(Enum):
    ABORTED = 'aborted'
    FAILED = 'failed'
    FINISHED = 'finished'
    STARTED = 'started'
    UNKNOWN = 'unknown'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class StorageDomainStatus(Enum):
    ACTIVATING = 'activating'
    ACTIVE = 'active'
    DETACHING = 'detaching'
    INACTIVE = 'inactive'
    LOCKED = 'locked'
    MAINTENANCE = 'maintenance'
    MIXED = 'mixed'
    PREPARING_FOR_MAINTENANCE = 'preparing_for_maintenance'
    UNATTACHED = 'unattached'
    UNKNOWN = 'unknown'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class StorageDomainType(Enum):
    DATA = 'data'
    EXPORT = 'export'
    IMAGE = 'image'
    ISO = 'iso'
    MANAGED_BLOCK_STORAGE = 'managed_block_storage'
    VOLUME = 'volume'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class StorageFormat(Enum):
    V1 = 'v1'
    V2 = 'v2'
    V3 = 'v3'
    V4 = 'v4'
    V5 = 'v5'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class StorageType(Enum):
    CINDER = 'cinder'
    FCP = 'fcp'
    GLANCE = 'glance'
    GLUSTERFS = 'glusterfs'
    ISCSI = 'iscsi'
    LOCALFS = 'localfs'
    MANAGED_BLOCK_STORAGE = 'managed_block_storage'
    NFS = 'nfs'
    POSIXFS = 'posixfs'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class SwitchType(Enum):
    LEGACY = 'legacy'
    OVS = 'ovs'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class TemplateStatus(Enum):
    ILLEGAL = 'illegal'
    LOCKED = 'locked'
    OK = 'ok'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class TransportType(Enum):
    RDMA = 'rdma'
    TCP = 'tcp'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class UsbType(Enum):
    LEGACY = 'legacy'
    NATIVE = 'native'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class ValueType(Enum):
    DECIMAL = 'decimal'
    INTEGER = 'integer'
    STRING = 'string'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class VgpuPlacement(Enum):
    CONSOLIDATED = 'consolidated'
    SEPARATED = 'separated'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class VmAffinity(Enum):
    MIGRATABLE = 'migratable'
    PINNED = 'pinned'
    USER_MIGRATABLE = 'user_migratable'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class VmDeviceType(Enum):
    CDROM = 'cdrom'
    FLOPPY = 'floppy'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class VmPoolType(Enum):
    AUTOMATIC = 'automatic'
    MANUAL = 'manual'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class VmStatus(Enum):
    DOWN = 'down'
    IMAGE_LOCKED = 'image_locked'
    MIGRATING = 'migrating'
    NOT_RESPONDING = 'not_responding'
    PAUSED = 'paused'
    POWERING_DOWN = 'powering_down'
    POWERING_UP = 'powering_up'
    REBOOT_IN_PROGRESS = 'reboot_in_progress'
    RESTORING_STATE = 'restoring_state'
    SAVING_STATE = 'saving_state'
    SUSPENDED = 'suspended'
    UNASSIGNED = 'unassigned'
    UNKNOWN = 'unknown'
    UP = 'up'
    WAIT_FOR_LAUNCH = 'wait_for_launch'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class VmStorageErrorResumeBehaviour(Enum):
    AUTO_RESUME = 'auto_resume'
    KILL = 'kill'
    LEAVE_PAUSED = 'leave_paused'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class VmType(Enum):
    DESKTOP = 'desktop'
    HIGH_PERFORMANCE = 'high_performance'
    SERVER = 'server'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class VnicPassThroughMode(Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class WatchdogAction(Enum):
    DUMP = 'dump'
    NONE = 'none'
    PAUSE = 'pause'
    POWEROFF = 'poweroff'
    RESET = 'reset'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image


@unique
class WatchdogModel(Enum):
    DIAG288 = 'diag288'
    I6300ESB = 'i6300esb'

    def __init__(self, image):
        self._image = image

    def __str__(self):
        return self._image
