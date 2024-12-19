import pymysql


def fetch_extracted_text():
    try:
        # Connect to MariaDB
        connection = pymysql.connect(
            host="localhost",
            user="root",       # Replace with your MariaDB username
            password="koala",  # Replace with your MariaDB password
            database="ocr_db"  # Database name
        )
        cursor = connection.cursor()

        # Fetch the most recent extracted text
        sql = "SELECT extracted_text FROM ocr_data ORDER BY created_at DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            print("No OCR data found.")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        if connection:
            connection.close()
