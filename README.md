# Currencies exchange service


Currency Exchange is a Flask-based web application that allows users to track and monitor exchange rates for various currencies. It provides historical data and real-time information for currencies of interest.

## Features

- View historical exchange rates for specific currencies.
- Get real-time exchange rates for a selected currency.
- Automatically update exchange rates on a regular schedule.
- Track changes in currency values over time.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)
- PostgreSQL database

### Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/YKonoplyov/currencies.git
   ```
2. Create a virtual environment:
    ```shell
   python -m venv venv
   ```
    and activate it:
    on windows
   ```shell
   venv\Scripts\activate 
   ```
   on macOS or Linux:
    ```shell
    source venv/bin/activate 
    ```
3. Install the required Python packages:
    ```shell
    pip install -r requirements.txt
    ```
4. Configure the application by setting environment variables:
    ```
    POSTGRES_URL - url of your postgres db
    API_KEY - key for sending request to exchange api. To get one visit [ExchangeRate-API](https://www.exchangerate-api.com/) page
   ```
5. Apply migrations for database:
    ```shell
   flask db upgrade
    ```
6. Start application:
    ```shell
    python app.py
    ```
The application will be accessible at http://localhost:5000 in your web browser.

## Used technologies:

- Flask/ APIFlask - API service
- SQLAlchemy - ORM
- Marshmallow - serializing and deserializing objects
- PostgreSQL, SQLite - data storage
- Apscheduler - for scheduling tasks

## Endpoints
### Currencies:
- GET /api/v1/currencies/history?date_from=<YYYY-MM-DD>&currency_code=<USD>:
Get currency exchange value history from <date_from> by <currency_code>
- GET /api/v1/currencies/<currency_code>:
Get currency exchange value and automatically add it to db if currency code in list of currencies to save