import numpy as np

def rotate_matrix(axis, angle):
    """Returns the rotation matrix of size 3x3 that rotates a point
    around axis by angle.
    See: https://en.wikipedia.org/wiki/Rotation_matrix
    """
    ux = axis[0]
    uy = axis[1]
    uz = axis[2]

    costheta = np.cos(angle)
    sintheta = np.sin(angle)
    rot = np.zeros((3, 3))

    rot[0, 0] = ux * ux * (1 - costheta) + costheta
    rot[0, 1] = ux * uy * (1 - costheta) - uz * sintheta
    rot[0, 2] = ux * uz * (1 - costheta) + uy * sintheta

    rot[1, 0] = uy * ux * (1 - costheta) + uz * sintheta
    rot[1, 1] = uy * uy * (1 - costheta) + costheta
    rot[1, 2] = uy * uz * (1 - costheta) - ux * sintheta

    rot[2, 0] = uz * ux * (1 - costheta) - uy * sintheta
    rot[2, 1] = uz * uy * (1 - costheta) + ux * sintheta
    rot[2, 2] = uz * uz * (1 - costheta) + costheta

    return rot