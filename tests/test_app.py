import pytest

from app import app, feedbacks


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    feedbacks.clear()

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Feedback System" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_submit_valid_feedback(client):
    response = client.post(
        "/",
        data={
            "name": "Aakash",
            "course": "DevOps",
            "feedback": "Very useful subject"
        }
    )

    assert response.status_code == 200
    assert b"Aakash" in response.data
    assert b"DevOps" in response.data
    assert b"Very useful subject" in response.data


def test_empty_name(client):
    response = client.post(
        "/",
        data={
            "name": "",
            "course": "DevOps",
            "feedback": "Good subject"
        }
    )

    assert response.status_code == 200
    assert b"Good subject" not in response.data


def test_empty_course(client):
    response = client.post(
        "/",
        data={
            "name": "Aakash",
            "course": "",
            "feedback": "Good subject"
        }
    )

    assert response.status_code == 200
    assert b"Good subject" not in response.data


def test_empty_feedback(client):
    response = client.post(
        "/",
        data={
            "name": "Aakash",
            "course": "DevOps",
            "feedback": ""
        }
    )

    assert response.status_code == 200
    assert b"Aakash" not in response.data


def test_multiple_feedbacks(client):
    client.post(
        "/",
        data={
            "name": "Aakash",
            "course": "DevOps",
            "feedback": "Excellent"
        }
    )

    response = client.post(
        "/",
        data={
            "name": "Rahul",
            "course": "Cloud Computing",
            "feedback": "Very good"
        }
    )

    assert response.status_code == 200
    assert b"Aakash" in response.data
    assert b"Rahul" in response.data