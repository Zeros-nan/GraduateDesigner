from models import db, User
db.create_all()
user = User(username='nanmu', email='123@233.com')
user.set_password('233')
db.session.add(user)
db.session.commit()
