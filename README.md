# Email Subs Backend Python

I created this project for email automation using Python, React, Tailwind, and Supabase. You can find the Frontend here: [Email Subs Frontend Repo](https://github.com/haikal-nurkalam/email-subs-frontend-python.git)

## Demo
Try the demo app here: [email.heykals.com](https://email.heykals.com/). Make sure to use your email.

## Why I Chose These Stacks
- **Python**: I can integrate it faster with Supabase, the code is cleaner, and I challenged myself to integrate Supabase with this language.
- **React**: This is used to build the frontend and to call Supabase. It’s also fast, so I decided to use it for this project.
- **Tailwind**: I didn’t want to write vanilla CSS, and because I wanted to speed up development, I chose this CSS framework.
- **Supabase**: Similar to Firebase in functionality. I didn’t want to set up & configure my own backend, so I used Supabase, and it has proven to be reliable and fast.

## How to Install this Program
### Supabase
First, you need a Supabase account and project.
You can find it [here](https://supabase.com/docs/guides/getting-started/quickstarts/reactjs).

Below is my table specification:
- `id`, primary key, `int8`
- `created_at`, `timestamptz`
- `nama`, `text`
- `email`, `text`
- `no_telp`, `text`
- `status`, `bool`

You can customize it.

### Let's Install It
1. **Clone the Repository**  
Clone the repository to your local machine.
2. **Set Up Virtual Environment**  
Activate a virtual environment to manage dependencies.
   ```bash
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Configure Environment Variables**  
Create a `.env` file in the root directory of the project and add your Supabase environment variables.  
Example `.env` file:
   ```plaintext
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```
4. **Customize Your Table in `main.py`**  
Modify the table name according to what you created in Supabase.
   ```python
   response = supabase.table("your_table_name").select("*").order("created_at", desc=True).limit(1).execute()
   ```
5. **Set Up Your Email and Password**  
Update the email and password in the script:
   ```python
   my_email = "your_email"
   my_password = "your_password"
   ```
   Here’s how to get your email password:
   1. Visit [myaccount.google.com](https://myaccount.google.com/), click on Security from the left-hand menu, and scroll down to “How you sign in to Google.” Enable “2-Step Verification.”
   2. Find the App Passwords section by searching for it or [click here](https://myaccount.google.com/apppasswords).
   3. Generate an App password, name your app (e.g., Python Mail), and click create.
   4. **COPY THE PASSWORD** - This is the only time it will be shown. The password is 16 characters with no spaces. Use this App password in the `my_password`.
6. **Customize the Email Template**  
You can customize the email template using HTML in `email_template.html`.
7. **Run the Program**
   ```bash
   python3 scheduler.py
   ```
   The program will continuously run using a scheduling principle. The latest email recorded in Supabase will receive your customized email.

## Thank You
If you have any questions, feel free to reach out to me on GitHub or LinkedIn. Thank you!
