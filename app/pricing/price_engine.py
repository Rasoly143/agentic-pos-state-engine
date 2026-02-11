# Base drink and food prices
BASE_PRICES = {
    "Espresso": 3.00,
    "Americano": 3.50,
    "Drip Coffee": 2.50,
    "Latte": 4.50,
    "Cappuccino": 4.50,
    "Flat White": 4.75,
    "Mocha": 5.00,
    "Caramel Macchiato": 5.25,
    "Cold Brew": 4.25,
    "Iced Coffee": 3.00,
    "Frappe (Coffee)": 5.50,
    "Frappe (Mocha)": 5.75,
    "Strawberry Smoothie": 6.00,
    "Chai Latte": 4.75,
    "Matcha Latte": 5.25,
    "Earl Grey Tea": 3.00,
    "Green Tea": 3.00,
    "Hot Chocolate": 4.00,
    "Butter Croissant": 3.50,
    "Blueberry Muffin": 3.75,
    "Bagel": 2.50,
    "Avocado Toast": 7.00,
    "Bacon Gouda Sandwich": 5.50,
}

# Size adjustments
SIZE_ADJUSTMENTS = {
    "Short": -0.50,
    "Tall": 0.00,
    "Grande": 0.50,
    "Venti": 1.00,
    "Trenta": 1.50,
}

# Modifier pricing
MODIFIER_PRICES = {
    # Milks
    "Oat Milk": 0.80,
    "Almond Milk": 0.60,
    "Soy Milk": 0.60,
    "Coconut Milk": 0.70,
    "Breve (Half & Half)": 0.80,
    "Skim Milk": 0.00,

    # Syrups
    "Vanilla Syrup": 0.50,
    "Caramel Syrup": 0.50,
    "Hazelnut Syrup": 0.50,
    "Peppermint Syrup": 0.50,
    "Sugar Free Vanilla": 0.50,
    "Classic Syrup": 0.00,

    # Toppings
    "Extra Shot": 1.00,
    "Whip Cream": 0.50,
    "No Whip": 0.00,
    "Cold Foam": 1.25,
    "Caramel Drizzle": 0.50,
    "Extra Hot": 0.00,
    "Light Ice": 0.00,
    "No Ice": 0.00,
}

from decimal import Decimal, ROUND_HALF_UP


def calculate_item_price(name: str, size: str, quantity: int, modifiers: list):
    """
    Calculate total price for a single item.
    """

    # Base price
    base_price = Decimal(str(BASE_PRICES[name]))

    # Size adjustment (only if size exists)
    if size:
        size_adjustment = Decimal(str(SIZE_ADJUSTMENTS.get(size, 0.0)))
    else:
        size_adjustment = Decimal("0.00")

    # Modifier total
    modifier_total = Decimal("0.00")
    for mod in modifiers:
        modifier_total += Decimal(str(MODIFIER_PRICES.get(mod, 0.0)))

    # Single unit total
    unit_total = base_price + size_adjustment + modifier_total

    # Multiply by quantity
    total = unit_total * Decimal(str(quantity))

    # Round to 2 decimal places safely
    total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return total


def calculate_order_total(items: list):
    """
    Items format:
    [
        {
            "name": "...",
            "size": "...",
            "quantity": int,
            "modifiers": [...]
        }
    ]
    """

    grand_total = Decimal("0.00")

    for item in items:
        item_total = calculate_item_price(
            item["name"],
            item.get("size"),
            item["quantity"],
            item.get("modifiers", [])
        )
        grand_total += item_total

    grand_total = grand_total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return float(grand_total)
