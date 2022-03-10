from code_challenges.quick_sort.quick_sort import quick_sort


def test_sort_assignment_input():
    lst = [8, 4, 23, 42, 16, 15]
    quick_sort(lst)

    assert lst == [4, 8, 15, 16, 23, 42]


def test_reverse_sorted():
    lst = [20, 18, 12, 8, 5, -2]
    quick_sort(lst)

    assert lst == [-2, 5, 8, 12, 18, 20]


def test_few_unique():
    lst = [5, 12, 7, 5, 5, 7]
    quick_sort(lst)

    assert lst == [5, 5, 5, 7, 7, 12]


def test_sort_nearly_sorted():
    lst = [2, 3, 5, 7, 13, 11]
    quick_sort(lst)

    assert lst == [2, 3, 5, 7, 11, 13]
