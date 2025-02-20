import Preclass_assignments.functions as fxn


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

    # Test case 1: bed length less than 140
    goldilocks(130)
    captured = capsys.readouterr()  # Capture the printed output
    assert captured.out == "Too small!\n"

    # Test case 2: bed length greater than 150
    goldilocks(160)
    captured = capsys.readouterr()  # Capture the printed output
    assert captured.out == "Too large!\n"

    # Test case 3: bed length equal to 140
    goldilocks(140)
    captured = capsys.readouterr()  # Capture the printed output
    assert captured.out == "Just right. :)\n"

    # Test case 4: bed length equal to 150
    goldilocks(150)
    captured = capsys.readouterr()  # Capture the printed output
    assert captured.out == "Just right. :)\n"


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
    # given
    # given
    # when
    # then
    assert False  # TODO! Update the contents of this function so it correctly tests fibonacci_stop


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    # when
    # then
    assert False  # TODO! Update the contents of this function so it correctly tests clean_pitch
