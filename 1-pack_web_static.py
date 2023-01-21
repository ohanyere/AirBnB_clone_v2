#!/usr/bin/python3
#creates a folder version and tarzip file

import os
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    if not os.path.exists("versions"):
        os.mkdir("versions")

    archive_name = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))

    local("tar -cvzf versions/{} web_static".format(archive_name))

    if os.path.exists("versions/{}".format(archive_name)):
        return "versions/{}".format(archive_name)
    return None
