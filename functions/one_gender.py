def genderalize(verb_male: str, verb_female: str, gender: str) -> str:
    return verb_male if gender == "male" else verb_female
