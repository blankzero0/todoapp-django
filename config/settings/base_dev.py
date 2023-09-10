import secrets
from .base import BASE_DIR

try:
    with open(BASE_DIR / '.secret', 'r') as f:
        SECRET_KEY = f.read()
except OSError:
    SECRET_KEY = secrets.token_hex()
    with open(BASE_DIR / '.secret', 'w') as f:
        f.write(SECRET_KEY)
    
DEBUG = True
