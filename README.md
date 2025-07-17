Launch Tracker API
A simple RESTful API for tracking fictional space launches, built with FastAPI and SQLAlchemy. This project simulates operational software for environments like SpaceX, demonstrating full-stack development, database integration, testing, and containerization.

Features
  Create, retrieve, and list launch records (vehicle, date, status).
  Input validation for status (Scheduled, Launched, Failed).
  Interactive API documentation via Swagger UI.
  Unit testing with pytest.
  Docker deployment for easy containerization.
    
Technologies
  Backend: FastAPI (Python 3.12)
  Database: SQLAlchemy ORM with SQLite
  Validation: Pydantic
  Testing: pytest
  Containerization: Docker
  Version Control: Git/GitHub
    
Setup (Local)
  1. Clone the repository:
      git clone https://github.com/Butlchr17/Launch_Tracker_API.git
      cd Launch_Tracker_API
      
  2. Create and activate a virtual environment:
      python -m venv venv
      source venv/bin/activate  # On Linux/Mac

      Or on Windows: venv\Scripts\activate

  4. Install dependencies:
       pip install -r requirements.txt

  6. Run the API:
       uvicorn main:app --reload

  8. Access the API:
       - Documentation: http://127.0.0.1:8000/docs
       - Root: http://127.0.0.1:8000/

Usage
Endpoints
  - GET /: Welcome message.
  - POST /launches/: Create a launch (body: {"vehicle": "Falcon 9", "date": "2025-07-18T12:00:00", "status": "Scheduled"}).
  - GET /launches/: Get all launches.
  - GET /launches/{launch_id}: Get a specific launch by ID.
    
Example with curl:
  Create a launch:
    curl -X POST "http://127.0.0.1:8000/launches/" -H "Content-Type: application/json" -d '{"vehicle": "Starship", "date": "2025-07-20T14:00:00", "status": "Scheduled"}'

  Get all launches:
    curl http://127.0.0.1:8000/launches/

Testing
Run unit tests:
  pytest test_main.py
  Covers valid/invalid creation, retrieval.

Deployment (Docker)
  1. Build the image:    
    docker build -t launch-tracker-api .

  2. Run the Container:
     docker run -d -p 8000:80 launch-tracker-api

  3. Access: http://localhost:8000/docs
     For persistent database:
     docker run -d -p 8000:80 -v $(pwd)/launches.db:/app/launches.db launch-tracker-api

Contributing
Fork the repo, create a branch, and submit a pull request.

License
MIT License - feel free to use and modify.
