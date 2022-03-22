from code_challenges.merge_sort.merge_sort import merge_sort


def test_sort_assignment_input():
    lst = [8, 4, 23, 42, 16, 15]
    merge_sort(lst)

    assert lst == [4, 8, 15, 16, 23, 42]


def test_reverse_sorted():
    lst = [20, 18, 12, 8, 5, -2]
    merge_sort(lst)

    assert lst == [-2, 5, 8, 12, 18, 20]


def test_few_unique():
    lst = [5, 12, 7, 5, 5, 7]
    merge_sort(lst)

    assert lst == [5, 5, 5, 7, 7, 12]


def test_sort_nearly_sorted():
    lst = [2, 3, 5, 7, 13, 11]
    merge_sort(lst)

    assert lst == [2, 3, 5, 7, 11, 13]
