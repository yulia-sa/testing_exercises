from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url("https://habr.com",
                     "ru/search/") == "https://habr.com/ru/search/"
    assert build_url("https://habr.com",
                     "ru/search/",
                     {}) == "https://habr.com/ru/search/"
    assert build_url("https://habr.com",
                     "ru/search/",
                     {
                         "q": "2023",
                     }) == "https://habr.com/ru/search/?q=2023"
    assert build_url("https://habr.com",
                     "ru/search/",
                     {
                         "q": "python",
                         "target_type": "posts",
                         "order": "relevance"
                     }) == "https://habr.com/ru/search/?q=python&target_type=posts&order=relevance"
