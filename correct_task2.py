# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re

EMAIL_REGEX = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")

def count_valid_emails(emails):
    count = 0
    for email in emails:
        if isinstance(email, str):
            stripped = email.strip()
            if EMAIL_REGEX.match(stripped):
                count += 1
    return count