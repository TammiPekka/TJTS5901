# TJTS5901

Course TJTS5901 group project.

## How to Run

### Locally

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the app:
    ```bash
    python app/app.py
    ```

### Using Docker

1. Build the Docker image:
    ```bash
    docker build -t my_python_web_app .
    ```

2. Run the container:
    ```bash
    docker run -p 5000:5000 my_python_web_app
    ```

## Testing

Run tests using:
```bash
pytest tests
```