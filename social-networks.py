import ollama

# Define each agent as a separate function
def agent_1(topic):
    prompt = f"As a member of a social network, write a post about: {topic}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def agent_2(post):
    prompt = f"As a member of a social network, write a comment on the following post: {post}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def agent_3(comment):
    prompt = f"As a member of a social network, reply to the following comment: {comment}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()



def social_network_simulation():
    topic = input("Enter the topic for the social network discussion: ")
    print(f"\nSocial Network Topic: {topic}\n")
    
    # Agent 1 writes a post
    post = agent_1(topic)
    print(f"Agent 1's Post:\n{post}\n")

    # Agent 2 comments on the post
    comment = agent_2(post)
    print(f"Agent 2's Comment:\n{comment}\n")

    # Agent 3 replies to the comment
    reply = agent_3(comment)
    print(f"Agent 3's Reply:\n{reply}\n")

# Start the social network simulation
social_network_simulation()