#!/bin/sh -ex

# Clean and then create the artifacts directory:
rm -rf exported-artifacts
mkdir -p exported-artifacts

# Create a settings file that uses the our artifactory server as proxy
# for all repositories:
settings="$(pwd)/settings.xml"
cat > "${settings}" <<.
<settings>
  <mirrors>

    <mirror>
      <id>ovirt-artifactory</id>
      <url>http://artifactory.ovirt.org/artifactory/ovirt-mirror</url>
      <mirrorOf>*</mirrorOf>
    </mirror>

    <mirror>
      <id>maven-central</id>
      <url>http://repo.maven.apache.org/maven2</url>
      <mirrorOf>*</mirrorOf>
    </mirror>

  </mirrors>
</settings>
.

# There may be several versions of Java installed in the build enviroment, and
# we need to make sure that Java 8 is used, as it is required by the code
# generator:
export JAVA_HOME="$(dirname $(rpm -ql java-1.8.0-openjdk-devel | grep '/bin$'))"

# Calculate the version number:
version="$(python sdk/lib/ovirtsdk4/version.py)"

# Build and run the tests using Python 2 and 3, if they are available:
for python_command in python2 python3
do
  if which "${python_command}" 2> /dev/null
  then
    mvn package -s "${settings}" -Dpython.command="${python_command}"
  fi
done

# Find the generated .tar.gz file:
tar_file="${PWD}/sdk/dist/ovirt-engine-sdk-python-${version}.tar.gz"

# Build the RPM:
date="$(date --utc +%Y%m%d)"
commit="$(git log -1 --pretty=format:%h)"
#suffix="1.${date}git${commit}"
suffix="1"
cp "${tar_file}" packaging/.
pushd packaging
  export tar_version="${version}"
  export tar_url="$(basename ${tar_file})"
  export rpm_dist="$(rpm --eval '%dist')"
  export rpm_release="${suffix}${rpm_dist}"
  ./build.sh
popd

# Copy the distributions and the RPM files to the exported artifacts
# directory:
for file in $(find sdk/dist -type f) $(find packaging -type f -name '*.rpm'); do
  echo "Archiving file \"$file\"."
  mv "$file" exported-artifacts
done
