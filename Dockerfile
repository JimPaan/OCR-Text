# Use Python 3.9 as the base image
FROM python:3.9

# Install Tesseract OCR and required system libraries
RUN apt-get update && \
    apt-get install -y tesseract-ocr poppler-utils && \
    apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files (Python script, dependencies, and PDFs) to the container
COPY . /app

# Install required Python libraries
RUN pip install --no-cache-dir pytesseract pdf2image pillow pyodbc

# Define the command to run the Python script
CMD ["python", "ocr_extraction.py"]
