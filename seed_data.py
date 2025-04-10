from app import create_app, db
from app.models import Category, Product

app = create_app()

with app.app_context():
    # Create or get categories
    men = Category.query.filter_by(name="Men").first()
    women = Category.query.filter_by(name="Women").first()

    if not men:
        men = Category(name="Men")
        db.session.add(men)

    if not women:
        women = Category(name="Women")
        db.session.add(women)

    db.session.commit()

    # Add products for men
    men_products = [
        Product(name="Men's Denim Jacket", description="Classic blue jacket", price=59.99, stock=10, size="L", color="Blue", category_id=men.id),
        Product(name="Men's Cargo Pants", description="Comfortable and stylish", price=49.99, stock=8, size="M", color="Green", category_id=men.id),
    ]

    # Add products for women
    women_products = [
        Product(name="Women's Summer Dress", description="Light and breezy dress", price=39.99, stock=15, size="M", color="Yellow", category_id=women.id),
        Product(name="Women's Knit Sweater", description="Cozy and warm", price=44.99, stock=12, size="S", color="Beige", category_id=women.id),
    ]

    db.session.add_all(men_products + women_products)
    db.session.commit()

    print("✅ Products added successfully!")
