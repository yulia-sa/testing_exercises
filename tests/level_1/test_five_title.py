import pytest
from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    "title",
    [
        (
            "Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Мартышка съела все бананы!!!!!!!"
        ),
        (
            "Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Мартышка съела все бананы!!!!!!!!"
        ),
        (
            "Copy of Внимание! Внимание! Внимание! Внимание! Внимание! Внимание! Мартышка съела все бананы"
        )
    ]
)
def test__change_copy_item__with_exceed_len_limit(title):
    """
    Если длина (additional_copy_text + title) >= 100 символов —
    должны получить исходный title, вне зависимости от наличия в нем
    текста "Copy of".
    """
    assert change_copy_item(title) == title


def test__change_copy_item__without_exceed_len_limit():
    """
    Если длина (additional_copy_text + title) < 100 символов
    и title не начинается с additional_copy_text —
    должны получить title_with_additional_copy_text.
    """
    title_len_91_with_add_text_len_99 = \
        "Осторожно!!! Из зооопарка сбежали: крокодил, пантера, пара волков, олени и все работники!!!"
    assert change_copy_item(title_len_91_with_add_text_len_99) == \
        "Copy of Осторожно!!! Из зооопарка сбежали: крокодил, пантера, пара волков, олени и все работники!!!"


@pytest.mark.parametrize(
    "title,expected_result",
    [
        (
            "Copy of Бегемот переселился к волкам?!",
            "Copy of Бегемот переселился к волкам?! (2)"
        ),
        (
            "Copy of Бегемот переселился к волкам?! (Слухи)",
            "Copy of Бегемот переселился к волкам?! (Слухи) (2)"
        ),
        (
            "Copy of Бегемот переселился к волкам?! ()",
            "Copy of Бегемот переселился к волкам?! () (2)"
        )
    ]
)
def test__change_copy_item__without_num_in_brackets(title, expected_result):
    """
    Если длина (additional_copy_text + title) < 100 символов
    и title начинается с additional_copy_text
    и в конце title нет числа копий в скобках —
    должны получить title c (2) на конце.
    """
    assert change_copy_item(title) == expected_result


@pytest.mark.parametrize(
    "title,expected_result",
    [
        (
            "Copy of Бегемот переселился к волкам?! (2)",
            "Copy of Бегемот переселился к волкам?! (3)"
        ),
        (
            "Copy of Copy of Бегемот переселился к волкам?! (100)",
            "Copy of Copy of Бегемот переселился к волкам?! (101)"
        ),
    ]
)
def test__change_copy_item__with_num_in_brackets(title, expected_result):
    """
    Если длина (additional_copy_text + title) < 100 символов
    и title начинается с additional_copy_text
    и в конце title уже стоит число копий в скобках —
    должны получить title с увеличением на 1 числа копий.
    """
    assert change_copy_item(title) == expected_result


@pytest.mark.parametrize(
    "title",
    [
        (
            "Важная информация"
        ),
        (
            "Важная информация!"
        ),
        (
            "Copy of Важно!!!!"
        )
    ]
)
def test__change_copy_item__with_exceed_custom_len_limit(title, num=25):
    """
    Вместо дефолтного ограничения длины явно его указываем.

    Если длина (additional_copy_text + title) >= кастомного ограничения —
    должны получить исходный title, вне зависимости от наличия в нем
    текста "Copy of".
    """
    assert change_copy_item(title, num) == title


def test__change_copy_item__without_exceed_custom_len_limit():
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


def test__change_copy_item__without_num_in_brackets_custom_len_limit():
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


def test__change_copy_item__with_num_in_brackets_custom_len_limit():
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
