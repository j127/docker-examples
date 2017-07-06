# This builds an image based on Python 3.6 and Alpine Linux
FROM python:3.6-alpine

# Add the src code from the current directory to `/code`
ADD . /code

# and move to that directory
WORKDIR /code

# Install the Python requirements
RUN pip install -r requirements.txt

# Start the Flask application
CMD ["python", "app.py"]
