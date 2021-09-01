# pylint: disable=redefined-outer-name
# ^^^ this
import io
import pathlib
from contextlib import redirect_stdout

import pytest

from myapp import app

test_string = 'MygrepTestCase'
answer_for_test = "test_myapp.py line=11: test_string = '" + test_string + "'\n"


class ClassArguments:
    path = pathlib.Path(__file__).parent.absolute()
    word = test_string


@pytest.fixture
def arguments():
    return ClassArguments()


@pytest.fixture
def text_stream():
    return io.StringIO()


def test_mygrep(text_stream):
    with redirect_stdout(text_stream):
        app.find(pathlib.Path(__file__).parent.absolute(), test_string)
    s = text_stream.getvalue()
    assert s == answer_for_test


def test_main_with_args(arguments):
    app.main(arguments)


def test_try_empty():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        app.main()
    assert pytest_wrapped_e.type == SystemExit
