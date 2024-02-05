# Flask Finance Tracker

Flask Finance Tracker is a web application built with Flask that allows users to manage their finances and expenses.

## Features

- User registration and authentication
- Add, edit, and delete financial transactions
- View transaction history
- Generate reports and summaries
- ...

## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/fnyamweya/flask-finance-tracker.git
cd flask-finance-tracker
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create the SQLite database:

```bash
flask db init
flask db migrate
flask db upgrade

```

5. Configure the environment variables:

Create a .env file in the project root directory and add the following:

```bash
FLASK_APP=run.py
FLASK_ENV=development  # Change to "production" for production deployment
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///finance.db  # Update with your database URL

```

6. Run the application:

```bash
flask run

```