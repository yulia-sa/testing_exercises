import pytest
from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    "host_name,relative_url,get_params,expected_result_url",
    [
        ("https://habr.com", "ru/search/", None, "https://habr.com/ru/search/"),
        ("https://habr.com", "ru/search/", {}, "https://habr.com/ru/search/"),
        ("https://habr.com", "ru/search/", {"q": "2023"}, "https://habr.com/ru/search/?q=2023"),
        (
            "https://habr.com",
            "ru/search/",
            {
                "q": "python",
                "target_type": "posts",
                "order": "relevance"
            },
            "https://habr.com/ru/search/?q=python&target_type=posts&order=relevance"
        )
    ]
)
def test__build_url(host_name, relative_url, get_params, expected_result_url):
    assert build_url(host_name, relative_url, get_params) == expected_result_url
