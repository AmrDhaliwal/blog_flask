import os


class Config:
    SECRET_KEY = os.environ.get('8BYkEfBA6O6dufzWlSihBXox7C0sKR6b')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
