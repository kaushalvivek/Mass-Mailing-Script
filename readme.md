#READ_ME 

Before sending a new mass email, do the following:

## Changes to Content files and Attachements

1. Enter text to be written before name of sender in file content1.txt
> For example:
> 
> Hi Jane Doe,
>
> Here, 'Hi<space>' will be the content in content1.txt

2. Enter whatever follows name of sender (comma, return, body of email and salutation) in HTML format in cotent2.txt
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
2. Fields should be exactly similar as in the given names.csv.
> Example: 
> S.No, Name, email,
> S.No, Name, email,

## Modifications in script before sending:

1. Enter the e-cell mail account password in **line 35.**
2. Add attachment (if any) in **line 27.**
3. Enter Subject for mail in **line 45.**

## General Instructions:

1. Send a mail to yourself first using the script before blasting it on the mailing list, the names-test.csv is for that purpose.
2. Proxy is not necessary.
3. If you need any help, mail me at vivek.kaushal@outlook.com, or text me on facebook, assuming we are friends.

**Coded by:**
- Deepanshu Jain
- Shivang Nagaria

**Modifications and Maintenance:**
- Vivek Kaushal

