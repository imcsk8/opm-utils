Name:           openstack-puppet-modules
Version:        2015.2.1
Release:        1%{?dist}
Summary:        Collection of Puppet modules for OpenStack deployment
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/rdo-puppet-modules

Source0: https://github.com/rdo-puppet-modules/puppetlabs-apache/archive/puppetlabs-apache-master-tag.tar.gz
Source1: https://github.com/rdo-puppet-modules/puppet_aviator/archive/puppet_aviator-master-tag.tar.gz
Source2: https://github.com/rdo-puppet-modules/puppet-ceilometer/archive/puppet-ceilometer-master-tag.tar.gz
Source3: https://github.com/rdo-puppet-modules/puppet-ceph/archive/puppet-ceph-master-tag.tar.gz
Source4: https://github.com/rdo-puppet-modules/puppet-certmonger/archive/puppet-certmonger-master-tag.tar.gz
Source5: https://github.com/rdo-puppet-modules/puppet-cinder/archive/puppet-cinder-master-tag.tar.gz
Source6: https://github.com/rdo-puppet-modules/puppet-common/archive/puppet-common-master-tag.tar.gz
Source7: https://github.com/rdo-puppet-modules/puppetlabs-concat/archive/puppetlabs-concat-master-tag.tar.gz
Source8: https://github.com/rdo-puppet-modules/puppetlabs-corosync/archive/puppetlabs-corosync-master-tag.tar.gz
Source9: https://github.com/rdo-puppet-modules/puppetlabs-firewall/archive/puppetlabs-firewall-master-tag.tar.gz
Source10: https://github.com/rdo-puppet-modules/puppet-galera/archive/puppet-galera-master-tag.tar.gz
Source11: https://github.com/rdo-puppet-modules/puppet-glance/archive/puppet-glance-master-tag.tar.gz
Source12: https://github.com/rdo-puppet-modules/puppet-gluster/archive/puppet-gluster-master-tag.tar.gz
Source13: https://github.com/rdo-puppet-modules/puppetlabs-haproxy/archive/puppetlabs-haproxy-master-tag.tar.gz
Source14: https://github.com/rdo-puppet-modules/puppetlabs-inifile/archive/puppetlabs-inifile-master-tag.tar.gz
Source15: https://github.com/rdo-puppet-modules/puppet-module-keepalived/archive/puppet-module-keepalived-master-tag.tar.gz
Source16: https://github.com/rdo-puppet-modules/puppet-module-data/archive/puppet-module-data-master-tag.tar.gz
Source17: https://github.com/rdo-puppet-modules/puppetlabs-mongodb/archive/puppetlabs-mongodb-master-tag.tar.gz
Source18: https://github.com/rdo-puppet-modules/puppetlabs-mysql/archive/puppetlabs-mysql-master-tag.tar.gz
Source19: https://github.com/rdo-puppet-modules/puppet-n1k-vsm/archive/puppet-n1k-vsm-master-tag.tar.gz
Source20: https://github.com/rdo-puppet-modules/puppet-nagios-openstack/archive/puppet-nagios-openstack-master-tag.tar.gz
Source21: https://github.com/rdo-puppet-modules/puppet-neutron/archive/puppet-neutron-master-tag.tar.gz
Source22: https://github.com/rdo-puppet-modules/puppet-nova/archive/puppet-nova-master-tag.tar.gz
Source23: https://github.com/rdo-puppet-modules/puppet-nssdb/archive/puppet-nssdb-master-tag.tar.gz
Source24: https://github.com/rdo-puppet-modules/puppetlabs-ntp/archive/puppetlabs-ntp-master-tag.tar.gz
Source25: https://github.com/rdo-puppet-modules/puppet-openstack_extras/archive/puppet-openstack_extras-master-tag.tar.gz
Source26: https://github.com/rdo-puppet-modules/puppet-openstacklib/archive/puppet-openstacklib-master-tag.tar.gz
Source27: https://github.com/rdo-puppet-modules/puppet-pacemaker/archive/puppet-pacemaker-master-tag.tar.gz
Source28: https://github.com/rdo-puppet-modules/puppet-puppet/archive/puppet-puppet-master-tag.tar.gz
Source29: https://github.com/rdo-puppet-modules/puppet-qpid/archive/puppet-qpid-master-tag.tar.gz
Source30: https://github.com/rdo-puppet-modules/puppetlabs-rabbitmq/archive/puppetlabs-rabbitmq-master-tag.tar.gz
Source31: https://github.com/rdo-puppet-modules/puppet-redis/archive/puppet-redis-master-tag.tar.gz
Source32: https://github.com/rdo-puppet-modules/puppet-remote/archive/puppet-remote-master-tag.tar.gz
Source33: https://github.com/rdo-puppet-modules/puppetlabs-rsync/archive/puppetlabs-rsync-master-tag.tar.gz
Source34: https://github.com/rdo-puppet-modules/puppet-sahara/archive/puppet-sahara-master-tag.tar.gz
Source35: https://github.com/rdo-puppet-modules/puppet-snmp/archive/puppet-snmp-master-tag.tar.gz
Source36: https://github.com/rdo-puppet-modules/puppet-ssh/archive/puppet-ssh-master-tag.tar.gz
Source37: https://github.com/rdo-puppet-modules/puppet-staging/archive/puppet-staging-master-tag.tar.gz
Source38: https://github.com/rdo-puppet-modules/puppetlabs-stdlib/archive/puppetlabs-stdlib-master-tag.tar.gz
Source39: https://github.com/rdo-puppet-modules/puppet-swift/archive/puppet-swift-master-tag.tar.gz
Source40: https://github.com/rdo-puppet-modules/puppetlabs-sysctl/archive/puppetlabs-sysctl-master-tag.tar.gz
Source41: https://github.com/rdo-puppet-modules/puppet-tempest/archive/puppet-tempest-master-tag.tar.gz
Source42: https://github.com/rdo-puppet-modules/puppet-timezone/archive/puppet-timezone-master-tag.tar.gz
Source43: https://github.com/rdo-puppet-modules/puppet-tripleo/archive/puppet-tripleo-master-tag.tar.gz
Source44: https://github.com/rdo-puppet-modules/puppet-trove/archive/puppet-trove-master-tag.tar.gz
Source45: https://github.com/rdo-puppet-modules/puppet-tuskar/archive/puppet-tuskar-master-tag.tar.gz
Source46: https://github.com/rdo-puppet-modules/puppetlabs-vcsrepo/archive/puppetlabs-vcsrepo-master-tag.tar.gz
Source47: https://github.com/rdo-puppet-modules/puppet-vlan/archive/puppet-vlan-master-tag.tar.gz
Source48: https://github.com/rdo-puppet-modules/puppet-vswitch/archive/puppet-vswitch-master-tag.tar.gz
Source49: https://github.com/rdo-puppet-modules/puppetlabs-xinetd/archive/puppetlabs-xinetd-master-tag.tar.gz
Source50: https://github.com/rdo-puppet-modules/puppet-gnocchi/archive/puppet-gnocchi-master-tag.tar.gz
Source51: https://github.com/rdo-puppet-modules/puppet-heat/archive/puppet-heat-master-tag.tar.gz
Source52: https://github.com/rdo-puppet-modules/puppet-horizon/archive/puppet-horizon-master-tag.tar.gz
Source53: https://github.com/rdo-puppet-modules/puppet-ironic/archive/puppet-ironic-master-tag.tar.gz
Source54: https://github.com/rdo-puppet-modules/puppet-keystone/archive/puppet-keystone-master-tag.tar.gz
Source55: https://github.com/rdo-puppet-modules/puppet-manila/archive/puppet-manila-master-tag.tar.gz
Source56: https://github.com/rdo-puppet-modules/puppet-memcached/archive/puppet-memcached-master-tag.tar.gz
Source57: https://github.com/rdo-puppet-modules/puppet-module-collectd/archive/puppet-module-collectd-master-tag.tar.gz

BuildArch:      noarch
Requires:       rubygem-json

%description
A collection of Puppet modules which are required to install and configure
OpenStack via installers using Puppet configuration tool.


%prep
%setup -D -c -q -n %{name}-%{version}
%setup -T -D -a 1 -c -q -n %{name}-%{version}
%setup -T -D -a 2 -c -q -n %{name}-%{version}
%setup -T -D -a 3 -c -q -n %{name}-%{version}
%setup -T -D -a 4 -c -q -n %{name}-%{version}
%setup -T -D -a 5 -c -q -n %{name}-%{version}
%setup -T -D -a 6 -c -q -n %{name}-%{version}
%setup -T -D -a 7 -c -q -n %{name}-%{version}
%setup -T -D -a 8 -c -q -n %{name}-%{version}
%setup -T -D -a 9 -c -q -n %{name}-%{version}
%setup -T -D -a 10 -c -q -n %{name}-%{version}
%setup -T -D -a 11 -c -q -n %{name}-%{version}
%setup -T -D -a 12 -c -q -n %{name}-%{version}
%setup -T -D -a 13 -c -q -n %{name}-%{version}
%setup -T -D -a 14 -c -q -n %{name}-%{version}
%setup -T -D -a 15 -c -q -n %{name}-%{version}
%setup -T -D -a 16 -c -q -n %{name}-%{version}
%setup -T -D -a 17 -c -q -n %{name}-%{version}
%setup -T -D -a 18 -c -q -n %{name}-%{version}
%setup -T -D -a 19 -c -q -n %{name}-%{version}
%setup -T -D -a 20 -c -q -n %{name}-%{version}
%setup -T -D -a 21 -c -q -n %{name}-%{version}
%setup -T -D -a 22 -c -q -n %{name}-%{version}
%setup -T -D -a 23 -c -q -n %{name}-%{version}
%setup -T -D -a 24 -c -q -n %{name}-%{version}
%setup -T -D -a 25 -c -q -n %{name}-%{version}
%setup -T -D -a 26 -c -q -n %{name}-%{version}
%setup -T -D -a 27 -c -q -n %{name}-%{version}
%setup -T -D -a 28 -c -q -n %{name}-%{version}
%setup -T -D -a 29 -c -q -n %{name}-%{version}
%setup -T -D -a 30 -c -q -n %{name}-%{version}
%setup -T -D -a 31 -c -q -n %{name}-%{version}
%setup -T -D -a 32 -c -q -n %{name}-%{version}
%setup -T -D -a 33 -c -q -n %{name}-%{version}
%setup -T -D -a 34 -c -q -n %{name}-%{version}
%setup -T -D -a 35 -c -q -n %{name}-%{version}
%setup -T -D -a 36 -c -q -n %{name}-%{version}
%setup -T -D -a 37 -c -q -n %{name}-%{version}
%setup -T -D -a 38 -c -q -n %{name}-%{version}
%setup -T -D -a 39 -c -q -n %{name}-%{version}
%setup -T -D -a 40 -c -q -n %{name}-%{version}
%setup -T -D -a 41 -c -q -n %{name}-%{version}
%setup -T -D -a 42 -c -q -n %{name}-%{version}
%setup -T -D -a 43 -c -q -n %{name}-%{version}
%setup -T -D -a 44 -c -q -n %{name}-%{version}
%setup -T -D -a 45 -c -q -n %{name}-%{version}
%setup -T -D -a 46 -c -q -n %{name}-%{version}
%setup -T -D -a 47 -c -q -n %{name}-%{version}
%setup -T -D -a 48 -c -q -n %{name}-%{version}
%setup -T -D -a 49 -c -q -n %{name}-%{version}
%setup -T -D -a 50 -c -q -n %{name}-%{version}
%setup -T -D -a 51 -c -q -n %{name}-%{version}
%setup -T -D -a 52 -c -q -n %{name}-%{version}
%setup -T -D -a 53 -c -q -n %{name}-%{version}
%setup -T -D -a 54 -c -q -n %{name}-%{version}
%setup -T -D -a 55 -c -q -n %{name}-%{version}
%setup -T -D -a 56 -c -q -n %{name}-%{version}
%setup -T -D -a 57 -c -q -n %{name}-%{version}


find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf


%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/


%files
%{_datadir}/openstack-puppet/modules/*
%{_datadir}/openstack-puppet/Puppetfile


%changelog

* Wed Jul 16 2015 Iván Chavero <ichavero@redhat.com> - 2015.2.1-1
- Initial build
