#!/usr/bin/python3
""" script that generates a .tgz archive from the
    contents of the web_static folder of your
    AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
import os
from fabric.api import local, run, put, env

env.hosts = ["54.242.12.22", "54.83.125.228"]


def do_pack():
    """ ... """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")

        if not os.path.exists("versions"):

            os.mkdir("versions")

        file_ = "versions/web_static_{}.tgz".format(date)

        local("tar -cvzf {} web_static".format(file_))

        return file_
    except:
        return(None)


def do_deploy(archive_path):
    """ point2 """

    if not os.path.exists(archive_path):
        return False

    file_ = archive_path.split('.')[0].split('/')[1]
    directory = "/data/web_static/releases/"

    complete = directory + file_

    try:

        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(complete))

        run('tar -xzf /tmp/{}.tgz -C {}'.format(file_, complete))
        run('rm -f /tmp/{}.tgz'.format(file_))

        run('mv {}/web_static/* {}/'.format(complete, complete))

        run('rm -rf {}/web_static'.format(complete))
        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(complete))

        return True

    except:
        return False


def deploy():
    """deploy"""
    new = do_pack()

    if new is None:
        return False

    return do_deploy(new)
