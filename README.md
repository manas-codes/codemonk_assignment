# Backend Assignment

This is a Django REST framework project with PostgreSQL that implements user authentication and provides endpoints for adding and searching paragraphs.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Postman Documentation](#postman-documentation)
- [Testing](#testing)
- [License](#license)

## Prerequisites

Make sure you have the following installed on your system:

- [Python 3.11](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/manas-codes/codemonk_assignment.git
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a PostgreSQL database:
    ```sql
    CREATE DATABASE core_db;
    CREATE USER postgres WITH PASSWORD 'yourpassword';
    ALTER ROLE postgres SET client_encoding TO 'utf8';
    ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
    ALTER ROLE postgres SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE core_db TO postgres;
    ```

5. Create a `.env` file in the root directory and add the following environment variables:
    ```env
    POSTGRES_DB=core_db
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=yourpassword
    SECRET_KEY=your-secret-key
    DEBUG=True
    ```

## Running the Project

1. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

2. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

3. Start the development server:
    ```bash
    python manage.py runserver
    ```

4. The project should now be running at `http://localhost:8000`.

## API Endpoints

### Authentication

- **Register**: `POST /api/register/`
  - Request body:
    ```json
    {
      "email": "user@example.com",
      "name": "User Name",
      "dob": "YYYY-MM-DD",
      "password": "yourpassword"
    }
    ```

- **Login**: `POST /api/token/`
  - Request body:
    ```json
    {
      "email": "user@example.com",
      "password": "yourpassword"
    }
    ```

### Paragraph Management

- **Add Paragraph**: `POST /api/paragraphs/`
  - Headers: `Authorization: Bearer <token>`
  - Request body:
    ```json
    {
      "text": "Your paragraph text.\n\nAnother paragraph."
    }
    ```

- **Search Paragraph**: `POST /api/search/`
  - Headers: `Authorization: Bearer <token>`
  - Request body:
    ```json
    {
      "word": "searchword"
    }
    ```

## Postman Documentation

For detailed API documentation and testing, please refer to the [Postman Documentation for this application](https://documenter.getpostman.com/view/29726683/2sA3Qwb9mC).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Explanation

- **Prerequisites**: Lists the tools needed to run the project.
- **Setup**: Provides steps to clone the repository, set up a virtual environment, install dependencies, and create a PostgreSQL database.
- **Running the Project**: Instructions to apply migrations, create a superuser, and start the development server.
- **API Endpoints**: Details on how to use the API endpoints for authentication, adding paragraphs, and searching paragraphs.
- **Postman Documentation**: A link to the Postman documentation for further details.
- **License**: Specifies the license for the project.
