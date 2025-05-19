import re

# Email validation
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

# Phone number validation
def is_valid_phone(phone):
    pattern = r'^(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}$'
    return re.match(pattern, phone) is not None

# Credit card validation
def is_valid_credit_card(card):
    pattern = r'^\d{4}([-\s]?)\d{4}\1\d{4}\1\d{4}$'
    return re.match(pattern, card) is not None

# Time format validation (12-hour & 24-hour)
def is_valid_time(time):
    pattern = r'^\b(1[0-9]|2[0-3]):[0-5][0-9]\b|\b([1-9]|1[0-2]):[0-5][0-9]\s?(AM|PM)\b'
    return re.match(pattern, time) is not None

# HTML tag validation
def is_valid_html_tag(tag):
    pattern = r'^<([a-zA-Z0-9]+)(\s+[^>]*)?>.*?</\1>$'
    return re.match(pattern, tag) is not None

# Example usage
test_data = {
    "emails": [
        "user@example.com",
        "firstname.lastname@company.co.uk",
        "bad-email@",
        "google@gmail.com"
    ],
    "phones": [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "4567890"
    ],
    "credit_cards": [
        "1234-5678-9012-3456",
        "1234 5678 9012 3456",
        "1234567890123456"
    ],
    "times": [
        "14:30",
        "2:30 PM",
        "25:00"
    ],
    "html_tags": [
        "<p>Hello</p>",
        "<div class='box'>Content</div>",
        "<img src='image.jpg' alt='pic' />"
    ]
}

# Testing all fields
for email in test_data["emails"]:
    print(f"Email '{email}' is valid? {is_valid_email(email)}")

for phone in test_data["phones"]:
    print(f"Phone '{phone}' is valid? {is_valid_phone(phone)}")

for card in test_data["credit_cards"]:
    print(f"Credit Card '{card}' is valid? {is_valid_credit_card(card)}")

for time in test_data["times"]:
    print(f"Time '{time}' is valid? {is_valid_time(time)}")

for tag in test_data["html_tags"]:
    print(f"HTML Tag '{tag}' is valid? {is_valid_html_tag(tag)}")
