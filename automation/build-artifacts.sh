#!/usr/bin/env sh

# cleanup
rm -Rf \
    exported-artifacts \
    rpmtop
mkdir exported-artifacts


git_head="$(git log -1 --pretty=format:%h)"
GIT_RELEASE="$(date --utc +%Y%m%d).git${git_head}"
make rpmsuffix=".${GIT_RELEASE}" srpm
yum-builddep ./ovirt-engine-sdk-python.spec
make rpmsuffix=".${GIT_RELEASE}" rpm

for file in $(find . -iregex ".*\.\(tar\.gz\|rpm\)$"); do
    echo "Archiving $file"
    mv "$file" exported-artifacts/
done
