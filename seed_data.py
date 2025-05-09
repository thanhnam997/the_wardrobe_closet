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
    accessories = Category(name="Accessories")
    db.session.add_all([men, women,accessories])
    db.session.commit()

    # Refresh categories to ensure we have IDs
    men = Category.query.filter_by(name="Men").first()
    women = Category.query.filter_by(name="Women").first()
    accessories = Category.query.filter_by(name="Accessories").first()
   
   
   
   
   
# Add products for Men category
    men_products = [
       Product(name="Astronaut Graphic Tee", description="Cosmic vibes for space lovers.",
              price=24.99, stock=10, size="L", color="Black", subcategory="tops",
              image_url="men_page/top/astronaut.jpg", category_id=men.id),
       Product(name="Crimson Fitted Tee", description="Deep red modern fit shirt.",
              price=19.99, stock=12, size="M", color="Crimson", subcategory="tops",
              image_url="men_page/top/crimson.jpg", category_id=men.id),
       Product(name="Tropical Floral Shirt", description="Relaxed summer look.",
              price=29.99, stock=8, size="L", color="Navy", subcategory="tops",
              image_url="men_page/top/flower.jpg", category_id=men.id),
       Product(name="Stan Smith Graphic Tee", description="Iconic Adidas style.",
              price=34.99, stock=10, size="XL", color="White", subcategory="tops",
              image_url="men_page/top/smith.jpg", category_id=men.id),
       Product(name="Classic White Tee", description="Essential plain white tee.",
              price=14.99, stock=20, size="M", color="White", subcategory="tops",
              image_url="men_page/top/whiteshirt.jpg", category_id=men.id)
       ]

# Add underwear & socks
    underwear_shock = [
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
              image_url="men_page/underwear_shock/shockhightop.jpg", category_id=men.id)
       ]

# Add jackets
    jackets = [
       Product(name="Black Neon Jacket", description="High-tech jacket with neon accents.",
              price=129.99, stock=5, size="L", color="Black/Red", subcategory="jackets",
              image_url="men_page/jackets/Jacket-mockupmens-jacket-mockup-b.jpg", category_id=men.id),
       Product(name="Gray Yellow Utility Jacket", description="Reflective utility jacket with yellow highlights.",
              price=139.99, stock=4, size="M", color="Gray/Yellow", subcategory="jackets",
              image_url="men_page/jackets/Jacket-sticker-mockup-c.jpg", category_id=men.id),
       Product(name="Classic Black Leather Jacket", description="Timeless leather jacket.",
              price=149.99, stock=6, size="L", color="Black", subcategory="jackets",
              image_url="men_page/jackets/Hanging-jacket-mockupjacket-a.jpg", category_id=men.id),
       Product(name="Minimalist White Jacket", description="Clean white style.",
              price=119.99, stock=7, size="M", color="White", subcategory="jackets",
              image_url="men_page/jackets/Mens-white-jacket-front-mockup-d.jpg", category_id=men.id)
       ]

# Add shoes
    shoes = [
       Product(name="Adidas Forum Low", description="Classic Adidas sneaker with velcro strap.",
              price=79.99, stock=8, size="10", color="White/Black", subcategory="shoes",
              image_url="men_page/shoes/adidas.jpg", category_id=men.id),
       Product(name="Nike Dunk High", description="High-top sneakers with bold yellow-black styling.",
              price=99.99, stock=6, size="11", color="Yellow/Black", subcategory="shoes",
              image_url="men_page/shoes/nike.jpg", category_id=men.id),
       Product(name="Puma Red Stripe", description="Sporty low-cut Puma sneakers with red stripe.",
              price=69.99, stock=10, size="10", color="White/Red", subcategory="shoes",
              image_url="men_page/shoes/puma.jpg", category_id=men.id),
       Product(name="Puma Clean White", description="Minimalist white Puma sneakers with subtle lining.",
              price=64.99, stock=12, size="9", color="White", subcategory="shoes",
              image_url="men_page/shoes/pumawhite.jpg", category_id=men.id)
       ]

# Add pants
    pants = [
       Product(name="Camo Baggy Jeans", description="Stylish camo print with a relaxed fit.",
              price=49.99, stock=10, size="M", color="Camo", subcategory="pants",
              image_url="men_page/pants/camo_baggy_jeans.jpg", category_id=men.id),
       Product(name="Super Baggy Jeans", description="Extra loose fit for ultimate comfort.",
              price=44.99, stock=12, size="L", color="Denim", subcategory="pants",
              image_url="men_page/pants/super_baggy_jeans.jpg", category_id=men.id),
       Product(name="Slim Black Jeans", description="Minimal and modern black jeans.",
              price=39.99, stock=15, size="M", color="Black", subcategory="pants",
              image_url="men_page/pants/slim_black_jeans.jpg", category_id=men.id)
       ]


# Add women's products

# Women's Dresses
    women_dresses = [
       Product(name="Halter Neck Cotton Dress", description="Breezy cotton halter dress for summer days.",
              price=49.99, stock=10, size="M", color="White", subcategory="dresses",
              image_url="women_page/dresses/halter_neck_cotton_dress.png", category_id=women.id),
       Product(name="Lyocell V-Neck Dress", description="Light and soft lyocell dress with v-neck detail.",
              price=59.99, stock=8, size="S", color="Light Blue", subcategory="dresses",
              image_url="women_page/dresses/lyocell_v_neck_dress.png", category_id=women.id),
       Product(name="Short Button Dress", description="Cute short dress with button accents.",
              price=54.99, stock=12, size="M", color="Pink", subcategory="dresses",
              image_url="women_page/dresses/short_button_dress.png", category_id=women.id),
       Product(name="Strapless Polka Dress", description="Fun strapless dress with classic polka dots.",
              price=44.99, stock=10, size="L", color="Black/White", subcategory="dresses",
              image_url="women_page/dresses/strapless_polka_dress.png", category_id=women.id)
       ]

# Women's Jackets
    women_jackets = [
       Product(name="Doubleside Leather Jacket with Pockets", description="Stylish leather jacket, dual side wear.",
              price=129.99, stock=9, size="M", color="Black/Brown", subcategory="jackets",
              image_url="women_page/jackets/doubleside_leather_with_pockets.png", category_id=women.id),
       Product(name="Linen Jacket with Belt", description="Light linen jacket perfect for spring days.",
              price=89.99, stock=7, size="S", color="Cream", subcategory="jackets",
              image_url="women_page/jackets/linen_jacket_belt.png", category_id=women.id),
       Product(name="Long Structured Wool Coat", description="Elegant wool coat for colder weather.",
              price=149.99, stock=6, size="M", color="Gray", subcategory="jackets",
              image_url="women_page/jackets/long_structured_wool_coat.png", category_id=women.id),
       Product(name="Quilted Mini Anorak with Hood", description="Cozy quilted jacket with hood.",
              price=119.99, stock=5, size="L", color="Olive Green", subcategory="jackets",
              image_url="women_page/jackets/quilted_mini_anorak_with_hood.png", category_id=women.id)
       ]

# Women's Pants
    women_pants = [
       Product(name="Bow Straight Trousers", description="Elegant straight trousers with bow accent.",
              price=59.99, stock=10, size="M", color="Navy Blue", subcategory="pants",
              image_url="women_page/pants/bow_straight_trousers.png", category_id=women.id),
       Product(name="Catherine Culotte High Rise Jeans", description="Trendy high-rise culotte jeans.",
              price=64.99, stock=12, size="S", color="Light Blue", subcategory="pants",
              image_url="women_page/pants/catherin_culotte_high_rise_jeans.png", category_id=women.id),
       Product(name="High Rise Balloon Jeans", description="Relaxed fit balloon-style high rise jeans.",
              price=69.99, stock=8, size="M", color="Denim Blue", subcategory="pants",
              image_url="women_page/pants/high_rise_balloon_jeans.png", category_id=women.id),
       Product(name="Wideleg Pleated Pants", description="Chic wide-leg pants with pleated front.",
              price=54.99, stock=14, size="L", color="Black", subcategory="pants",
              image_url="women_page/pants/wideleg_pleated_pant.png", category_id=women.id)
       ]

# Women's Shoes
    women_shoes = [
       Product(name="Contrast Panel Sneakers", description="Sporty sneakers with contrast panel design.",
              price=74.99, stock=9, size="7", color="White/Gray", subcategory="shoes",
              image_url="women_page/shoes/contrast_panel_sneakers.png", category_id=women.id),
       Product(name="Cotton Ballet Flats", description="Comfortable and breathable cotton flats.",
              price=59.99, stock=7, size="8", color="Beige", subcategory="shoes",
              image_url="women_page/shoes/cotton_ballet_flats.png", category_id=women.id),
       Product(name="Strappy Heeled Sandals", description="Stylish strappy sandals with moderate heel.",
              price=69.99, stock=10, size="7.5", color="Black", subcategory="shoes",
              image_url="women_page/shoes/strappy_heeled_sandals.png", category_id=women.id),
       Product(name="Suede Block Heel Ankle Boots", description="Soft suede ankle boots with block heel.",
              price=89.99, stock=11, size="8", color="Brown", subcategory="shoes",
              image_url="women_page/shoes/suede_block_heel_ankle_boots.png", category_id=women.id)
       ]

# Women's Tops
    women_tops = [
       Product(name="Knit Asymmetric Top", description="Trendy knit top with asymmetric cut.",
              price=39.99, stock=15, size="M", color="White", subcategory="tops",
              image_url="women_page/tops_tshirts/knit_asymmetric_top.png", category_id=women.id),
       Product(name="Knot Hem Cotton Top", description="Casual cotton top with cute knot hem design.",
              price=34.99, stock=12, size="S", color="Sky Blue", subcategory="tops",
              image_url="women_page/tops_tshirts/knot_hem_cotton_top.png", category_id=women.id),
       Product(name="Short Sleeved Cotton Polo", description="Classic short-sleeved cotton polo shirt.",
              price=29.99, stock=18, size="M", color="Light Pink", subcategory="tops",
              image_url="women_page/tops_tshirts/short_sleeved_cotton_polo.png", category_id=women.id),
       Product(name="Short Sleeved Printed T-shirt", description="Fun printed tee for everyday casual wear.",
              price=24.99, stock=10, size="L", color="Multi-color", subcategory="tops",
              image_url="women_page/tops_tshirts/short_sleeved_printed_tshirt.png", category_id=women.id)
       ]    


# Add accessories

# Bags
    bags = [
       Product(name="Rainbow Sophia Bag", description="Colorful rainbow print personalized tote.",
              price=19.99, stock=10, size="One Size", color="White", subcategory="bags",
              image_url="accessories/bags/rainbow_bag.jpg", category_id=accessories.id),
       Product(name="Momager Tote", description="Stylish tote for the ultimate mom manager.",
              price=21.99, stock=8, size="One Size", color="Cream", subcategory="bags",
              image_url="accessories/bags/momager_bag.jpg", category_id=accessories.id),
       Product(name="Napa Valley Tote", description="Vintage style Napa Valley branded tote.",
              price=24.99, stock=6, size="One Size", color="Natural", subcategory="bags",
              image_url="accessories/bags/napa_valley_bag.jpg", category_id=accessories.id)
       ]
    db.session.add_all(bags)
    db.session.commit()
    print("✅ Bags added!")

# Hats
    hats = [
       Product(name="Captain Jeremy Hat", description="Nautical theme trucker hat with anchor.",
              price=17.99, stock=12, size="Adjustable", color="Navy/White", subcategory="hats",
              image_url="accessories/hats/captain_jeremy_hat.jpg", category_id=accessories.id),
       Product(name="Your Logo Hat", description="Custom logo colorful print trucker hat.",
              price=16.99, stock=15, size="Adjustable", color="White", subcategory="hats",
              image_url="accessories/hats/your_logo_hat.jpg", category_id=accessories.id),
       Product(name="Golf Club Hat", description="Classic personalized golf club trucker hat.",
              price=18.99, stock=10, size="Adjustable", color="Black/White", subcategory="hats",
              image_url="accessories/hats/golf_club_hat.jpg", category_id=accessories.id)
       ]
    db.session.add_all(hats)
    db.session.commit()
    print("✅ Hats added!")

# Belts
    belts = [
       Product(name="Classic Brown Leather Belt", description="Traditional brown leather belt with sturdy buckle.",
              price=34.99, stock=10, size="M", color="Brown", subcategory="belts",
              image_url="accessories/belts/Classic Brown Leather Belt.jpg", category_id=accessories.id),
       Product(name="Dark Brown Heritage Belt", description="Premium leather with vintage finish.",
              price=39.99, stock=8, size="L", color="Dark Brown", subcategory="belts",
              image_url="accessories/belts/Dark Brown Heritage Belt.jpg", category_id=accessories.id),
       Product(name="Black Patterned Belt", description="Textured leather design with modern stitching.",
              price=42.99, stock=6, size="M", color="Black", subcategory="belts",
              image_url="accessories/belts/Black Patterned Belt.jpg", category_id=accessories.id)
       ]
    db.session.add_all(belts)
    db.session.commit()
    print("✅ Belts added!")

# Jewelry
    jewelry = [
       Product(name="Patriotic Flag Bracelet", description="Silver bracelet with American flag charm.",
              price=14.99, stock=15, size="One Size", color="Silver/Red/Blue", subcategory="jewelry",
              image_url="accessories/jewelry/Flag Bracelet.jpg", category_id=accessories.id),
       Product(name="Gold Heart Bracelet", description="Elegant gold bracelet with a heart charm.",
              price=24.99, stock=12, size="One Size", color="Gold", subcategory="jewelry",
              image_url="accessories/jewelry/Heart Bracelet.jpg", category_id=accessories.id),
       Product(name="Pearl Heart Earrings", description="Classy pearl earrings with heart detail.",
              price=29.99, stock=10, size="One Size", color="White/Gold", subcategory="jewelry",
              image_url="accessories/jewelry/Pearl Heart Earrings.jpg", category_id=accessories.id)
       ]
    db.session.add_all(jewelry)
    db.session.commit()
    print("✅ Jewelry added!")

# Watches
    watches = [
       Product(name="Floral Stripe Apple Watch Band", description="Stylish watch band with black & white stripes and floral pattern.",
              price=29.99, stock=10, size="One Size", color="Black/White/Floral", subcategory="watches",
              image_url="accessories/watches/Floral Stripe Apple Watch Band.jpg", category_id=accessories.id),
       Product(name="Minimalist White Wristwatch", description="Elegant white leather strap with rose gold accents.",
              price=74.99, stock=7, size="One Size", color="White/Rose Gold", subcategory="watches",
              image_url="accessories/watches/Minimalist White Wristwatch.jpg", category_id=accessories.id),
       Product(name="Engraved Watch Box Set", description="Watch gift box with engraved glass display cover.",
              price=89.99, stock=5, size="Box Set", color="Black", subcategory="watches",
              image_url="accessories/watches/Engraved Watch Box Set.jpg", category_id=accessories.id)
       ]

    db.session.add_all(watches)
    db.session.commit()
    print("✅ Watches added successfully!")

       # Insert all products
    all_men_products = men_products + underwear_shock + jackets + shoes + pants
    all_women_products = women_dresses + women_jackets + women_pants + women_shoes + women_tops
    all_accessories = bags + hats + belts + jewelry + watches

    db.session.add_all(all_men_products + all_women_products + all_accessories)
    db.session.commit()
    print(f"✅ {len(all_men_products)} men's products added successfully!")
    print(f"✅ {len(all_women_products)} women's products added successfully!")
    print(f"✅ {len(all_accessories)} accessories added successfully!")


