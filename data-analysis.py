import ollama
import pandas as pd
import matplotlib.pyplot as plt

# Define each agent as a separate function
def data_loading_agent(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    return data

def statistical_analysis_agent(data):
    prompt = f"Perform statistical analysis on the following dataset: {data.head().to_string()}"
    response = ollama.generate(model="codellama", prompt=prompt)
    return response["response"].strip()

def visualization_agent(data):
    # Create a simple visualization (e.g., histogram of a numeric column)
    numeric_columns = data.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 0:
        column = numeric_columns[0]
        plt.hist(data[column], bins=10)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.savefig("histogram.png")
        return f"Visualization saved as 'histogram.png'"
    else:
        return "No numeric columns found for visualization."

def report_generation_agent(analysis, visualization):
    prompt = f"Generate a report based on the following statistical analysis and visualization: {analysis}, {visualization}"
    response = ollama.generate(model="codellama", prompt=prompt)
    return response["response"].strip()



def data_analysis(file_path):
    print("Loading dataset...")
    data = data_loading_agent(file_path)
    print("Dataset loaded.\n")

    # Perform statistical analysis
    print("Performing statistical analysis...")
    analysis = statistical_analysis_agent(data)
    print(f"Statistical Analysis:\n{analysis}\n")

    # Create visualization
    print("Creating visualization...")
    visualization = visualization_agent(data)
    print(f"Visualization: {visualization}\n")

    # Generate report
    print("Generating report...")
    report = report_generation_agent(analysis, visualization)
    print(f"Report:\n{report}\n")

# Start the data analysis process
file_path = input("Enter the path to the dataset (CSV file): ")
data_analysis(file_path)