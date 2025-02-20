"""Test your functions from Week 2 assignment.
"""
import Preclass_assignments.functions as fxn
import pytest  # Import pytest for capturing output and running the tests

def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect


def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""

    # Test when bed_length is too small
    fxn.goldilocks(139)
    captured = capsys.readouterr()
    assert captured.out == "Too small!\n"  # Ensure output matches

    # Test when bed_length is too large
    fxn.goldilocks(151)
    captured = capsys.readouterr()
    assert captured.out == "Too large!\n"  # Ensure output matches

    # Test when bed_length is just right
    fxn.goldilocks(145)
    captured = capsys.readouterr()
    assert captured.out == "Just right. :)\n"  # Ensure output matches


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    inp = 30  # test input to function
    exp_out = [1, 1, 2, 3, 5, 8, 13, 21]  # expected output
    # when
    out = fxn.fibonacci_stop(inp)  # actual output
    # then
    assert out == exp_out


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # Test case: x and status as given in the example
    x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
    status = [1, 0, 0, 0]  # status signal
    
    # Expected output after running clean_pitch
    expected_output = [-999, 2, 6, 95]
    
    # Run the function and check the result
    result = fxn.clean_pitch(x, status)  # Call clean_pitch from fxn module
    
    # Assert the result matches the expected output
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


if __name__ == '__main__':
    # Run all test functions
    test_greet(capsys)
    test_goldilocks(capsys)
    test_square_list()
    test_fibonacci_stop()
    test_clean_pitch()
