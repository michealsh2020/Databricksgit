from flask import Flask  
  
# Create a Flask app instance  
app = Flask(__name__)  
  
# Define a route for the root URL  
@app.route('/')  
def hello_world():  
    return 'Hello, World! This is a simple Flask app running on Azure Databricks.'  
  
# Run the app only if the script is executed directly  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)  
