from flask import session

def init_cart():
    if 'cart' not in session:
        session['cart'] = {}

def add_to_cart(product_id, quantity=1):
    init_cart()
    pid = str(product_id)
    session['cart'][pid] = session['cart'].get(pid, 0) + quantity
    session.modified = True

def remove_from_cart(product_id):
    pid = str(product_id)
    session['cart'].pop(pid, None)
    session.modified = True

def update_cart(product_id, quantity):
    pid = str(product_id)
    if quantity <= 0:
        remove_from_cart(pid)
    else:
        session['cart'][pid] = quantity
    session.modified = True

def clear_cart():
    session.pop('cart', None)
    session.modified = True

def get_cart_items(product_model):
    init_cart()
    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = product_model.query.get(int(pid))
        if product:
            subtotal = round(product.price * qty, 2)
            items.append({'product': product, 'quantity': qty, 'total': subtotal})
            total += subtotal
    return items, total

