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


def test_square_list(capsys):
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    fxn.square_list(inp)  # actual output is printed, so capture it
    captured = capsys.readouterr()
    # then
    assert captured.out == " ".join(map(str, exp_out)) + "\n"  # check printed output matches expected


def test_fibonacci_stop(capsys):
    """Check fibonacci functions works as expected."""
    inp = 30  # test input to function
    exp_out = [1, 1, 2, 3, 5, 8, 13, 21]  # expected output
    # when
    fxn.fibonacci_stop(inp)  # actual output is printed, so capture it
    captured = capsys.readouterr()
    # then
    assert captured.out == " ".join(map(str, exp_out)) + "\n"  # check printed output matches expected


def test_clean_pitch(capsys):
    """Check clean_pitch works as expected."""
    # Test case: x and status as given in the example
    x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
    status = [1, 0, 0, 0]  # status signal
    
    # Expected output after running clean_pitch
    expected_output = [-999, 2, 6, 95]
    
    # Run the function and check the result
    fxn.clean_pitch(x, status)  # the function prints output, so capture it
    captured = capsys.readouterr()
    
    # Assert the result matches the expected output
    assert captured.out == " ".join(map(str, expected_output)) + "\n", f"Expected {expected_output}, but got {captured.out.strip()}"

if __name__ == '__main__':
    # Run all test functions
    test_greet(capsys)
    test_goldilocks(capsys)
    test_square_list(capsys)
    test_fibonacci_stop(capsys)
    test_clean_pitch(capsys)
