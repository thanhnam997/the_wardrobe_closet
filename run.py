from app import create_app
from seed_data import seed_all
app = create_app()

if __name__ == '__main__':
   
    print("🌱 Seeding database...")
    seed_all()
    print("🚀 Starting Flask server...")
    app.run(debug=True)
