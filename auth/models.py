from collector import db, app, bcrypt
from datetime import datetime
from sqlalchemy import exc


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    login = db.Column(db.String(30), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    date = db.Column(db.DateTime(timezone = True), default = lambda: datetime.now(), onupdate = datetime.now())

    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.set_password(password)

    def __repr__(self):
        return f"<User {self.login}>"

    def set_password(self, password: str) -> None:
        self.password = bcrypt.generate_password_hash(password).decode()

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password)


#todo check connection to DataBase
#* Test   
try:
    
    with app.app_context():
        db.create_all()
        
        # logging
        print("\n[Server-Postgres]\n\t✅ Successful connection to the database!\n\t✅ 200 OK\n[Server-Postgres]\n")
        
except exc.OperationalError as e:
    print(f"\n[Server-Postgers]\n\t❌ Connection error: \n{e}\t\n[Server-Postgers]\n") 
    
