# Environment Variables (.env)

## Install python-dotenv
```bash
pip install python-dotenv
```

## Create .env file
Create `.env` in the same directory as `manage.py`:
```
SECRET_KEY='your-secret-key-from-settings'
STATIC_ROOT='path/to/static/folder'
```

## Update settings.py
```python
# settings.py - Add at top
from dotenv import load_dotenv
import os

load_dotenv()

# Update these settings
SECRET_KEY = os.getenv('SECRET_KEY')
STATIC_ROOT = os.getenv('STATIC_ROOT')
```
