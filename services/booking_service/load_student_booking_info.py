import requests

from services.enum import *
from services.utility import *


def load_student_booking_info(student_id, begin_date, end_date):
    url = HOSTNAME + BookingServicesURLs.LoadStudentBookingInfo
    body_data = {
        "Member_id": student_id,
        "BeginUtcDate": begin_date,
        "EndUtcDate": end_date
    }
    response = requests.post(url=url, json=body_data, headers=headers, verify=False)
    assert response.status_code == StatusCode.Success, response.text

    return response.text

