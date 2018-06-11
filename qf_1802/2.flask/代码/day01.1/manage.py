
from flask_script import Manager

from utils.functions import create_app

app = create_app()

manege = Manager(app=app)

if __name__ == '__main__':
    manege.run()

