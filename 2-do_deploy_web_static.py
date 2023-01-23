#!/usr/bin/python3
""" a Fabric script that distributes an
    archive to your web servers, using the function do_deploy
"""


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['54.165.158.100', '54.209.231.85']


def do_deploy(archive_path):
    """ distributes an archive to my web servers
    """
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    a_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(a_tgz))
        run("tar -xzf {} -C {}/".format(tmp, a_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(a_tgz, a_tgz))
        run("rm -rf {}/web_static".format(a_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(a_tgz))

        return True
    except:
        return False
