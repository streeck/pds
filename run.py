import os
from bullet_journal import db
from bullet_journal.bullet_journal import create_app

app = create_app()

with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run()
