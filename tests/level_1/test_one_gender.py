from functions.level_1.one_gender import genderalize


def test_genderalize_male():
    assert genderalize("Купил", "Купила", "male") == "Купил"


def test_genderalize_female():
    assert genderalize("Купил", "Купила", "female") == "Купила"
