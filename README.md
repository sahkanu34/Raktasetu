# Raktasetu

<img src ="https://github.com/sahkanu34/Raktasetu/blob/main/screenshots/home.png">

Raktasetu is an online web application designed to connect blood donors with recipients in need. This system serves as a bridge to facilitate blood donation and management efficiently and effectively. With user-friendly interfaces and robust backend features, Raktasetu aims to make blood donation and management accessible to everyone.

---

## Features
<h1>User Dashboard</h1>
<img  src = "https://github.com/sahkanu34/Raktasetu/blob/main/screenshots/user_dash.png">

### User Features:
- **User Registration and Profile Management**: Users can create and manage their profiles.
- **Blood Donation Requests**: Users can post requests for specific blood groups.
- **Community Engagement**: Join a community of donors and recipients to share resources and information.

<h1>Admin Dashboard</h1>
<img src = "https://github.com/sahkanu34/Raktasetu/blob/main/screenshots/admin_dash.png">

### Admin Features:
- **Donor Profile Management**: Manage the profiles of registered donors.
- **Request Management**: Review and manage blood requests.
- **Blood Group Inventory**: Monitor and manage the availability of different blood groups.

---

## Tech Stack

### Frontend:
- **HTML5**, **CSS3**, **JavaScript**: For building a responsive and interactive user interface.

### Backend:
- **Django**: A Python-based web framework for robust backend logic and management.

### Database:
- **MySQL**: For storing and managing user profiles, blood requests, and inventory data.

---

## Installation

### Prerequisites:
- Python 3.8+
- Django 4.0+
- MySQL 8.0+

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/sahkanu34/Raktasetu.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Raktasetu
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - Create a MySQL database named `raktasetu`.
   - Configure database settings in `settings.py`.
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'raktasetu',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
5. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the application at:

---

## Usage

1. **For Users**:
   - Sign up or log in to create a profile.
   - Search or post blood requests.
   - Connect with donors in your community.

2. **For Admins**:
   - Log in to access the admin dashboard.
   - Run the following scripts and add your credentials.
      ```bash
      python manage.py createsuperuser
      ```
   - Manage donor profiles, blood requests, and inventory data.

---

## Contribution

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
<img src ="https://github.com/sahkanu34/Raktasetu/blob/main/screenshots/thank.jpg">

- Thanks to all contributors and supporters of this project.
- Special thanks to blood donors worldwide for saving lives every day.
