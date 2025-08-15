# 360

## Overview

360 is Django based web applicable which allows user to upload their image and based on the provided images it will simulate 360 view.

## Features

- Secure user authentication
- Simulate 360 view based on the images

## Tools and Technology used

- Django
- three.js
- Bootstrap and Tailwind

## Getting Started

### Platforms

This project supports the following platforms:

- Linux
- macOS
- Windows

### Requirements

- python >= 3.12.0 
- pip

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/abhishekk1004/360.git
    ```
    ```sh
    cd 360
    ```

2. **Setup virtual environment:**
    
    Linux
    ```sh
    python -m venv env source # setup virtual environment
    ```
    ```sh
    source env/bin/activate # activate virtual environment
    ```
    ```sh
    deactivate # run this when you need to deactivate virtual environment
    ```
    Windows
    ```sh
    env\Scripts\activate
    ```

3. **Install the packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run migrations**
    ```bash
    python manage.py makemigrations
    ```
    ```bash
    python manage.py migrate
    ```

2. **Create superuser for admin**
    ```bash
    python manage.py createsuperuser
    ```

3. **Run the server**
    ```bash
    python manage.py runserver
    ```

4. **Open in browser**
    ```
    http://127.0.0.1:8000/
    ```

5. **Admin Panel**
    - Visit: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
    - Use your superuser credentials to manage users and uploaded images.

## Contributing

Contributions are welcome! Please fork the repo, make changes, and submit pull requests. Open issues for bugs or feature requests.
