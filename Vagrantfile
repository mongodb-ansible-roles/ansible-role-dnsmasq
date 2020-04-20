Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.provision "docker"

  config.vm.provision "shell",
    inline: "docker run --rm --privileged multiarch/qemu-user-static --reset -p yes"

  config.vm.provision "shell",
    inline: <<-SCRIPT
apt-get -y install python3-venv
python3 -m venv venv
. venv/bin/activate
pip install -r /vagrant/requirements.txt
echo '. venv/bin/activate' >> ~/.bashrc
SCRIPT
end
