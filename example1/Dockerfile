# Use the official Python 3.8 image from the Docker Hub
FROM python:3.8

# Add the main.py file to the root of the Docker image
# The '.' stands for the current directory
ADD main.py .

# Install scikit-learn using pip
RUN pip install scikit-learn

# Set the command to run the main.py script
CMD ["python", "./main.py"]
