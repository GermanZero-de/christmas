import pytest
import json

import christmas.data as data


def test_invalid_input():
    assert data.validate_input('foobar') is False
    assert data.validate_input(b'postcode=foobar') is False
    assert data.validate_input('111111') is False
    assert data.validate_input(b'0') is False
    assert data.validate_input(b'; exec bla') is False
    assert data.validate_input(b'postcode=; exec bla') is False
    assert data.validate_input(b'True') is False
    assert data.validate_input('12f34') is False


def test_valid_input():
    assert data.validate_input(b'postcode=12345') == '12345'
    assert data.validate_input(b'postcode=01234') == '01234'
    assert data.validate_input(b'postcode=12589') == '12589'


def test_valid_uuid():
    assert data.get_uuid("12589") == "2c8dfdc9-5efd-4b38-a0dc-300ad96d537d"
    assert data.get_uuid("91058") == "bbee4f1d-36c1-444e-a021-d35ea954be5f"
    assert data.get_uuid("68789") == "48db5bda-0234-4ba0-b584-d14a6cbe5bc9"
    assert data.get_uuid("88499") == "d13c5f23-39a7-4246-971e-5a54e750c30b"
    assert data.get_uuid("01561") == "f1cb7f2e-0ed7-4c0c-a1fd-b23f901c460c"

def test_invalid_uuid():
    assert data.get_uuid("12345") == False
    assert data.get_uuid("00000") == False
    assert data.get_uuid("98765") == False

def test_get_profile_success():
    assert data.get_profile("bbee4f1d-36c1-444e-a021-d35ea954be5f") == {'degree': None, 'first_name': 'Stefan', 'last_name': 'Müller', 'party': 'CSU', 'picture_url': 'https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/stefan_mueller_114.jpg'}
    assert data.get_profile("2c8dfdc9-5efd-4b38-a0dc-300ad96d537d") == {'degree': 'Dr.', 'first_name': 'Gregor', 'last_name': 'Gysi', 'party': 'DIE LINKE', 'picture_url': 'https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/dr_gregor_gysi_13.jpg'}
    assert data.get_profile("680f2d5e-5506-4104-908a-bdcb51d6b172") == {'degree': None, 'first_name': 'Helge', 'last_name': 'Lindh', 'party': 'SPD', 'picture_url': 'https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/users/helgelindh3m.jpg'}
    assert data.get_profile("776af5e3-42e2-47d2-9941-63740bf12384") == {'degree': 'Dr.', 'first_name': 'Matthias', 'last_name': 'Bartke', 'party': 'SPD', 'picture_url': 'https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/users/18010148_1122966434515952_2325588779670743477_n_0.jpg'}

def test_get_profile_fail():
    assert data.get_profile("foobar") == False
    assert data.get_profile("4f981600-1744-4e44-adeb-1af1a7fc6d7a") == False
    assert data.get_profile("&%$") == False
