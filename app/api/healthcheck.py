"""
Healthcheck 
"""

from fastapi import APIRouter, Response, status


router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK
)
def get_healthcheck():
    """
    Check and return status of the service health
    """
    return Response(content="OK")
