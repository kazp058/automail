import smtplib, ssl, email
from PIL import Image, ImageDraw, ImageFont
import string

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL

#Execute python -m smtpd -c DebuggingServer -n localhost:1025

with open("Lista.csv", encoding= "utf-8") as f:

    sender_email = "robotronduran@gmail.com"
    password = "robotron123"

    for linea in f.readlines():
        linea = "ISRRAEL FABRICA QUISPE;Isrraelfcaq@hotmail.com"
        linea = linea.split(";")

        name = linea[0].strip().lower()
        name = string.capwords(name)
        nameCertificate = name.split(" ")
        nameList = name.split(" ")

        if len(nameCertificate) == 2:
            nameCertificate = nameCertificate[0] + "\n" + nameCertificate[1]
        elif len(nameCertificate) == 4:
            nameCertificate = nameCertificate[0] + " " + nameCertificate[1] + "\n" + nameCertificate[2] + " " + nameCertificate[3]
        else:
            if len(nameCertificate)%2 == 0:
                name1 = nameCertificate[:(len(nameCertificate))//2]
                name2 = nameCertificate[len(nameCertificate)//2:]
                nameCertificate = " ".join(name1) + "\n" + " ".join(name2)
            else:
                name1 = nameCertificate[:(len(nameCertificate) + 1) // 2]
                name2 = nameCertificate[(len(nameCertificate) + 1) // 2:]
                nameCertificate = " ".join(name1) + "\n" + " ".join(name2)

        subject = "Certificado Algoritmos Geneticos"

        reciever_email = linea[1]

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = reciever_email
        message["Subject"] = subject
        message["Bcc"] = reciever_email

        html = """\
        <html>
          <body>
            <h2>Felicidades {name} por cumplir el webinar de Algoritmos Geneticos!<br></h2>
            <p>Esperamos que hayas disfrutado de nuestro curso, recuerda seguirnos en nuestras redes para seguir mas informacion<br>
            El certificado que has recibido es verficable y tiene un sello de garantia.
            Recuerda seguirnos en nuestras redes:<br>
            <a href="https://www.facebook.com/RobotronEcuador/">Facebook<br></a> 
            <a href="https://www.youtube.com/channel/UCI8AzDicR45-uFt3YdEI9Sg">Youtube</a> 
            </p>
          </body>
        </html>
        """.format(name= name)

        # Turn these into plain/html MIMEText objects
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part2)

        # Create a secure SSL context
        context = ssl.create_default_context()

        image = Image.open("Certificado.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('SecularOne-Regular.ttf',size= 200)
        (x,y) = (800,900)
        color = 'rgb(255,195,0)'
        draw.text((x,y),nameCertificate, fill=color, font=font)
        filename = 'Certificado_'+ "_".join(nameList) +'.pdf'

        image = image.convert('RGB')
        image.save(filename)

        with open(filename, "rb") as attachment:
            part = MIMEBase("application","octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(part)
        body = message.as_string()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, body)
            print("Mensaje enviado a:" + name + "\nCorreo "+ reciever_email)