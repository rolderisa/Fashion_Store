from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
import os

# Set up Django's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the Django WSGI application
django_app = get_wsgi_application()

# Create FastAPI instance
app = FastAPI(title="Fashion Store API")

# Example API endpoints
@app.get("/api/products")
async def get_products():
    return {"products": ["Product 1", "Product 2", "Product 3"]}

@app.get("/api/cart")
async def get_cart():
    return {"cart_items": []}

# Mount Django app
app.mount("/", WSGIMiddleware(django_app))

# Don't include this line anymore:
# app.mount("/", WSGIMiddleware(django_app))