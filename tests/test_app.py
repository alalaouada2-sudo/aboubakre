from app import app, PAGES


def test_pages_count_at_least_ten():
    assert len(PAGES) >= 10


def test_all_main_pages_return_success():
    client = app.test_client()
    urls = [url for _, _, url in PAGES]
    for url in urls:
        response = client.get(url)
        assert response.status_code == 200, f"Expected 200 for {url}"


def test_assistant_api():
    client = app.test_client()
    response = client.post("/api/assistant", json={"question": "ما هي المجرة؟"})
    assert response.status_code == 200
    body = response.get_json()
    assert "answer" in body
