import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_influxdata_repo(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
        c = host.run('apt-cache search telegraf').rc
    else:
        c = host.run('yum --disablerepo="*" --enablerepo="influxdb" \
        list available').rc

    assert c == 0
