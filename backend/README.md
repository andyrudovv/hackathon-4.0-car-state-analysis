# FastAPI Photo Analytics

This project is a FastAPI application that provides a service for uploading photos and retrieving analytic results from a custom AI model.

## Features

- Upload photos for analysis
- Retrieve analytic results from the uploaded photos
- Built with FastAPI for high performance and easy scalability

## Project Structure

```
fastapi-photo-analytics
├── src
│   ├── main.py          # Entry point of the FastAPI application
│   ├── models.py        # Data models for request and response validation
│   ├── routers
│   │   └── photos.py    # Routes for photo uploads and analytics
│   ├── services
│   │   └── analytics.py  # Logic for processing photos and generating analytics
│   └── utils.py         # Utility functions for various tasks
├── tests
│   └── test_main.py     # Unit tests for the application
├── Dockerfile            # Instructions to build a Docker image
├── docker-compose.yml    # Configuration for Docker services
├── .gitignore            # Files and directories to ignore by Git
└── requirements.txt      # Project dependencies
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-photo-analytics
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

4. Access the API documentation at `http://localhost:8000/docs`.

## Usage

- To upload a photo, send a POST request to `/photos/upload` with the photo file.
- To retrieve analytics, send a GET request to `/photos/analytics/{photo_id}`.

## License

This project is licensed under the MIT License.