import requests

from services.enum import *
from services.utility import *


def load_student_booking_info():
    url = HOSTNAME + BookingServicesURLs.ProcessClassBooking
    body_data = {
        "Member_id": 11270970,
        "SelectedUtcDate": "2017-04-07 16:00:00",
        "School_id": 36,
        'ScheduledClass_id': 3030692,
        'BookingStatus': 12
    }
    response = requests.post(url=url, json=body_data, headers=headers, verify=False)
    print(response.content)

load_student_booking_info()