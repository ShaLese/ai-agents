import ollama

# Define each agent as a separate function
def consumer_agent(resources, prices):
    prompt = f"As a consumer, decide how to allocate your resources based on the following prices: {prices}. You have {resources} units of resources."
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def producer_agent(demand, costs):
    prompt = f"As a producer, decide how much to produce based on the following demand: {demand} and costs: {costs}."
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()

def government_agent(economy_status):
    prompt = f"As the government, decide on policies to improve the economy based on the following status: {economy_status}."
    response = ollama.generate(model="llama3.2", prompt=prompt)
    return response["response"].strip()


def economic_simulation():
    # Initial conditions
    resources = 100
    prices = {"food": 10, "clothing": 20, "housing": 30}
    demand = {"food": 50, "clothing": 30, "housing": 20}
    costs = {"food": 5, "clothing": 10, "housing": 15}
    economy_status = "stable"

    print("Starting Economic Simulation...\n")

    # Consumer decision
    consumer_decision = consumer_agent(resources, prices)
    print(f"Consumer Decision:\n{consumer_decision}\n")

    # Producer decision
    producer_decision = producer_agent(demand, costs)
    print(f"Producer Decision:\n{producer_decision}\n")

    # Government decision
    government_decision = government_agent(economy_status)
    print(f"Government Decision:\n{government_decision}\n")

    # Simulate interactions and update conditions
    print("Simulating interactions and updating conditions...\n")
    # (In a real simulation, you would update resources, prices, demand, costs, and economy_status based on the decisions)

    print("Simulation complete.")

# Start the economic simulation
economic_simulation()