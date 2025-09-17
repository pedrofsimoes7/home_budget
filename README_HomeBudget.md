
# 🧾 HomeBudget — Personal Expenses Tracker (Django)

A simple **budget & expenses tracker** built with **Django**. It lets you register and log in, create **categories**, add **income/expense entries**, and view a **summary report**.

## ✨ Features
- 🔐 User registration & login (Django auth)
- ➕ Add income/expense entries (with date, category, value, comment)
- 🏷️ Category CRUD (create, edit, delete)
- 📊 Report view with aggregated totals (JSON endpoint for charts)
- 🏠 Clean home page and list views
- 🧱 SQLite database for quick local setup

## 📂 Project Structure (core parts)
```
homebudget/
├─ homebudget/              # Django project
│  ├─ homebudget/           # settings, urls
│  └─ mainapp/              # models, views, forms, templates
│
├─ templates/               # (resolved in app) multiple html files
├─ db.sqlite3               # local database (ignored in production)
└─ manage.py
```

## 🚀 Quickstart (Local)
> Requirements: Python 3.11+

```bash
# 1) Clone repository
git clone https://github.com/pedrofsimoes7/homebudget.git
cd homebudget

# 2) Create virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt  # (create it with `pip freeze > requirements.txt`)

# 4) Django setup
python manage.py migrate
python manage.py createsuperuser  # create admin user

# 5) Run
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## 🔧 Configuration
- `DEBUG=True` for local development (see `homebudget/homebudget/settings.py`).
- `SECRET_KEY` should be set via environment variable in production.
- Add your host to `ALLOWED_HOSTS` if deploying (e.g., on Render, Railway, or Vercel + Django).

## 🔐 Auth URLs
- `/register/` — sign up
- `/login/` — sign in
- `/logout/` — sign out

## 🌐 App URLs (main flows)
- `/` — home
- `/entries/` — list of entries
- `/entries/new/` — create new entry
- `/categories/` — list categories
- `/categories/add/` — add category
- `/categories/edit/<id>/` — edit category
- `/categories/delete/<id>/` — delete category
- `/report/` — report page
- `/report/data/` — JSON data for charts

## 🗃️ Tech Stack
- **Backend:** Django
- **DB:** SQLite (development)
- **Auth:** Django built-in authentication
- **Templates:** HTML (Django templates)

## 📝 License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE).
