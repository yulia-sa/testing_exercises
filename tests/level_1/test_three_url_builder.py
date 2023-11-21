from functions.level_1.three_url_builder import build_url


def test_build_url_without_get_params():
    assert build_url("https://habr.com",
                     "ru/search/") == "https://habr.com/ru/search/"


def test_build_url_with_empty_get_params():
    assert build_url("https://habr.com",
                     "ru/search/",
                     {}) == "https://habr.com/ru/search/"


def test_build_url_with_one_param_in_get_params():
    assert build_url("https://habr.com",
                     "ru/search/",
                     {
                         "q": "2023",
                     }) == "https://habr.com/ru/search/?q=2023"


def test_build_url_with_several_params_in_get_params():
    assert build_url("https://habr.com",
                     "ru/search/",
                     {
                         "q": "python",
                         "target_type": "posts",
                         "order": "relevance"
                     }) == "https://habr.com/ru/search/?q=python&target_type=posts&order=relevance"
