import logging
import time

import requests
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .models import Repository, PopularityResponse
from .github_api import get_repo_data
from .popularity_calculator import calculate_popularity

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post('/is-popular', response_model=PopularityResponse)
async def check_popularity(repository: Repository):
    """
    Endpoint to check if a GitHub repository is popular.
    """
    try:
        start_time = time.time()  # Record start time
        repo_info = get_repo_data(repository.owner, repository.repo)
        score = calculate_popularity(repo_info)
        is_popular = score >= 500
        response_time_seconds = time.time() - start_time

        return {
            "repository": f"{repository.owner}/{repository.repo}",
            "is_popular": is_popular,
            "score": score,
            "response_time": response_time_seconds,
        }

    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "error": f"Validation error: {e}",
                "repository": f"{repository.owner}/{repository.repo}",
            },
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Internal server error: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": f"Internal server error: {e}",
                "repository": f"{repository.owner}/{repository.repo}",
            },
        )
    except KeyError:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "error": "Repository not found",
                "repository": f"{repository.owner}/{repository.repo}",
            },
        )


@router.get('/health', status_code=status.HTTP_200_OK)
async def health_check():
    """
    Endpoint to perform a health check.
    """
    return {"status": "OK"}
