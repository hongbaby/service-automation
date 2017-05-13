import requests
import json
from random import choice, randint
from services.schedule_class_service.sql_handler import *
from services.utility import *
from services.schedule_class_service.fetch_session import fetch_session1


Class_Toic_Sample = "Topic Test"
Class_Topic_Description = "Descriptyion Test"
s = fetch_session1()
capicity = randint(1, 10)

# support apply, bf,


def schedule_class(schedule_date='6/5/2017', school_id=28, class_category_id=43):
    """

    :param schedule_date: which date needs to schedule, format like "mm/dd/yyyy"
    :param school_id: which school id needs to schedule
    :param class_category_id: can get from classcategory_lkp table
    :return:
    """

    url = "https://uat2oboe.ef.com/oboe2/ScheduledClass/Insert"

    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept":  "* / *"
    }

    dict_data = {"StartDate": schedule_date,
                 "EndDate":	schedule_date,
                 "School_id":	school_id,
                 "LastUpdateUTCDateTicks": '',
                 "StartTime": "1140",
                 "EndTime":	"1230",
                 "ClassRoom_id":	get_class_room_id_from_specified_school(school_id),
                 "Capacity":	capicity,
                 "ClassCategory_id":	class_category_id,
                 "ClassType_id":	get_random_class_type_id_from_class_category(class_category_id),
                 "ScheduledClassTopic_id":	'',
                 "Teacher_id":	get_teacher_id_from_specified_school(school_id),
                 "LCDescription":	Class_Topic_Description,
                 "EnterableClassTopic":	Class_Toic_Sample}

    response = s.post(url=url, data=dict_data, headers=headers, verify=False)

    assert response.status_code == StatusCode.Success, response.text
    print(response.text)
    json_response = string_to_json(response.text)

    if json_response[JsonResponse.IsSuccess] == ResponseStatus.Success:
        print(json_response)

    else:
        print(json_response[JsonResponse.ErrorMsg])


def get_random_class_type_id_from_class_category(class_category_id):

    type_list = execute_sql('SELECT ct.ClassType_id FROM Oboe.dbo.ClassType_lkp ct WHERE '
                            'ct.ClassCategory_id IN (%d)' % class_category_id)

    random_class_type_id = choice(type_list)
    if random_class_type_id:
        return random_class_type_id[0]


def get_class_room_id_from_specified_school(school_id):

    sql = 'select classroom_id from oboe.dbo.Classroom_lkp where School_id = %d ' \
          'and IsDeleted = 0 and (IsHidden is NULL OR IsHidden = 0)' % school_id

    class_room_list = execute_sql(sql)

    random_class_room_id = choice(class_room_list)
    if random_class_room_id:
        return random_class_room_id[0]


def get_teacher_id_from_specified_school(school_id):
    sql = 'select user_id from oboe.dbo.UserRoleSchool_lnk where School_id = %d and ' \
          'Role_id = 82 and IsDeleted = 0' % school_id

    teacher_id_list = execute_sql(sql)

    random_teacher_id = choice(teacher_id_list)

    if random_teacher_id:
        return random_teacher_id[0]


schedule_class()