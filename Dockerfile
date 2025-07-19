# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /code

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all project files to the container
COPY . .

# Expose port 8000 for Django dev server
EXPOSE 8000

# Run Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
