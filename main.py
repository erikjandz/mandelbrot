from matplotlib import pyplot as plt


def decimal_range(start, stop, increment):
    while start < stop: # and not math.isclose(start, stop): Py>3.5
        yield start
        start += increment


def square_tuple(inp: tuple) -> tuple:
    return inp[0] * inp[0] - inp[1] * inp[1], 2 * inp[0] * inp[1]


def one_iteration(x, z):
    x = (x[0], x[1]) # (abs(x[0]), abs(x[1]))
    result = square_tuple(x)
    return result[0] + z[0], result[1] + z[1]


def check_if_in_circle(inp: tuple) -> bool:
    return (inp[0] * inp[0] + inp[1] * inp[1]) <= 4


def calculate_iter_count_out_of_circle(inp: tuple):
    count = 1
    value = inp
    prev_values = [(0, 0)]
    while True:
        count += 1
        prev_values.append(value)
        value = one_iteration(value, inp)
        if not check_if_in_circle(value):
            return count

        if value in prev_values:
            return 0

        if count == 100:
            return 0


start_x, start_y = -2, -2 #-1.84, -0.14
end_x, end_y = 2, 2#-1.68, 0.02
values_x, values_y = 1000, 1000


interval_x, interval_y = (end_x - start_x) / values_x, (end_y - start_y) / values_y


array = []
for y in decimal_range(start_y, end_y, interval_y):
    tmp = []
    for x in decimal_range(start_x, end_x, interval_x):
        value = calculate_iter_count_out_of_circle((x, y))
        tmp.append(value)
    array.append(tmp)

plt.imshow(array, interpolation='nearest')
plt.show()

