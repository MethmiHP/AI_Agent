from agent.agent import EventOpsAgent


def main():

    agent = EventOpsAgent()

    response = agent.ask(
        "What can an AI agent do for a banquet hall business?"
    )

    print(response)


if __name__ == "__main__":
    main()