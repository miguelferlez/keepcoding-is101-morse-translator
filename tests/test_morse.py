from app.morse import to_morse, to_string

def test_string_to_morse():
    assert to_morse('Hello, World!') == '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    assert to_morse('hello world') == '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    assert to_morse('SOS') == '... --- ...'
    assert to_morse('1967') == '.---- ----. -.... --...'

    assert to_morse('') == ''
    assert to_morse('! !!,, .??') == ''

def test_morse_to_string():
    assert to_string('.... . .-.. .-.. --- / .-- --- .-. .-.. -..') == 'HELLO WORLD'
    assert to_string('... --- ...') == 'SOS'
    assert to_string('.---- ----. -.... --...') == '1967'

    assert to_string('') == ''
    assert to_string('! !!,, .??') == ''