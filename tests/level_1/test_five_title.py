from functions.level_1.five_title import change_copy_item


def test_change_copy_item_with_exceed_len_limit():
    """
    Если длина (additional_copy_text + title) >= 100 символов —
    должны получить исходный title, вне зависимости от наличия в нем
    текста "Copy of".
    """
    title_len_92_with_add_text_len_100 = \
        "Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Мартышка съела все бананы!!!!!!!"
    assert change_copy_item(title_len_92_with_add_text_len_100) == \
        title_len_92_with_add_text_len_100
    title_len_93_with_add_text_len_101 = \
        "Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Мартышка съела все бананы!!!!!!!!"
    assert change_copy_item(title_len_93_with_add_text_len_101) == \
        title_len_93_with_add_text_len_101


def test_change_copy_item_without_exceed_len_limit():
    """
    Если длина (additional_copy_text + title) < 100 символов
    и title не начинается с additional_copy_text —
    должны получить title_with_additional_copy_text.
    """
    title_len_91_with_add_text_len_99 = \
        "Осторожно!!! Из зооопарка сбежали: крокодил, пантера, пара волков, олени и все работники!!!"
    assert change_copy_item(title_len_91_with_add_text_len_99) == \
        "Copy of Осторожно!!! Из зооопарка сбежали: крокодил, пантера, пара волков, олени и все работники!!!"


def test_change_copy_item_without_num_in_brackets():
    """
    Если длина (additional_copy_text + title) < 100 символов
    и title начинается с additional_copy_text
    и в конце title нет числа копий в скобках —
    должны получить title c (2) на конце.
    """
    title_len_38_with_add_text_len_46 = \
        "Copy of Бегемот переселился к волкам?!"
    assert change_copy_item(title_len_38_with_add_text_len_46) == \
        "Copy of Бегемот переселился к волкам?! (2)"
    title_len_with_add_text_len_54 = \
        "Copy of Бегемот переселился к волкам?! (Слухи)"
    assert change_copy_item(title_len_with_add_text_len_54) == \
        "Copy of Бегемот переселился к волкам?! (Слухи) (2)"
    title_len_41_with_add_text_len_49 = \
        "Copy of Бегемот переселился к волкам?! ()"
    assert change_copy_item(title_len_41_with_add_text_len_49) == \
        "Copy of Бегемот переселился к волкам?! () (2)"


def test_change_copy_item_with_num_in_brackets():
    """
    Если длина (additional_copy_text + title) < 100 символов
    и title начинается с additional_copy_text
    и в конце title уже стоит число копий в скобках —
    должны получить title с увеличением на 1 числа копий.
    """
    title_len_42_with_add_text_len_50 = \
        "Copy of Бегемот переселился к волкам?! (2)"
    assert change_copy_item(title_len_42_with_add_text_len_50) == \
        "Copy of Бегемот переселился к волкам?! (3)"
    title_len_52_with_add_text_len_60 = \
        "Copy of Copy of Бегемот переселился к волкам?! (100)"
    assert change_copy_item(title_len_52_with_add_text_len_60) == \
        "Copy of Copy of Бегемот переселился к волкам?! (101)"


def test_change_copy_item_with_exceed_custom_len_limit():
    """
    Вместо дефолтного ограничения длины явно его указываем.

    Если длина (additional_copy_text + title) >= кастомного ограничения —
    должны получить исходный title.
    """
    title_len_17_with_add_text_len_25 = \
        "Важная информация"
    assert change_copy_item(title_len_17_with_add_text_len_25, 25) == \
        title_len_17_with_add_text_len_25
    title_len_18_with_add_text_len_26 = \
        "Важная информация!"
    assert change_copy_item(title_len_18_with_add_text_len_26, 25) == \
        title_len_18_with_add_text_len_26


def test_change_copy_item_without_exceed_custom_len_limit():
    """
    Вместо дефолтного ограничения длины явно его указываем.

    Если длина (additional_copy_text + title) < кастомного ограничения
    и title не начинается с additional_copy_text —
    должны получить title_with_additional_copy_text.
    """
    title_len_5_with_add_text_len_13 = \
        "Важно"
    assert change_copy_item(title_len_5_with_add_text_len_13, 14) == \
        "Copy of Важно"


def test_change_copy_item_without_num_in_brackets_custom_len_limit():
    """
    Если длина (additional_copy_text + title) < кастомного ограничения
    и title начинается с additional_copy_text
    и в конце title нет числа копий в скобках —
    должны получить title c (2) на конце.
    """
    title_len_13_with_add_text_len_21 = \
        "Copy of Важно"
    assert change_copy_item(title_len_13_with_add_text_len_21, 22) == \
        "Copy of Важно (2)"


def test_change_copy_item_with_num_in_brackets_custom_len_limit():
    """
    Если длина (additional_copy_text + title) < кастомного ограничения
    и title начинается с additional_copy_text
    и в конце title уже стоит число копий в скобках —
    должны получить title с увеличением на 1 числа копий.
    """
    title_len_18_with_add_text_len_26 = \
        "Copy of Важно (11)"
    assert change_copy_item(title_len_18_with_add_text_len_26, 27) == \
        "Copy of Важно (12)"
