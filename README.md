# Mass Mailing Script

Before sending a new mass email, do the following:

## Changes to Content files and Attachements

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

Paste attachment in same folder. In case of multiple attachments, make a zip.

## Format of Mailing List

1. CSV file format.
2. Fields should be exactly similar as in the given ```target.csv```.  
Example: 
```
S.No, Name, email,
S.No, Name, email,
```

## Modifications in script before sending:

Enter details in the IMPORTANT CONSTANT section in the script, support for text based rendering will be added soon.

```python
########################################

# IMPORTANT CONSTANTS

target_csv = 'target.csv'

email_id = ''
# Enter your name/organisation name for iden
iden = ''
psswrd = ''
SMTP_server = ''

subject = ""
attachment_path_and_name = "./sample_attachment.jpg"

########################################

```

## General Instructions:

1. Send a mail to yourself first using the script before blasting it on mailing lists.
3. If you need any help, create an issue.

**Coded by:**
- Vivek Kaushal
- Deepanshu Jain
- Shivang Nagaria