

def check_tweet_sentiment(text: str, good_words: set[str], bad_words: set[str]) -> str | None:
    words = [w.lower() for w in text.split()]
    good_words_num = sum(1 for w in words if w in good_words)
    bad_words_num = sum(1 for w in words if w in bad_words)
    if not good_words_num and not bad_words_num or good_words == bad_words:
        return None
    if good_words > bad_words:
        return "GOOD"
    return "BAD"
