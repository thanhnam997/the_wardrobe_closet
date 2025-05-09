from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required,current_user
from .models import User, Category, Product
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from app.models import Order, OrderItem, CartItem, Product
from flask import request



bp = Blueprint('main', __name__)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("Email already registered. Please log in.", "error")
            return redirect(url_for('main.signup'))

        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please log in.")
        return redirect(url_for('main.login'))

    return render_template('signup.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully!")
            return redirect(url_for('main.index'))
        else:
            flash("Incorrect email or password.", "error")
            return redirect(url_for('main.login'))

    # ✅ Fix: Make sure GET requests return the login form
    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('main.index'))

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/profile')
@login_required
def profile():
    user_orders = current_user.orders
    order_data = []

    for order in user_orders:
        items = OrderItem.query.filter_by(order_id=order.id).all()
        products = [{
            'name': item.product.name,
            'image_url': item.product.image_url,
            'quantity': item.quantity,
            'price': item.price
        } for item in items]

        order_data.append({
            'id': order.id,
            'date': order.date,
            'total': order.total,
            'status': order.status,
            'products': products
        })

    return render_template('profile.html', user=current_user, orders=order_data)















@bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        new_name = request.form['name']
        new_email = request.form['email']

        # Optionally check if email already exists and isn't their current one
        if new_email != current_user.email:
            if User.query.filter_by(email=new_email).first():
                flash("Email already in use by another account.", "error")
                return redirect(url_for('main.edit_profile'))

        current_user.name = new_name
        current_user.email = new_email
        db.session.commit()
        flash("Profile updated successfully!")
        return redirect(url_for('main.profile'))

    return render_template('edit_profile.html', user=current_user)



#women's products
@bp.route('/women')
def women():
    return render_template('women/women.html')

@bp.route('/women/dresses')
def women_dresses():
    women_category = Category.query.filter_by(name='Women').first()
    products = Product.query.filter_by(category_id=women_category.id, subcategory='dresses').all()
    return render_template('women/dresses.html', products=products)

@bp.route('/women/jackets')
def women_jackets():
    women_category = Category.query.filter_by(name='Women').first()
    products = Product.query.filter_by(category_id=women_category.id, subcategory='jackets').all()
    return render_template('women/jackets.html', products=products)

@bp.route('/women/pants')
def women_pants():
    women_category = Category.query.filter_by(name='Women').first()
    products = Product.query.filter_by(category_id=women_category.id, subcategory='pants').all()
    return render_template('women/pants.html', products=products)

@bp.route('/women/shoes')
def women_shoes():
    women_category = Category.query.filter_by(name='Women').first()
    products = Product.query.filter_by(category_id=women_category.id, subcategory='shoes').all()
    return render_template('women/shoes.html', products=products)

@bp.route('/women/tops')
def women_tops():
    women_category = Category.query.filter_by(name='Women').first()
    products = Product.query.filter_by(category_id=women_category.id, subcategory='tops').all()
    return render_template('women/tops.html', products=products)




#men's products
@bp.route('/men')
def men():
    return render_template('men/men.html')


@bp.route('/men/tops')
def men_tops():
    men_category = Category.query.filter_by(name='Men').first()
    products = Product.query.filter_by(category_id=men_category.id, subcategory='tops').all()
    return render_template('men/men_tops.html', products=products)

@bp.route('/men/Pants')
def men_pants():
    men_category = Category.query.filter_by(name='Men').first()
    products = Product.query.filter_by(category_id=men_category.id, subcategory='pants').all()
    return render_template('men/men_pants.html', products=products)

@bp.route('/men/Shoes')
def men_shoes():
    men_category = Category.query.filter_by(name='Men').first()
    products = Product.query.filter_by(category_id=men_category.id, subcategory='shoes').all()
    return render_template('men/men_shoes.html',products=products)

@bp.route('/men/underwear&shock')
def men_underwearshock():
    men_category = Category.query.filter_by(name='Men').first()
    products = Product.query.filter_by(category_id=men_category.id, subcategory='underwear&shock').all()
    return render_template('men/men_underwear&shock.html', products=products)

@bp.route('/men/jackets')
def men_jackets():
    men_category = Category.query.filter_by(name='Men').first()
    products = Product.query.filter_by(category_id=men_category.id, subcategory='jackets').all()
    return render_template('men/men_jackets.html', products=products)






#accessories
@bp.route('/accessories')
def accessories():
    return render_template('accessories/accessories.html')

@bp.route('/accessories/hats')
def hats():
    accessories_category = Category.query.filter_by(name='Accessories').first()
    products = Product.query.filter_by(category_id= accessories_category.id, subcategory='hats').all()
    return render_template('accessories/hats.html', products=products)
   

@bp.route('/accessories/bags')
def bags():
    accessories_category = Category.query.filter_by(name='Accessories').first()
    products = Product.query.filter_by(category_id= accessories_category.id, subcategory='bags').all()
    return render_template('accessories/bags.html', products=products)


@bp.route('/accessories/watches')
def watches():
    accessories_category = Category.query.filter_by(name='Accessories').first()
    products = Product.query.filter_by(category_id= accessories_category.id, subcategory='watches').all()
    return render_template('accessories/watches.html', products=products)


@bp.route('/accessories/belts')
def belts():
    accessories_category = Category.query.filter_by(name='Accessories').first()
    products = Product.query.filter_by(category_id= accessories_category.id, subcategory='belts').all()
    return render_template('accessories/belts.html', products=products)
   

@bp.route('/accessories/jewelry')
def jewelry():
    accessories_category = Category.query.filter_by(name='Accessories').first()
    products = Product.query.filter_by(category_id= accessories_category.id, subcategory='jewelry').all()
    return render_template('accessories/jewelry.html', products=products)
    
    






@bp.route('/our-story')
def our_story():
    return render_template('our_story.html')

@bp.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@bp.route('/email-support')
def email_support():
    return render_template('email_support.html')

@bp.route('/live-chat')
def live_chat():
    return render_template('live_chat.html')

@bp.route('/call-us')
def call_us():
    return render_template('call_us.html')

@bp.route('/order-history')
def order_history():
    return render_template('order_history.html')

@bp.route('/faq')
def faq():
    return render_template('faq.html')

@bp.route('/returns')
def returns():
    return render_template('returns.html')

@bp.route('/shipping-info')
def shipping_info():
    return render_template('shipping_info.html')

#Cart
#Cart for guest
@bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)

    if 'user_id' not in session:
        cart = session.get('cart', {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        session['cart'] = cart
        session.modified = True
    else:
        user_id = session['user_id']
        cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += 1
        else:
            new_item = CartItem(user_id=user_id, product_id=product_id, quantity=1)
            db.session.add(new_item)
        db.session.commit()

    flash("Item added to cart!")
    return redirect(request.referrer or url_for('main.index'))


@bp.route('/cart')
def view_cart():
    cart_items = []
    if 'user_id' in session:
        user_id = session['user_id']
        items = CartItem.query.filter_by(user_id=user_id).all()
        cart_items = [{
            'id': item.id,
            'name': item.product.name,
            'price': item.product.price,
            'quantity': item.quantity,
            'image_url': item.product.image_url
        } for item in items]
    else:
        session_cart = session.get('cart', {})
        for pid, qty in session_cart.items():
            product = Product.query.get(int(pid))
            if product:
                cart_items.append({
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'quantity': qty,
                    'image_url': product.image_url
                })

    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)


@bp.route('/remove-from-cart/<int:item_id>', methods=['POST'])
def remove_from_cart(item_id):
    if 'user_id' in session:
        cart_item = CartItem.query.get_or_404(item_id)
        if cart_item.user_id != session['user_id']:
            flash('Unauthorized action', 'error')
            return redirect(url_for('main.view_cart'))
        db.session.delete(cart_item)
        db.session.commit()
    else:
        cart = session.get('cart', {})
        if str(item_id) in cart:
            del cart[str(item_id)]
            session['cart'] = cart
            session.modified = True

    flash('Item removed from cart.')
    return redirect(url_for('main.view_cart'))

@bp.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        if current_user.is_authenticated:
            # ✅ Fetch user's cart items
            cart_items = CartItem.query.filter_by(user_id=current_user.id).all()

            # ✅ Calculate total
            total = sum(item.quantity * item.product.price for item in cart_items)

            # ✅ Create a new order
            order = Order(user_id=current_user.id, status="Processing", total=total)
            db.session.add(order)
            db.session.commit()  # Save to generate order.id

            # ✅ Create order items
            for item in cart_items:
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=item.product.id,
                    quantity=item.quantity,
                    price=item.product.price
                )
                db.session.add(order_item)

            db.session.commit()  # Save all order items

            # ✅ Clear the user's cart
            CartItem.query.filter_by(user_id=current_user.id).delete()
            db.session.commit()

            flash("Order placed successfully!")
        else:
            # Handle guest checkout (optional)
            name = request.form.get('guest_name')
            email = request.form.get('guest_email')
            flash(f"Order placed for guest: {name} ({email})")
            session.pop('cart', None)

        return redirect(url_for('main.order_success'))

    return render_template('payment.html')


@bp.route('/order-success')
def order_success():
    return render_template('order_success.html')

@bp.route('/order-history-full')
@login_required
def order_history_full():
    user_orders = current_user.orders
    order_data = []

    for order in user_orders:
        items = OrderItem.query.filter_by(order_id=order.id).all()
        products = [{
            'name': item.product.name,
            'image_url': item.product.image_url,
            'quantity': item.quantity,
            'price': item.price
        } for item in items]

        order_data.append({
            'id': order.id,
            'date': order.date,
            'total': order.total,
            'status': order.status,
            'products': products
        })

    return render_template('order_history.html', orders=order_data)

#searching bar
@bp.route('/search')
def search():
    query = request.args.get('q')
    if query:
        products = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
    else:
        products = []
    return render_template('search_results.html', query=query, products=products)
