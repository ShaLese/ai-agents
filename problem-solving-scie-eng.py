import ollama
import requests
import json
import os

# Step 1: Fetch or Read Data
def fetch_data(source):
    if source.startswith(("http://", "https://")):  # If it's a URL
        try:
            response = requests.get(source)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()  # Assuming the data is in JSON format
        except requests.exceptions.RequestException as e:
            return f"Error fetching data: {e}"
    else:  # If it's a local file path
        if os.path.exists(source):
            try:
                with open(source, "r", encoding="utf-8") as file:
                    return json.load(file)
            except Exception as e:
                return f"Error reading file: {e}"
        else:
            return f"File not found: {source}"

# Step 2: Define Each Agent
def hypothesis_generation_agent(problem):
    prompt = f"Generate hypotheses to solve the following scientific or engineering problem: {problem}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def data_analysis_agent(data):
    prompt = f"Analyze the following data to support or refute the hypotheses: {json.dumps(data)}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def solution_validation_agent(hypotheses, analysis):
    prompt = f"Validate the following hypotheses based on the analysis: {hypotheses}, {analysis}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

# Step 3: Define the Problem-Solving Function
def problem_solving():
    problem = input("Enter the scientific or engineering problem: ")
    source = input("Enter the URL of the online resource or the path to a local JSON file: ")
    print(f"\nProblem: {problem}\n")
    
    # Fetch or read data
    print("Fetching or reading data...")
    data = fetch_data(source)
    if isinstance(data, str):  # If there's an error
        print(data)
        return
    print(f"Data fetched/read: {json.dumps(data, indent=2)}\n")

    # Generate hypotheses
    hypotheses = hypothesis_generation_agent(problem)
    print(f"Generated Hypotheses:\n{hypotheses}\n")

    # Analyze data
    analysis = data_analysis_agent(data)
    print(f"Data Analysis:\n{analysis}\n")

    # Validate solutions
    validation = solution_validation_agent(hypotheses, analysis)
    print(f"Solution Validation:\n{validation}\n")

# Start the problem-solving process
problem_solving()