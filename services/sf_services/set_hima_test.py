import requests
from services.enum import *
from bs4 import BeautifulSoup as bs
from services.utility import HOSTNAME, StatusCode


def set_hima_test(student_id, level_code):
    headers = {
        'SOAPAction': "\"http://tempuri.org/ISalesForceService/SetHimaTestInfo\"",
        'Content-type': 'text/xml',
        'Accept': 'text/xml'
    }

    data = """
        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
            <s:Header>
            <o:Security s:mustUnderstand="1" xmlns:o="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
            <o:UsernameToken>
            <o:Username>{0}</o:Username>
            <o:Password>{1}</o:Password>
            </o:UsernameToken>
            </o:Security>
            </s:Header>
            <s:Body>
            <SetHimaTestInfo xmlns="http://tempuri.org/">
            <param xmlns:a="http://schemas.datacontract.org/2004/07/EFSchools.Englishtown.Oboe.Services.DataContract.SalesForce" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
            <a:LevelCode>{2}</a:LevelCode>
            <a:StudentId>{3}</a:StudentId>
            <a:TestId>28</a:TestId>
            </param>
            </SetHimaTestInfo>
            </s:Body>
        </s:Envelope>"""

    result = requests.post(HOSTNAME + SFServicesURLs.SFBaseServiceURL, data=data.format(SALESFORCE_USERNAME, SALESFORCE_PASSWORD,
                                                                       level_code, student_id), headers=headers, verify=False)

    if result.status_code == StatusCode.Success:
        doc = bs(result.content, 'xml')

        if doc.find("IsSuccess").string == 'true':
            return True
        else:
            return False

    else:
        print(result.text)
        return False
