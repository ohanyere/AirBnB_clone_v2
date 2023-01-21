#!/usr/bin/python3
'''
    create a tar.zip file
    from web_static
'''
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    '''creates .tgz file'''

    date = datetime.now().strftime('%Y%m%d%H%M%S')
    name = f"web_static_{date}.tgz"
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local(f"tar -zcvf versions/{name} web_static").Failed is True:
        return None
    return name
