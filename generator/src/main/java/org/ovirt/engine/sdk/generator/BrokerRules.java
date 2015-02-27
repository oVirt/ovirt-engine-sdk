//
// Copyright (c) 2015 Red Hat, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

package org.ovirt.engine.sdk.generator;

import org.ovirt.engine.sdk.generator.utils.Tree;

import java.util.HashMap;
import java.util.Map;

import static java.util.stream.Collectors.joining;

/**
 * This class contains methods that implement various rules and calculations associated with broker class names, like
 * calculating the name of the broker class corresponding to a location.
 */
public class BrokerRules {
    /**
     * Calculate the name of the broker class that will be generated for the entity or collection represented by the
     * given location.
     *
     * @param tree the location whose broker name will be calculated
     * @return the name of the broker class, or {@code null} if it can't be determined
     */
    public static String getBrokerType(Tree<Location> tree) {
        // First we need to check if there is an exception for the given location:
        String path = tree.getPath().stream().skip(1).collect(joining("/"));
        String exception = BROKER_TYPE_EXCEPTIONS.get(path);
        if (exception != null) {
            return exception;
        }

        // The name of a broker type is calculated concatenating the types of all the parent entity resources (not the
        // collections, as they are redundant) and the name of the resource itself:
        return tree.getBranch().stream()
            .skip(1)
            .filter(x -> LocationRules.isEntity(x) || x == tree)
            .map(SchemaRules::getSchemaType)
            .collect(joining());
    }

    /**
     * These exceptions are needed for backwards compatibility, as the previous version of the generator used an
     * algorithm to calculate singulars from plurals and the other way around. This algorithm isn't used any longer, but
     * the resulting class names can't be changed.
     */
    private static final Map<String, String> BROKER_TYPE_EXCEPTIONS = new HashMap<>();

    static {
        // These exceptions are needed for backwards compatibility.
        BROKER_TYPE_EXCEPTIONS.put(
            "capabilities/{capabilitie:id}",
            "VersionCaps"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}",
            "ClusterGlusterVolumeGlusterBrick"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/statistics",
            "ClusterGlusterVolumeGlusterBrickStatistics"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/statistics/{statistic:id}",
            "ClusterGlusterVolumeGlusterBrickStatistic"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks",
            "ClusterGlusterVolumeGlusterBricks"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}",
            "DataCenterClusterGlusterVolumeGlusterBrick"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/statistics",
            "DataCenterClusterGlusterVolumeGlusterBrickStatistics"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/statistics/{statistic:id}",
            "DataCenterClusterGlusterVolumeGlusterBrickStatistic"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks",
            "DataCenterClusterGlusterVolumeGlusterBricks"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "hosts/{host:id}/nics",
            "HostNICs"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "hosts/{host:id}/nics/{nic:id}",
            "HostNIC"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "hosts/{host:id}/nics/{nic:id}/labels",
            "HostNICLabels"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "hosts/{host:id}/nics/{nic:id}/labels/{label:id}",
            "HostNICLabel"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "hosts/{host:id}/nics/{nic:id}/statistics",
            "HostNICStatistics"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "hosts/{host:id}/nics/{nic:id}/statistics/{statistic:id}",
            "HostNICStatistic"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "instancetypes/{instancetype:id}/nics",
            "InstanceTypeNICs"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "schedulingpolicies/{schedulingpolicie:id}/balances/{balance:id}",
            "SchedulingPolicyBalance"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "schedulingpolicies/{schedulingpolicie:id}/balances",
            "SchedulingPolicyBalances"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "schedulingpolicies/{schedulingpolicie:id}/filters/{filter:id}",
            "SchedulingPolicyFilter"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "schedulingpolicies/{schedulingpolicie:id}/filters",
            "SchedulingPolicyFilters"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "schedulingpolicies/{schedulingpolicie:id}",
            "SchedulingPolicy"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "schedulingpolicies/{schedulingpolicie:id}/weights",
            "SchedulingPolicyWeights"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "schedulingpolicies/{schedulingpolicie:id}/weights/{weight:id}",
            "SchedulingPolicyWeight"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "templates/{template:id}/nics",
            "TemplateNICs"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "vms/{vm:id}/nics",
            "VMNICs"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "vms/{vm:id}/numanodes/{numanode:id}",
            "VMVirtualNumaNode"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "vms/{vm:id}/numanodes",
            "VMVirtualNumaNodes"
        );

        // These exceptions are needed to handle the special case of host storage, as the name of the collection and
        // the name of the entity are the same, and both will result in the decorator name "HostStorage".
        BROKER_TYPE_EXCEPTIONS.put(
            "hosts/{host:id}/storage/{storage:id}",
            "HostStorage"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "hosts/{host:id}/storage",
            "HostStorages"
        );

        // These aren't really needed, as the names were introduced in 3.6, this no need to be backwards compatible,
        // will probably remove them soon.
        BROKER_TYPE_EXCEPTIONS.put(
            "operatingsystems/{operatingsystem:id}",
            "OperatingSystemInfo"
        );
        BROKER_TYPE_EXCEPTIONS.put(
            "operatingsystems",
            "OperatingSystemInfos"
        );
    }
}
