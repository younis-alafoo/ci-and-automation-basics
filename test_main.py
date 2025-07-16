# test_main.py

import pytest
from main import add_to_cart, calculate_cart_total, apply_shipping, apply_payment_fee

def test_add_to_cart_valid_item():
    cart = []
    item = {'name': 'Wireless Mouse', 'price': 10.0}
    updated_cart = add_to_cart(cart, item)
    assert len(updated_cart) == 1
    assert updated_cart[0]['name'] == 'Wireless Mouse'

def test_add_to_cart_invalid_item():
    cart = []
    with pytest.raises(ValueError):
        add_to_cart(cart, {'name': 'No Price'})

def test_calculate_cart_total():
    cart = [{'name': 'Laptop Sleeve', 'price': 15.0}, {'name': 'USB Cable', 'price': 3.5}]
    total = calculate_cart_total(cart)
    assert total == 18.5

def test_apply_shipping_standard():
    total = apply_shipping(50.0, 'standard')
    assert total == 52.0

def test_apply_shipping_invalid_method():
    with pytest.raises(ValueError):
        apply_shipping(50.0, 'overnight')

def test_apply_payment_fee_credit_card():
    total = apply_payment_fee(100.0, 'credit_card')
    assert total == 101.0

def test_apply_payment_fee_benefit_pay():
    total = apply_payment_fee(100.0, 'benefit_pay')
    assert total == 100.0

def test_apply_payment_fee_invalid():
    with pytest.raises(ValueError):
        apply_payment_fee(100.0, 'paypal')
