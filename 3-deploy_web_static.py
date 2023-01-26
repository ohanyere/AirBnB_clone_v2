#!/usr/bin/python3
'''
    contains the do_pack method
'''

from datetime import datetime
from fabric.api import local
import os

env.user = "ubuntu"
env.key_filename = "~/.ssh/school"
env.hosts = ['54.165.158.100', '54.209.231.85']


def do_pack():
    '''creates a tar.zip file'''

    if not os.path.exists("versions"):
        os.makedirs("versions")

    date_format = "%Y%m%d%H%M%S"
    timestamp = datetime.now().strftime(date_format)
    filename = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(filename)

    local("tar -cvzf {} web_static".format(archive_path))
    if os.path.exists(archive_path):
        return archive_path
    return None


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

def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
