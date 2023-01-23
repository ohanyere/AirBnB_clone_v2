#!/usr/bin/python3
'''
    contains the module for setting up remote module
'''

from fabric.api import *
import os

env.hosts = ['54.165.158.100', '54.209.231.85']


def do_deploy():
    '''method to set up remote servers'''

    a_path = '~/AirBnB_clone_v2/versions/web_static_20230122121617.tgz'
    if not os.path.exists(a_path):
        return False

    filename = 'web_static_20230122121617.tgz'
    release_folder = '/data/web_static/releases/web_static_20230122121617'

    put(a_path, '/tmp/')
    run('mkdir -p ' + release_folder)
    run('tar -xzf /tmp/' + filename + ' -C ' + release_folder)
    run('rm /tmp/' + filename)
    run('rm -rf /data/web_static/current')
    run('ln -s ' + release_folder + ' /data/web_static/current')

    return True
