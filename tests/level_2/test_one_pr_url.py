from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__yes():
    assert is_github_pull_request_url("https://github.com/yulia-sa/typing_challenges/pull/1")
    assert is_github_pull_request_url("https://github.com/yulia-sa/typing_challenges/pull/9999999999")
    assert is_github_pull_request_url("https://github.com/yulia-sa/typing_challenges/pull/")


def test__is_github_pull_request_url__no():
    assert not is_github_pull_request_url("https://github.com/yulia-sa/typing_challenges/pull/1/")
    assert not is_github_pull_request_url("https://github.com/yulia-sa/typing_challenges/pull/1/1")
    assert not is_github_pull_request_url("https://github.com/yulia-sa/typing_challenges/pull")
    assert not is_github_pull_request_url("https://github.co/yulia-sa/typing_challenges/pull/1")
    assert not is_github_pull_request_url("https://github.com/yulia-sa/typing_challenges/pul/1")
    assert not is_github_pull_request_url("https:||github.com|yulia-sa|typing_challenges|pull|1")
    assert not is_github_pull_request_url("github.com/yulia-sa/typing_challenges/pull/1")
