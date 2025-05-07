ABOUT THE PROJECT
The Wardrobe Closet 🛍️

Welcome to The Wardrobe Closet, a fully functional online fashion store built with Flask. This application lets customer browse products, add them to a cart, register/login, and checkout with order tracking. 

This project was built as a capstone for coursework and serves as a foundation for a scalable e-commerce platform.

🛠️ Built With
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Migrate
- Jinja2
- SQLite
- HTML5, CSS3

🚀 Getting Started
To get a local copy up and running, follow these simple steps.

Prerequisites
- Python 3.10+
- Virtual environment (optional but recommended)

Installation
- Clone the repo
- git clone https://github.com/your_username/the_wardrobe_closet.git
- cd the_wardrobe_closet

Set up a virtual environment
- python -m venv venv
- source venv/bin/activate

Install dependencies
- pip install -r requirements.txt

Set up the database
- flask db init
- flask db migrate -m "Initial migration"
- flask db upgrade

Run the app
- python run.py 

Usage
- View products by category: /men, /women, /accessories
- Add products to cart (works for guests and logged-in users)
- Manage cart: update quantities, remove items, and checkout
- User account: register, login, edit profile, view order history


