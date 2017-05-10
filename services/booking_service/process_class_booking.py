import requests

from services.enum import *
from services.utility import *


def load_student_booking_info(student_id, scheduled_class_id):
    url = HOSTNAME + BookingServicesURLs.ProcessClassBooking
    body_data = {
        "Member_id": student_id,
        "SelectedUtcDate": "2017-05-9 16:00:00",
        "School_id": 39,
        'ScheduledClass_id': scheduled_class_id,
        'BookingStatus': 11
    }
    response = requests.post(url=url, json=body_data, headers=headers, verify=False)
    print(response.content)

load_student_booking_info(11282834, 3031309)
