import numpy as np
import pytest
from bhfdft.mesh import mesh_exp


class TestMesh(object):
    def test_1(self):
        mesh_correct = np.loadtxt('test_mesh_1.txt')
        rmin = 0
        rmax = 50
        a = 1.15e3
        mesh_points = 200
        tol = 1.0e-12
        mesh = mesh_exp(rmin, rmax, a, mesh_points)
        assert (np.abs(mesh-mesh_correct) < tol).all()
