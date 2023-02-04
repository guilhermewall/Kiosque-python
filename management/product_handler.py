from menu import products


def get_product_by_id(id):
    if (type(id) == int):
        for elem in products:
            if (elem["_id"] == id):
                return elem
        return {}
    else:
        raise TypeError("product id must be an int")


def get_products_by_type(type_string):
    if (type(type_string) == str):
        products_found = []

        for elem in products:
            if (elem["type"] == type_string):
                products_found.append(elem)
        return products_found
    else:
        raise TypeError("product type must be a str")


def add_product(list_products: list, **kwargs):
    list_id = []
    if (len(list_products) > 0):
        for index, product in enumerate(products):
            list_id.append(products[index]["_id"])

        new_id = max(list_id) + 1
        new_product = {"_id": new_id, **kwargs}
        list_products.append(new_product)
        return new_product

    else:
        new_product = {"_id": 1, **kwargs}
        list_products.append(new_product)
        return new_product


def menu_report():
    product_count = len(products)
    price_products = []

    for product in products:
        price_products.append(product["price"])

    average_price = (sum(price_products) / product_count)
    types = []
    count_type = 0
    type_with_higher_occurence = ''

    for product in products:
        types.append(product["type"])

    print(average_price)
    for type_product in types:
        if (types.count(type_product) > count_type):
            type_with_higher_occurence = type_product
            count_type = types.count(type_product)
    return (f"Products Count: {product_count} - Average Price: ${average_price:.1f} - Most Common Type: {type_with_higher_occurence}")
