from design_patterns import utils


def test_int():
    expected = 'Hi, dude!'
    result = utils.hello_world()
    assert expected == result
