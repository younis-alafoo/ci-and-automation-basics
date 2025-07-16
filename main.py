# main.py

def add_to_cart(cart, item):
    """
    Adds an item to the cart.
    Item should be a dictionary with 'name' and 'price' keys.
    """
    if not isinstance(item, dict) or 'name' not in item or 'price' not in item:
        raise ValueError("Item must be a dict with 'name' and 'price'.")
    cart.append(item)
    return cart

def calculate_cart_total(cart):
    """
    Calculates the total price of all items in the cart.
    """
    return sum(item['price'] for item in cart)

def apply_shipping(cart_total, shipping_method):
    """
    Applies a flat shipping fee based on method.
    - 'standard': 2.0 BHD
    - 'express': 5.0 BHD
    """
    shipping_fees = {
        'standard': 2.0,
        'express': 5.0
    }
    fee = shipping_fees.get(shipping_method)
    if fee is None:
        raise ValueError("Unsupported shipping method.")
    return cart_total + fee

def apply_payment_fee(cart_total, method):
    """
    Adds a fee for specific payment methods.
    - 'credit_card': 1.0 BHD fee
    - 'cash_on_delivery': 0.5 BHD fee
    - 'benefit_pay': no fee
    """
    fees = {
        'credit_card': 1.0,
        'cash_on_delivery': 0.5,
        'benefit_pay': 0.0
    }
    fee = fees.get(method)
    if fee is None:
        raise ValueError("Unsupported payment method.")
    return cart_total + fee