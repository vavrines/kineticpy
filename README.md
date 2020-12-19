# kineticpy

Python wrapper of [Kinetic.jl](https://github.com/vavrines/Kinetic.jl), which is a lightweight Julia toolbox for the study of kinetic theory and scientific machine learning.

## How to use
We start by cloning the repository and changing into the directory.
    
    git clone https://github.com/vavrines/kineticpy.git
    cd kineticpy
    
Next, we start `python`.
    
    python

We can initialize the module by
    
```pycon
>>> import kineticpy
>>> diffeqpy.install()
```

while the basic structs and methods are stored in 

```pycon
>>> from kineticpy import base
```