#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Apply Some configurations 
python manage.py shell < site_config.py

# Create categories
python manage.py shell < create_categories.py

# Create product attributes
python manage.py shell < create_product_attributes.py

# Countries add
python manage.py oscar_populate_countries
