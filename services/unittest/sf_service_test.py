import pytest
from services.sf_services.set_hima_test import set_hima_test


def test_set_hima():
    student_id = 23911699
    level_code = "3"
    set_hima_test(student_id, level_code)


if __name__ == "__main__":
    pytest.main()
