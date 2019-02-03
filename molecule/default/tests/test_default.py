import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file_exists(host):
    f = host.file('/etc/hosts-test')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_hosts_file_localhost(host):
    f = host.file('/etc/hosts-test')

    assert f.contains("127.0.0.1")


def test_hosts_file_entry(host):
    f = host.file('/etc/hosts-test')

    assert f.contains("myserver")
