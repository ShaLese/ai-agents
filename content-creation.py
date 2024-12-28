import ollama

# Define each agent as a separate function
def idea_generation_agent(topic):
    prompt = f"Generate creative ideas for marketing content about: {topic}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def content_writing_agent(idea):
    prompt = f"Write a detailed marketing content piece based on the following idea: {idea}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def seo_optimization_agent(content):
    prompt = f"Optimize the following marketing content for SEO: {content}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()



def content_creation():
    topic = input("Enter the topic for the marketing content: ")
    print(f"\nMarketing Content Topic: {topic}\n")
    
    # Generate ideas
    idea = idea_generation_agent(topic)
    print(f"Generated Idea:\n{idea}\n")

    # Write content
    content = content_writing_agent(idea)
    print(f"Written Content:\n{content}\n")

    # Optimize for SEO
    optimized_content = seo_optimization_agent(content)
    print(f"SEO-Optimized Content:\n{optimized_content}\n")

    # Combine the outputs into a complete marketing content
    marketing_content = f"Generated Idea:\n{idea}\n\nWritten Content:\n{content}\n\nSEO-Optimized Content:\n{optimized_content}"
    print("Final Marketing Content:")
    print(marketing_content)

# Start the content creation process
content_creation()