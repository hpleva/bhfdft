import pytest
from bhfdft.atomic_states import *

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
