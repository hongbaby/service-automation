import requests
import json
from ptest.assertion import assert_that
from services.enum import *
from services.utility import *

BasicInfo = "BasicInfo"
BookingInfo = "BookingInfo"
ScheduledClassId = "ScheduledClass_id"


def load_class_booking_detail_info(student_id, scheduled_class_id):
    url = HOSTNAME + BookingServicesURLs.LoadClassBookingDetailInfo
    body_data = {
        "Member_id": student_id,
        ScheduledClassId: scheduled_class_id
    }

    response = requests.post(url=url, json=body_data, headers=headers, verify=False)
    assert response.status_code == StatusCode.Success, response.text
    json_response = json.loads(response.text)

    if json_response[JsonResponse.Success] == ResponseStatus.Success:
        verify_class_detail_info(scheduled_class_id, json_response[BookingServiceResponse.
                                 ScheduledClassBookingDetailInfo])
    else:
        error_code = json_response[JsonResponse.ErrorCode]
        error_message = json_response[JsonResponse.ErrorMessage]

        return error_code, error_message


def verify_class_detail_info(scheduled_class_id, json_data):
    scheduled_id_from_basic_info = json_data[BasicInfo][ScheduledClassId]
    scheduled_id_from_booking_info = json_data[BookingInfo][ScheduledClassId]

    assert_that(scheduled_id_from_basic_info).is_equal_to(scheduled_class_id)
    assert_that(scheduled_id_from_booking_info).is_equal_to(scheduled_class_id)
