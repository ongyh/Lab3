import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 69, 68, 67]
    test_arr = [11, 12, 22, 25, 34, 64, 67, 68, 69, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 69, 68, 67]
    test_arr = [90, 69, 68, 67, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 69, 68, 67]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_bubble_sort_not_int():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 69, 68, "67"]
    test_arr = 3

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_array_greater_than_10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 69, 68, 67, 67]
    test_arr = 1

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_array_lesser_than_10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 69, 68]
    test_arr = 2

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)