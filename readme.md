# Personalized News

A project for delivering personalized news recommendations using advanced language models and graph-based techniques.

## Features

- User profiling for tailored news feeds
- Integration with multiple news sources
- Real-time updates and recommendations
- Scalable architecture using LangGraph

## Installation

```bash
git clone https://github.com/yourusername/personalized-news.git
cd personalized-news
pip install -r requirements.txt
```
## Project Structure

```
personalized-news/
├── config.py
├── constants.py
├── langchain_main.py
├── langchain_tools.py
├── langgraph_main.py
├── langgraph_nodes.py
├── langgraph.json
├── LICENSE
├── llm_output_structures.py
└── requirements.txt
```
## Usage

1. Run the main application using one of the following methods:

    - **LangGraph approach:**
      ```bash
      python langgraph_main.py
      ```
    - **LangChain approach:**
      ```bash
      python langchain_main.py
      ```

2. Access personalized news recommendations via the provided interface.

## Technologies

- Python
- LangGraph
- LangChain
- OpenAI/LLM APIs

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the **[MIT License](LICENSE)**.
