#!/bin/bash -ex

# Name and version of the package:
tar_version="${tar_version:=4.0.0a4}"
tar_url="${tar_url:=https://pypi.python.org/packages/source/o/ovirt-engine-sdk-python/ovirt-engine-sdk-python-${tar_version}.tar.gz}"
rpm_version="${rpm_version:=4.0.0}"
rpm_dist="${rpm_dist:=$(rpm --eval '%dist')}"
rpm_release="${rpm_release:=0.4.a4${rpm_dist}}"

# Generate the .spec file from the template for the distribution where the
# build process is running:
spec_template="spec${rpm_dist}.in"
spec_file="ovirt-engine-sdk-python.spec"
sed \
  -e "s|@TAR_VERSION@|${tar_version}|g" \
  -e "s|@TAR_URL@|${tar_url}|g" \
  -e "s|@RPM_VERSION@|${rpm_version}|g" \
  -e "s|@RPM_RELEASE@|${rpm_release}|g" \
  < "${spec_template}" \
  > "${spec_file}" \

# Download the sources:
spectool \
  --get-files \
  "${spec_file}"

# Build the source and binary .rpm files:
rpmbuild \
  -bb \
  --define="_sourcedir ${PWD}" \
  --define="_rpmdir ${PWD}" \
  "${spec_file}"
