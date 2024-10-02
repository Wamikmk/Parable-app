# Book of Parables

Book of Parables is a web application that simplifies complex concepts through intuitive stories and parables. It uses Google's Generative AI to create explanations and matplotlib to generate simple diagrams.

## Features

- Generate parables and intuitive explanations for any concept or question
- Create simple diagrams to illustrate concepts
- Clean and user-friendly interface

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/book-of-parables.git
   cd book-of-parables
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google API key:
   ```bash
   SECRET_KEY='your_secret_key'
   GOOGLE_API_KEY='your_google_api_key'
   ```

## Usage

1. Run the Flask application:
   ```bash
   python run.py
   ```

2. Open a web browser and go to `http://localhost:5000`

3. Enter a concept or question in the input field and click "Enlighten Me"

4. The application will generate a parable, an explanation, and a simple diagram to illustrate the concept

## Project Structure

- `run.py`: The entry point of the application
- `config.py`: Configuration settings for the app
- `app/`: The main application package
  - `__init__.py`: Initializes the Flask application
  - `routes.py`: Defines the routes for the web application
  - `explanation_generator.py`: Generates explanations using Google's Generative AI
  - `diagram_generator.py`: Generates simple diagrams using matplotlib
  - `templates/`: Contains HTML templates
  - `static/`: Contains static files (CSS, JavaScript)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.