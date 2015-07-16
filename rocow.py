#!/usr/bin/env python

# manages repos from https://github.com/rdo-puppet-modules
# Ivan Chavero <ichavero@redhat.com>


import os
import urllib
from github import Github
from optparse import OptionParser, OptionGroup, IndentedHelpFormatter


def get_org_repos(org_name):
    mygithub = Github()
    org = mygithub.get_organization(org_name)
    repos = org.get_repos()
    return repos

def list_repos(org_name):
    repos = get_org_repos(org_name)
    count = 0
    for repo in repos:
        url = "https://github.com/%s/%s/archive/%s-master-tag.tar.gz" % (org_name, repo.name, repo.name)
        print "Source%s: %s" % (count, url)
        count += 1

def download_org_repos(org_name):
    repos = get_org_repos(org_name)
    count = 0
    for repo in repos:
        url = "https://github.com/%s/%s/archive/master-tag.tar.gz" % (org_name, repo.name)
        spec_url = "https://github.com/%s/%s/archive/%s-master-tag.tar.gz" % (org_name, repo.name, repo.name)
        print "Source%s: %s" % (count, spec_url)
        print "Downloading: %s" % url
        download_repo(repo.name, "master-tag", url)
        count += 1

def download_repo(name, version, url):
    if not os.path.isdir("downloads"):
        os.mkdir("downloads")
    urllib.urlretrieve (url, "downloads/%s-%s.tar.gz" % (name, version))

def get_options():
    usage = "usage: %prog [options] [--help]"
    parser = OptionParser(usage=usage)
    parser.add_option("-r", "--repos", action="store_true",
        help="List modules formatted for spec file")
    parser.add_option("-d", "--download", action="store_true",
         help="Download Modules to a download directory in the local path")
    (options, args) = parser.parse_args()
    if not options:
        print "Missing option\n"
        parser.print_help()
        raise SystemExit
    return options


ORG = "rdo-puppet-modules"

options = get_options()

if options.repos:
    print "Listing repos for %s\n" % ORG
    list_repos(ORG)
if options.download:
    print "Download repos for %s\n" % ORG
    download_org_repos(ORG)

