require_relative "test_helper"

describe "Newman Conway Tests" do
  it "works with 13" do
    # Arrange
    input = 13

    # Act
    answer = newman_conway(input)

    # Assert
    expect(answer).must_equal "1 1 2 2 3 4 4 4 5 6 7 7 8"
  end

  it "works with 20" do
    # Arrange
    input = 20

    # Act
    answer = newman_conway(input)

    # Assert
    expect(answer).must_equal "1 1 2 2 3 4 4 4 5 6 7 7 8 8 8 8 9 10 11 12"
  end

  it "works with base cases" do
        # Arrange
        input = 0

        # Act-Assert
        expect {
          newman_conway(input)
        }.must_raise ArgumentError
    

        # Arrange
        input = 1

        # Act
        answer = newman_conway(input)
    
        # Assert
        expect(answer).must_equal "1"

        # Arrange
        input = 2

        # Act
        answer = newman_conway(input)
    
        # Assert
        expect(answer).must_equal "1 1"        
  end
end
