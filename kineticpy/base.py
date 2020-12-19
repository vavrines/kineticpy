"""
KitBase.jl

"""

import sys

from julia.api import Julia
jl = Julia(compiled_modules=False)
from julia import KitBase

sys.modules[__name__] = KitBase # mutate myself