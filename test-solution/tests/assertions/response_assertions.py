import requests
from hamcrest import *


def assert_response_status_code_is_200(response):
    assert_that(response.status_code, is_(equal_to(requests.codes.ok)))


def assert_response_status_is_not_found(response):
    assert_that(response.status_code, is_(equal_to(404)))


def assert_response_json_is_not_empty(response):
    assert_that(response.json(), is_not(empty()))


def assert_all_elements_are_greater_than_given_value(li, value):
    for item in li:
        assert_that(item, is_(greater_than(value)))


def assert_all_pair_elements_are_greater_than_given_values(li1, li2, val1, val2):
    for item1, item2 in zip(li1, li2):
        assert_that(item1, is_(greater_than(val1)))
        assert_that(item2, is_(greater_than(val2)))


def assert_that_response_contains_only_one_process_info(response):
    assert_that(response.json(), all_of(has_key("pid"), has_key("num_threads"),
                                        has_key("memory_percent"), has_key("name")))
    assert_that(len(response.json()), is_(equal_to(4)))


def assert_that_pid_equals_to_given_pid(response, pid):
    assert_that(response.json()['pid'], is_(equal_to(int(pid))))
