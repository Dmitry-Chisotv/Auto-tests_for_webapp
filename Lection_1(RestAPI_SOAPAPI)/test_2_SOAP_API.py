from zeep import Client
wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = """ ДОБАВИТЬ КОД ПОДПИСИ"""
client = Client(wsdl=wsdl)

def test_step1():
    client.service.VerifySignature('CMS', sign)['Result']

# print(client.service.VerifySignature('CMS', sign))
#
# print(client.service.VerifySignature('CMS', sign)['Result'])
