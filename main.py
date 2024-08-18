import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from supabase import create_client
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Ensure that supabase_url and supabase_key are available
if not supabase_url or not supabase_key:
    raise Exception("Supabase URL and Key are required")

# Initialize the Supabase client
supabase = create_client(supabase_url, supabase_key)

# Fetch the latest email record
response = supabase.table("EmailTampung").select("*").order("created_at", desc=True).limit(1).execute()

if response.data:
    latest_record = response.data[0]
    if latest_record.get("status") is False:
        # Your credentials
        my_email = ""
        my_password = ""

        # Recipient email
        to_email = latest_record.get("email")

        # Load HTML content from the file
        with open("email_template.html", "r") as file:
            html_content = file.read()

        # Create a multipart message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Automated HTML Email"
        msg["From"] = my_email
        msg["To"] = to_email

        # Attach the HTML content
        msg.attach(MIMEText(html_content, "html"))

        try:
            # Send the email
            with smtplib.SMTP("smtp.gmail.com", 587) as roks:
                roks.starttls()
                roks.login(user=my_email, password=my_password)
                roks.sendmail(from_addr=my_email, to_addrs=to_email, msg=msg.as_string())
                roks.close()

            # Update the record in Supabase
            update_response = supabase.table("EmailTampung").update({"status": True}).eq("id", latest_record.get("id")).execute()

            # Check if the update was successful
            if update_response.data:
                print("Record updated successfully.")
            elif update_response.error_message:
                print(f"Failed to update record: {update_response.error_message}")
            else:
                print("Unknown error occurred during record update.")

        except Exception as e:
            print(f"Failed to send email: {e}")
    else:
        print("Status is not 0, no action taken.")
else:
    print("No data found.")
