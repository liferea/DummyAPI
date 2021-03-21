import time

import jsonschema
import json
import requests

URL = 'http://dummy.restapiexample.com/'
URL_GET = f'{URL}api/v1/employee/'
URL_POST = f'{URL}api/v1/create'


RESPONSE_CODE_OK = 200
RESPONSE_CODE_BAD_REQUEST = 400


def send_get_dummy_rest(request_id, with_data, positive_test):
    headers = {
        'User-agent': 'your bot 0.'+str(time.time())
    }
    s = requests.Session()
    for _ in range(10):
        response = s.get(url=f'{URL_GET}{request_id}', headers=headers)
        if response.status_code == 429:
            time.sleep(1)
            if _ == 9:
                assert False, 'Many 429 Error'
        else:
            if positive_test:
                assert_correct_response(response, RESPONSE_CODE_OK)
                if with_data:
                    scheme_validation(response, 'schemeGetResponseWithData')
                else:
                    scheme_validation(response, 'schemeGetResponseWithoutData')
            else:
                assert_correct_response(response, RESPONSE_CODE_BAD_REQUEST)
            return response


def send_post_dummy_rest(body):
    headers = {
        'User-agent': 'your bot 0.'+str(time.time())
    }
    s = requests.Session()
    for _ in range(10):
        response = s.post(url=URL_POST, json=body, headers=headers)
        if response.status_code == 429:
            time.sleep(1)
            if _ == 9:
                assert False, 'Many 429 Error'
        else:
            print(response.text)
            assert_correct_response(response, RESPONSE_CODE_OK)
            scheme_validation(response, 'schemePostResponse')
            return response


def scheme_validation(response, controller_name):
    with open(f'schemes/{controller_name}.json', encoding='utf-8') as scheme:
        jsonschema.validate(response.json(), json.loads(scheme.read()))


def assert_correct_response(response, response_code):
    if response.status_code == response_code:
        assert True
    else:
        print(f'REQUEST:\n{response.url}\nFAILED')
        print(f'METHOD => {response.request.method}')
        print(f'ACTUAL RESULT: {response.status_code}')
        print(f'EXPECTED RESULT: {response_code}')
        print(response.json())
        assert False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_post_dummy_rest()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
