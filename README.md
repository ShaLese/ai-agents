# AI Agents Collection

This repository contains a collection of specialized AI agents built using the Ollama framework, each designed to handle specific tasks and scenarios. These agents demonstrate various applications of AI in different domains, from scientific problem-solving to legal simulations.

## Agents Overview

### 1. Business Meeting Simulator
**File:** `business-meeting.py`

A multi-agent system simulating a business meeting with different department representatives:
- Marketing Department Agent
- Finance Department Agent
- Operations Department Agent
- Client Representative Agent
- Facilitates structured discussions and decision-making processes

### 2. Code Development Assistant
**File:** `code-development.py`

A comprehensive code development pipeline with specialized agents:
- Code Writing Agent: Generates Python code based on requirements
- Code Review Agent: Reviews code for errors and improvements
- Code Testing Agent: Creates test cases for the code
- Documentation Agent: Writes code documentation
- Provides end-to-end development support

### 3. Content Creation System
**File:** `content-creation.py`

Marketing content creation system with specialized agents:
- Idea Generation Agent: Creates creative marketing concepts
- Content Writing Agent: Develops detailed content pieces
- SEO Optimization Agent: Optimizes content for search engines
- Streamlines the content creation workflow

### 4. Customer Support System
**File:** `customer-support.py`

Multi-agent customer support system featuring:
- FAQ Agent: Handles common customer questions
- Technical Support Agent: Troubleshoots technical issues
- Refund Agent: Processes refund requests
- Interactive menu-driven interface

### 5. Data Analysis System
**File:** `data-analysis.py`

A comprehensive data analysis pipeline with specialized agents:
- Data Loading Agent: Handles dataset import
- Statistical Analysis Agent: Performs statistical computations
- Visualization Agent: Creates data visualizations
- Report Generation Agent: Produces comprehensive analysis reports
- Supports CSV file analysis with automatic visualization generation

### 6. Debate System
**File:** `debate.py`

A multi-agent debate system featuring:
- 5 distinct agents participating in structured debates
- Sequential argument presentation
- Topic-based discussion flow
- Consensus building capabilities

### 7. Language Translation System
**File:** `language-translation.py`

Multi-lingual translation system with cultural adaptation:
- English to French translation
- English to Spanish translation
- English to German translation
- Cultural localization capabilities
- Supports multiple translation pairs

### 8. Posts Agents System
**File:** `postsAgents.py`

Collaborative blog post creation system with three specialized agents:
- Researcher Agent: Gathers and organizes topic information
- Writer Agent: Crafts blog posts from research
- Editor Agent: Reviews and refines content
- Supports customizable temperature settings for each agent

### 9. Problem-Solving System
**Files:** 
- `problem-solving-scie-eng.py` (Command-line version)
- `problem-solving-scie-eng-streamlit.py` (Web interface version)

An agent designed to tackle scientific and engineering problems through a structured approach:
- Generates hypotheses for given problems
- Analyzes data to support or refute hypotheses
- Validates solutions based on analysis
- Handles both online resources and local JSON data files
- Available in both command-line and Streamlit web interface versions

### 10. Simultaneous Agents
**Files:**
- `simulated-classroom.py`: Educational simulation with teacher, student, and tutor agents
- `simulated-economy.py`: Economic system simulation

The classroom simulation features:
- Teacher Agent: Provides topic explanations
- Student Agent: Asks relevant questions
- Tutor Agent: Offers additional clarification
- Interactive learning environment

The economy simulation features:
- Consumer Agent: Makes resource allocation decisions
- Producer Agent: Determines production levels
- Government Agent: Sets economic policies
- Simulates market interactions and economic decision-making

### 11. Social Networks Simulator
**File:** `social-networks.py`

Simulates social network interactions with multiple agents:
- Agent 1: Creates initial posts on given topics
- Agent 2: Generates responses to posts
- Agent 3: Provides replies to comments
- Demonstrates chain-of-thought interactions in social media contexts

### 12. Storytelling Agent
**File:** `storytelling-agent.py`

[Description pending - need to analyze file]

### 13. Kenyan Legal Team Simulator
**File:** `kenyan-legal-team.py`

A sophisticated legal simulation system featuring multiple legal roles:
- Judge Agent: Manages proceedings and makes rulings
- Lawyer Agent: Presents arguments and evidence
- Prosecutor Agent: Presents cases against the accused
- Accused Agent: Provides defense statements
- Witness Agent: Offers testimony
- Integrates with the Kenyan Constitution for reference

## Requirements

- Python 3.x
- Ollama framework
- Additional dependencies:
  - PyPDF2 (for legal team simulator)
  - pandas (for data analysis)
  - matplotlib (for visualizations)
  - requests (for problem solver)
  - streamlit (for web interface)

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
```

2. Install required dependencies:
```bash
pip install ollama pandas matplotlib PyPDF2 requests streamlit
```

## Usage

### Business Meeting Simulator
```bash
python business-meeting.py
```

### Code Development Assistant
```bash
python code-development.py
```

### Content Creation System
```bash
python content-creation.py
```

### Customer Support System
```bash
python customer-support.py
```

### Data Analysis System
```bash
python data-analysis.py
```

### Debate System
```bash
python debate.py
```

### Language Translation System
```bash
python language-translation.py
```

### Posts Agents System
```bash
python postsAgents.py
```

### Problem-Solving System
```bash
python problem-solving-scie-eng.py
```

### Problem-Solving System (Streamlit version)
```bash
streamlit run problem-solving-scie-eng-streamlit.py
```

### Simultaneous Agents
```bash
python simulated-classroom.py
```

### Social Networks Simulator
```bash
python social-networks.py
```

### Storytelling Agent
```bash
python storytelling-agent.py
```

### Kenyan Legal Team Simulator
```bash
python kenyan-legal-team.py
```

## File Structure
```
ai-agents0/
├── business-meeting.py
├── code-development.py
├── content-creation.py
├── customer-support.py
├── data-analysis.py
├── debate.py
├── dummy-data.csv (Sample dataset with age, income, and education data)
├── histogram.png (Generated visualization from data analysis)
├── kenyan-legal-team.py
├── language-translation.py
├── postsAgents.py
├── problem-solving-scie-eng.py
├── problem-solving-scie-eng-streamlit.py
├── simulated-classroom.py
├── simulated-economy.py
├── social-networks.py
├── TheConstitutionOfKenya.pdf (Reference document for legal team)
└── README.md
```

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch for your feature
3. Submitting a pull request

## License

This project is open-source and available under the MIT License.
