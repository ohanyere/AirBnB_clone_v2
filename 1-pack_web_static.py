#!/usr/bin/python3
'''
    create a tar.zip file
    from web_static
'''

from datetime import datetime
import os
from fabric.api import local, task


@task
def do_pack():
    '''creates .tgz file'''

    if not os.path.exists('versions'):
        os.mkdirs('versions')
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    name = f"web_static_{date}.tgz"
    local(f"tar -zcvf versions/{name} web_static")

    if os.path.exists(f"versions/{name}"):
        return f"versions/{name}"
    else:
        return None
