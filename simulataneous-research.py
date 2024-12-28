import ollama

# Define each agent as a separate function
def agent_1(subtopic):
    prompt = f"Research the following subtopic: {subtopic}. Provide a detailed summary."
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def agent_2(subtopic):
    prompt = f"Research the following subtopic: {subtopic}. Provide a detailed summary."
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def agent_3(subtopic):
    prompt = f"Research the following subtopic: {subtopic}. Provide a detailed summary."
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def agent_4(subtopic):
    prompt = f"Research the following subtopic: {subtopic}. Provide a detailed summary."
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def agent_5(subtopic):
    prompt = f"Research the following subtopic: {subtopic}. Provide a detailed summary."
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()


def research_and_synthesize(main_topic, subtopics):
    print(f"Main Research Topic: {main_topic}\n")
    findings = []

    # Assign subtopics to agents and collect their findings
    findings.append(agent_1(subtopics[0]))
    findings.append(agent_2(subtopics[1]))
    findings.append(agent_3(subtopics[2]))
    findings.append(agent_4(subtopics[3]))
    findings.append(agent_5(subtopics[4]))

    # Synthesize the final report
    print("Research Findings:")
    for i, finding in enumerate(findings):
        print(f"Subtopic {i + 1}: {finding}\n")

    print("Synthesized Final Report:")
    final_report = " ".join(findings)
    print(final_report)

# Get user input for the main topic and subtopics
main_topic = input("Enter the main research topic: ")
subtopics = set()  # Use a set to avoid duplicate subtopics

print("Enter subtopics (type 'done' to finish):")
while True:
    subtopic = input("Subtopic: ")
    if subtopic.lower() == "done":
        break
    subtopics.add(subtopic)

# Convert the set to a list for indexing
subtopics = list(subtopics)

# Start the research and synthesis
research_and_synthesize(main_topic, subtopics)