import os
import smtplib
import ssl
from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate


def send(subject, body_text, file_to_attach):
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, 'email.ini')
    header = 'Content-Disposition', 'attachment; filename="%s"' % file_to_attach
    
    cfg = ConfigParser()
    cfg.read(config_path)
    
    host = cfg.get("smtp", "server")
    login = cfg.get('smtp', 'login')
    password = cfg.get('smtp', 'password')
    from_addr = cfg.get("smtp", "from_addr")
    to_addr = cfg.get('smtp', 'to_addr')

    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    
    if body_text:
        msg.attach(MIMEText(body_text))

    msg["To"] = to_addr
    
    attachment = MIMEBase('application', "octet-stream")
    
    with open(file_to_attach, "rb") as fh:
        data = fh.read()
        
    attachment.set_payload(data)
    encoders.encode_base64(attachment)
    attachment.add_header(*header)
    msg.attach(attachment)

    server = smtplib.SMTP_SSL(host, 465)
    server.ehlo()
    server.login(login, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
