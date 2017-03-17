import timeit
import sorter
import drawer
import helper

number_series = []
time_series = []
g_list = []
new_list = []
sub_matrix = [0 for n in range(helper.MATRIX_RANK)]
matrix = [0 for n in range(helper.MATRIX_RANK**2)]


for i in range(helper.K):
    g_list = helper.generate_random_list(i * helper.ARRAY_SIZE_KOEF)
    time = timeit.timeit('sorter.insertion_sort(g_list)', setup='from __main__ import sorter, g_list', number=10)
    number_series.append(i * helper.ARRAY_SIZE_KOEF)
    time_series.append(time)

new_list = helper.generate_random_list(helper.NEW_ARRAY_SIZE)
new_time = timeit.timeit('sorter.insertion_sort(new_list)', setup='from __main__ import sorter, new_list', number=10)


helper.fill_determinant_matrix(matrix, time_series, number_series, sub_matrix)

A = helper.calc_koef("a", matrix, sub_matrix)
B = helper.calc_koef("b", matrix, sub_matrix)
C = helper.calc_koef("c", matrix, sub_matrix)

drawer.draw_measured(number_series,
                     time_series,
                     drawer.draw_figure(new_time, helper.get_function_value(helper.NEW_ARRAY_SIZE, A, B, C)))

drawer.draw_calculated(number_series,
                       helper.calculated_time_series(number_series, A, B, C))

drawer.show_plot()
