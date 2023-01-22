#!/usr/bin/python3
'''
    contains the module for setting up remote module
'''

from fabric.api import *
import os

env.hosts = ['ubuntu@54.165.158.100', 'ubuntu@54.209.231.85']


def do_deploy(archive_path):
    '''method to set up remote servers'''

    if not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    release_folder = '/data/web_static/releases/' + filename.split('.')[0]

    put(archive_path, '/tmp/')
    run('mkdir -p ' + release_folder)
    run('tar -xzf /tmp/' + filename + ' -C ' + release_folder)
    run('rm /tmp/' + filename)
    run('rm -rf /data/web_static/current')
    run('ln -s ' + release_folder + ' /data/web_static/current')

    return True
