import ollama

# Define each agent as a separate function
def introduction_agent(theme):
    prompt = f"Write an engaging introduction for a story about: {theme}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def plot_agent(theme, introduction):
    prompt = f"Develop the plot for a story about: {theme}. Here is the introduction: {introduction}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def conclusion_agent(theme, plot):
    prompt = f"Write a satisfying conclusion for a story about: {theme}. Here is the plot: {plot}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()
    

# Define the storytelling function
def collaborative_storytelling():
    theme = input("Enter the theme or topic for the story: ")
    
    # Generate the introduction
    introduction = introduction_agent(theme)

    # Develop the plot
    plot = plot_agent(theme, introduction)

    # Write the conclusion
    conclusion = conclusion_agent(theme, plot)

    # Combine the parts into a complete story
    story = f"Introduction:\n{introduction}\n\nPlot Development:\n{plot}\n\nConclusion:\n{conclusion}"
    print("\nFinal Story:")
    print(story)

# Start the collaborative storytelling process
collaborative_storytelling()