# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "debian7_amd64-puppet"
    # Pour une utilisation interne
    #config.vm.box_url = "http://cdrom.srv.gov.pf/boxes/debian7_amd64-puppet.box"
    config.vm.box_url = "https://s3-us-west-1.amazonaws.com/dsi-vagrant-boxes/debian7_amd64-puppet_vb.box"
    config.vm.hostname = "srv1.dev"
    config.vm.provision :puppet do |puppet|
      puppet.manifests_path = "manifests"
      puppet.module_path= "modules"
      puppet.manifest_file  = "site.pp"
      puppet.options = "--hiera_config /vagrant/hiera.yaml"
    end
end
