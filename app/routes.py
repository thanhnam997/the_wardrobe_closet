from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required,current_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash



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
    user_orders = current_user.orders  # fetch related orders
    return render_template('profile.html', user=current_user, orders=user_orders)

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

@bp.route('/women')
def women():
    return render_template('women.html')

