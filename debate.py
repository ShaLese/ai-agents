# Multi-Agent Debate and Consensus Building (Using Ollama and Llama 3.2)
import ollama

# Define each agent as a separate function
def agent_1(topic, previous_arguments):
    prompt = f"{topic} Previous arguments: {' '.join(previous_arguments)}. As Agent 1, what is your argument?"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def agent_2(topic, previous_arguments):
    prompt = f"{topic} Previous arguments: {' '.join(previous_arguments)}. As Agent 2, what is your argument?"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def agent_3(topic, previous_arguments):
    prompt = f"{topic} Previous arguments: {' '.join(previous_arguments)}. As Agent 3, what is your argument?"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def agent_4(topic, previous_arguments):
    prompt = f"{topic} Previous arguments: {' '.join(previous_arguments)}. As Agent 4, what is your argument?"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def agent_5(topic, previous_arguments):
    prompt = f"{topic} Previous arguments: {' '.join(previous_arguments)}. As Agent 5, what is your argument?"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()


# The debate function
def debate(topic, max_turns=5):
    print(f"Debate Topic: {topic}\n")
    arguments = []

    for turn in range(max_turns):
        print(f"Turn {turn + 1}:")
        
        # Call each agent in sequence
        arg1 = agent_1(topic, arguments)
        arguments.append(arg1)
        print(f"Agent 1: {arg1}\n")

        arg2 = agent_2(topic, arguments)
        arguments.append(arg2)
        print(f"Agent 2: {arg2}\n")

        arg3 = agent_3(topic, arguments)
        arguments.append(arg3)
        print(f"Agent 3: {arg3}\n")

        arg4 = agent_4(topic, arguments)
        arguments.append(arg4)
        print(f"Agent 4: {arg4}\n")

        arg5 = agent_5(topic, arguments)
        arguments.append(arg5)
        print(f"Agent 5: {arg5}\n")

    print("Debate concluded. Final arguments:")
    for i, arg in enumerate(arguments):
        print(f"Agent {i + 1}: {arg}")

# Define the topic
topic = input("Enter the topic for the debate: ")

# Start the debate
debate(topic)

