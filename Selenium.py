from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup # note that the import package command is `bs4`

#
# INITIALIZE THE DRIVER and Capture Screen Shots
#

CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

driver.get("https://www.bls.gov/news.release/empsit.nr0.htm")
print(driver.title) #> BLS Employment Situation
driver.save_screenshot("unemployment_rate.pdf")

#Generates Email Using SendGrid (Option 1)
import os
import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")

message = Mail(
    from_email='MY_EMAIL_ADDRESS',
    to_emails='MY_EMAIL_ADDRESS',
    subject='Unemployment Data',
    html_content='<Updated U.S Unemployment Rate Attached>'
)

with open('unemployment_rate.pdf', 'rb') as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('unemployment_rate.pdf'),
    FileType('application/pdf'),
    Disposition('attachment')
)
message.attachment = attachedFile

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.send(message)
print(response.status_code, response.body, response.headers)

                                                                                                                                                                              
#Generates the email using SendGrid (Option 2)

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")

def send_email(subject="Unemployment Data", html="<p>Unemployment Data</p>", pdf="unemployment_rate.pdf"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    message = Mail(from_email=MY_EMAIL, to_emails=MY_EMAIL, subject=subject, html_content=html)
    #attaches the PDF we generated earlier
    #file_path = 'unemployment_rate.png'
    with open(file_path, 'rb') as f:
       data = f.read()
       f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/pdf')
    attachment.file_name = FileName('unemployment_rate.pdf')
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment
    #send email
    try:
        response = client.send(message)
        return response
    except Exception as e:
        print("OOPS", e.message)
        return None

#where we get into the actual contents of the email, the message, subject, etc.
if __name__ == "__main__":
    email_subject = "Unemployment Data"
    email_html = f""" 
    <h3> Good Morning Alexa, the current unemployment rate in the U.S is attached</h3>
    """
    email_pdf = "unemployment_rate.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")
    