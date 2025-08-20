"""
File: langgraph_nodes.py
Author: Ali Reza (ARO) Omrani
Email: omrani.alireza95@gmail.com
Date: 20 August 2025

Description
-----------
This file contains the node definitions for the LangGraph application.

Classes
-------

    States: Represents the state of the LangGraph application.

Functions
---------
    run_search_node: Searches for relevant articles based on the user's request.
    summarizer_node: Summarizes the content of the current article.
    format_digest_node: Formats the final output from the acquired summaries.
    decision_function: Decides the next step based on the remaining URLs.

Requirements
------------
    None
"""

import logging
from typing import Any, Dict, List, Literal, TypedDict

from langchain_tools import summarizer_tool, url_reader_tool, TAVILY_SEARCH_TOOL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class States(TypedDict):
    """
    Represents the state of the LangGraph application.

    Fields:
        original_request (str): The user's original search request.
        urls (List[str]): List of URLs to process.
        summaries (List[str]): List of article summaries.
        current_url (str): The URL currently being processed.
        output (str): The final formatted output.
    """

    original_request: str
    urls: List[str]
    summaries: List[str]
    current_url: str
    output: str


def run_search_node(state: States) -> Dict[str, Any]:
    """
    Search for relevant articles based on the user's request.

    Args:
        state (States): The current state of the application.

    Returns:
        Dict[str, Any]: The updated state of the application.
    """
    logger.info("Running search node with request: %s", state["original_request"])
    urls: List[str] = []
    user_input: str = state["original_request"]
    result: Dict[str, Any] = TAVILY_SEARCH_TOOL.invoke({"query": user_input})

    for item in result["results"]:
        urls.append(item["url"])
    return {"urls": urls, "summaries": []}


def summarizer_node(state: States) -> Dict[str, Any]:
    """
    Summarizes the content of the current article.

    Args:
        state (States): The current state of the application.

    Returns:
        Dict[str, Any]: The updated state of the application.
    """
    logger.info("Running summarizer node with the current URL")
    state["current_url"] = state["urls"][0]
    article: str = url_reader_tool(state["current_url"])
    if "Error reading URL" in article:
        logger.error("Failed to read article from URL: %s", state["current_url"])
        return {"urls": state["urls"][1:]}
    summary: Dict[str, Any] = summarizer_tool(article)

    summaries = state["summaries"] + [summary]

    return {"summaries": summaries, "urls": state["urls"][1:]}


def format_digest_node(state: States) -> Dict[str, Any]:
    """
    Format the final output from the acquired summaries.

    Args:
        state (States): The current state of the application.

    Returns:
        Dict[str, Any]: The updated state of the application.
    """
    logger.info("Formatting the digest from summaries")
    counter = 1
    summaries: str = ""
    for summary in state["summaries"]:
        summaries += f"\n{counter}) **Title:** {summary.title}\n- {summary.summary}\n"
        counter += 1

    return {"output": summaries}


def decision_function(state: States) -> Literal["continue", "finish"]:
    """
    Decide the next step based on the remaining URLs.

    Args:
        state (States): The current state of the application.

    Returns:
        Literal["continue", "finish"]: The next step to take.
    """
    logger.info("Deciding next step based on remaining URLs")
    if state["urls"]:
        return "continue"
    return "finish"
