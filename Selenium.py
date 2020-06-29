from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
import base64
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName,FileType, Disposition, ContentId)

#Generate the screenshot using selenium from BLS.com

CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

driver.get("https://www.bls.gov/news.release/empsit.nr0.htm")
print(driver.title) #> BLS Employment Situation
driver.save_screenshot("unemployment_rate.png")

#Generates Email to Send the Screen Shot using SendGrid

load_dotenv()
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
                                                                                                                                                                
#Citing the Code Author: https://github.com/sendgrid/sendgrid-python/issues/340
#Citing the Code Author: https://github.com/Gplafferty0219/workout-app/blob/master/app/workout.py#L230-L235

image_name = os.path.join(os.path.dirname(__file__), "unemployment_rate.png")

def send_email(subject="Unemployment Data", html="<p>Unemployment Data</p>", png=image_name):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    message = Mail(from_email=MY_EMAIL, to_emails=MY_EMAIL, subject=subject, html_content=html)
    
#Attaches the PNG we Generated Earlier Using Selenium

    with open(image_name, 'rb') as f:
        image = f.read()
        f.close()
    
    image_encoded = base64.b64encode(image).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(image_encoded)
    attachment.file_type = FileType('image/png')
    attachment.file_name = FileName('unemployment_rate.png')
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment
  
    #Send Email
    try:
        response = client.send(message)
        print(response.status_code)
        print(response.body)
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
    email_png = image_name

    #Send My Email
    send_email(email_subject, email_html, email_png)
    print(" ")
    print("Your email has been sent!")
    print(" ")

    #All SET! Set up with Heroku on a daily schedule