from code_challenges.validate_brackets.validate_brackets import validate_brackets

def test_no_brackets():
    assert validate_brackets("") == True


def test_one_valid_brackets():
    assert validate_brackets("{}") == True

def test_complex_valid_brackets():
    assert validate_brackets("()[[Extra Characters]]") == True


def test_text_complex_brackets():
    assert validate_brackets("{}{Code}[Fellows](())") == True


def test_invalid1_brackets():
    assert validate_brackets("[({}]") == False


def test_invalid2_brackets():
    assert validate_brackets("{(})") == False


def test_invalid_single_brackets():
    assert validate_brackets("{") == False

