"""
File: langchain_tools.py
Author: Ali Reza (ARO) Omrani
Email: omrani.alireza95@gmail.com
Date: 20 August 2025

Description
-----------
This file contains utility functions and tools for interacting with the LangChain framework
and various APIs.

Functions
---------
    summarizer_tool(article_text): summarizes the content of an article and returns the title and
    summary.
    url_reader_tool(url): reads the article at the given URL and returns its content.

Variables
---------
    TAVILY_SEARCH_TOOL: A tool for searching articles using the Tavily API.

Requirements
------------
- langchain_core
- langchain
- langchain_ollama
- langchain_tavily
"""

import requests
from typing import Dict, Any

from langchain_core.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

from constants import SYSTEM_PROMPT, USER_PROMPT
from llm_output_structures import summarization_request
from config import TAVILY_INFO


# Langchain Tools
@tool
def summarizer_tool(article_text: str) -> Dict[str, Any]:
    """
    This tool summarizes the content of an article and returns the title and summary.

    Args:
        article_text (str): The text of the article to summarize.

    Returns:
        Dict[str, Any]: A dictionary containing the title and summary of the article.
    """
    model = ChatOllama(model="gemma3:12b", temperature=0.0)
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", SYSTEM_PROMPT), ("user", USER_PROMPT)]
    )
    summary_parser = PydanticOutputParser(pydantic_object=summarization_request)

    summarizer_chain = (
        {"article": lambda x: x["article"]}
        | prompt_template.partial(instructions=summary_parser.get_format_instructions())
        | model
        | summary_parser
    )
    summary: Dict[str, Any] = summarizer_chain.invoke({"article": article_text})
    return summary


@tool
def url_reader_tool(url: str) -> str:
    """
    This tool reads the article in the URL and returns its content as a str.

    Args:
        url (str): The URL to read.

    Returns:
        str: The content of the article.
    """
    jina_url = "https://r.jina.ai/" + url
    response = requests.get(jina_url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error reading URL {url}: {response.status_code}"


TAVILY_SEARCH_TOOL = TavilySearch(
    max_results=TAVILY_INFO["max_results"],
    topic=TAVILY_INFO["topic"],
    search_depth=TAVILY_INFO["search_depth"],
    time_range=TAVILY_INFO["time_range"],
)
