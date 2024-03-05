import os
import logging
import requests

from .exceptions import APIError, RateLimitExceededError, AuthenticationError

logger = logging.getLogger(__name__)

GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", "GITHUB_SECRET_API_KEY")


def get_repo_data(owner: str, repo: str) -> dict:
    """
    Retrieve repository data from GitHub API.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        dict: A dictionary containing repository data, including 'stargazers_count' and 'forks_count'.

    Raises:
        KeyError: If the repository is not found.
        RateLimitExceededError: If GitHub API rate limit is exceeded.
        AuthenticationError: If the GitHub access token is invalid.
        APIError: If there is an error communicating with the GitHub API.
    """
    if not GITHUB_ACCESS_TOKEN:
        raise AuthenticationError("GitHub access token is not provided")

    headers = {'Authorization': f'token {GITHUB_ACCESS_TOKEN}'}
    url = f'https://api.github.com/repos/{owner}/{repo}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            'stargazers_count': data['stargazers_count'],
            'forks_count': data['forks_count']
        }
    elif response.status_code == 404:
        logger.error(f"Repository not found. Error: {response.text}")
        raise KeyError("Repository not found")
    elif response.status_code == 403:
        logger.error(f"GitHub API rate limit exceeded. Error: {response.text}")
        raise RateLimitExceededError("GitHub API rate limit exceeded")
    elif response.status_code == 401:
        logger.error(f"Invalid GitHub access token. Error: {response.text}")
        raise AuthenticationError("Invalid GitHub access token")
    else:
        logger.error(f"GitHub API error: {response.status_code} - {response.text}")
        raise APIError(f"GitHub API error: {response.status_code} - {response.text}")
