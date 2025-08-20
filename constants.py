"""
File: constants.py
Author: Ali Reza (ARO) Omrani
Email: omrani.alireza95@gmail.com
Date: 20 August 2025

Description
-----------
This file contains constants used throughout the application. If you wish to change or add more
constants, please do so in this file.

Variables
---------
    SYSTEM_PROMPT: Contains system prompt for the summarization task.
    USER_PROMPT: Contains user prompt for the summarization task.

Requirements
------------
    None
"""

SYSTEM_PROMPT: str = (
    "You are a helpful assistant. Your task is to summarize the Tech news articles provided to you "
    " to three sentences.\n"
)
USER_PROMPT: str = (
    "Please summarize the following article:\n{article}"
    "**IMPORTANT**: You must only return the title and the summary in the following format:\n {instructions}"
)
