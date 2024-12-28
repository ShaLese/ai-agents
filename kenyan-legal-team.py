import PyPDF2
import ollama

# Step 1: Convert PDF to Text
def pdf_to_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Load the Kenyan Constitution
kenyan_constitution = pdf_to_text("C:/Users/USER/ai-agents/TheConstitutionOfKenya.pdf")

# Step 2: Define the Agents
def judge_agent(context, constitution):
    prompt = f"As a judge in a Kenyan courtroom, manage the proceedings and make a ruling based on the following context: {context}. Refer to the Kenyan Constitution: {constitution}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def lawyer_agent(context):
    prompt = f"As a lawyer in a Kenyan courtroom, present arguments and evidence based on the following context: {context}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def accused_agent(context):
    prompt = f"As the accused in a Kenyan courtroom, present your defense based on the following context: {context}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def prosecutor_agent(context):
    prompt = f"As the prosecutor in a Kenyan courtroom, present the case against the accused based on the following context: {context}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def witness_agent(context):
    prompt = f"As a witness in a Kenyan courtroom, provide testimony based on the following context: {context}"
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

# Step 3: Define the Courtroom Simulation
def courtroom_simulation(case_details, has_lawyer=True):
    print(f"\nCase Details: {case_details}\n")
    context = case_details

    # Prosecutor presents the case
    print("Prosecutor's Statement:")
    prosecutor_statement = prosecutor_agent(context)
    print(prosecutor_statement)
    context += f"\nProsecutor's Statement: {prosecutor_statement}"

    # Witness provides testimony
    print("\nWitness Testimony:")
    witness_testimony = witness_agent(context)
    print(witness_testimony)
    context += f"\nWitness Testimony: {witness_testimony}"

    # Accused or Lawyer presents the defense
    if has_lawyer:
        print("\nLawyer's Defense:")
        defense = lawyer_agent(context)
    else:
        print("\nAccused's Defense:")
        defense = accused_agent(context)
    print(defense)
    context += f"\nDefense: {defense}"

    # Judge makes a ruling
    print("\nJudge's Ruling:")
    ruling = judge_agent(context, kenyan_constitution)
    print(ruling)

# Step 4: Start the Courtroom Simulation
case_details = input("Enter the details of the case: ")
has_lawyer = input("Does the accused have a lawyer? (yes/no): ").lower() == "yes"
courtroom_simulation(case_details, has_lawyer) 