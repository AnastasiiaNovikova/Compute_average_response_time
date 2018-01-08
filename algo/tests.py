from django.test import TestCase

from algo.views import compute_average_response_time


class ResultTestCase(TestCase):
    """
    Check compute_average_response_time function works properly in case the log file is empty
        
    """

    def test_compute_average_response_time(self):
        self.maxDiff = None

        input_data = [
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
        response = (
            {'status_code: 200': {'average for 5': '4.440', 'average for 10': '4.533', 'average for 20': '4.533'},
             'status_code: 404': {'average for 5': '6.733', 'average for 10': '6.733', 'average for 20': '6.733'},
             'status_code: 500': {'average for 5': '4.400', 'average for 10': '4.400', 'average for 20': '4.400'}},
            ['average for 10 for code 200 was computed with 6 values',
             'average for 20 for code 200 was computed with 6 values',
             'average for 5 for code 404 was computed with 3 values',
             'average for 10 for code 404 was computed with 3 values',
             'average for 20 for code 404 was computed with 3 values',
             'average for 5 for code 500 was computed with 4 values',
             'average for 10 for code 500 was computed with 4 values',
             'average for 20 for code 500 was computed with 4 values'])

        result = compute_average_response_time(input_data)
        self.assertEqual(result, response)
