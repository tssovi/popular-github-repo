import os

import pytest
import requests


API_BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost:8000')


@pytest.mark.parametrize(
    "owner,repo,is_popular,expected_status",
    [
        ("facebook", "react", True, 200),
        ("test_user", "nonexistent_repo", False, 404),
    ],
)
def test_is_popular(owner, repo, is_popular, expected_status):
    response = requests.post(
        f"{API_BASE_URL}/is-popular",
        json={"owner": owner, "repo": repo}
    )
    assert response.status_code == expected_status

    if expected_status == 200:
        assert response.json()["is_popular"] == is_popular
    else:
        assert "error" in response.json()
