AI-Nutritionist Chatbot 
# Nutrition Plan Generator API

This FastAPI application generates personalized nutrition plans based on user information using the Google Gemini API. It also allows for custom prompts to be sent to the Gemini model.

## Features

* **Personalized Nutrition Plans:** Generates detailed nutrition plans (breakfast, lunch, dinner, and snacks) including estimated calories and nutrition tips based on age, weight, height, and gender.
* **Custom Prompts:** Allows users to send any custom prompt to the Gemini model and receive its response.
* **CORS Enabled:** Enables Cross-Origin Resource Sharing for easy integration with frontend applications.

## Prerequisites

* Python 3.7+
* pip (Python package installer)
* A Google Cloud project with the Gemini API enabled and an API key.

## Installation

1.  **Clone the repository (if applicable) or create a new project directory.**
2.  **Navigate to the project directory in your terminal.**
3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```
4.  **Install the required dependencies:**
    ```bash
    pip install fastapi uvicorn python-dotenv google-generativeai pydantic
    ```
5.  **Create a `.env` file in your project directory and add your Gemini API key:**
    ```
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    ```
    Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

## Running the Application

1.  **Navigate to your project directory in the terminal.**
2.  **Run the FastAPI application using Uvicorn:**
    ```bash
    uvicorn main:app --reload
    ```
    (Assuming your main Python file is named `main.py`)

    The `--reload` flag enables automatic reloading of the server upon code changes, which is helpful during development.

## API Endpoints

### `/get_plan` (POST)

Generates a personalized nutrition plan.

**Request Body (JSON):**

```json
{
    "age": 30,
    "weight": 70.5,
    "height": 175.0,
    "gender": "male"
}
