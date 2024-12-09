import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search.tool import TavilySearchResults
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(temperature=0, model="llama-3.1-70b-versatile")
search_tool = TavilySearchResults(search_depth="advanced", max_results=10)
tools = [search_tool]
memory = ConversationBufferWindowMemory(window_size=5, output_key='output', input_key='input')