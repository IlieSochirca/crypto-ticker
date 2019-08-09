"""
Module that contains functionality for sending emails
"""
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
account = os.environ.get("ACCOUNT")
password = os.environ.get("PASSWORD")

sender_email = os.environ.get("ACCOUNT")
receiver_email = os.environ.get("RECEIVER_ACCOUNT")


def send_email(data):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Crypto Daily Updates"
    message["From"] = sender_email
    message["To"] = receiver_email
    template_array = []
    for key in data.keys():
        dynamic_content_html = """<table>
                              <tr>
                                <th>Crypto</th>
                                <th>Current Price</th> 
                                <th>Market Cap</th>
                                <th>Circulating Supply</th>
                                <th>Total Supply</th>
                                <th>Hour Change</th>
                                <th>Day Change</th>
                                <th>Week Change</th>
                              </tr>
                              <tr>
                                <td><b>""" + str(data[key]["Name"]) + """</b></td>
                                <td>""" + str(data[key]["Price"]) + """</td> 
                                <td>""" + str(data[key]["Market Cap"]) + """</td> 
                                <td>""" + str(data[key]["Circulation Supply"]) + """</td> 
                                <td>""" + str(data[key]["Total Supply"]) + """</td> 
                                <td>""" + str(data[key]["Hour Change"]) + """</td> 
                                <td>""" + str(data[key]["Day Change"]) + """</td> 
                                <td>""" + str(data[key]["Week Change"]) + """</td> 
                              </tr>
                                 </table>"""
        template_array.append(dynamic_content_html)

    message_html = """<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                            </head>
                            <body>
                            <p>Hello Dear Crypto Friend, <br> I want to give you great news regarding your portfolio 
                            and leave you here the latest updates.</p>
                            """ + ''.join(template_array) + """
                            <p>Thank you for your desire to be in updated!</p>
                            <p>Keep your in touch, <br>
                               CryptoManiac 
                            </p>
                            </body>
                            </html>"""

    message.attach(MIMEText(message_html, "html"))
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port=port, context=context) as server:
        server.login(user=account, password=password)
        server.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=message.as_string())
