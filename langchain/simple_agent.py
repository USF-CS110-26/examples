from langchain.agents import create_agent


def get_price(product: str):
    """Return the price of a product."""
    print("get_price tool")
    prices = {"apple": 2, "milk": 4, "bread": 3}
    return prices.get(product, "Unknown product")


def get_stock(product: str):
    """Return the quantity in stock."""
    print("get_stock tool")
    stock = {"apple": 10, "milk": 5, "bread": 0}
    return stock.get(product, "Unknown product")


def main():
    agent = create_agent(
        model="openai:gpt-4o-mini",
        tools=[get_price, get_stock],
        system_prompt="You are a helpful shopping assistant. "
                      "Use the available tools to answer questions "
                      "about product prices and availability."
    )

    while True:
        question = input("Ask a question (or quit): ")

        if question.lower() == "quit":
            break

        result = agent.invoke({
            "messages": [
                {"role": "user", "content": question}
            ]
        })

        print(result["messages"][-1].content)


if __name__ == "__main__":
    main()