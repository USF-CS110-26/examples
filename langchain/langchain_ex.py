from langchain.chat_models import init_chat_model

model = init_chat_model("openai:gpt-4o-mini")

def ask_tutor(question):
    messages = [
        ("system", "You are a Python tutor for beginners. "
                   "Explain concepts in simple language. "
                   "Give short examples."),
        ("human", question)
    ]

    response = model.invoke(messages)
    return response.content


def main():
    while True:
        question = input("Ask a Python question (or quit): ")

        if question.lower() == "quit":
            break

        answer = ask_tutor(question)
        print(answer)


if __name__ == "__main__":
    main()