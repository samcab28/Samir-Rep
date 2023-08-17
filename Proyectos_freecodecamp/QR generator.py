#pip install qrcode
#instalar qr code para correcta ejecucion, seguir formato de entrega
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1, 
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10, 
        border = 4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qrimg2.png')

generate_qrcode('me encantan las tetas de pamela')