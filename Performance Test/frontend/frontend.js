function handleUserInput() {
    var userInput = document.getElementById("user-input").value;
    if (userInput === '1') {
        // Start tests
        startTests();
    } else if (userInput === '2') {
        // Provide information about each test
        showTestDescriptions();
    } else if (userInput === '3') {
        // Cancel the application
        cancelApplication();
    } else {
        alert("Invalid input. Please enter 1, 2, or 3.");
    }
}

function startTests() {
    // Make a request to the backend to start tests
    // You can use fetch or XMLHttpRequest for this purpose
    // Example:
    fetch('/api/start-tests')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to start tests');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            // Handle the response from the backend
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function showTestDescriptions() {
    // Display information about each test to the user
    // You can use alert or console.log for this purpose
    // Example:
    alert("Test 1: Measure performance of NumPy computation\nTest 2: Sort a large array of random numbers\nTest 3: Compute Mandelbrot set\nTest 4: Measure performance of nested loops\nTest 5: Print a large range of numbers");
}

function cancelApplication() {
    // Cancel the application
    // You can implement additional logic if needed
    console.log("Exiting the application...");
}
