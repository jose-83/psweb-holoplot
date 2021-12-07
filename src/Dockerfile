# Use Python
FROM python:3.9-slim
EXPOSE 8080

# Create a new folder for my application files
RUN mkdir /app

# Install requirements
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files from host machine to image filesystem
COPY psweb.py /app

# Set the directory for executing future commands
WORKDIR /app

# Entry point: instruction of what the built container must do
CMD python3 psweb.py