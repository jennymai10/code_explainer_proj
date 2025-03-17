# Python Code Explainer Prototype

A Django-based web application that explains Python code using the Gemini API. This project allows users to input Python code and receive a detailed explanation of its functionality.

## Features

- **Code Input**: Users can input Python code into a text area.
- **Code Explanation**: The application uses the Gemini API to generate a detailed explanation of the code.
- **Structured Breakdown**: The explanation is broken down into components (e.g., loops, conditionals, functions) for better understanding.
- **Modern UI**: Clean and responsive design for a great user experience.

## Technologies Used

- **Django**: Backend framework for handling requests and rendering templates.
- **Gemini API**: AI-powered code explanation.
- **HTML/CSS/JavaScript**: Frontend for user interaction and styling.
- **Gunicorn**: Production-ready WSGI server for deploying Django apps.
- **Render**: Cloud platform for hosting the application.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.11 or higher
- Pip (Python package manager)
- A Gemini API key (get it from [Google AI Studio](https://ai.google.dev/))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Gemini API key:
   ```plaintext
   GEMINI_API_KEY=your-api-key-here
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`.

## Deployment

This project is configured for deployment on **Render**. Follow these steps to deploy:

1. **Push your code to GitHub**:
   Ensure your project is pushed to a GitHub repository.

2. **Create a Render account**:
   Sign up at [Render](https://render.com/).

3. **Create a new Web Service**:
   - Connect your GitHub repository.
   - Render will detect the `render.yaml` file and configure the service automatically.

4. **Set environment variables**:
   In the Render dashboard, add the following environment variables:
   - `GEMINI_API_KEY`: Your Gemini API key.
   - `SECRET_KEY`: A secure Django secret key.
   - `DEBUG`: Set to `False` for production.
   - `ALLOWED_HOSTS`: Set to `.onrender.com`.

5. **Deploy**:
   Render will automatically deploy your application. Once deployed, you’ll receive a URL to access your app.

## Project Structure

```
codehs_project/
├── codehs_project/          # Django project settings and configurations
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── explainer/               # Django app for code explanation
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   ├── templates/           # HTML templates
│   └── static/              # Static files (CSS, JS)
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── render.yaml              # Render deployment configuration
├── .env                     # Environment variables
└── .gitignore               # Files to ignore in Git
```

## Acknowledgments

- [Django](https://www.djangoproject.com/) for the web framework.
- [Gemini API](https://ai.google.dev/) for AI-powered code explanations.
- [Render](https://render.com/) for hosting the application.

---
