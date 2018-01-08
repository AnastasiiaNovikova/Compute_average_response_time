import json
import os
import tempfile
from statistics import mean

from django.http import HttpResponse

# test_data for requests

requests = [
    (200, 5.0),
    (404, 4.2),
    (200, 6.4),
    (500, 8.5),
    (500, 2.3),
    (200, 0.5),
    (404, 8.5),
    (200, 5.4),
    (500, 1.5),
    (500, 5.3),
    (200, 4.5),
    (404, 7.5),
    (200, 5.4)
]


class Algorithm:
    def __init__(self, algo):
        self.algorithm = algo

    def show_error_msg(self, error_type):
        print("Can't compute the result for {} because of {}".format(self.algorithm.__name__, error_type))

    def apply(self, *args, **kwargs):
        try:
            return self.algorithm(*args, **kwargs)
        except Exception as err:
            self.show_error_msg(err.__class__.__name__)


def compute_average_response_time(requests):
    response_data = dict()
    average_response_time_stat = dict()
    logs = list()

    def check_input_params(requests):
        print("type", type(requests))
        if not isinstance(requests, list):
            raise TypeError("Input data must be a list")

        for item in requests:
            if len(item) != 2:
                raise TypeError("Input data must be list of tuples with length 2")
            if not isinstance(item[0], int) or not isinstance(item[1], float):
                raise TypeError("The first argument must have type 'int', the second - type 'float' ")
            if not 100 <= item[0] <= 600:
                raise ValueError("The first argument must be an integer between 100 fnd 600")
            if not 0.0 <= item[1] <= 100.0:
                raise ValueError("The second argument must be a float between 0.0 and 100.0")

    def check_length(key, code, item, needed_num):
        if len(item) < needed_num:
            logs.append("{} for code {} was computed with {} values".format(code, key, len(item)))

    check_input_params(requests)
    storage_path = os.path.join(tempfile.gettempdir(), 'requests11.data')

    def get_data():
        if not os.path.exists(storage_path):
            return {}

        with open(storage_path, 'r') as f:
            raw_data = f.read()
            if raw_data:
                return json.loads(raw_data)

            return {}

    def put_data(data):
        with open(storage_path, 'w') as f:
            f.write(json.dumps(data))

    def build_request_dict():
        for item in requests:
            try:
                response_data[str(item[0])].append(item[1])
            except KeyError:
                response_data[str(item[0])] = [item[1]]

    old_data = get_data()

    def extend_statistics():
        for key, value in response_data.items():
            try:
                old_data[key].extend(value)
            except KeyError:
                old_data[key] = value

        put_data(old_data)

    def compute_average_for_request(txt, container, number_of_requests, key, value):
        container[txt] = "%.3f" % mean(value[-number_of_requests:])
        check_length(key, txt, value, number_of_requests)

    def compute_result():
        build_request_dict()
        extend_statistics()

        for key, value in old_data.items():
            tmp = dict()
            compute_average_for_request('average for 5', tmp, 5, key, value)
            compute_average_for_request('average for 10', tmp, 10, key, value)
            compute_average_for_request('average for 20', tmp, 20, key, value)
            average_response_time_stat['status_code: {}'.format(key)] = tmp

        return average_response_time_stat, logs

    return compute_result()


def show_response(requests):
    alg = Algorithm(compute_average_response_time)
    response = alg.apply(requests)
    return HttpResponse(json.dumps(response), content_type='application/json')