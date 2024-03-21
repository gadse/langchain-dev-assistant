import time

from langchain.agents import AgentExecutor


def launch(agent_executor: AgentExecutor):
    chat_history = []

    while True:
        command = input("🤖 > ")
        start = time.process_time()

        if command == "exit":
            print("exiting...")
            break

        else:
            response = agent_executor.invoke(
                {
                    "input": command,
                    "chat_history": chat_history,
                }
            )
            chat_history.append(command)
            chat_history.append(response["output"])

        end = time.process_time()
        elapsed = str(round(end - start, 2))
        print(f"Answering time: {elapsed} seconds")
