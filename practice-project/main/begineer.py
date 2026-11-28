from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(model="groq:openai/gpt-oss-20b", temperature=0.6)

# > ================================================================= MODELS/AGENTS =======================================================================

# agent = create_agent(model=llm)
# response = agent.invoke(
#     {
#         "messages": [
#             HumanMessage(content="Hi my name is Amit"),
#             AIMessage(content="Hello Amit! 👋 How can I help you today?"),
#             HumanMessage(content="tell me more about my name!")            
#         ]
#     }
# )
# print(response["messages"][-1].content)

# ? ================================================================= STREAMING =======================================================================

# for token, metadata in agent.stream(
#     {
#         "messages": [
#             HumanMessage(content="Hi my name is Amit"),
#             AIMessage(content="Hello Amit! 👋 How can I help you today?"),
#             HumanMessage(content="tell me more about my name!")            
#         ]
#     },
#     stream_mode="messages"
# ):
#     if token.content:
#         print(token.content, end="")
        
        
# > ================================================================= TOOLS =======================================================================

# ? ================================================================= BASIC USE =======================================================================
# from langchain.tools import tool

# @tool
# def print_documents(name: str)-> str:
#     """use this tool to generate the proper document for your student"""
#     return f"this is the document of {name}"

# agent=create_agent(
#     llm,
#     tools=[print_documents],
#     system_prompt="use the tool for the students and dont give any other response than this "
# )

# res = agent.invoke(
#     {
#         "messages": [
#             HumanMessage(content="Hello my name is Bruce Banner and generate the documents for the report card")
#         ]
#     }
# )

# print(res["messages"][-1].content)

# ? ================================================================= BETTER USE-CASE  =======================================================================
# using Tavily for the searching functionality

# from langchain.tools import tool
# from tavily import TavilyClient
# tavily_client = TavilyClient()

# @tool
# def web_search(query:str) -> any:
#     """Tool for web searching for the further information"""
#     return tavily_client.search(query)

# agent = create_agent(
#     llm,
#     tools=[web_search],
# )
    
# response = agent.invoke(
#     {
#         "messages":[
#             HumanMessage(content="give me the latest news for the ipo of the day")
#         ]
#     }
# )

# print(response["messages"][-1].content)

# > ================================================================= IN MEMORY =======================================================================
# from dotenv import load_dotenv
# from langchain.agents import create_agent
# from langchain.messages import HumanMessage, AIMessage
# from langgraph.checkpoint.memory import InMemorySaver

# load_dotenv()
# agent = create_agent(model="groq:openai/gpt-oss-20b", checkpointer=InMemorySaver())

# config = {"configurable": {"thread_id": "1"}}

# response = agent.invoke(
#     {
#         "messages": [
#             HumanMessage(content="My name is Bruce and i like blue color"),
#         ]
#     }, config
# )

# print(response["messages"][-1].content)


# response = agent.invoke(
#     {
#         "messages":[
#             HumanMessage(content="what is my favorite color")
#         ]
#     }, config
# )

# print(response["messages"][-1].content)

