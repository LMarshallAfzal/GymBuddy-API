# GymBuddy-API
## Overview

The GymBuddy API is a RESTful interface that empowers developers to access and integrate comprehensive workout data into their applications. It provides a one-stop shop for information on exercises, muscles, equipment, and more, fueling innovative fitness experiences.

**Key Features:**
- Extensive Exercise Library: Access detailed information on hundreds of exercises, including descriptions, instructions, muscle groups targeted, equipment needs, and difficulty levels.
- Image Repository: Enhance understanding with a library of exercise images for visual guidance.
- Flexible Data Access: Utilize a RESTful API with multiple endpoints for retrieving specific exercises, filtering by muscle groups or equipment, and exploring the entire database.
- Streamlined Integration: Easily integrate exercise data into your fitness apps, websites, or training tools, enriching user experiences and boosting engagement.

**Dive deeper into the power of GymBuddy API - explore the documentation for API usage, data models, and more!**

## Author(s)
Leonard Marshall Afzal (lmarshallafzal)

## Installation and Setup

1. **Prerequisites:**
    - Python (v3.6+)
    - Virtual Environment (Recommended): Create a virtual environment to isolate project dependancies
        - Using `venv`:
            ```bash
            python -m venv env
            source env/bin/activate  # Activate the environment
            ``` 
2. **Dependencies:**
    - Install required libraries using pip
        ```bash
        pip install -r requirements.txt
        ```
3. **Database Setup:**
    - SQLite: For development, create a database file:
        ```bash
        python manage.py migrate
        ```
4. **Running the API Server:**
    - Start the Django development server
        ```
        python manage.py runserver
        ```
    - This API should be accessible at `http://127.0.0.1:8000`
## Usage

Interacting with GymBuddy API is straightforward. Here's a guide to get started

1. **Avaiable Endpoints:**

    | Endpoint              | Description                                       |
    |------------------------|---------------------------------------------------|
    | `/exercises/`          | Retrieve a list of exercises                      |
    | `/exercises/<id>/`     | Retrieve a specific exercise by ID                |
    | `/exercises/?name=<exercise_name>` | Filter exercises by muscle group          |

2. **Supported Request Methods:**
    - **GET**: Retrieve data from the API.
    - **POST**: Create new resources (e.g., add a new exercise).
    - **PUT**: Update existing resources (e.g., modify an exercise's details).
    - **DELETE**: Delete resources (e.g., remove an exercise).

3. **Authentication:**
    - The API currently uses a custom authentication mechanism based on API keys.
    - To authenticate requests, you need to include a valid API key in the 'Authorization' header of your HTTP requests.
    - For non-GET requests, the API key must be valid, and failure to provide a valid key will result in an `AuthenticationFailed` response.
    - For GET requests, no authentication is required, allowing unauthenticated access to certain endpoints.

## Contributing
Contributions are welcome! Feel free to open issues and pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.