# importing library statistic
# This is a stat calculator terminal program
# Includes common statistic functions
import statistics
import math
import Utils


# basic util function
def data_entry():
    return int(input("Number of entries: "))


def easy_entry():
    entry = int(input("Enter value >> "))
    return entry


def set_list():
    n = data_entry()
    this_list = []
    i = 0
    while i < n:
        this_list.append(easy_entry())
        i += 1
    return this_list


# statistic functions
# takes list as input, return int
def my_mean(sample):
    return statistics.mean(sample)


# takes list as input., return double
def my_median(sample):
    return statistics.median(sample)


def standard_deviation(sample):
    return "%.4f" % statistics.stdev(sample)


# Independent t test functions
def sp2(n1, n2, s1, s2):
    a = (((n1 - 1) * s1 ** 2) + ((n2 - 1) * s2 ** 2)) / (n1 + n2 - 2)
    return "{0:.4f}".format(a)


def lower_part_t(n1, n2):
    a = (1 / n1 + 1 / n2)
    return "{0:.4f}".format(a)


def get_df(n1, n2):
    return n1 + n2 - 2


def independent_t_test(x1, x2, s1, s2, n1, n2):
    a = (x1 - x2) / math.sqrt(float(sp2(n1, n2, s1, s2)) * float(lower_part_t(n1, n2)))
    return "{0:.3f}".format(a)


# Dependent T test functions below
def get_d(sample1, sample2):
    size = len(sample1)
    n = 0
    total = 0
    while n < size:
        total += sample1[n] - sample2[n]
        n += 1
    return "{0:.4f}".format(total / size)


def get_sd(_d, sample1, sample2):
    size = len(sample1)
    n = 0
    total = 0
    while n < size:
        total += ((sample1[n] - sample2[n]) - _d) ** 2
        n += 1

    a = math.sqrt(total / float(get_df_d(sample1)))
    return "{0:.4f}".format(a)


def get_df_d(sample1):
    return len(sample1) - 1


def dependent_t_test(sample1, sample2):
    _d = float(get_d(sample1, sample2))
    sd = float(get_sd(_d, sample1, sample2))
    nd = len(sample1)

    a = _d / (sd / math.sqrt(nd))
    return "{0:.3f}".format(a)


# Overload method 1
def dependent_t_test(_d, sd, nd):
    a = _d / (sd / math.sqrt(nd))
    return "{0:.3f}".format(a)


# goodness of fit test
def goodness_of_fit(sample1):
    expected = my_mean(sample1)
    sum = 0
    for num in sample1:
        sum += ((num-expected)**2)/expected

    return "{0:.3f}".format(sum)


# independence_test functions
# get expected matrix
def get_expected_f_mat(row_list, col_list):
    ans_mat = mat = [[0 for _ in range(len(col_list))] for _ in range(len(row_list))]
    total = sum(row_list)
    for i in range(0,len(row_list)):
        for j in range(0,len(col_list)):
            ans_mat[i][j] = float(row_list[i]*col_list[j])/total

    return ans_mat


# independence_test function (chi-square)
def independence_test(mat):
    total = 0
    row_list = Utils.get_row_total(mat)
    col_list = Utils.get_col_total(mat)
    expected_mat = get_expected_f_mat(row_list, col_list)
    for i in range(0, len(row_list)):
        for j in range(0, len(col_list)):
            total += ((mat[i][j] - expected_mat[i][j])**2)/expected_mat[i][j]

    return "{0:.4f}".format(total)

