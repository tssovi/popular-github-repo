from typing import Dict


def calculate_popularity(repository: Dict[str, int]) -> int:
    """
    Calculate the popularity score of a repository based on the number of stars and forks.

    Args:
        repository (Dict[str, int]): A dictionary containing the number of stars and forks of the repository.

    Returns:
        int: The popularity score of the repository.
    """
    score = repository.get('stargazers_count', 0) + (repository.get('forks_count', 0) * 2)
    return score
