# mailer

The `mailer` project is a simple email automation tool designed to send personalized emails to a list of recipients. The configuration for the email server and sender details are stored in `config.yaml`. The email content is templated in `body.txt`, allowing for dynamic insertion of recipient-specific data. The main functionality is implemented in `send_mail.py`, which reads recipient data from a CSV file, formats the email content, and sends the emails using the SMTP protocol. This project is ideal for automating email campaigns and notifications.
