import requests

from services.enum import *
from services.utility import *


def load_student_booking_info():
    url = HOSTNAME + BookingServicesURLs.LoadStudentBookingInfo
    body_data = {
        "Member_id": 11281836,
        "BeginUtcDate": "2017-05-04 08:38:02",
        "EndUtcDate": "2017-05-18 08:38:02"
    }
    response = requests.post(url=url, json=body_data, headers=headers, verify=False)
    print(response.content)

load_student_booking_info()
