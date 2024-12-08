import os
from dotenv import load_dotenv
from model import llm, tools, memory
from langchain.agents import AgentExecutor, create_tool_calling_agent
from prompt import prompt

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

agent = create_tool_calling_agent(llm, tools, prompt=prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=False,
    return_intermediate_steps=True,
)



