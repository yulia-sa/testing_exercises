import pytest
from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
    "url,expected_result",
    [
        ("https://github.com/yulia-sa/typing_challenges/pull/1", True),
        ("https://github.com/yulia-sa/typing_challenges/pull/9999999999", True),
        ("https://github.com/yulia-sa/typing_challenges/pull/", True),
        ("https://github.com/yulia-sa/typing_challenges/pull/1/", False),
        ("https://github.com/yulia-sa/typing_challenges/pull/1/1", False),
        ("https://github.com/yulia-sa/typing_challenges/pull", False),
        ("https://github.co/yulia-sa/typing_challenges/pull/1", False),
        ("https://github.com/yulia-sa/typing_challenges/pul/1", False),
        ("https:||github.com|yulia-sa|typing_challenges|pull|1", False),
        ("github.com/yulia-sa/typing_challenges/pull/1", False)
    ]
)
def test__is_github_pull_request_url(url, expected_result):
    assert is_github_pull_request_url(url) is expected_result
