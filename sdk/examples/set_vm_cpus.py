#!/usr/bin/env python3
# Copyright (c) 2020 The Center for Biomolecular NMR Data Processing and Analysis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
import configparser
import logging

import ovirtsdk4 as sdk
from ovirtsdk4 import types

TESTVM = 'sdkclone2'
NUM_CPUS = 10

logging.basicConfig(level=logging.DEBUG, filename="example.log")
logger = logging.getLogger('set cpus')

# get connection info from config
config = configparser.ConfigParser()
with open('ovirt.conf') as f:
    config.read_file(f)
engine_cfg = config['engine1']
url = engine_cfg['engine_url']
username = engine_cfg['username']
certfile = engine_cfg['cafile']
insecure = engine_cfg['secure'] != 'yes'
password = engine_cfg['password']

# get connection. Note password is written to log file
connection = sdk.Connection(url=url,
                            username=username,
                            password=password,
                            ca_file=certfile,
                            insecure=insecure,
                            debug=True,
                            log=logger)
system_service = connection.system_service()
# find VM
vms_service = system_service.vms_service()
vms = vms_service.list()
vm = vms_service.list(search=f'name={TESTVM}')[0]

# create new CPU object
cpu = types.Cpu(topology=types.CpuTopology(cores=2, sockets=2))
# set two cores per socket if even number
if NUM_CPUS % 2 == 0:
    c = int(NUM_CPUS / 2)
    cpu.topology.cores = c
    cpu.topology.sockets = 2
else:  # just set one socket if odd
    cpu.topology.cores = NUM_CPUS
    cpu.topology.sockets = 1
# find service for this VM
service = vms_service.vm_service(vm.id)
# update just the cpu portion of the VM. This takes effect immediately if shutdown, or after reboot
# if VM is running
service.update(vm=sdk.types.Vm(cpu=cpu))
