from configparser import ConfigParser
from os import path

from group_expense_tracker.app import create_app

config = ConfigParser()
config.read([
    path.abspath('config.ini'),
    path.abspath('sample_config.ini')
])

app = create_app(config['DEFAULT'])
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)
