from services.sf_services.set_hima_test import set_hima_test


def test_set_hima():
    student_id = 2391165911
    level_code = "3"
    set_hima_test(student_id, level_code)


test_set_hima()
