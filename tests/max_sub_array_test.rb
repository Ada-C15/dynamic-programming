require_relative "test_helper"

xdescribe "max subarray" do
  it "will work for [-2,1,-3,4,-1,2,1,-5,4]" do
    # Arrange
    input = [-2,1,-3,4,-1,2,1,-5,4]

    # Act
    answer = max_sub_array(input)

    # Assert
    expect(answer).must_equal 6
  end

  it "will work with a totally negative array" do
    # Arrange
    input = [-3, -4, -5, -6, -7]

    # Act
    answer = max_sub_array(input)

    # Assert
    expect(answer).must_equal(-3)
  end

  it "will work with a totally negative array with the largest element at the rear" do
    # Arrange
    input = [ -4, -5, -6, -7, -3]

    # Act
    answer = max_sub_array(input)

    # Assert
    expect(answer).must_equal(-3)
  end

  it "will work with a 1-element array" do
    # Arrange
    input = [3]

    # Act
    answer = max_sub_array(input)

    # Assert
    expect(answer).must_equal 3
  end

  it "will return nil for an empty array" do
   # Arrange
   input = []

   # Act
   answer = max_sub_array(input)

   # Assert
   expect(answer).must_be_nil
  end

  it "will work for [50, -50, 50]" do
    # Arrange
    input = [50, -50, 50]

    # Act
    answer = max_sub_array(input)

    # Assert
    expect(answer).must_equal 50
  end

end