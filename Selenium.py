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
driver.save_screenshot("unemployment_rate.png")

#Generates Email Using SendGrid (Option 1)
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
                                                                                                                                                                
# Citing the Code Author: https://github.com/sendgrid/sendgrid-python/issues/340

def send_email(subject="Unemployment Data", html="<p>Unemployment Data</p>", png="unemployment_rate.png"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    message = Mail(from_email=MY_EMAIL, to_emails=MY_EMAIL, subject=subject, html_content=html)
    
    #attaches the PNG we generated earlier
    image_name = 'unemployment_rate.png'
    with open(image_name, 'rb') as f:
        image = f.read()
        f.close()

    image_encoded = base64.b64encode(image)

    attachment = Attachment()
    attachment.content = image_encoded
    attachment.type = "image/png"
    attachment.filename = image_name
    attachment.disposition = 'attachment'
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment
    
    #Send Email
    try:
        response = client.send(message)
        return response
    except Exception as e:
        print("OOPS", e.message)
        return None
    
    #Email Contents

    if __name__ == "__main__":
        email_subject = "Unemployment Data"
        email_html = f""" 
        <p> Unemployment Data </p>
        """
        email_png = "unemployment_rate.png"
   
        #send my message to users
        send_email(subject="Unemployment Data", html="<p>Unemployment Data</p>", png="unemployment_rate.png")