from llm import llm
from graph import graph

# Create a movie chat chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a movie expert providing information about movies."),
        ("human", "{input}"),
    ]
)

movie_chat = chat_prompt | llm | StrOutputParser()
# Create a set of tools
tools = [
    Tool.from_function(
        name="General Chat",
        description="For general movie chat not covered by other tools",
        func=movie_chat.invoke,
    )
]
# Create chat history callback

# Create the agent

# Create a handler to call the agent