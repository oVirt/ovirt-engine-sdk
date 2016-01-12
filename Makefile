all: rpm

PWD=$(shell bash -c "pwd -P")
version=3.6.2.1
rpmversion=$(version)
rpmdist=$(shell rpm --eval '%dist')
rpmrelease=1$(rpmdist)

RPMTOP=$(PWD)/rpmtop
NAME=ovirt-engine-sdk-python
SPEC=$(NAME).spec

TARBALL=$(NAME)-$(version).tar.gz
SRPM=$(RPMTOP)/SRPMS/$(NAME)-$(rpmversion)-$(rpmrelease).src.rpm

.PHONY: spec
spec: $(SPEC).in
	sed \
		-e 's/@RPM_VERSION@/$(rpmversion)/g' \
		-e 's/@RPM_RELEASE@/$(rpmrelease)/g' \
		-e 's/@TARBALL@/$(TARBALL)/g' \
		< $(SPEC).in \
		> $(SPEC)

.PHONY: tarball
tarball: spec
	git ls-files | tar --transform='s|^|$(NAME)/|' --files-from /proc/self/fd/0 -czf $(TARBALL) $(SPEC)

.PHONY: srpm
srpm: tarball
	rpmbuild \
		--define="_topdir $(RPMTOP)" \
		-ts $(TARBALL)

.PHONY: rpm
rpm: srpm
	rpmbuild \
		--define="_topdir $(RPMTOP)" \
		--rebuild $(SRPM)

.PHONY: clean
clean:
	$(RM) $(NAME)*.tar.gz $(SPEC)
	$(RM) -r rpmtop
