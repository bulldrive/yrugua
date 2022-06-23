from flaskapp import *

def test_var_value_exists():
    assert get_variable() != 500, "The variable is undefined"