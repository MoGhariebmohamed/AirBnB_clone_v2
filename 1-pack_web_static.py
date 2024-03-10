#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
"""


from datetime import datetime
from fabric.api import *


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
