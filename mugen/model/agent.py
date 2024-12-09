import os
from dotenv import load_dotenv
from model import llm, tools, memory
from langchain.agents import AgentExecutor, create_tool_calling_agent
from prompt import prompt
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

agent = create_tool_calling_agent(llm, tools, prompt=prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=False,
    return_intermediate_steps=True,
)

def invoke_agent(question):
    response = agent_executor.invoke({"input": question})['output']
    return response


