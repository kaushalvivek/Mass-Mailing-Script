#READ_ME 

Before sending a new mass email, do the following:

## Changes to Content files and Attachements

1.```salutation.txt``` Enter text to be written before name of sender in file content1.txt
> For example:
> 
> Hi Jane Doe,
>
> Here, 'Hi<space>' will be the content in content1.txt

2.```body.txt``` Enter whatever follows name of sender (comma, return, body of email and salutation) in HTML format in cotent2.txt
> For example:
> ,
>
>Greetings from E-Cell IIIT Hyderabad!
>
> We are .... (body)

*Please note that a comma and a return key after that is necessary to start, as content2.txt is directly after name of sender*

3. Paste attachment in same folder. In case of multiple attachments, make a zip.

## Format of Mailing List

1. CSV file format.
2. Fields should be exactly similar as in the given ```target.csv```.
> Example: 
> S.No, Name, email,
> S.No, Name, email,

## Modifications in script before sending:

Enter details in the IMPORTANT CONSTANT section in the script, support for text based rendering will be added soon.

```python
########################################

# IMPORTANT CONSTANTS

target_csv = 'target.csv'

email_id = ''
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

