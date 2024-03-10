#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
"""


from datetime import datetime
from os.path import exists, isdir
from fabric.api import *
env.hosts = ['100.26.219.106', '35.153.16.107']


def do_pack():
    """
    function for archive all content
    """
    time_now = datetime.now()
    tarballnm = 'web_static_' + time_now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create_tar = local('tar -cvzf versions/{} web_static'.format(tarballnm))
    if create_tar is not None:
        return tarballnm
    else:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    args:
        archive_path
    """
    if exists(archive_path) is False:
        return False
    try:
        name_file = archive_path.split("/")[-1]
        extension_file = name_file.split(".")[0]
        direct = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(direct, extension_file))
        run('tar -xzf /tmp/{} -C {}{}/'
            .format(name_file, direct, extension_file))
        run('rm /tmp/{}'.format(name_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(direct, extension_file))
        run('rm -rf {}{}/web_static'.format(direct, extension_file))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'
            .format(direct, extension_file))
        return True
    except:
        return False


def deploy():
    """
    create and distributes an archive to the web servers
    """
    archived_path = do_pack()
    if archived_path is None:
        return False
    return do_deploy(archived_path)
