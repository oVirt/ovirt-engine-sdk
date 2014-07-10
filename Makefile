all: rpm

rpmrelease:=0.1
rpmversion=3.4.3.1
RPMTOP=$(shell bash -c "pwd -P")/rpmtop
SPEC=ovirt-engine-sdk-python.spec

TARBALL=ovirt-engine-sdk-python-$(rpmversion).tar.gz
SRPM=$(RPMTOP)/SRPMS/ovirt-engine-sdk-python-$(rpmversion)-$(rpmrelease)*.src.rpm

TESTS=pyflakes

test: pyflakes exceptions
	echo $(rpmrelease) $(rpmversion)

pyflakes:
	@git ls-files '*.py' | xargs pyflakes \
	    || (echo "Pyflakes errors or pyflakes not found"; exit 1)

.PHONY: tarball
tarball: $(TARBALL)
$(TARBALL): Makefile #$(TESTS)
	git archive --format=tar --prefix ovirt-engine-sdk-python/ HEAD | gzip > $(TARBALL)

.PHONY: srpm rpm
srpm: $(SRPM)
$(SRPM): $(TARBALL) ovirt-engine-sdk-python.spec.in
	sed 's/^Version:.*/Version: $(rpmversion)/;s/^Release:.*/Release: $(rpmrelease)%{dist}/;s/%{release}/$(rpmrelease)/' ovirt-engine-sdk-python.spec.in > $(SPEC)
	mkdir -p $(RPMTOP)/{RPMS,SRPMS,SOURCES,BUILD}
	rpmbuild -bs \
	    --define="_topdir $(RPMTOP)" \
	    --define="_sourcedir ." $(SPEC)

rpm: $(SRPM)
	rpmbuild --define="_topdir $(RPMTOP)" --rebuild $<

clean:
	$(RM) *~ *.pyc ovirt-engine-sdk*.tar.gz $(SPEC)
	$(RM) -r rpmtop
