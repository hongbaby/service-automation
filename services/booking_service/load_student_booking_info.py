import requests

from services.enum import *
from services.utility import *


def load_student_booking_info():
    url = HOSTNAME + BookingServicesURLs.LoadStudentBookingInfo
    body_data = {
        "Member_id": 11270970,
        "BeginUtcDate": "2017-04-08 08:38:02",
        "EndUtcDate": "2017-04-30 08:38:02"
    }
    response = requests.post(url=url, json=body_data, headers=headers, verify=False)
    print(response.content)

load_student_booking_info()
