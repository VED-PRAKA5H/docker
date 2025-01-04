# Use the official Python 3.9 image from the Docker Hub
FROM python:3.9

# Set the working directory inside the Docker container to /example2
WORKDIR /example2

# Copy the requirements.txt file from the local machine to the working directory in the Docker container
COPY requirements.txt .

# Copy the contents of the local src directory to the src directory in the Docker container
COPY ./src ./src

# Install the Python dependencies listed in requirements.txt using pip
RUN pip install -r requirements.txt

# Set the command to run the main.py script located in the src directory
CMD ["python", "./src/main.py"]
