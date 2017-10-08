import requests,time,datetime,json,xml
from hashlib import sha1
from hmac import new as hmac
from xml.etree import ElementTree
SECRET = 'XvAmRTGhQchFwzwduKYK'
DadosConsulta = {}

def consulta(placa): 
    with requests.Session() as s:
        requests.packages.urllib3.disable_warnings() 
        hed = {'User-Agent':'ksoap2-android/2.6.0+','Content-Type':'text/xml;charset=utf-8','Accept-Encoding': 'gzip','Content-Lenght':'592','Host':'sinespcidadao.sinesp.gov.br','Connection':'Keep-Alive'}
        s.headers.update(hed)
        plate = placa
        plate_and_secret = '%s%s' % (placa, SECRET)
        plate_and_secret = bytes(plate_and_secret.encode('utf-8'))
        plate = plate.encode('utf-8')
        hmac_key = hmac(plate_and_secret, plate, sha1)
        chave = hmac_key.hexdigest()
        dados = ("<v:Envelope xmlns:i=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:d=\"http://www.w3.org/2001/XMLSchema\" xmlns:c=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:v=\"http://schemas.xmlsoap.org/soap/envelope/\"><v:Header><b>motorola Moto G Play</b><c>ANDROID</c><d>6.0.1</d><e>4.2.3</e><f>192.168.0.20</f><g>"+str(chave)+"</g><h>0.0</h><i>0.0</i><k></k><l>"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"</l><m>8797e74f0d6eb7b1ff3dc114d4aa12d3</m></v:Header><v:Body><n0:getStatus xmlns:n0=\"http://soap.ws.placa.service.sinesp.serpro.gov.br/\"><a>"+str(placa)+"</a></n0:getStatus></v:Body></v:Envelope>")
        r = s.post('https://sinespcidadao.sinesp.gov.br/sinesp-cidadao/mobile/consultar-placa/v2',data=dados,verify=False)
        root = ElementTree.XML(str(r.content.decode("utf-8")))
        body_tag = '{http://schemas.xmlsoap.org/soap/envelope/}Body'
        response_tag = ('{http://soap.ws.placa.service.sinesp.serpro.gov.br/}''getStatusResponse')
        response = ('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
        for item in root.iter():
            dados = str(item.tag)
            dados = dados.replace(body_tag,'')
            dados = dados.replace(response,'')
            dados = dados.replace(response_tag,'')
            DadosConsulta[dados] = item.text
        print(json.dumps(DadosConsulta))
		
if __name__ == '__main__':
   consulta(*sys.argv[1:])
