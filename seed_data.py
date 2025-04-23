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
    men_products = [ Product(name="Astronaut Graphic Tee",description="Cosmic vibes for space lovers.", price=24.99, stock=10, size="L", color="Black", subcategory="tops",image_url="men_page/top/astronaut.jpg",category_id=men.id),
                     Product( name="Crimson Fitted Tee",description="Deep red modern fit shirt.", price=19.99,stock=12,size="M",color="Crimson",subcategory="tops",image_url="men_page/top/crimson.jpg",category_id=men.id),
                     Product(name="Tropical Floral Shirt",description="Relaxed summer look.",price=29.99,stock=8,size="L",color="Navy",subcategory="tops",image_url="men_page/top/flower.jpg",category_id=men.id),
                     Product(name="Stan Smith Graphic Tee",description="Iconic Adidas style.",price=34.99,stock=10,size="XL", color="White",subcategory="tops",image_url="men_page/top/smith.jpg", category_id=men.id ),
                     Product(name="Classic White Tee", description="Essential plain white tee.", price=14.99, stock=20,size="M",color="White",subcategory="tops",image_url="men_page/top/whiteshirt.jpg", category_id=men.id),
                   ]

 # ✅ Add products for underwear & shock
    underwear_shock = [
        # Underwear
        Product(name="Nike Essential Micro Boxers (3PK)", description="Comfortable Nike micro boxers for everyday wear.",
                price=29.99, stock=15, size="M", color="Black", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/Nk-Esntl-MICRO-Box-3PK.jpg", category_id=men.id),
        Product(name="Men's Plaid Boxer Brief (2PK)", description="Classic plaid design, soft stretch cotton.",
                price=19.99, stock=10, size="L", color="Plaid", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/MENS+PLAID+BOXER+BRIEF+2PK.jpg", category_id=men.id),
        Product(name="Flight Modal Boxer Brief (3PK)", description="Lightweight breathable fit from Jordan.",
                price=34.99, stock=12, size="M", color="Black", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/FLIGHT+MODAL+3PK+BB.jpg", category_id=men.id),
        Product(name="Essential+ Micro Boxer Brief", description="Premium micro boxer with extra comfort.",
                price=24.99, stock=14, size="M", color="Gray", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/ESSENTIAL+MICRO.jpg", category_id=men.id),
     # Socks
        Product(name="White Ankle Socks", description="Soft breathable cotton socks.",
                price=9.99, stock=20, size="Free", color="White", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/whiteshock.jpg", category_id=men.id),
        Product(name="Camo Crew Socks", description="Stylish camo shock-absorbing socks.",
                price=12.99, stock=10, size="Free", color="Camo", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/camo.jpg", category_id=men.id),
        Product(name="Gray Ankle Socks", description="Everyday essential with soft texture.",
                price=9.99, stock=18, size="Free", color="Gray", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/grayshock.jpg", category_id=men.id),
        Product(name="Yellow High-Top Socks", description="Pop color high socks for bold look.",
                price=10.99, stock=12, size="Free", color="Yellow", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/yellowshock.jpg", category_id=men.id),
        Product(name="Black Sports Crew Socks", description="Cushioned and durable for training.",
                price=11.99, stock=14, size="Free", color="Black", subcategory="underwear&shock",
                image_url="men_page/underwear_shock/shockhightop.jpg", category_id=men.id),
    ]
    db.session.add_all(men_products + underwear_shock)           
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  # ✅ Add products for Women category
    women_products = [Product(name="Women's Summer Dress", description="Light and breezy dress", price=39.99, stock=15, size="M", color="Yellow", category_id=women.id), Product(name="Women's Knit Sweater", description="Cozy and warm", price=44.99, stock=12, size="S", color="Beige", category_id=women.id)]


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
