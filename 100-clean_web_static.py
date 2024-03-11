#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
"""


from datetime import datetime
from os.path import exists, isdir
from fabric.api import *
env.hosts = ['100.26.219.106', '35.153.16.107']


def do_clean(number=0):
     """
    function for archive all content
    Args:
        number (int): The number of kept archives.
    """
    number = 1 if int(number) == 0 else int(number)

    archives_tarball = sorted(os.listdir("versions"))
    [archives_tarball.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives_tarball]

    with cd("/data/web_static/releases"):
        archives_tarball = run("ls -tr").split()
        archives_tarball = [a for a in archives_tarball if "web_static_" in a]
        [archives_tarball.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives_tarball]
