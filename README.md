# Mass Mailing Script

This script is designed to help you send mass mails that are rich in HTML content, with attachments to users.

## Configuration:

1.```salutation.txt``` Enter text to be written before name of sender here.  
For example:
```html
Hi Jane Doe,

<!--Here, 

'Hi<_space_>' 
will be the content in salutation.txt

--> 
```

2.```body.txt``` Enter whatever follows name of sender (comma, return, body of email and salutation) in HTML format.  
For example:
```html

,<br/>

<b>Greetings from E-Cell IIIT Hyderabad!</b>

<p>We are .... (body)</p>
```

3.```Attachments``` Configure attachement path and file name in ```IMPORTANT CONSTANTS.```

4. ```IMPORTANT CONSTANTS``` Ensure that these are correctly filled.

```python
########################################

# IMPORTANT CONSTANTS

# File with e-mail address of targets
target_csv = 'target.csv'

# Sender E-Mail Address
email_id = 'batman@justiceleague.org'

# Enter your name/organisation name for identification
identification = 'Justice League Inc.'

# Mailing Server
SMTP_server = 'mail.justiceleague.org'

# Mail's Subject
subject = "Resignition Citing Lack of Superpowers"

attachment_path_and_name = "./sample_attachment.jpg"

########################################
```

Support for a better method will be added soon.

## Format of Mailing List :-

1. CSV file format.
2. Fields should be exactly similar as in the given ```target.csv```.  
Example: 
```
S.No, Name, email,
S.No, Name, email,
```

## General Instructions:

1. Send a mail to yourself first using the script before blasting it on mailing lists.
2. If you need any help, create an issue.
3. Don't spam. It's unbecoming.
3. Post configuration, enter the following with your email account password:

```python
python send_mail.py MAIL_PASSWORD_HERE
```