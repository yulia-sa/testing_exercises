import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    "text,good_words,bad_words,expected_result",
    [
        (
            "Neutral_word_1 neutral_word_2 good_word_3",
            {"good_word_1", "good_word_2", "good_word_3"},
            set(),
            "GOOD"
        ),
        (
            "Neutral_word_1 neutral_word_2 good_word_2 bad_word_1 good_word_3",
            {"good_word_1", "good_word_2", "good_word_3"},
            {"bad_word_1", "bad_word_2", "bad_word_3"},
            "GOOD"
        ),
        (
            "Bad_word_1 neutral_word_1 neutral_word_2 bad_word_3",
            set(),
            {"bad_word_1", "bad_word_2", "bad_word_3"},
            "BAD"
        ),
        (
            "Good_word_1 bad_word_1 neutral_word_1 good_word_3 neutral_word_2 bad_word_1 bad_word_2",
            {"good_word_1", "good_word_2", "good_word_3"},
            {"bad_word_1", "bad_word_2", "bad_word_3"},
            "BAD"
        ),
        (
            "Neutral_word_1 neutral_word_2",
            {"good_word_1", "good_word_2", "good_word_3"},
            {"bad_word_1", "bad_word_2", "bad_word_3"},
            None
        ),
        (
            "Neutral_word_1 neutral_word_2",
            set(),
            set(),
            None
        ),
        (
            "",
            set(),
            set(),
            None
        ),
        (
            "Good_word_1 bad_word_2 good_word_3 bad_word_2 neutral_word_1",
            {"good_word_1", "good_word_2", "good_word_3"},
            {"bad_word_1", "bad_word_2", "bad_word_3"},
            None
        ),
        (
            "good_word_1 GOOD_WORD_2 gOoD_wOrD_3 Bad_Word_3 NEUTRAL_word_1",
            {"good_word_1", "good_word_2", "good_word_3"},
            {"bad_word_1", "bad_word_2", "bad_word_3"},
            "GOOD"
        )
    ]
)
def test__check_tweet_sentiment(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result
