# 3 AI Agents that work together to research and write a blog post
# Each agent has a different role and set of tasks
# The agents are:
# - Researcher: finds and reads articles on a given topic
# - Writer: writes a blog post based on the articles
# - Editor: edits the blog post written by the writer
# The agents communicate with each other to complete the posts

import ollama

# Function for the Researcher Agent
def researcher_agent(topic, temperature=0.5, max_tokens=300, stream=False):
    prompt = f"""
    You are a Researcher AI. Your task is to gather and organize relevant information about the following topic:
    Topic: {topic}

    Provide a detailed outline with key points, statistics, and quotes from reliable sources. Ensure the information is accurate and up-to-date.
    """
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        options={
            "temperature": temperature,
            "max_tokens": max_tokens
        },
        stream=stream
    )
    if stream:
        return "".join(chunk['response'] for chunk in response)
    return response['response']

# Function for the Writer Agent
def writer_agent(research_output, temperature=0.7, max_tokens=500, stream=False):
    prompt = f"""
    You are a Writer AI. Your task is to write a clear, engaging, and well-structured post based on the following research:
    Research: {research_output}

    Write a draft post that incorporates the research data, statistics, and quotes. Ensure the tone is professional and the content is easy to read.
    """
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        options={
            "temperature": temperature,
            "max_tokens": max_tokens
        },
        stream=stream
    )
    if stream:
        return "".join(chunk['response'] for chunk in response)
    return response['response']

# Function for the Editor Agent
def editor_agent(draft_post, temperature=0.3, max_tokens=400, stream=False):
    prompt = f"""
    You are an Editor AI. Your task is to refine and polish the following draft post:
    Draft Post: {draft_post}

    Review the post for grammar, spelling, and punctuation errors. Ensure clarity, coherence, and consistency. Optimize the tone and style for a professional audience. Suggest improvements for structure and flow.
    """
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        options={
            "temperature": temperature,
            "max_tokens": max_tokens
        },
        stream=stream
    )
    if stream:
        return "".join(chunk['response'] for chunk in response)
    return response['response']

# Main function to run the agents
def create_post(topic, researcher_temp=0.5, writer_temp=0.7, editor_temp=0.3, stream=False):
    print("Starting Researcher Agent...")
    research_output = researcher_agent(topic, temperature=researcher_temp, stream=stream)
    print("Researcher Output:\n", research_output)

    print("\nStarting Writer Agent...")
    draft_post = writer_agent(research_output, temperature=writer_temp, stream=stream)
    print("Writer Output (Draft):\n", draft_post)

    print("\nStarting Editor Agent...")
    final_post = editor_agent(draft_post, temperature=editor_temp, stream=stream)
    print("Editor Output (Final Post):\n", final_post)

    return final_post

# Function to get user input
def get_user_input():
    topic = input("Enter the topic for the post: ")
    researcher_temp = float(input("Enter temperature for Researcher (0.0 to 1.0): "))
    writer_temp = float(input("Enter temperature for Writer (0.0 to 1.0): "))
    editor_temp = float(input("Enter temperature for Editor (0.0 to 1.0): "))
    stream = input("Enable streaming? (yes/no): ").strip().lower() == "yes"
    return topic, researcher_temp, writer_temp, editor_temp, stream

# Example usage
if __name__ == "__main__":
    topic, researcher_temp, writer_temp, editor_temp, stream = get_user_input()
    final_post = create_post(
        topic,
        researcher_temp=researcher_temp,
        writer_temp=writer_temp,
        editor_temp=editor_temp,
        stream=stream
    )
    print("\nFinal Post:\n", final_post)