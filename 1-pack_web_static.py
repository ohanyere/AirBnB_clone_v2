#!/usr/bin/python3
'''
    contains the do_pack method
'''

from datetime import datetime
from fabric.api import local
import os


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
