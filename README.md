## super-benchmark: A FastAPI Test Task Project

This project, `super-benchmark`, is a test task demonstrating the use of several popular Python libraries:

* **FastAPI:** A high-performance, web framework for building APIs.
* **uvicorn:** An ASGI server for running FastAPI applications.
* **SQLModel:** An ORM (Object-Relational Mapper) for interacting with databases in a Pythonic way.
* **python-dotenv:** A library for loading environment variables from a `.env` file.

**Note:** This README currently serves as a starting point. You'll likely need to update it with project-specific details as you develop the application.

### Installation

1. **Prerequisites:**
    - Ensure you have Python 3.12 or later installed. You can check by running `python --version` in your terminal.

2. **Clone the repository:**

   ```bash
   git clone [https://github.com/Acutapugione/super-benchmark.git](https://github.com/Acutapugione/super-benchmark.git)


3. **Install dependencies:**

   ```bash
    cd super-benchmark
    poetry install

### Usage
1. **Create a .env file (optional):**

    - If your application requires environment variables (e.g., database connection details), create a file named .env at the project root and add your  variables one per line. For example:
    ```code
    SUPERBENCHMARK_DEBUG=False

2. **Run the application:**
    ```bash
    poetry run start

    - This will start the FastAPI server, typically accessible at http://localhost:8000 (default port) by default.