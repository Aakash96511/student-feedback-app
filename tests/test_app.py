import pytest

from app import app, feedbacks


@pytest.fixture()
def client():

    app.config["TESTING"] = True

    feedbacks.clear()

    with app.test_client() as client:
        yield client


# Test 1: Home page
def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200

    assert b"Student Feedback System" in response.data


# Test 2: Health check
def test_health_endpoint(client):

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json["status"] == "healthy"


# Test 3: Valid feedback submission
def test_submit_valid_feedback(client):

    response = client.post(
        "/",

        data={
            "name": "Aakash",
            "email": "aakash@example.com",
            "course": "DevOps",
            "feedback": "Very useful subject"
        }
    )

    assert response.status_code == 200

    assert b"Aakash" in response.data

    assert b"aakash@example.com" in response.data

    assert b"DevOps" in response.data

    assert b"Very useful subject" in response.data


# Test 4: Empty name
def test_empty_name(client):

    response = client.post(
        "/",

        data={
            "name": "",
            "email": "aakash@example.com",
            "course": "DevOps",
            "feedback": "Good subject"
        }
    )

    assert response.status_code == 200

    assert b"Good subject" not in response.data


# Test 5: Empty email
def test_empty_email(client):

    response = client.post(
        "/",

        data={
            "name": "Aakash",
            "email": "",
            "course": "DevOps",
            "feedback": "Good subject"
        }
    )

    assert response.status_code == 200

    assert b"Good subject" not in response.data


# Test 6: Empty course
def test_empty_course(client):

    response = client.post(
        "/",

        data={
            "name": "Aakash",
            "email": "aakash@example.com",
            "course": "",
            "feedback": "Good subject"
        }
    )

    assert response.status_code == 200

    assert b"Good subject" not in response.data


# Test 7: Empty feedback
def test_empty_feedback(client):

    response = client.post(
        "/",

        data={
            "name": "Aakash",
            "email": "aakash@example.com",
            "course": "DevOps",
            "feedback": ""
        }
    )

    assert response.status_code == 200

    assert b"Aakash" not in response.data


# Test 8: Multiple feedback submissions
def test_multiple_feedbacks(client):

    client.post(
        "/",

        data={
            "name": "Aakash",
            "email": "aakash@example.com",
            "course": "DevOps",
            "feedback": "Excellent"
        }
    )

    response = client.post(
        "/",

        data={
            "name": "Rahul",
            "email": "rahul@example.com",
            "course": "Cloud Computing",
            "feedback": "Very good"
        }
    )

    assert response.status_code == 200

    assert b"Aakash" in response.data

    assert b"Rahul" in response.data

    assert b"rahul@example.com" in response.data