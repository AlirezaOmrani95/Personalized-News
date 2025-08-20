"""
File: langgraph_main.py
Author: Ali Reza (ARO) Omrani
Email: omrani.alireza95@gmail.com
Date: 20 August 2025

Description
-----------
This file contains the main entry point for the LangGraph application.

Requirements
------------
- langgraph
"""

import logging
from typing import Any, Dict

from langgraph.graph import StateGraph, START, END


from langgraph_nodes import (
    run_search_node,
    summarizer_node,
    format_digest_node,
    decision_function,
    States,
)
from config import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


builder = StateGraph(States)
builder.add_node("search", run_search_node)
builder.add_node("summarize_one", summarizer_node)
builder.add_node("format_digest", format_digest_node)

builder.add_edge(START, "search")
builder.add_conditional_edges(
    "search", decision_function, {"continue": "summarize_one", "finish": END}
)
builder.add_conditional_edges(
    "summarize_one",
    decision_function,
    {"continue": "summarize_one", "finish": "format_digest"},
)
builder.add_edge("format_digest", END)

graph = builder.compile()


result: Dict[str, Any] = graph.invoke(
    {"original_request": "What's the latest news on AI chips?"}
)

print(result["output"])
