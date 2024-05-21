import mysql.connector
import base64

# Connect to the database
connection = mysql.connector.connect(
    host="real-estate-management-system.cn2k4i2qwl2o.us-east-1.rds.amazonaws.com",
    user="root",
    password="yadidiah",
    database="real_estate_management_system"
)

# Create a cursor object
cursor = connection.cursor()

# Loop through each property ID and update the image data
for property_id in range(4, 13):  # Assuming you have properties from ID 1 to 12
    # Construct the image file path
    file_path = f"media/p{property_id}.jpg"

    try:
        # Read the image file
        with open(file_path, "rb") as image_file:
            image_data = image_file.read()

        # Encode the image data
        image_data = base64.b64encode(image_data)

        # Update the image data for the property
        update_query = "UPDATE properties SET image = %s WHERE PropertyID = %s"
        cursor.execute(update_query, (image_data, property_id))
        connection.commit()
        print(f"Image for property ID {property_id} inserted successfully.")
    except FileNotFoundError:
        print(f"Image file not found for property ID {property_id}.")
    except mysql.connector.Error as error:
        print(f"Error inserting image for property ID {property_id}: {error}")

# Close the cursor and connection
cursor.close()
connection.close()
