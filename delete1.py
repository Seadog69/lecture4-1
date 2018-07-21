import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db_connect_string = "postgresql://postgres:!JwQ=y92@localhost:5432/postgres"

app.config["SQLALCHEMY_DATABASE_URI"] = db_connect_string;
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.all()
    # get the last flight in the database based on its origin, destination and duration
    # f2 = db.session.query(flight).filter(flight.id == db.session.query(func.max(flight.id)))
    # db.session.delete(flight)
    # print(f"Deleted {f2.id} {f2.origin} from database")
    for flight in flights:
        print(f"{flight.id} {flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()
