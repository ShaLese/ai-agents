import ollama

# Define each agent as a separate function
def marketing_agent(topic, previous_arguments):
    prompt = f"As the Marketing Department, present your position on: {topic}. Previous arguments: {' '.join(previous_arguments)}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def finance_agent(topic, previous_arguments):
    prompt = f"As the Finance Department, present your position on: {topic}. Previous arguments: {' '.join(previous_arguments)}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def operations_agent(topic, previous_arguments):
    prompt = f"As the Operations Department, present your position on: {topic}. Previous arguments: {' '.join(previous_arguments)}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def client_agent(topic, previous_arguments):
    prompt = f"As the Client Representative, present your position on: {topic}. Previous arguments: {' '.join(previous_arguments)}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()



def business_meeting():
    topic = input("Enter the topic for the business meeting: ")
    print(f"\nBusiness Meeting Topic: {topic}\n")
    arguments = []

    for turn in range(3):  # Simulate 3 rounds of discussion
        print(f"Round {turn + 1}:")
        
        # Marketing Department presents their position
        arg1 = marketing_agent(topic, arguments)
        arguments.append(arg1)
        print(f"Marketing Department: {arg1}\n")

        # Finance Department presents their position
        arg2 = finance_agent(topic, arguments)
        arguments.append(arg2)
        print(f"Finance Department: {arg2}\n")

        # Operations Department presents their position
        arg3 = operations_agent(topic, arguments)
        arguments.append(arg3)
        print(f"Operations Department: {arg3}\n")

        # Client Representative presents their position
        arg4 = client_agent(topic, arguments)
        arguments.append(arg4)
        print(f"Client Representative: {arg4}\n")

    print("Meeting concluded. Final arguments:")
    for i, arg in enumerate(arguments):
        print(f"Round {i // 4 + 1}, Argument {i % 4 + 1}: {arg}")

# Start the business meeting
business_meeting()