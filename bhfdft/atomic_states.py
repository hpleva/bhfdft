import numpy as np


def get_atomic_states(Z):
    """Generate occupations and quantum numbers using Aufbau principle.

    Only closed-shell atoms are supported.
    """
    def find_diagonal_starting_point(n, l):
        while n - l > 2:
            n -= 1
            l += 1
        return n, l
    n_array = [1]
    l_array = [0]
    occ_array = [2]
    Z_list = [2]
    l_letters = ['s','p','d','f','g','h','i','j','k','l','m','n','o']
    total_occupation = 0
    n = 1
    l = 0
    occ = 2
    current_Z = 2
    find_closest_Z = False
    current_Z_too_large = False
    counter = 1
    counter_max = 2
    #
    if not isinstance(Z, int):
        raise Exception('Z has to be an integer!')
    if Z < 1:
        raise Exception('Z has to be larger than zero!')
    elif Z == 1:
        return np.array([1], dtype=int), np.array([0], dtype=int),\
        np.array([1], dtype=int)
    elif Z == 2:
        return np.array(n_array, dtype=int), np.array(l_array, dtype=int),\
        np.array(occ_array, dtype=int)
    while current_Z < Z or find_closest_Z:
        # Check if we have reached the left "border" (s-orbital) of the Aufbau diagram.
        if l == 0:
            # Go to the beginning of the next diagonal
            n, l = find_diagonal_starting_point(n+1,l)
        else:
            n += 1
            l -= 1
        occ = 2*(2*l+1)
        current_Z += 2*(2*l+1)
        Z_list.append(current_Z)
        if current_Z > Z and current_Z_too_large == False:
            current_Z_too_large = True
            find_closest_Z = True
        if counter == counter_max:
            if len(Z_list) < 4:
                raise Exception('There is no closed-shell atom for Z = {0}!\n'.format(Z) +\
                                'Closest closed-shell atoms are: Z = {0}, {1}, {2}\n'.format(*Z_list[-3:]))
            else:
                raise Exception('There is no closed-shell atom for Z = {0}!\n'.format(Z) +\
                                'Closest closed-shell atoms are Z = {0}, {1}, {2}, {3}\n'.format(*Z_list[-4:]))
        if find_closest_Z:
            counter += 1
        n_array.append(n)
        l_array.append(l)
        occ_array.append(occ)
    # Sort arrays
    n_array = np.array(n_array, dtype=int)
    l_array = np.array(l_array, dtype=int)
    occ_array = np.array(occ_array, dtype=int)
    ind = np.lexsort((l_array, n_array))
    n_array = n_array[ind]
    l_array = l_array[ind]
    occ_array = occ_array[ind]
    return n_array, l_array, occ_array


def get_atomic_states_rel(Z):
    """Generate relativistic occupations and quantum numbers using Aufbau principle.

    Only closed-shell atoms are supported.
    """
    n2, l2, occ2 = get_atomic_states(Z)
    n_array = []
    kappa_array = []
    l_array = []
    j_array = []
    #s_array = []
    occ_array = []
    for i in range(len(n2)):
        if l2[i] == 0:
            n_array.append(n2[i])
            l_array.append(l2[i])
            j_array.append(1./2)
            kappa_array.append(-1)
            occ_array.append(occ2[i])
            #s_array.append(1)
        else:
            n_array.append(n2[i])
            l_array.append(l2[i])
            j_array.append(l2[i]-1./2)
            kappa_array.append(l2[i])
            occ_array.append(occ2[i] * (2*l2[i]) / (2*(2*l2[i]+1)))
            #s_array.append(0)

            n_array.append(n2[i])
            l_array.append(l2[i])
            j_array.append(l2[i]+1./2)
            kappa_array.append(-l2[i]-1)
            occ_array.append(occ2[i] * (2*l2[i]+2) / (2*(2*l2[i]+1)))
            #s_array.append(1)
    n_array = np.array(n_array, dtype=int)
    l_array = np.array(l_array, dtype=int)
    j_array = np.array(j_array, dtype=float)
    #s_array = np.array(s_array,dtype=int)
    kappa_array = np.array(kappa_array, dtype=int)
    occ_array = np.array(occ_array, dtype=int)
    #return n_array, l_array, s_array, occ_array
    return n_array, l_array, j_array, kappa_array, occ_array
