import ollama

# Define each agent as a separate function
def faq_agent(question):
    prompt = f"As a FAQ agent, answer the following customer question: {question}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def technical_support_agent(issue):
    prompt = f"As a technical support agent, troubleshoot the following issue: {issue}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def refund_agent(request):
    prompt = f"As a refund agent, process the following refund request: {request}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()


def customer_support():
    print("Welcome to the Customer Support System!\n")

while True:
    print("Choose the type of support you need:")
    print("1. FAQ")
    print("2. Technical Support")
    print("3. Refund Request")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        question = input("Enter your question: ")
        response = faq_agent(question)
        print(f"FAQ Agent: {response}\n")
    elif choice == "2":
        issue = input("Describe your technical issue: ")
        response = technical_support_agent(issue)
        print(f"Technical Support Agent: {response}\n")
    elif choice == "3":
        request = input("Describe your refund request: ")
        response = refund_agent(request)
        print(f"Refund Agent: {response}\n")
    elif choice == "4":
        print("Thank you for using our customer support system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")

# Start the customer support system
customer_support()   