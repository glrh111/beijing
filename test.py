#! /usr/bin/env python

import random

def growing_array_generate(start, count):
    n = start
    counter = 0
    while counter < count:
        counter += 1
        n += random.randint(1, 10)
        yield n

def generate_array(m, n):
    '''
    m * n array, m is row number, n is column number
    '''
    if not (m > 1 and n > 1):
        raise ValueError('m, n not satisfy')

    # generate two one array of length m
    array_row = [
        i for i in growing_array_generate(3, m)
    ]
    array_whole = [
        [
            i for i in growing_array_generate(k, n)
        ] for k in array_row
    ]
    return array_whole


def test_ele_index(test_array, test_number):
    '''test_array is a 1-D array
    '''
    for idx, ele in enumerate(test_array):
        if ele == test_number:
            return True
        if 
    pass

def test_if_in_array(test_array, test_number):
    '''test_array is a 2-D array
    '''
    fir_num_of_array = map(
        lambda x: x[0],
        test_array
    )

    pass

if __name__ == '__main__':
    array_for_test = generate_array(5, 6)