from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize("Купил", "Купила", "male") == "Купил"
    assert genderalize("Купил", "Купила", "female") == "Купила"
