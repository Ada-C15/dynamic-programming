from lib.max_subarray import max_sub_array


def test_max_subarray_on_empty_array():
    assert max_sub_array([]) == 0


def test_max_subarray_with_negative_elements():
    # Arrange
    input = [-3, -4, -5, -6, -7]

    # Act
    answer = max_sub_array(input)

    # Assert
    assert answer == -3


def test_max_subarray_with_negative_array_with_largest_element_at_rear():
    # Arrange
    input = [-4, -5, -6, -7, -1]

    # Act
    answer = max_sub_array(input)

    # Assert
    assert answer == -1


def test_max_subarray_with_one_element_array():
    # Arrange
    input = [3]

    # Act
    answer = max_sub_array(input)

    # Assert
    assert answer == 3


def test_max_sub_array_with_50_neg_50_50():
    # Arrange
    input = [50, -50, 50]

    # Act
    answer = max_sub_array(input)

    # Assert
    assert answer == 50


def test_max_sub_array_with_50_3_neg_50_3():
    # Arrange
    input = [50, 3, -50, 50, 3]

    # Act
    answer = max_sub_array(input)

    # Assert
    assert answer == 56


def test_max_sub_array_with_50_3_neg_50_10_65_neg_3():
    # Arrange
    input = [50, 3, -50, 10, 65, -3]

    # Act
    answer = max_sub_array(input)

    # Assert
    assert answer == 78  # 50, 3, -50, 10, 65 (largest subarray)
