import pikepdf
from pikepdf import Pdf


def encryptPdf(filepath,ownPass,userPass):
    try:
        pdf = Pdf.open(filepath)    
        pdf.save(filepath[:-4]+'_enrypted.pdf', encryption=pikepdf.Encryption(owner=ownPass, user=userPass, R=4))
        pdf.close()
        return [0,filepath[:-4]+'_enrypted.pdf']
    except:
        return [1]