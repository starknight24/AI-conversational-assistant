import sys
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic functions with numbers"""
    print("Tool has been called")
    return f"sum of {a} and {b} is {a + b}"
    

def main():
    model = ChatOpenAI(temperature = 0) 
    #temp 0 means there is no randomness

    tools = [calculator]
    #tool is an external servie an agent can call or utilise 

    agent_executor = create_react_agent(model, tools)

    print("Welcome! I am your AI assistant. Type 'quit' to exit")
    print("You can ask me to perform calculations or just chat with me")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            print("Assistant: Goodbye! Feel free to come back if you have any more questions. Have a great day!")
            sys.exit()

        print("\nAssistant: ", end="")
        try:
            for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
                 if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="")
            print()

        except SystemExit:
            raise
        except Exception as e:
            print(f"\n[Error]: {e}")


if __name__ == "__main__":
    main()
