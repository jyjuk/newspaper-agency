# newspaper-agency
Django project for managing redactors and newspaper in newspaper agency


# Installation
Python3 must be already installed

1. Clone the repository:
    ```bash
   git clone https://github.com/jyjuk/newspaper-agency.git
   cd news_paper_agency
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the server:
    ```bash
    python manage.py runserver
    ```

# Importing Data
To import data from the newspaper_db_data.json file, follow these steps:

1. Ensure your virtual environment is activated:
   ```bash
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
   ```
2. Load the data into your database:
   ```bash
   python manage.py loaddata newspaper_db_data.json
   ```
   This will populate your database with the initial data from the newspaper_db_data.json file.

3. After loading data from fixture you can use following superuser (or create another one by yourself):
   Login: testuser
   Password: AKtm8CxschaiVJ5

## Link to project deployment:
   ```bash
   https://newspaper-agency-vklt.onrender.com/
   ```

## Features
* Authentication functionality for Redactor/User
* Managing news redactor & topic directly from website interface
* Powerful admin panel for advanced managing

## Demo
![](db_structure.png)
