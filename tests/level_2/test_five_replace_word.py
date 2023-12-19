from functions.level_2.five_replace_word import replace_word


def test__replace_word__replace_one_word():
    text = "old_word"
    replace_from = "old_word"
    replace_to = "new_word"

    result = replace_word(text, replace_from, replace_to)

    assert result == "new_word"


def test__replace_word__replace_several_words():
    text = "old_word and one more old_word and another old_word"
    replace_from = "old_word"
    replace_to = "new_word"

    result = replace_word(text, replace_from, replace_to)

    assert result == "new_word and one more new_word and another new_word"


def test__replace_word__no_words_to_replace():
    text = "some nice text without words to replace"
    replace_from = "old_word"
    replace_to = "new_word"

    result = replace_word(text, replace_from, replace_to)

    assert result == "some nice text without words to replace"


def test__replace_word__empty_text():
    text = ""
    replace_from = "old_word"
    replace_to = "new_word"

    result = replace_word(text, replace_from, replace_to)

    assert result == ""


def test__replace_word__empty_words():
    text = "some nice text"
    replace_from = ""
    replace_to = ""

    result = replace_word(text, replace_from, replace_to)

    assert result == "some nice text"


def test__replace_word__empty_text_empty_words():
    text = ""
    replace_from = ""
    replace_to = ""

    result = replace_word(text, replace_from, replace_to)

    assert result == ""


def test__replace_word__text_with_capitalization():
    text = "Old_word some text old_word OLD_WorD and old_word"
    replace_from = "old_word"
    replace_to = "new_word"

    result = replace_word(text, replace_from, replace_to)

    assert result == "new_word some text new_word new_word and new_word"
