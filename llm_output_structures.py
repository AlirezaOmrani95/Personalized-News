"""
File: llm_output_structures.py
Author: Ali Reza (ARO) Omrani
Email: omrani.alireza95@gmail.com
Date: 20 August 2025

Description:
This file contains the output structures for the LangGraph application.

Classes
-------
    summarization_request: Represents a request for article summarization.

Requirements
------------
    None
"""

from pydantic import BaseModel, Field


class summarization_request(BaseModel):
    summary: str = Field(
        default_factory=str, description="The summary content of the article."
    )
    title: str = Field(default_factory=str, description="The title of the article.")
    notes: str = Field(
        default="",
        description="Any additional notes or comments from the llm model.",
    )
