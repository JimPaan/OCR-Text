import pymysql


def fetch_extracted_text():
    try:
        # Connect to the live database
        connection = pymysql.connect(
            host="sql12.freesqldatabase.com",
            user="sql12753386",
            password="MKBtYICIP5",
            database="sql12753386",
            port=3306
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
        if 'connection' in locals() and connection:
            connection.close()
