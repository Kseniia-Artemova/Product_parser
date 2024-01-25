def format_product_dict(element):
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
