from app import create_app, db

# Create the app instance
app = create_app()

# Create all tables
with app.app_context():
    db.create_all()
    print("✅ SQLite database and tables created!")
