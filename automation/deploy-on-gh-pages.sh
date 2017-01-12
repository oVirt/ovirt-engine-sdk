#!/usr/bin/env bash
#
# Should be executed only by Travis CI which has encrypted keys available.


set -xe

function _load_ssh_key {
    set +x  # hide keys
    openssl aes-256-cbc \
        -K $encrypted_1fc90f464345_key \
        -iv $encrypted_1fc90f464345_iv \
        -in automation/travis_rsa.enc \
        -out automation/travis_rsa \
        -d
    set -x
    eval "$(ssh-agent)"
    chmod 0600 automation/travis_rsa
    ssh-add automation/travis_rsa
}


function _init_git_config {
    git config --global user.email "ovirt-engine-sdk@travis-ci.org"
    git config --global user.name "oVirt Engine SDK Python"
}


function _clone_gh_pages {
    git clone git@github.com:oVirt/ovirt-engine-sdk.git gh-pages
}


function _checkout_gh_pages {
    pushd gh-pages
    git checkout origin/gh-pages -b gh-pages
    popd
}


function _copy_to_master {
    mkdir -p gh-pages/master
    cp -r target/generated-html/ovirtsdk4/* gh-pages/master/
}


function _copy_to_tagged {
    description=$(git describe)
    major_version=${description:0:3}
    full_version=${description:0:8}

    mkdir -p gh-pages/${major_version}/${full_version}
    cp -r target/generated-html/ovirtsdk4/* gh-pages/${major_version}/${full_version}
}


function _push_gh_pages {
    # Push only if there are changes in documentation:
    if ! git diff-index --quiet HEAD --
    then
      commit=$(git log --format="%H" -n 1)
      description=$(git describe)

      pushd gh-pages
      git add .
      git commit -m "gh-pages ${description} ${commit}"
      git push origin HEAD:gh-pages
      popd
    fi
}

_load_ssh_key
_init_git_config
_clone_gh_pages
_checkout_gh_pages
case "$1" in
    master)
        _copy_to_master
        ;;
    tagged)
        _copy_to_tagged
        ;;
esac
_push_gh_pages
