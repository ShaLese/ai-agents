import ollama

# Define each agent as a separate function
def code_writing_agent(requirements):
    prompt = f"Write Python code based on the following requirements: {requirements}"
    response = ollama.generate(model="codellama", prompt=prompt)
    return response["response"].strip()

def code_review_agent(code):
    prompt = f"Review the following Python code for errors and improvements:\n{code}"
    response = ollama.generate(model="codellama", prompt=prompt)
    return response["response"].strip()

def code_testing_agent(code):
    prompt = f"Write test cases for the following Python code:\n{code}"
    response = ollama.generate(model="codellama", prompt=prompt)
    return response["response"].strip()

def documentation_agent(code):
    prompt = f"Write documentation for the following Python code:\n{code}"
    response = ollama.generate(model="codellama", prompt=prompt)
    return response["response"].strip()

def code_development():
    requirements = input("Enter the requirements for the code: ")
    
    # Write the code
    code = code_writing_agent(requirements)
    print(f"\nGenerated Code:\n{code}\n")

    # Review the code
    review = code_review_agent(code)
    print(f"Code Review:\n{review}\n")

    # Test the code
    tests = code_testing_agent(code)
    print(f"Test Cases:\n{tests}\n")

    # Document the code
    documentation = documentation_agent(code)
    print(f"Documentation:\n{documentation}\n")

    # Combine the outputs into a complete project
    project = f"Generated Code:\n{code}\n\nCode Review:\n{review}\n\nTest Cases:\n{tests}\n\nDocumentation:\n{documentation}"
    print("Final Project:")
    print(project)

# Start the code development process
code_development()