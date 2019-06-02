from django.core.management.base import BaseCommand, CommandError
from OpenSSL import SSL
import OpenSSL
import ssl
import datetime
from Dominios.models import Dominio as Dominio
from django.db import models
from django.core.mail import send_mail

class Command (BaseCommand): 
 help = 'verify things'
 def handle (self, *args, **options):
  d= Dominio.objects.all()
  today = datetime.datetime.now()
  datetoday= datetime.date.today()
  for dominio in d:

    url= dominio.Direction
    owner= dominio.Owner.email
    date= dominio.Expirationdate
 
    #print ssl.get_server_certificate(('www.google.com', 443))
    cert=ssl.get_server_certificate((url, 443))
    # OpenSSL
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    x510= x509.get_notBefore()
    byear= int(x510[0:4])
    bmonth=int(x510[4:6])
    bday=int(x510[6:8])
    bhour=int(x510[8:10])
    bminute=int(x510[10:12])
    bsecond=int(x510[12:14])
    bdate= datetime.datetime(byear,bmonth,bday,bhour,bminute,bsecond)

    print (url + ' No es valido antes de:')
    print(bdate)
    x511= OpenSSL.crypto.X509.get_notAfter(x509).decode("utf-8")
    ayear= int(x511[0:4])
    amonth=int(x511[4:6])
    aday=int(x511[6:8])
    ahour=int(x511[8:10])
    aminute=int(x511[10:12])
    asecond=int(x511[12:14])
    adate= datetime.datetime(ayear,amonth,aday,ahour,aminute,asecond)
    
    print (url + ' No es valido despues de:')
    print(adate)
    if adate < today   :
     print('Certificado Expirado')
     send_mail(
     'Su certificado ha expirado',
     'Renueve su certificado vago',
     'Dominionnoreply@gmail.com',
     [owner],
     fail_silently=False,
     )
    else:
     print('Certificado Valido')
    if date < datetoday:
     print('Dominio Expirado')
     