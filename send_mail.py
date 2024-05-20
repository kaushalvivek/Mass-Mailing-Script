import smtplib
import csv
import argparse
import yaml
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tqdm import tqdm
import random

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

EMAIL = config['email']
PASSWORD = config['password']
IDENTIFICATION = config['identification']
SMTP_SERVER = config['smtp']

parser = argparse.ArgumentParser(description='Process email details.')
parser.add_argument('--subject', required=True, help='Subject of the email')
parser.add_argument('--template', required=True, help='Path to the email template file')
parser.add_argument('--csv', required=True, help='Path to the CSV file with recipient data')
parser.add_argument('--test', action='store_true', help='Send 1/10 sampled emails to the sender for testing')

args = parser.parse_args()

subject = args.subject

def get_data(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def load_template(template_file):
    with open(template_file, 'r') as f:
        template = f.read()
    return template

def send_email(smtp_client, subject, sender, recipient, content):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    body = MIMEText(content, 'html')
    msg.attach(body)

    smtp_client.sendmail(sender, recipient, msg.as_string())

if __name__ == "__main__":
    data = get_data(args.csv)
    template = load_template(args.template)

    if args.test:
        data = random.sample(data, max(1, len(data) // 10))

    with smtplib.SMTP(SMTP_SERVER, 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)

        for row in tqdm(data, desc="Sending emails"):
            content = template.format(**row)
            recipient = EMAIL if args.test else row['email']
            send_email(server, subject, f"{IDENTIFICATION}<{EMAIL}>", recipient, content)
