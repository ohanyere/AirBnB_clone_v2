#!/usr/bin/python3
'''
    contains the do_pack method
'''

from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.165.158.100', '54.209.231.85']


def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
