from flask import Flask, render_template, request

# Create an instance of the Flask class for the web application
app = Flask(__name__)

# Define the main route for the application, which handles both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():

    # Initialize a variable to store the calculated woman's age, default is None
    woman_age = None
    
    if request.method == 'POST':
        try:
            # Retrieve the age input from the form and convert it to an integer
            age = int(request.form['age'])
            # Calculate the woman's age using the formula: Woman's Age = Man's Age / 2 + 7
            woman_age = age / 2 + 7
        except ValueError:
            # If the input is not a valid integer, return an empty string
            woman_age = None
            
    # Render the index.html template and pass the calculated woman's age to it
    return render_template("index.html", woman_age=woman_age)

# Run the Flask application in debug mode when the script is executed directly
if __name__ == '__main__':
  app.run(debug=True)
