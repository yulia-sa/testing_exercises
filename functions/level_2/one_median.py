

def get_median_value(items: list[int]) -> int | None:
    """
    Вычисляет медиану списка целых чисел.

    Подробнее про медиану: https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%B8%D0%B0%D0%BD%D0%B0_(%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0)
    """
    if not items:
        return None

    sorted_items = sorted(items)

    middle_index = len(sorted_items) // 2 + 1
    if len(sorted_items) % 2:
        return items[middle_index]
    else:
        return (items[middle_index] + items[middle_index + 1]) // 2
