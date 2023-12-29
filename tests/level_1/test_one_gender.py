import pytest
from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male,verb_female,gender,expected_result_gender_verb",
    [
        ("Купил", "Купила", "male", "Купил"),
        ("Купил", "Купила", "female", "Купила")
    ]
)
def test_genderalize(verb_male,
                     verb_female,
                     gender,
                     expected_result_gender_verb):
    assert genderalize(verb_male,
                       verb_female,
                       gender) == expected_result_gender_verb
