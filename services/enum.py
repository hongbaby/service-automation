ECOAuthToken = 'AGEAYgBjAGQAMQAyADMANAAxADIAMwA0AF4AMQA1ADIAMwAxADcANgA1ADYANwBeADcAOAA4ADUAN' \
               'gA5AF4AMgAyAGYAMwA2ADgANABmADkAZQA4ADMANwA5ADcAMwA5AGMAZQA4AGEAZABjADkAYwA0ADg' \
               'AZgAxAGIAOAA5AGYAYwAyADUAOABjADQA'

SALESFORCE_USERNAME = "SalesforceSmartUser"
SALESFORCE_PASSWORD = "SalesforceSmartPwd"

headers = {
    'ECOAuthToken': ECOAuthToken,
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
    }


class BookingServicesURLs:
    BookingBaseURL = "/services/ecplatform/BookingService.svc/rest"
    LoadStudentBookingInfo = BookingBaseURL + '/LoadStudentBookingInfo'
    LoadScheduledClassBookingInfoList = BookingBaseURL + '/LoadScheduledClassBookingInfoList'
    ProcessClassBooking = BookingBaseURL + "/ProcessClassBooking"
    LoadClassBookingDetailInfo = BookingBaseURL + "/LoadClassBookingDetailInfo"


class SFServicesURLs:
    SFBaseServiceURL = "/services/Oboe2/1.0/SalesForceService.svc"
    SFNewOrgServiceBaseURL = "/services/Oboe2/1.0/SalesforceNewOrgService.svc"


class BookingServiceResponse:
    ScheduledClassBookingDetailInfo = "ScheduledClassBookingDetailInfo"
