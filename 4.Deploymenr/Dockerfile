# Use official Python 3.9 image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project files (app.py and model)
COPY . .

# Expose port 8501 for Solara
EXPOSE 8501

# Run the Solara app
CMD ["solara", "run", "app.py", "--port", "8501"]