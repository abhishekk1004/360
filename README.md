🌀 360° Image Viewer Web App
This Django-based web application allows users to register, log in, upload their own images, and simulate 360° views. It's designed for ease of use and can be extended to support true 360° viewers or sprite animations.

🔥 Features
✅ User Registration and Login

✅ Authentication-protected Image Upload

✅ Simulated 360° Viewer

✅ Sample Albums on Home Page

✅ Admin Dashboard for User & Upload Management

✅ Clean, Gradient-Styled UI with Navigation

✅ Secure Logout (POST only)

📁 Folder Structure

image_rt/
├── checking/                 # Django app
│   ├── templates/viewer/   # All HTML templates
│   ├── static/
│   │   ├── css/style.css
│   │   ├── js/viewer.js
│   │   └── images/sample1.jpg ...
│   ├── models.py           # UploadedImage model
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
├── media/                  # Stores uploaded images
├── db.sqlite3
├── manage.py
├── project/settings.py
├── project/urls.py
└── README.md
🚀 Setup Instructions
1. Clone the repo:
    git clone https://github.com/yourusername/360-image-viewer.git
cd image_rt

2. Create a virtual environment:
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

3. Install dependencies:
    pip install django pillow

4. Run migrations:
    python manage.py makemigrations
    python manage.py migrate

5. Create superuser for admin:
    python manage.py createsuperuser

6. Run the server:
    python manage.py runserver

7. Open in browser:
    http://127.0.0.1:8000/

🖼 Sample Images
Add your sample album images here:

viewer/static/images/sample1.jpg
viewer/static/images/sample2.jpg
viewer/static/images/sample3.jpg


🔐 Admin Panel
Visit:
    http://127.0.0.1:8000/admin/
    Use the superuser credentials to manage users and uploaded images.

💡 To Do / Future Ideas
🔄 Real 360° rotation using sprite frames or three.js

🖼 Multi-image upload for full spin

📱 Responsive mobile view

☁️ Cloud image storage (AWS S3 / Firebase)

✨ Use Bootstrap or Tailwind for better UI



