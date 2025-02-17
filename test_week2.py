"""Test your functions from Week 2 assignment.
"""
from Preclass_assignments.functions import *


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = ['Nicklas']  # who should we greet?
    # when
    greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, Nicklas!\n'  # check that the greeting was what we expect


def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    length = 10  # test input to function
    # when
    goldilocks(length)  # actual output
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Too short!\n'  # throw error if actual and expected output don't match

def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    input_value = 30  # test input to function
    exp_output = [1, 1, 2, 3, 5, 8, 13, 21]  # expected output
    # given
    # when
    output = fibonacci_stop(input_value)  # actual output
    # then
    assert exp_output == output  # throw error if actual and expected output don't match

def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    input_pitch_angles = [10, 95, 45, -5, 85]  # test input to function
    status_signals = [0, 1, 0, 1, 0]  # test input to function
    exp_output = [10, -999, 45, -999, 85]  # expected output
    # when
    output = clean_pitch(input_pitch_angles, [0, 1, 0, 1, 0])  # actual output
    # then
    assert exp_output == output  # throw error if actual and expected output don't match
