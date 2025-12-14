# Django Blog Project

A full-featured blog web application built with Python and the Django Web Framework.

This project was created by [Mahmoud Saadallah](https://github.com/mahmoudSaaadallah) to demonstrate core concepts of web development with Django, including user authentication, CRUD operations, and static file management.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Profile Management**: Authenticated users have a profile page where they can view and update their information, including a profile picture.
- **CRUD Operations for Posts**: Authenticated users can create, read, update, and delete their own blog posts.
- **Pagination**: The home page displays posts in a paginated view for easy navigation.
- **Responsive Design**: The site is built with Bootstrap 5 for a responsive experience on all devices.
- **Static and Media File Handling**: Correctly configured to serve static files (CSS, JS) and manage user-uploaded media (profile pictures).

---

## Pages & Screenshots

Here is a preview of the main pages of the application.

### Home Page

Displays all blog posts from all users, with pagination.

_(Image placeholder: Add a screenshot of your home page here)_

### Register Page

Allows new users to create an account.

_(Image placeholder: Add a screenshot of your register page here)_

### Login Page

Allows existing users to sign in.

_(Image placeholder: Add a screenshot of your login page here)_

### Profile Page

Displays the user's profile information (username, email, profile picture) and a list of their posts. Users can also update their profile from this page.

_(Image placeholder: Add a screenshot of a user profile page here)_

### New Post / Update Post Page

A form for creating or updating a blog post.

_(Image placeholder: Add a screenshot of the post creation form here)_

### Post Detail Page

Shows the full content of a single post. If the logged-in user is the author, they will see options to update or delete the post.

_(Image placeholder: Add a screenshot of a post detail page here)_

### About Page

Contains information about the project and the developer.

_(Image placeholder: Add a screenshot of your about page here)_

---

## Setup and Installation

Follow these instructions to get a local copy of the project up and running.

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation Steps

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/mahmoudSaaadallah/Blog_Project.git
    cd Blog_Project
    ```

2.  **Create and activate a virtual environment:**

    For Windows:

    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```

    For macOS/Linux:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    _(Note: You should create a `requirements.txt` file by running `pip freeze > requirements.txt` in your project)_

    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply the database migrations:**

    ```sh
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.

---

## Contact

Mahmoud Saadallah

- **Email**: [mahmoud.saadallah73@gmail.com](mailto:mahmoud.saadallah73@gmail.com)
- **GitHub**: [mahmoudSaaadallah](https://github.com/mahmoudSaaadallah)
- **LinkedIn**: [Mahmoud Saadallah](https://www.linkedin.com/in/mahmoudsaadallahi/)
- **Facebook**: [Mahmoud Saadallah](https://www.facebook.com/mahmoudsaaadallah)
