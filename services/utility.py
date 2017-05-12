import datetime
HOSTNAME = "https://qa.englishtown.com"


class StatusCode:
    Success = 200


class ResponseStatus:
    Success = True
    Failed = False


class JsonResponse:
    Success = "Success"
    ErrorCode = "ErrorCode"
    ErrorMessage = "ErrorMessage"


def get_further_date(day=0):
    """
    this function default return today's date, format like '2017-05-03'
    :param day:  if day = 0 means today
    :return: further date
    """
    now = datetime.datetime.now()
    further = now + datetime.timedelta(days=day)
    return further.strftime('%Y-%m-%d')
