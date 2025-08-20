"""
File: langchain_main.py
Author: Ali Reza (ARO) Omrani
Email: omrani.alireza95@gmail.com
Date: 20 August 2025

Description
-----------
This file contains the main entry point for the LangChain application.

Functions
---------
    main(): Entry point for the LangChain application.

Requirements
------------
- langchain
- langchain_ollama
"""

import logging

from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from langchain_tools import TAVILY_SEARCH_TOOL, summarizer_tool, url_reader_tool
from config import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    """
    Entry point for the LangChain application.

    Args
    ----
        None

    Returns
    -------
        None
    """
    tools_list = [TAVILY_SEARCH_TOOL, summarizer_tool, url_reader_tool]
    model = ChatOllama(model="qwen3:14b", temperature=0.0)

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("placeholder", "{messages}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    agent = create_tool_calling_agent(
        llm=model,
        prompt=prompt_template,
        tools=tools_list,
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_list,
        verbose=True,
    )

    user_input: str = input("Enter your query: ")

    response = agent_executor.invoke({"messages": [("user", user_input)]})

    print(response)


if __name__ == "__main__":
    main()
