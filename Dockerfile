# Use Python 3.9
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app