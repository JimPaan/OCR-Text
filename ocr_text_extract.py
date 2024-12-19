import os
import pymysql
import pytesseract
from pdf2image import convert_from_path


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    extracted_text = ""
    for image in images:
        extracted_text += pytesseract.image_to_string(image)
    return extracted_text


# Function to store data in MariaDB
def store_in_mariadb(filename, extracted_text):
    try:
        # Connect to MariaDB
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="koala",
            database="ocr_db"
        )
        cursor = connection.cursor()

        # Insert data into the table
        sql = "INSERT INTO ocr_data (filename, extracted_text) VALUES (%s, %s)"
        cursor.execute(sql, (filename, extracted_text))
        connection.commit()

        print(f"Data stored successfully for file: {filename}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()


# Main program
if __name__ == "__main__":
    pdf_file = "iraya_paper.pdf"  # Replace with your PDF file path
    if not os.path.exists(pdf_file):
        print("PDF file not found!")
    else:
        extracted_text = extract_text_from_pdf(pdf_file)
        store_in_mariadb(os.path.basename(pdf_file), extracted_text)
