from api_demo import fetch_posts


def test_fetch_posts_success(mocker):
    mock_response = mocker.Mock()
    expected_data = [{"id": 1, "title": "Test Post", "body": "This is a test."}]
    mock_response.status_code = 200
    mock_response.json.return_value = expected_data

    mocker.patch("requests.get", return_value=mock_response)

    posts = fetch_posts()
    assert posts == expected_data
    assert len(posts) == 1
    assert posts[0]["id"] == 1


def test_fetch_posts_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404

    mocker.patch("requests.get", return_value=mock_response)

    posts = fetch_posts()
    assert posts is None
