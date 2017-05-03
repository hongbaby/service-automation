# -*- coding: utf-8 -*-

"""
This module provides methods to suspend student.

-----
"""
import requests
import uuid
from services.enum import *
from services.utility import *
from bs4 import BeautifulSoup as bs


def suspend_student(member_id, suspend_date, resume_date):
    """

    :param member_id: student's member id
    :param suspend_date: format like 'yyyy-mm-dd', e.g. '2017-04-02'
    :param resume_date: format like 'yyyy-mm-dd', e.g. '2017-04-02'
    :return:
    """
    reason_code = 'Internal Test'
    transaction_id = uuid.uuid4()

    headers = {
        'SOAPAction': "\"http://tempuri.org/ISalesforceNewOrgService/SuspendV2\"",
        'Content-type': 'text/xml',
        'Accept': 'text/xml'
    }

    data = """<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"><s:Header><o:Security s:mustUnderstand="1" xmlns:o="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
    <o:UsernameToken>
      <o:Username>{0}</o:Username>
      <o:Password>{1}</o:Password>
    </o:UsernameToken></o:Security></s:Header>

    <s:Body>
      <SuspendV2 xmlns="http://tempuri.org/">
        <param xmlns:a="http://schemas.datacontract.org/2004/07/EFSchools.Englishtown.Oboe.Services.DataContract.SalesForce" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
          <a:IsAsync>false</a:IsAsync>
          <a:Member_id>{2}</a:Member_id>
          <a:ReasonCode>{3}</a:ReasonCode>
          <a:ResumeDate>{4}</a:ResumeDate>
          <a:SuspendDate>{5}</a:SuspendDate>
          <a:TransactionId>{6}</a:TransactionId>
        </param>
        </SuspendV2>
    </s:Body>
    </s:Envelope>"""

    search_result = search_rows('suspend_info', {'member_id': member_id})
    if search_result:
        raise ValueError("This student {} has been suspended on {} and will resume on {}, no need to suspend again. "
                         "Please resume first".format(member_id, search_result[0]['suspend_date'],
                                                      search_result[0]['resume_date']))

    result = requests.post(HOSTNAME + SFServicesURLs.SFNewOrgServiceBaseURL, data=data.
                           format(SALESFORCE_USERNAME, SALESFORCE_PASSWORD, member_id, reason_code, resume_date,
                                  suspend_date, transaction_id), headers=headers, verify=False)

    assert result.status_code == StatusCode.Success, result.text

    doc = bs(result.content, 'xml')

    if doc.find('IsSuccess').string == 'true':
        suspend_external_id = doc.find('SuspendExternalId').string
        add_row('suspend_info', member_id, suspend_date, resume_date, suspend_external_id)

        return suspend_external_id
    else:
        error_code = doc.find('ErrorCode').string
        error_message = doc.find('ErrorMessage').string

        raise SystemError('Error code and error message are: \n{}.\n{}'.format(error_code, error_message))
