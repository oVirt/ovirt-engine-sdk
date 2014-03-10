oVirt Python SDK
================

Introduction
------------

The oVirt Python SDK is a Python library that simplfies access to the oVirt
Engine REST API.

Examples
--------

There are examples of how to use the SDK with a Python IDE available
[here](http://www.ovirt.org/wiki/SDK#IDE_Examples).

Generating
----------

Most of the source code of the Python SDK is automatically generated from the
metadata provided by the oVirt Engine. The code generator is a Java program
that resides in the `generator` directory. In order to run it you will need
first to build it, using Maven:

    $ cd generator
    $ mvn clean install

Then you will need to place the files containing the XML schema of entities and
the RSDL in the `src/main/resources` directory. This can be done manually, but
it is better to download them from a live engine, running the following
command:

    $ mvn validate -Pupdate-metadata \
    -Dapi.url="https://localhost/ovirt-engine/api" \
    -Dapi.user="admin@internal" \
    -Dapi.password="letmein!"

This will use the `wget` command to download the files, so make sure that you
have it installed.

The `api.url`, `api.user` and `api.password` properties are optional, and their
default values are as in the above example. If you are going to use this
frequently it may be convenient to put them in your `~/.m2/settins.xml` file,
something like this:

    <settings
      xmlns="http://maven.apache.org/POM/4.0.0"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">

      <activeProfiles>
        <activeProfile>api</activeProfile>
      </activeProfiles>

      <profiles>
        <profile>
          <id>api</id>
          <properties>
            <api.url>https://localhost/ovirt-engine/api</api.url>
            <api.user>admin@internal</api.user>
            <api.password>mypass</api.password>
          </properties>
        </profile>
      </profiles>

    </settings>

If you do this then to download the files just run this:

    $ mvn validate -Pupdate-metadata

With the metadata files in place you can update the generate source code as
follows:

    $ mvn validate -Pupdate-code

After doing this make sure to inspect the generated source code (running `git
diff`, for example) to make sure that no backwards compatibility breaking
changes are introduced.

Once you have inspected the code, and if everything looks correct, commit the
modified metadata and source files. The commit message for this change should
include a reference to the commit or tag of the engine that was used to
download the updated metadata. For example:

    sdk: Regenerate agains the latest API
    
    This patch regenerates the SDK using the latest API obtained from
    the engine built from commit fffffff, corresponding to tag
    ovirt-engine-3.5.7.

Releasing
---------

In order to do a new release the first thing to do is to decide what will be
the release number. Curently the release numbers of the Python SDK have for
numbers, separated by dots. The first three numbers correspond to the version
of the engine that was used in the last generation. So if last generation was
for engine 3.5.7 then the version number should be 3.5.7.`x`. The value of `x`
is increased for each release, and reset to 0 when the other three numbers
change.

Once the next release number is decided the `Makefile` *may* need to be changed
to reflect that number and also change the RPM release number to `1`.

The `setup.py` file *may* also need to be changed, as it also contains the
version number.

The `%changelog` in the `ovirt-engine-sdk-python.spec.in` should be updated so
that it contains short descriptions of bugs fixed and relevant changes.

Look at commit 7a05754 (with command, `git show 7a05754`) for a typical release
commit.

Don't forget to create tag the release commit, and push it to the upstream repository:

    $ git commit -a -m "Release 3.5.7.0" 3.5.7.0
    $ git push origin 3.5.7.0 HEAD:refs/heads/sdk_3.5

To finish the release you need to do an additional change that prepares for the
next development iteration, basically setting the version number to the next
expected one in the `Makefile` and in `setup.py`. Commit ff49af0 is a good
example. Note that this change will usually contain the correct next version
number, so usually there is no need to change it when doing next release.

Uploading
---------

After performing the release process in the repository you will need to upload
the new version of the package to the [Python Package
Index](https://pypi.python.org/pypi):

    $ git branch -D tmp
    $ git checkout -b tmp 3.5.7.0
    $ git clean -dfx
    $ python setup.py sdist upload

Note that doing this requires package index maintainer permissions.

Verify that the new version of the package is available
[here](https://pypi.python.org/pypi/ovirt-engine-sdk-python).

Packaging
---------

To create the RPM packages just run `make rpm`:

    $ git branch -D tmp
    $ git checkout -b tmp 3.5.7.0
    $ git clean -dfx
    $ make rpm

The generated `.rpm` file will be available in the `rpmtop/RPMS/noarch`
directory.
