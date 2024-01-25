def format_product_dict(element: dict) -> dict:
    """
    Перевод словаря с данными о продукте в формат,
    подходящий для записи в базу данных.

    Подходит только для таблицы, которая создается в скрипте
    saving_content/create_product_table_samokat.sql
    """

    formatted_element = {
        'id': element['id'],
        'name': element['name'],
        'price': element['price'],
        'has_discount': element['hasDiscount'],
        'old_price': element.get('oldPrice', None),
        'discount_percent': element.get('discountPercent', None),
        'quantity': element['quantity'],
        'is_available': element['isAvailable'],
        'highlights': ', '.join(element['highlights']),
        'preview_image': element['previewImage'],
        'has_variants': True if element.get('variants') else False
    }

    return formatted_element
