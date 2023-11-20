from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    # Если длина additional_copy_text + title >= 100 символов — должны
    # получить исходный title, вне зависимости от наличия в нем "Copy of".
    title_len_92 = "Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Мартышка съела все бананы!!!!!!!"
    assert change_copy_item(title_len_92) == title_len_92
    title_len_93 = "Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Мартышка съела все бананы!!!!!!!!"
    assert change_copy_item(title_len_93) == title_len_93
    title_len_111 = "Copy of Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Мартышка съела все бананы!!!!!!!!"
    assert change_copy_item(title_len_111) == title_len_111

    # Если длина additional_copy_text + title < 100 символов и title
    # не начинается с additional_copy_text — должны получить
    # title_with_additional_copy_text.
    title_len_40 = "Осторожно! Из зооопарка сбежал крокодил!"
    assert change_copy_item(title_len_40) == "Copy of Осторожно! Из зооопарка сбежал крокодил!"
    title_len_45 = "Copy Осторожно! Из зооопарка сбежал крокодил!"
    assert change_copy_item(title_len_45) == "Copy of Copy Осторожно! Из зооопарка сбежал крокодил!"

    # Если длина additional_copy_text + title < 100 символов и title
    # начинается с additional_copy_text и в конце title нет числа
    # копий в скобках — должны получить title c (2) на конце.
    title_len_38 = "Copy of Бегемот переселился к волкам?!"
    assert change_copy_item(title_len_38) == "Copy of Бегемот переселился к волкам?! (2)"

    # Если длина additional_copy_text + title < 100 символов и title
    # начинается с additional_copy_text и в конце title уже стоит число
    # копий в скобках — должны получить title с увеличением на 1 числа копий.
    title_len_42 = "Copy of Бегемот переселился к волкам?! (2)"
    assert change_copy_item(title_len_42) == "Copy of Бегемот переселился к волкам?! (3)"
    title_len_52 = "Copy of Copy of Бегемот переселился к волкам?! (100)"
    assert change_copy_item(title_len_52) == "Copy of Copy of Бегемот переселился к волкам?! (101)"

    # Вместо дефолтного ограничения длины в 100 символов явно его указываем.
    title_len_17 = "Важная информация"
    assert change_copy_item(title_len_17, 20) == title_len_17
    title_len_5 = "Важно"
    assert change_copy_item(title_len_5, 20) == "Copy of Важно"
    title_len_13 = "Copy of Важно"
    assert change_copy_item(title_len_13, 25) == "Copy of Важно (2)"
    title_len_18 = "Copy of Важно (11)"
    assert change_copy_item(title_len_18, 30) == "Copy of Важно (12)"
