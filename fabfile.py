from fabric.api import *

env.hosts = ['vagrant@10.0.2.15']

def deploy():
    with cd("/tmp/"):
        run("git clone https://github.com/dsi-infrastructure/puppet-config.git config")