import sys
import os
from myapp import app as application

# Add the project directory to the Python path
sys.path.insert(0, '/var/www/myapp')

# Set the Flask application environment
os.environ['FLASK_APP'] = 'myapp'

application = app
