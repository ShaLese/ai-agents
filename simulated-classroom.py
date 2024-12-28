import ollama

# Define each agent as a separate function
def teacher_agent(topic):
    prompt = f"As a teacher, explain the following topic in simple terms: {topic}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def student_agent(topic, explanation):
    prompt = f"As a student, ask a question about the following topic: {topic}. Here is the teacher's explanation: {explanation}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def tutor_agent(question, explanation):
    prompt = f"As a tutor, provide additional clarification for the following question: {question}. Here is the teacher's explanation: {explanation}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()


def classroom():
    topic = input("Enter the topic for the classroom session: ")
    print(f"\nClassroom Topic: {topic}\n")
    
    # Teacher explains the topic
    explanation = teacher_agent(topic)
    print(f"Teacher: {explanation}\n")

    # Student asks a question
    question = student_agent(topic, explanation)
    print(f"Student: {question}\n")

    # Tutor provides additional clarification
    clarification = tutor_agent(question, explanation)
    print(f"Tutor: {clarification}\n")

# Start the classroom session
classroom()