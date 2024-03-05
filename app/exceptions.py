class APIError(Exception):
    """Base class for exceptions raised due to issues with the GitHub API."""
    pass


class RateLimitExceededError(APIError):
    """Exception raised when the GitHub API rate limit is exceeded."""
    pass


class AuthenticationError(APIError):
    """Exception raised when there is an authentication issue with the GitHub API."""
    pass
