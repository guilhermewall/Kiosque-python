from menu import products


def calculate_tab(consumption):
    result = 0
    for product in products:
        for elem in consumption:
            if (product["_id"] == elem["_id"]):
                result += product["price"] * elem["amount"]
    return {"subtotal": f"${round(result, 2)}"}
