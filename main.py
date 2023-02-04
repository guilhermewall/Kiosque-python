from menu import products
from management import product_handler, tab_handler


my_product = {
    "title": "X-Python",
    "price": 5.0,
    "rating": 5,
    "description": "Sanduiche de Python",
    "type": "fast-food"
}

my_consumption = [{"_id": 25, "amount": 3}, {"_id": 8, "amount": 2}]


def main():
    print(product_handler.get_product_by_id(8))
    print(product_handler.get_products_by_type("vegetable"))
    print(product_handler.add_product(products, **my_product))
    print(tab_handler.calculate_tab(my_consumption))
    print(product_handler.menu_report())


if __name__ == "__main__":
    main()
