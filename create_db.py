from app.models import User
from app import db, create_app
app = create_app()
app.app_context().push()
db.create_all(app=create_app())
user = User(username='nanmu', email='123@233.com')
user.set_password('233')
db.session.add(user)
db.session.commit()
