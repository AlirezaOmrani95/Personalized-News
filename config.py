"""
File: config.py
Author: Ali Reza (ARO) Omrani
Email: omrani.alireza95@gmail.com
Date: 20 August 2025

Description
-----------
This file contains configuration settings for the LangChain framework and various APIs. If you wish to
change the configuration, please modify the values below.

Variables
---------
    TAVILY_INFO: values for the Tavily API integration.

Requirements
------------
    None
"""

import os
from typing import Any, Dict

# Langsmith environemtal information
os.environ.get("LANGSMITH_API_KEY")
os.environ.get("LANGSMITH_TRACING")
os.environ.get("LANGSMITH_PROJECT")
os.environ.get("LANGSMITH_ENDPOINT")

# Tavily environmental information
os.environ.get("TAVILY_API_KEY")
TAVILY_INFO: Dict[str, Any] = {
    "max_results": 20,
    "topic": "news",  # can be general, news, or finance
    "search_depth": "advanced",  # can be basic or advanced
    "time_range": "day",  # can be day, week, month, or year
    # To look at the library itself, visit:
    # https://python.langchain.com/docs/integrations/tools/tavily_search/
}
