from agent import agent_executor

def invoke_agent(question):
    response = agent_executor.invoke({"input": question})['output']
    return response
