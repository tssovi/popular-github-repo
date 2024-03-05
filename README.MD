# Popular GitHub Repository Service 

[Add a concise tagline describing your service in a few words]

## Description

* Provide a clear description of what your service does, the problem it solves, and its primary features.

## Installation for Local Executions

1. **Prerequisites:**
   * Python
   * FastAPI
   * Docker
2. **Clone the repository:**
   ```bash
   git clone https://github.com/tssovi/popular-github-repo.git
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
## Development & Workflow with Docker Compose

The following Makefile commands are provided to manage and interact with the application. Ensure you have both Docker and Docker Compose installed. 

* **Start the API in detached mode:**
    ```bash
    make up
    ```
* **Stop and remove containers, networks, volumes, and images:**
    ```bash
    make down
    ```
* **Build the Docker images:**
    ```bash
    make build
    ```
* **Run the API container:**
    ```bash
    make start-api
    ```
* **Run tests:**
    ```bash
    make run-test
    ```
* **Clean up test artifacts:**
    ```bash
    make clean
    ```

## API Endpoints

* **`/is-popular` (POST)**
    * **Description:** Determines if a GitHub repository is popular based on its stargazers and forks counts. 
    * **Parameters:**
        * **owner (str):** The owner of the repository.
        * **repo (str):** The name of the repository.
    * **Example Request (JSON):**
        ```json
        {
            "owner": "facebook",
            "repo": "react"
        }
        ```
    * **Example Response (JSON):**
        ```json
        {
            "repository": "facebook/react",
            "is_popular": true,
            "score": 12345,  
            "response_time": 0.231
        }
        ```

* **`/health` (GET)**
    * **Description:** Performs a basic health check of the service.
    * **Example Response (JSON):**
        ```json
        {"status": "OK"}
        ```