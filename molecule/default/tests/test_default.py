import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_dnsmasq_service(host):
    assert host.service("dnsmasq").is_running
    assert host.service("dnsmasq").is_enabled
