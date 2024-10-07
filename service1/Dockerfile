# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the app file
COPY app.py .


#Getting help from LLM since uptime and process was having some troubles
# Install required dependencies for Python and system utilities
RUN apt-get update && apt-get install -y procps

# Install required dependencies
RUN pip install Flask requests

# Expose the required port
EXPOSE 8199

# Command to run the app
CMD ["python", "app.py"]
