
---

# Company Email Lead Generation

This script is designed to generate valid email leads for companies by utilizing the LinkedIn API to fetch company data and then constructing email addresses based on the company names and domains extracted from the LinkedIn data. It also attempts to validate these email addresses using the Google API.

## Prerequisites

- **LinkedIn API Token:** You will need a valid LinkedIn API token to access the LinkedIn API.
- **Google API Token:** Obtain a Google API token to use the Gmail API for email validation.
- **Python Libraries:** Ensure you have the necessary Python libraries installed, particularly `requests` and `json`.

## Setup

1. Clone the repository or download the script file.
2. Install the required Python libraries if not already installed:
   ```bash
   pip install requests
   ```
3. Replace placeholders `YOUR_LINKEDIN_TOKEN` and `YOUR_GOOGLE_TOKEN` in the script with your actual LinkedIn and Google API tokens.

## Usage

1. Run the `generate_company_emails()` function in the script.
2. The script will connect to the LinkedIn API to fetch company data and extract company names and domains.
3. It will then generate potential email addresses based on the extracted information.
4. The script will attempt to validate these email addresses using the Google API.
5. Valid email leads will be saved to a text file (`valid_email_leads.txt`) in the `email_leads` folder.

## Notes

- The LinkedIn API might have rate limits or restrictions, so be cautious about making too many requests.
- The Google API usage might be subject to quotas and limitations as well.

## Disclaimer

This script is provided as-is and might require further modifications or adjustments based on API changes or specific use cases. Use it responsibly and adhere to API terms of service and rate limitations.

---
