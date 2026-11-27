# GreatKart

GreatKart is a Django storefront project for browsing products, managing a shopping cart, and placing orders. It includes account registration and login, product categories and reviews, customer profiles, and order history.

## Features

- Browse and search products, with category pages and product details
- Register, log in, activate accounts by email, and reset passwords
- Add products and variations to a cart, then check out
- Place orders and view order details and history
- Manage products, categories, accounts, and orders through Django admin

## Project structure

- `greatkart/` — Django settings, root URLs, and application entry points
- `accounts/` — custom user accounts, profiles, and account views
- `category/` — product categories
- `store/` — products, variations, galleries, and reviews
- `carts/` — shopping cart
- `orders/` — orders and payment records
- `templates/` — storefront, account, cart, and order templates
- `static/` — CSS, JavaScript, fonts, and images
- `media/` — uploaded images during local development

## Requirements

- Python compatible with the Django version pinned in `requirements.txt`
- PostgreSQL, configured with the database settings listed below

Install the Python dependencies from the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Configuration

The project reads its database and email configuration from environment variables (a local `.env` file can be used). Create a PostgreSQL database, then configure these settings:

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Django secret key |
| `PGDB_ENGINE` | Database backend; use `django.db.backends.postgresql` for PostgreSQL |
| `PGDB_NAME` | PostgreSQL database name |
| `PGDB_USER` | PostgreSQL username |
| `PGDB_PASS` | PostgreSQL password |
| `PGDB_HOST` | PostgreSQL host |
| `PGDB_PORT` | PostgreSQL port, usually `5432` |
| `DEBUG` | Development debug setting |
| `ALLOWED_HOSTS` | Hosts allowed to serve the project |
| `EMAIL_BACKEND` | Email backend; Django's console backend is useful locally |

Keep real credentials in your local environment and out of version control. Review `greatkart/settings.py` for the full set of supported settings.

## Run locally

From the repository root, with the virtual environment active and PostgreSQL running:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the storefront. The admin interface is routed at `/beh/`.

## Tests

Run the Django test suite with:

```bash
python manage.py test
```

## Author

**behrouzyou@github.com**
