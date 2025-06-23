import os
from typing import List


def get_recipients() -> List[str]:
    """
    Get recipients from environment variable or file.
    Environment variable takes precedence over file.
    
    Returns:
        List of email addresses
    """
    recipients = []
    
    # First, check for recipients in environment variable
    env_recipients = os.getenv("RECIPIENTS")
    if env_recipients:
        # Parse comma-separated email addresses
        recipients = [email.strip() for email in env_recipients.split(',') if email.strip()]
    
    # If no env recipients, try to read from file
    if not recipients and os.path.exists('recipients.txt'):
        with open('recipients.txt', 'r') as f:
            recipients = [line.strip() for line in f if line.strip()]
    
    return recipients