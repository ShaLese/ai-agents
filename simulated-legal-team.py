import ollama

# Define each agent as a separate function
def lawyer_agent(case_details):
    prompt = f"As a lawyer, present your arguments for the following case: {case_details}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def judge_agent(arguments):
    prompt = f"As a judge, review the following arguments and provide your ruling: {arguments}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def client_agent(case_details):
    prompt = f"As a client, explain your perspective on the following case: {case_details}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()



def legal_simulation():
    case_details = input("Enter the details of the legal case: ")
    print(f"\nLegal Case: {case_details}\n")
    
    # Lawyer presents arguments
    arguments = lawyer_agent(case_details)
    print(f"Lawyer's Arguments:\n{arguments}\n")

    # Client provides perspective
    client_perspective = client_agent(case_details)
    print(f"Client's Perspective:\n{client_perspective}\n")

    # Judge reviews arguments and makes a ruling
    ruling = judge_agent(arguments)
    print(f"Judge's Ruling:\n{ruling}\n")

# Start the legal simulation
legal_simulation()