import smtplib
import mysql.connector as sql
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

my_email = "automatedbdayemailsender@gmail.com"
password = "gwdttjodrgdxbrtw"

# Connect to MySQL
mycon = sql.connect(host='localhost', user='root', password='MySQL@Python', database='emailbd')
cursor = mycon.cursor()

# Query to get birthdays
query1 = "SELECT * FROM births"
cursor.execute(query1)
result = cursor.fetchall()

# Loop through the results
for x in result:
    if x[5] == 'N':  # Check if not processed
        rec_email = x[1]  # Receiver's email
        message = x[2]  # Birthday message
        image_path = x[4]  # Path to image
        print(x[4])
        query2 = "UPDATE births SET processed = 'Y' WHERE receiver_email = %s"
        cursor.execute(query2, (rec_email,))

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = rec_email
        msg['Subject'] = "Happy Birthday Wishes!"

        # Attach the message text
        msg.attach(MIMEText(message, 'plain'))

        # Attach the image (simplified)
        with open(image_path, 'rb') as img_file:
            msg.attach(MIMEImage(img_file.read(), name=image_path))

        # Send the email
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=rec_email,
                msg=msg.as_string()
            )
            print(f"Email sent to {rec_email}")

# Commit changes to the database
mycon.commit()
cursor.close()
mycon.close()
