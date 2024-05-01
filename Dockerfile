FROM python:3.8

# Create app directory
WORKDIR /usr/src/app

# Copy the Flask app source to the working directory
COPY . .

# Install Flask
RUN pip install Flask==3.0.0

# Expose the required port
EXPOSE 8080

# Specify the command to run the Flask app
CMD ["python", "randomquotes.py"]
