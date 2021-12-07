FROM python:3.9-slim

# Install requirements
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy test files from host to the container
RUN mkdir /web-tests
WORKDIR /web-tests
ADD /tests ./tests

# Entry point: instruction of what the built container must do
CMD ["bash"]