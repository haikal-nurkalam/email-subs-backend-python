from supabase import create_client, Client
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


response = supabase.table("EmailTampung").select("*").order("created_at", desc=True).limit(1).execute()

print(response.data[0]["email"])

