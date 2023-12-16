from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__good_and_no_bad():
    text = "Neutral_word_1 neutral_word_2 good_word_3"
    good_words = {"good_word_1", "good_word_2", "good_word_3"}
    bad_words = set()

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "GOOD"


def test__check_tweet_sentiment__good_more_than_bad():
    text = "Neutral_word_1 neutral_word_2 good_word_2 bad_word_1 good_word_3"
    good_words = {"good_word_1", "good_word_2", "good_word_3"}
    bad_words = {"bad_word_1", "bad_word_2", "bad_word_3"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "GOOD"


def test__check_tweet_sentiment__bad_and_no_good():
    text = "Bad_word_1 neutral_word_1 neutral_word_2 bad_word_3"
    good_words = set()
    bad_words = {"bad_word_1", "bad_word_2", "bad_word_3"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "BAD"


def test__check_tweet_sentiment__bad_more_than_good():
    text = "Good_word_1 bad_word_1 neutral_word_1 good_word_3 neutral_word_2 bad_word_1 bad_word_2"
    good_words = {"good_word_1", "good_word_2", "good_word_3"}
    bad_words = {"bad_word_1", "bad_word_2", "bad_word_3"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "BAD"


def test__check_tweet_sentiment__no_good_no_bad():
    text = "Neutral_word_1 neutral_word_2"
    good_words = {"good_word_1", "good_word_2", "good_word_3"}
    bad_words = {"bad_word_1", "bad_word_2", "bad_word_3"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result is None


def test__check_tweet_sentiment__no_good_no_bad_sets():
    text = "Neutral_word_1 neutral_word_2"
    good_words = set()
    bad_words = set()

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result is None


def test__check_tweet_sentiment__no_good_no_bad_sets_no_text():
    text = ""
    good_words = set()
    bad_words = set()

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result is None


def test__check_tweet_sentiment__equal_num_good_and_num_bad():
    text = "Good_word_1 bad_word_2 good_word_3 bad_word_2 neutral_word_1"
    good_words = {"good_word_1", "good_word_2", "good_word_3"}
    bad_words = {"bad_word_1", "bad_word_2", "bad_word_3"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result is None


def test__check_tweet_sentiment__text_to_lowercase():
    text = "good_word_1 GOOD_WORD_2 gOoD_wOrD_3 Bad_Word_3 NEUTRAL_word_1"
    good_words = {"good_word_1", "good_word_2", "good_word_3"}
    bad_words = {"bad_word_1", "bad_word_2", "bad_word_3"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "GOOD"


def test__check_tweet_sentiment__text_split():
    text = "good_word_1, good_word_2, good_word_3, good_word_3 bad_word_1 bad_word_2"
    good_words = {"good_word_1", "good_word_2", "good_word_3"}
    bad_words = {"bad_word_1", "bad_word_2", "bad_word_3"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "BAD"
