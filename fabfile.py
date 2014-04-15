from fabric.api import *

env.hosts = ['andrew']

def deploy():
    with cd("/tmp/"):
        sudo("mkdir test")

def request(hostname):
    sudo("puppet cert list --all | grep %s" %hostname)

def sign(hostname):
    sudo("puppet cert sign %s" % hostname)

def restart():
    sudo("service apache2 restart")
