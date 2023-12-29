import pytest
from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    "text,replace_from,replace_to,expected_result",
    [
        (
            "old_word",
            "old_word",
            "new_word",
            "new_word"
        ),
        (
            "old_word and one more old_word and another old_word",
            "old_word",
            "new_word",
            "new_word and one more new_word and another new_word"
        ),
        (
            "some nice text without words to replace",
            "old_word",
            "new_word",
            "some nice text without words to replace"
        ),
        (
            "",
            "old_word",
            "new_word",
            ""
        ),
        (
            "some nice text",
            "",
            "",
            "some nice text"
        ),
        (
            "",
            "",
            "",
            ""
        ),
        (
            "Old_word some text old_word OLD_WorD and old_word",
            "old_word",
            "new_word",
            "new_word some text new_word new_word and new_word"
        )
    ]
)
def test__replace_word(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result
