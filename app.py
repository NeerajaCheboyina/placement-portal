from flask import Flask
from config import Config
from models import db, Admin   # <-- IMPORTANT FIX

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return "Placement Portal Database Setup Successful!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        existing_admin = Admin.query.filter_by(username="admin").first()

        if not existing_admin:
            default_admin = Admin(
                username="admin",
                password="admin123"
            )
            db.session.add(default_admin)
            db.session.commit()
            print("Default Admin Created!")
        else:
            print("Admin already exists.")

    app.run(debug=True)