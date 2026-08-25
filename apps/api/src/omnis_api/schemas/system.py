"""
System API schemas.
"""

from pydantic import BaseModel


class SystemResponse(BaseModel):
    """System runtime information."""

    name: str
    version: str
    environment: str
    status: str
