import qrcode
import image
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data="https://www.coursera.org/account/accomplishments/verify/UWE87WZRCVJF?utm_source%3Dandroid%26utm_medium%3Dcertificate%26utm_content%3Dcert_image%26utm_campaign%3Dsharing_cta%26utm_product%3Dcourse"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='balck',back_color='white')
img.save("crashcourspythonqrcode.png")