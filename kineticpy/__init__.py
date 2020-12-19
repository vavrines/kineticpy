"""
Lightweight Framework for Kinetic Theory and Scientific Machine Learning 
==================================

This module is built upon Kinetic.jl ecosystem.
Copyright (c) 2020 Tianbai Xiao <<tianbaixiao@gmail.com>>
"""

import os
import subprocess

script_dir = os.path.dirname(os.path.realpath(__file__))

def install():
    """
    Install Julia packages required for diffeqpy.
    """
    subprocess.check_call(['julia', os.path.join(script_dir, 'install.jl')])

from kineticpy.__about__ import __author__, __author_email__, __version__
from .geo import rotate_matrix

__all__ = [
    "rotate_matrix",
]
