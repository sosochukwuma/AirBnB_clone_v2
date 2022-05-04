#!/usr/bin/python3
""" script that generates a .tgz archive from the
    contents of the web_static folder of your
    AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
import os
from fabric.api import local


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
