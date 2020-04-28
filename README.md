#Bookversations

This is a landing page for the bookversations podcast with the latest episodes and our current reading list. In only a few steps you have this running on your local machine or deployed on a web server. 

##Prerequisites

The requirements necessary to run the code on your machine are:

- python3 and pip3

  - Check that you have python3 installed on your computer with the command: 

    ```
    python --version
    OR 
    python3 --version
    ```

  - If you don’t have python3 installed, you may find these useful: 

    - https://www.python.org/
    - https://brew.sh/

##On Local Machine: Quick Start Guide

1. Create a new empty folder on your computer

2. Navigate into the folder from the terminal and run: 

   ```
   # OVER HTTPS:
   git clone https://github.com/suadolaps/bookversations.git
   
   # OVER SSH:
   git clone ssh://git@github.com:suadolaps/bookversations.git
   ```

3. Set up a virtual env in your directory:

   - To set up a virtualenv, you can follow the instructions here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

4. If you’ve set up your virtual environment as stated above, activate your virtualenv with the command:

   `source <env name>/bin/activate`

5. Set up database?

   - Install postgres ?

   - Log into the postgres shell:

     `sudo -u postgres psql`

   - Create a database:

     `CREATE DATABASE bookversations;`

   - Create user with **username** and **password** of choice: 

     `CREATE USER dbadmin WITH PASSWORD 'abc123!’;`

   - Set default encoding, transaction isolation scheme (Recommended from Django)

     `ALTER ROLE dbadmin SET client_encoding TO 'utf8';`
     `ALTER ROLE dbadmin SET default_transaction_isolation TO 'read committed';`
     `ALTER ROLE dbadmin SET timezone TO 'UTC';`

   - Give user access to database

     `GRANT ALL PRIVILEGES ON DATABASE btre_prod TO dbadmin;`

   - Quit out of the postgres shell

     `\q`

6. Run the following command from your terminal to install required packages for the project:

   `pip install -r requirements.txt`

7. Run Migrations: to create database tables according to database settings and models

   `python manage.py makemigrations`

   `python manage.py migrate` 

8. Create a superuser

   `python manage.py createsuperuser`

   - You’ll be requested to input a username, email (optional) and password for the superuser
   - This allows you the flexible option of managing data (?) using the Django Admin panel

9. Create static files

   `python manage.py collectstatic`

10. Run Server

    `python manage.py runserver 0.0.0.0:8000`

11. In a browser of your choice, test the site at:

    `http://server_domain_or_IP:8000`

##Deploy on a server: Quick Start Guide

