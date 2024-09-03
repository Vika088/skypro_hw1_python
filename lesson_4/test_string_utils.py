import pytest
from string_utils import StringUtils


@pytest.mark.parametrize('string, result',
                         [('hello', 'Hello'), ('hi, dude', 'Hi, dude'),
                          ('2024', '2024'), ('august 2024', 'August 2024')])
def test_capitalize_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(string)
    assert res == result


@pytest.mark.parametrize('string, result',
                         [('', ''), ('0hi, dude', '0hi, dude'), ('   ', '   '),
                          ('2024 august', '2024 august')])
def test_capitalize_negative(string, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(string)
    assert res == result


@pytest.mark.parametrize('string, result',
                         [('   hello', 'hello'),
                          ('   hi, dude   ', 'hi, dude   '),
                          ('   august 2024', 'august 2024')])
def test_trim_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result


@pytest.mark.parametrize('string, result',
                         [('', ''), (' ', '')])
def test_trim_negative(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result


@pytest.mark.xfail(reises=AttributeError)
def test_trim_negative_num():
    string_utils = StringUtils()
    res = string_utils.trim(2024)
    assert res is None


@pytest.mark.parametrize('string, delimiter, result',
                         [('h,e,l,l,o', None, ['h', 'e', 'l', 'l', 'o']),
                          ('1and2', 'and', ['1', '2'])])
def test_to_list_positive(string, delimiter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimiter)
    if delimiter is None:
        res == string_utils.to_list(string),
    else:
        res == result


@pytest.mark.parametrize('string, delimiter, result',
                         [('', None, [])])
def test_to_list_negative(string, delimiter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimiter)
    if delimiter is None:
        res == string_utils.to_list(string),
    else:
        res == result


@pytest.mark.xfail(reises=AttributeError)
def test_to_list_negative_num():
    string_utils = StringUtils()
    res = string_utils.trim(2024, None)
    assert res is None


@pytest.mark.parametrize('string, symbol, result',
                         [('student', 'n', True),
                          ('student', 'y', False),
                          ('2024', '0', True)])
def test_contains_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result',
                         [('', 'a', False),
                          ('student', '', False)])
def test_contains_negative(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result


@pytest.mark.xfail(reises=AttributeError)
def test_contains_negative_num():
    string_utils = StringUtils()
    res = string_utils.trim(2024, None)
    assert res is None


@pytest.mark.parametrize('string, symbol, result',
                         [('annigilation', 'n', 'aigilatio'),
                          ('good morning', 'good ', 'morning'),
                          ('2024', '4', '202')])
def test_delete_symbol_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result',
                         [('annigilation', 'm', 'annigilation'),
                          ('annigilation', '', 'annigilation'),
                          ('', '', ''),
                          ('', '4', '')])
def test_delete_symbol_negative(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.xfail(reises=AttributeError)
def test_delete_symbol_negative_num():
    string_utils = StringUtils()
    res = string_utils.trim(2024, None)
    assert res is None


@pytest.mark.parametrize('string, symbol, result',
                         [('annigilation', 'a', True),
                          ('good day', 'g', True),
                          ('2024', '2', True)])
def test_starts_with_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result',
                         [('morning', 'n', False),
                          ('morning', ' ', False),
                          ('', 'm', False)])
def test_starts_with_negative(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.xfail(reises=AttributeError)
def test_starts_with_negative_num():
    string_utils = StringUtils()
    res = string_utils.trim(2024, None)
    assert res is None


@pytest.mark.parametrize('string, symbol, result',
                         [('annigilation', 'n', True),
                          ('morning', 'g', True),
                          ('good day', 'y', True),
                          ('2024', '4', True)])
def test_end_with_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result',
                         [('annigilation', 'a', False),
                          ('morning', ' ', False),
                          (' ', 'a', False),
                          ('2024', '2', False)])
def test_end_with_negative(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result


@pytest.mark.xfail(reises=AttributeError)
def test_end_with_negative_num():
    string_utils = StringUtils()
    res = string_utils.trim(2024, None)
    assert res is None


@pytest.mark.parametrize('string, result',
                         [('', True),
                          (' ', True),
                          ('     ', True)])
def test_is_empty_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result


@pytest.mark.parametrize('string, result',
                         [('annigilation', False),
                          (' morning', False),
                          ('2024 ', False)])
def test_is_empty_negative(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result


@pytest.mark.xfail(reises=AttributeError)
def test_is_empty_negative_num():
    string_utils = StringUtils()
    res = string_utils.trim(2024, None)
    assert res is None


@pytest.mark.parametrize('lst, joiner, result',
                         [([8, 9, 10], '', '8, 9, 10'),
                          (['help', 'me'], '_', 'help_me'),
                          (['A', 'S', 'A', 'P'], '', 'ASAP')])
def test_list_to_string_positive(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    if joiner is None:
        res == string_utils.list_to_string(list),
    else:
        res == result


@pytest.mark.parametrize('lst, joiner, result',
                         [([], None, ''),
                          ([], '/', '')])
def test_list_to_string_negative(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    if joiner is None:
        res == string_utils.list_to_string(lst),
    else:
        res == result
