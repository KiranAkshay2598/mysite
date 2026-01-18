# Django Beginner Learning Project

This is my very first learning project (created in 2020) designed to understand the core concepts of web development with Django. The primary focus of this project is on the **Backend (BE)**, understanding how data flows through the application, and how Django handles requests and responses.

It serves as a playground to explore the **MVT (Model-View-Template)** architecture, **Django Template Language (DTL)**, and custom **Middleware**.

## 🎯 Learning Objectives

This project encapsulates basic beginner tasks to understand:
- **Django MVT Structure**: How Models, Views, and Templates interact.
- **Django Template Language (DTL)**: Rendering dynamic data in HTML.
- **Authentication**: A basic Login/Logout flow to understand session management.
- **Middleware**: Custom implementation to handle request processing globally (e.g., URL redirection).
- **Calculator Flow**: A simple form-based interaction to demonstrate request handling and data processing in views.

## 🛠️ Tech Stack

- **Python**: 3.x
- **Django**: 3.1
- **Database**: PostgreSQL
- **Frontend**: Basic HTML/CSS/Bootstrap (Templates downloaded from online resources; focus is on backend integration).

## 📂 Project Structure

This is a standard Django project structure:
- `account/`: Handles user authentication views (Login/Logout) and registration logic.
- `mysite/`: The project core.
    - `settings.py`: Main configuration (Database, Middleware, Static files).
    - `urls.py`: Main URL routing.
    - `middleware.py`: Custom `ParseHostMiddleware`.
- `polls/`: A sample app demonstrating a basic calculation flow.
    - Includes a simple HTML form (`home.html`) that accepts two numbers and displays the result, teaching basic request handling (`POST` method).
- `travello/`: An app handling the main homepage logic with dynamic content rendering.
- `templates/`: HTML templates using DTL. **Note:** These templates are sourced online; the learning focus is on manipulating them dynamically using **DTL (Django Template Language)**.
- `static/`: Static assets (CSS, JS, images, plugins) serving the frontend.
- `media/`: Handles user-uploaded content (configured but currently unused).
- `manage.py`: Django's command-line utility for administrative tasks.

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites
- Python installed on your machine.
- **PostgreSQL** installed and running.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd mysite
    ```

2.  **Install Dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Database Setup:**
    This project uses **PostgreSQL**.

    *   **Start the Server:**
        Ensure your PostgreSQL service is running.
        ```bash
        # Linux
        sudo service postgresql start
        ```

    *   **Create a Database:**
        Access the PostgreSQL shell and create a new database. You can choose any name (e.g., `mysite_db`).
        ```bash
        sudo -u postgres psql
        ```
        Inside the SQL shell, run:
        ```sql
        CREATE DATABASE mysite_db;
        ```
        Then exit the shell with `\q`.

    *   **Configure Settings:**
        Open `mysite/settings.py` and check the `DATABASES` configuration. Update the `NAME`, `USER`, and `PASSWORD` to match your local PostgreSQL configuration.

    ```python
    # mysite/settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mysite_db', # Match the name of the DB created above
            'USER': 'postgres',
            'PASSWORD': 'your_password',
            'HOST': 'localhost'
        }
    }
    ```

4.  **Apply Migrations:**
    This creates the necessary tables in your PostgreSQL database based on the models.
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin):**
    To access the admin panel.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

    Access the application at `http://localhost:8000`.

## ⚙️ Middleware Feature
This project includes a custom middleware (`ParseHostMiddleware`) that enforces the use of `localhost` over `127.0.0.1` for consistency. If you access the site via IP, it will automatically redirect you to the localhost domain.


