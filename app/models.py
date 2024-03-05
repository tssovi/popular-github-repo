from pydantic import BaseModel, Field


class Repository(BaseModel):
    """
    Represents a GitHub repository.
    """
    owner: str = Field(..., description="The owner of the repository")
    repo: str = Field(..., description="The name of the repository")


class PopularityResponse(BaseModel):
    """
    Represents the response indicating the popularity of a GitHub repository.
    """
    repository: str = Field(..., description="The full name of the repository (owner/repo)")
    is_popular: bool = Field(..., description="Indicates whether the repository is popular")
    score: int = Field(..., description="The popularity score of the repository")
    response_time: float = Field(..., description="Response time in seconds")
