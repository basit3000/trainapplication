NOTE: This project is currently being worked on and if anyone wants to contribute to it, feel free to. It's very casual and mostly for practicing. {Current progress; login functionality has been added but not all templates have been done yet so there might be issues with it}

# Train application

# Steps for Docker

## Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose (optional but recommended): [Install Docker Compose](https://docs.docker.com/compose/install/)

1. **Clone the repository**

    ```sh
    git clone https://github.com/basit3000/trainapplication.git
    ```

2. **Navigate to the Project Directory**

    ```sh
    cd trainapplication
    ```

3. **Build the Docker container**

    ```sh
    docker build -t trainapplication .
    ```

4. **Run the Docker Container**
    
    ```sh
    docker run -d -p 8000:8000 trainapplication
    ```

# Steps for Manual Django setup and to run the server:

- Ensure Python is installed locally. You can download it from [python.org](https://www.python.org/).

1. **Clone the Repository**

    ```sh
    git clone https://github.com/basit3000/trainapplication.git
    ```

2. **Navigate to the Project Directory**

    ```sh
    cd trainapplication
    ```

3. **Upgrade pip (Optional but Recommended)**

    ```sh
    python -m pip install --upgrade pip
    ```

4. **Create a Virtual Environment**

    ```sh
    python -m venv venv
    ```

5. **Activate the Virtual Environment**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

6. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

7. **Run the Django Server**

    ```sh
    python app/manage.py runserver

## License

This project is licensed under the MIT License.

Feel free to contribute and make improvements to this script. If you encounter any issues, please open an issue on the GitHub repository.
