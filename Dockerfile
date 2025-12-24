# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
# (Note: We do NOT copy the models/ or data/ folders yet. 
# In production, the container would run 'dvc pull'.)
COPY . .

# Expose the Flask port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
