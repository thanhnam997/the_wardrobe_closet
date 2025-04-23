from app import create_app, db
from app.models import Category, Product, Order

# Create the Flask app instance
app = create_app()

# Use application context to access the database
with app.app_context():
    # ❌ Clear existing data to avoid duplication
    Order.query.delete()
    Product.query.delete()
    Category.query.delete()
    db.session.commit()

    # ✅ Create categories
    men = Category(name="Men")
    women = Category(name="Women")
    db.session.add_all([men, women])
    db.session.commit()

    # ✅ Add products for Men category
    men_products = [
        Product(
            name="Astronaut Graphic Tee",
            description="Cosmic vibes for space lovers.",
            price=24.99,
            stock=10,
            size="L",
            color="Black",
            subcategory="tops",
            image_url="men_page/top/astronaut.jpg",
            category_id=men.id
        ),
        Product(
            name="Crimson Fitted Tee",
            description="Deep red modern fit shirt.",
            price=19.99,
            stock=12,
            size="M",
            color="Crimson",
            subcategory="tops",
            image_url="men_page/top/crimson.jpg",
            category_id=men.id
        ),
        Product(
            name="Tropical Floral Shirt",
            description="Relaxed summer look.",
            price=29.99,
            stock=8,
            size="L",
            color="Navy",
            subcategory="tops",
            image_url="men_page/top/flower.jpg",
            category_id=men.id
        ),
        Product(
            name="Stan Smith Graphic Tee",
            description="Iconic Adidas style.",
            price=34.99,
            stock=10,
            size="XL",
            color="White",
            subcategory="tops",
            image_url="men_page/top/smith.jpg",
            category_id=men.id
        ),
        Product(
            name="Classic White Tee",
            description="Essential plain white tee.",
            price=14.99,
            stock=20,
            size="M",
            color="White",
            subcategory="tops",
            image_url="men_page/top/whiteshirt.jpg",
            category_id=men.id
        ),
    ]

    # ✅ Add products for Women category
    women_products = [
        Product(
            name="Women's Summer Dress",
            description="Light and breezy dress",
            price=39.99,
            stock=15,
            size="M",
            color="Yellow",
            category_id=women.id
        ),
        Product(
            name="Women's Knit Sweater",
            description="Cozy and warm",
            price=44.99,
            stock=12,
            size="S",
            color="Beige",
            category_id=women.id
        ),
    ]

    # ✅ Insert all products into the database
    db.session.add_all(men_products + women_products)
    db.session.commit()
    print("✅ Products added successfully!")

    # ✅ Optionally add some sample orders
    order1 = Order(user_id=1, status="Delivered")
    order2 = Order(user_id=1, status="Processing")
    db.session.add_all([order1, order2])
    db.session.commit()
    print("✅ Orders added successfully!")
