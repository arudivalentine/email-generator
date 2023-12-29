import requests
import json
import os

def generate_company_emails():
    # Connect to LinkedIn API to pull company data
    linkedin_url = "https://api.linkedin.com/v2/companies"
    linkedin_token = "YOUR_LINKEDIN_TOKEN"
    linkedin_headers = {
        "Authorization": f"Bearer {linkedin_token}",
        "Content-Type": "application/json"
    }
    linkedin_response = requests.get(linkedin_url, headers=linkedin_headers)
    linkedin_data = json.loads(linkedin_response.text)

    # Extract company names and domains from LinkedIn data
    company_names = [company['name'] for company in linkedin_data['companies']]
    company_domains = [company['websiteUrl'].split('//')[1] for company in linkedin_data['companies']]

    # Generate email addresses using company names and domains
    email_leads = []
    for name, domain in zip(company_names, company_domains):
        email_leads.append(f"{name.lower().replace(' ', '')}@{domain}")

    # Connect to Google API to validate email addresses
    google_url = "https://www.googleapis.com/gmail/v1/users"
    google_token = "AIzaSyBwK5mznzQYsYC-VA0BYttwV6XddcBGbnQ"
    google_headers = {
        "Authorization": f"Bearer {google_token}",
        "Content-Type": "application/json"
    }

    valid_email_leads = []
    for email in email_leads:
        google_params = {
            "emailAddress": email
        }
        google_response = requests.get(google_url, headers=google_headers, params=google_params)
        if google_response.status_code == 200:
            valid_email_leads.append(email)

    # Save valid email leads to a text file
    save_folder = "email_leads"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    with open(os.path.join(save_folder, "valid_email_leads.txt"), "w") as file:
        for email in valid_email_leads:
            file.write(email + "\n")

    print("Valid email leads generated and saved successfully.")

# Call the function to generate valid company email leads
generate_company_emails()
