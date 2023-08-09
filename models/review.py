#!/usr/bin/python3
""" class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review."""

    place_id = ""
    user_id = ""
    text = ""
