import datetime
import qrcode
from PIL import Image

def qrhash(points):
    current_date = datetime.datetime.now()
    machine_number = 123
    smn=str(machine_number)
    spoints=str(points)
    intdatehash= current_date.year*10000000000 + current_date.month * 100000000 + current_date.day * 1000000 + current_date.hour*10000 + current_date.minute*100 + current_date.second
    sdatehash= str(intdatehash)
    finalhash= smn + sdatehash + spoints
    #print(finalhash) format: machine no. - year - month - day - hour - min - sec - pts
    img = qrcode.make(finalhash)
    img.save('static/qr/newQr.png')
    return finalhash
