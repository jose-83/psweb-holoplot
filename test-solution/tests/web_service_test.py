import pytest
import time

from assertions.response_assertions import *
from config import BASE_URI
# BASE_URI = "http://localhost:8080/processes"


def test_response_ok():
    response = requests.get(BASE_URI)
    assert_response_status_code_is_200(response)


@pytest.mark.parametrize("value", [1, 3, 5])
def test_retrieve_processes_consume_memory_above(value):
    response = requests.get(BASE_URI, params={'mem-above': value})
    assert_response_status_code_is_200(response)

    memory_usage = [pid['memory_percent'] for pid in response.json().values()]
    assert_all_elements_are_greater_than_given_value(memory_usage, value)


@pytest.mark.parametrize("value", [5, 15, 25])
def test_retrieve_processes_have_threads_more_than(value):
    response = requests.get(BASE_URI, params={'threads-above': value})
    assert_response_status_code_is_200(response)

    num_threads = [pid['num_threads'] for pid in response.json().values()]
    assert_all_elements_are_greater_than_given_value(num_threads, value)


@pytest.mark.parametrize("memory_value, thread_value", [(1, 1), (2, 10), (5, 25)])
def test_retrieve_processes_consume_memory_and_have_threads_more_than_values(memory_value, thread_value):
    response = requests.get(BASE_URI, params={'mem-above': memory_value, 'threads-above': thread_value})
    assert_response_status_code_is_200(response)

    memory_usage = [pid['memory_percent'] for pid in response.json().values()]
    num_threads = [pid['num_threads'] for pid in response.json().values()]
    assert_all_pair_elements_are_greater_than_given_values(memory_usage, num_threads, memory_value, thread_value)


def test_retrieve_a_process_by_pid():
    response = requests.get(BASE_URI)
    assert_response_status_code_is_200(response)
    assert_response_json_is_not_empty(response)

    desired_pid = list(response.json().keys())[0]
    pid_response = requests.get(BASE_URI + f'/{desired_pid}')
    assert_that_response_contains_only_one_process_info(pid_response)
    assert_that_pid_equals_to_given_pid(pid_response, desired_pid)


@pytest.mark.parametrize("value", [5])
def test_killing_a_process(value):
    response = requests.get(BASE_URI, params={'threads-above': value})
    assert_response_status_code_is_200(response)
    assert_response_json_is_not_empty(response)

    desired_pid = list(response.json().keys())[0]
    before_kill_response = requests.get(BASE_URI + f'/{desired_pid}')
    assert_response_status_code_is_200(before_kill_response)

    kill_response = requests.post(BASE_URI + f'/{desired_pid}/kill')
    assert_response_status_code_is_200(kill_response)
    time.sleep(5)

    after_kill_response = requests.get(BASE_URI + f'/{desired_pid}')
    assert_response_status_is_not_found(after_kill_response)
