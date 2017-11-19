import numpy as np
import pytest
from bhfdft.atomic_states import get_atomic_states
from bhfdft.atomic_states import get_atomic_states_rel


class TestAtomicStates(object):
    def test_1(self):
        with pytest.raises(Exception):
            get_atomic_states_rel(0)

    def test_2(self):
        with pytest.raises(Exception):
            get_atomic_states_rel(-5)

    def test_3(self):
        with pytest.raises(Exception):
            get_atomic_states_rel(5)

    def test_4(self):
        with pytest.raises(Exception):
            get_atomic_states_rel(4.0)

    def test_5(self):
        n, l, occ = get_atomic_states(1)
        assert n[0] == 1
        assert l[0] == 0
        assert occ[0] == 1

    def test_6(self):
        n, l, j, kappa, occ = get_atomic_states_rel(1)
        assert n[0] == 1
        assert l[0] == 0
        assert j[0] == 0.5
        assert kappa[0] == -1
        assert occ[0] == 1

    def test_7(self):
        n_correct = np.array([1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
                              5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7])
        l_correct = np.array([0, 0, 1, 1, 0, 1, 1, 2, 2, 0, 1, 1, 2, 2, 3, 3,
                              0, 1, 1, 2, 2, 3, 3, 0, 1, 1, 2, 2, 0])
        j_correct = np.array([0.5, 0.5, 0.5, 1.5, 0.5, 0.5, 1.5, 1.5,
                              2.5, 0.5, 0.5, 1.5, 1.5, 2.5, 2.5, 3.5,
                              0.5, 0.5, 1.5, 1.5, 2.5, 2.5, 3.5, 0.5,
                              0.5, 1.5, 1.5, 2.5, 0.5])
        kappa_correct = np.array([-1, -1,  1, -2, -1,  1, -2,  2, -3, -1,  1,
                                  -2,  2, -3,  3, -4, -1,  1, -2,  2, -3,  3,
                                  -4, -1,  1, -2,  2, -3, -1])
        occ_correct = np.array([2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6,
                                8, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 2])
        n, l, j, kappa, occ = get_atomic_states_rel(112)
        assert (n == n_correct).all()
        assert (l == l_correct).all()
        assert (j == j_correct).all()
        assert (kappa == kappa_correct).all()
        assert (occ == occ_correct).all()
