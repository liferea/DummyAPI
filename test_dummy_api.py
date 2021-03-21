import base_checks
import create_customer

POSITIVE_ID_VALUES_WITH_DATA = {'3', 5, '12'}
POSITIVE_ID_VALUES_WITHOUT_DATA = {1342344, 'asd', '-3432'}
NEGATIVE_ID_VALUES = {0, '$%^'}

POSITIVE_NAMES = {'', 'asd', '$%^*', '123', 123, True, -342}


# Tests GET request
def test_get_positive_request():
    for request_id in POSITIVE_ID_VALUES_WITH_DATA:
        base_checks.send_get_dummy_rest(request_id=request_id, with_data=True, positive_test=True)


def test_get_positive_request_without_data():
    for request_id in POSITIVE_ID_VALUES_WITHOUT_DATA:
        base_checks.send_get_dummy_rest(request_id=request_id, with_data=False, positive_test=True)


def test_get_negative_request():
    for request_id in NEGATIVE_ID_VALUES:
        base_checks.send_get_dummy_rest(request_id=request_id, with_data=False, positive_test=False)


# Tests POST request
def test_post_positive_name():
    for name in POSITIVE_NAMES:
        body = create_customer.create_body(name=name)
        base_checks.send_post_dummy_rest(body)


def test_post_positive_salary():
    for salary in POSITIVE_NAMES:
        body = create_customer.create_body(name=salary)
        base_checks.send_post_dummy_rest(body)


def test_post_positive_age():
    for age in POSITIVE_NAMES:
        body = create_customer.create_body(name=age)
        base_checks.send_post_dummy_rest(body)


def test_post_positive_without_data():
    base_checks.send_post_dummy_rest(body={})
