# FoodieLens

This is a web application that allows users to upload an image of a dish, and it provides a recipe for the same.

## Features

- **Image Upload:** Users can upload an image of a dish item directly through the web interface.

- **AI Recipe Generation:** The application analyzes the uploaded image and provide a recipe based on the recognized food item.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs.

- [Replicate API](https://replicate.ai/): For running a pretrained multimodal model for recipe prediction.

- [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/): A templating engine for rendering HTML templates.

- [uvicorn](https://www.uvicorn.org/): ASGI server for hosting the FastAPI application.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/recipe-predictor-app.git
   cd recipe-predictor-app
   ```
2. Install Dependencies:
    ```
   pip install -r requirements.txt
   ```
   
3. Configure Replicate API:
    - Sign up for a Replicate API account and obtain an API key.
    - Create a .env file in your directory.
    - Set your Replicate API key as an environment variable in the .env file.

4. Run the Application:
    ```
   python main.py
   ```
   
## Usage
- Open your web browser and navigate to http://localhost:8000.

- Click the "Choose File" button to upload an image of a food item.

- Enter a description or caption for the image in the provided text field.

- Click the "Submit" button to process the image and receive the recipe.