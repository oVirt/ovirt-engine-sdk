all: rpm

rpmrelease:=1
rpmversion=1.2
RPMTOP=$(shell bash -c "pwd -P")/rpmtop
SPEC=ovirt-engine-sdk.spec

TARBALL=ovirt-engine-sdk-$(rpmversion).tar.gz
SRPM=$(RPMTOP)/SRPMS/ovirt-engine-sdk-$(rpmversion)-$(rpmrelease)*.src.rpm

TESTS=pyflakes

test: pyflakes exceptions
	echo $(rpmrelease) $(rpmversion)

pyflakes:
	@git ls-files '*.py' | xargs pyflakes \
	    || (echo "Pyflakes errors or pyflakes not found"; exit 1)

.PHONY: tarball
tarball: $(TARBALL)
$(TARBALL): Makefile #$(TESTS)
	git archive --format=tar --prefix ovirt-engine-sdk/ HEAD | gzip > $(TARBALL)

.PHONY: srpm rpm
srpm: $(SRPM)
$(SRPM): $(TARBALL) ovirt-engine-sdk.spec.in
	sed 's/^Version:.*/Version: $(rpmversion)/;s/^Release:.*/Release: $(rpmrelease)%{dist}/;s/%{release}/$(rpmrelease)/' ovirt-engine-sdk.spec.in > $(SPEC)
	mkdir -p $(RPMTOP)/{RPMS,SRPMS,SOURCES,BUILD}
	rpmbuild -bs \
	    --define="_topdir $(RPMTOP)" \
	    --define="_sourcedir ." $(SPEC)

rpm: $(SRPM)
	rpmbuild --define="_topdir $(RPMTOP)" --rebuild $<

clean:
	$(RM) *~ *.pyc ovirt-engine-sdk*.tar.gz $(SPEC)
	$(RM) -r rpmtop
