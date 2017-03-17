from __future__ import division
import copy
import random

K = 10
MATRIX_RANK = 3
ARRAY_SIZE_KOEF = 200
NEW_ARRAY_SIZE = 2500


def generate_random_list(length):
    l = []
    for i in range(length):
        l.append(random.randrange(1, length))
    return l


def fill_determinant_matrix(matrix, time_series, number_series, submatrix):
    for i in range(K):
        submatrix[0] += time_series[i]*(number_series[i]**2)
        submatrix[1] += time_series[i] * number_series[i]

        matrix[0] += number_series[i] ** 4
        matrix[1] += number_series[i] ** 3
        matrix[2] += number_series[i] ** 2
        matrix[3] += number_series[i] ** 3
        matrix[4] += number_series[i] ** 2
        matrix[5] += number_series[i]
        matrix[6] += number_series[i] ** 2
        matrix[7] += number_series[i]
        matrix[8] = 10

    submatrix[2] = sum(time_series)


def determinant(m):
    result = m[0]*(m[4]*m[8]-m[5]*m[7]) - m[1]*(m[3]*m[8]-m[5]*m[6]) + m[2]*(m[3]*m[7]-m[4]*m[6])
    return result


def calc_koef(koef, matrix, submatrix):
    new_matrix = copy.deepcopy(matrix)
    index_settings = {'a': 0, 'b': 3, 'c': 6}

    for i in range(MATRIX_RANK):
        new_matrix[i+index_settings[koef]] = submatrix[i]

    return (determinant(new_matrix)) / (determinant(matrix))


def calculated_time_series(ns, a, b, c):
    ts2 = []
    for i in range(K):
        ts2.append((a * (ns[i] ** 2)) + b * ns[i] + c)

    return ts2


def get_function_value(n, a, b, c):
    return (a * (n ** 2)) + b * n + c
