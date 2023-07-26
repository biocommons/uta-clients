import re
import warnings

import pkg_resources


def hgvs_version():
    try:
        return pkg_resources.get_distribution("hgvs").version
    except pkg_resources.DistributionNotFound:
        raise Exception("can't get __version__ because hgvs package isn't installed")
