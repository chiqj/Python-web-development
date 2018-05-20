# coding=utf-8

import pytest

from url_list_converter import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client

def test_list_converter(client):
    rv = client.get("/list1/a+b+c/")
    assert b"Separator: + ['a', 'b', 'c']" == rv.data

def test_user_defined_list_converter(client):
    rv = client.get("/list2/a|b|c/")
    assert b"Separator: | ['a', 'b', 'c']" == rv.data
