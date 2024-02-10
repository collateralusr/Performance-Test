# Performance Test

This Performance Test project is designed to measure the performance of various computational tasks on a computer system. It includes backend scripts written in Python and a frontend interface written in HTML and JavaScript.

## Functionality

1. **Start Tests**: Allows the user to initiate performance tests on the backend server.
2. **Know What Each Test Does**: Provides information about each test to the user.
3. **Cancel**: Allows the user to cancel the application.

## Test Levels

500,000: This represents a sample test with 500,000 elements.

1 million: This represents a test with 1,000,000 elements.

1 billion: This represents a test with 1,000,000,000 elements.

1 trillion: This represents a test with 1,000,000,000,000 elements.

Please note that running tests with higher numbers of elements may require significant computational resources and time.

## Installation

1. Clone the repository and navigate into the project directory by running the following commands in your terminal:

   ```bash
   git clone https://github.com/collateralusr/Performance-Test
   cd Performance-Test
   pip install -r requirements.txt

   ```

4. Start the backend server by running:
   ```
   python app.py
   ```

## Compatibility

- **Operating Systems**: The Performance Test application has been tested on macOS and should work on Linux distributions (e.g., Kali, Ubuntu) and Windows.

## Usage

### Backend

The backend consists of Python scripts responsible for conducting performance tests and providing test descriptions.

- `app.py`: This script serves as the main backend application. It includes functions to conduct performance tests, display test descriptions, handle user input, and start the tests.
- `run_tests.py`: This script contains a placeholder function `run_tests()` that simulates running performance tests. You can replace this function with your actual test implementation.

### Frontend

The frontend provides a user interface for interacting with the backend and displaying test information.

- `index.html`: This HTML file contains the frontend interface, including input fields for user interaction.
- `frontend.js`: This JavaScript file handles user input and makes requests to the backend server to start tests and display test descriptions.


## Disclaimer

This Performance Test is provided for educational and testing purposes only. The creator of this project is not responsible for any misuse of this software. Use responsibly and at your own risk.
