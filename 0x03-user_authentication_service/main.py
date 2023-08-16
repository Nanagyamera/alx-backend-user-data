#!/usr/bin/env python3
"""
A simple end-to-end (E2E) integration test for `app.py`.
"""
import requests


BASE_URL = "http://localhost:5000"  # Update with your server's URL
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    url = f"{BASE_URL}/users"
    response = requests.post(url, data={"email": email, "password": password})
    assert response.status_code == 200
    print("User registered successfully")


def log_in_wrong_password(email: str, password: str) -> None:
    url = f"{BASE_URL}/sessions"
    response = requests.post(url, data={"email": email, "password": password})
    assert response.status_code == 401
    print("Incorrect login attempt handled successfully")


def profile_unlogged() -> None:
    url = f"{BASE_URL}/profile"
    response = requests.get(url)
    assert response.status_code == 403
    print("Access to unlogged profile handled successfully")


def log_in(email: str, password: str) -> str:
    url = f"{BASE_URL}/sessions"
    response = requests.post(url, data={"email": email, "password": password})
    assert response.status_code == 200
    session_id = response.cookies.get("session_id")
    print("Logged in successfully")
    return session_id


def profile_logged(session_id: str) -> None:
    url = f"{BASE_URL}/profile"
    cookies = {"session_id": session_id}
    response = requests.get(url, cookies=cookies)
    assert response.status_code == 200
    print("Access to logged-in profile handled successfully")


def log_out(session_id: str) -> None:
    url = f"{BASE_URL}/sessions"
    cookies = {"session_id": session_id}
    response = requests.delete(url, cookies=cookies)
    assert response.status_code == 302
    print("Logged out successfully")


def reset_password_token(email: str) -> str:
    url = f"{BASE_URL}/reset_password"
    response = requests.post(url, data={"email": email})
    assert response.status_code == 200
    reset_token = response.json()["reset_token"]
    print("Password reset token obtained successfully")
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    url = f"{BASE_URL}/update_password"
    body = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password,
    }
    data = {body}
    response = requests.post(url, data=body)
    assert response.status_code == 200
    print("Password updated successfully")


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
