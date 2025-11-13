## 🤖📚 Kaggle 5-Day Agents Course Notebooks

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/SujitYalmar/AI-Agent-Development-ADK?style=social)](https://github.com/SujitYalmar/AI-Agent-Development-ADK/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/SujitYalmar/AI-Agent-Development-ADK)](https://github.com/SujitYalmar/AI-Agent-Development-ADK/commits/main)

> **Building Intelligent AI Agents using Google's Agent Development Kit (ADK)**
>
> A comprehensive implementation of AI agents powered by Google's Gemini models, featuring Google Search integration and multi-agent architectures.

## 📋 Table of Contents



This repository includes notebooks from the Google ADK "5 Days of Agents" course on Kaggle, demonstrating practical implementations of AI agents from basic to advanced architectures.

### Course Materials

#### Day 1a - From Prompt to Action
**Location:** `notebooks/day-1a-from-prompt-to-action.ipynb`

Your first step into agent development. Learn how to:
- Build a basic agent using the Google ADK
- Integrate with Gemini LLM models
- Use Google Search as a tool for information retrieval
- Understand the core agent workflow: Think → Act → Observe

**Key Concepts:**
- Single-agent systems
- Tool integration patterns
- Prompt engineering for agents
- API key management in Kaggle Notebooks

#### Day 1b - Agent Architectures  
**Location:** `notebooks/day-1b-agent-architectures.ipynb`

Scale your agent knowledge to multi-agent systems. Explore:
- Multi-agent team structures and specialization
- Sequential agent workflows (execute agents one after another)
- Parallel agent execution (run agents concurrently)
- Loop agents (iterative refinement and feedback cycles)
- Real-world applications: research, summarization, content generation

**Key Concepts:**
- Agent composition and orchestration
- Workflow patterns for complex tasks
- Agent communication and coordination
- Error handling in multi-agent systems
- Performance optimization

- #### Day 2a - Agent Tools: Custom Logic & Multi-Agent Systems

**Location:** `notebooks/day-2a-agent-tools.ipynb`

**Overview:**  
On Day 2a, you learn how to transform simple language agents into powerful problem-solvers by integrating custom tools. While built-in tools like Google Search are useful, every business has unique requirements. This module teaches how to create Python functions as agent tools, delegate tasks to specialist agents, and orchestrate multi-tool workflows using the Agent Development Kit (ADK).

**Key Highlights:**
- Understand the importance of tools in unlocking agent capabilities beyond static knowledge
- Learn to turn any Python function into a callable tool for agents (best practices: dictionary returns, docstrings, type hints, error handling)
- Build a working currency conversion agent using multiple custom tools
- Discover "agent tools" - leveraging agents as callable tools by other agents
- Compare agent tools vs sub-agents (delegation vs full control handoff)
- Explore ADK's ecosystem: function tools, agent tools, long-running tools, OpenAPI tools, MCP tools, and built-in Gemini tools
- Practice integrating custom business logic instead of relying only on generic capabilities

**Key Concepts:**
- Custom tool development patterns
- Agent-to-agent tool composition
- Business logic integration
- Tool orchestration and error handling
- Multi-agent collaboration strategies

#### Day 2b - Agent Tools: Reliable Code Execution & Advanced Tool Patterns

**Location:** `notebooks/day-2b-agent-tools-best-practices.ipynb`

**Overview:**  
Day 2b builds on custom tool skills by ensuring agents deliver reliable results—not just text-based answers. You implement code execution workflows where agents generate Python code and delegate calculations to a specialist calculation agent. This sandboxed execution guarantees mathematically correct results.

**Key Highlights:**
- Use Gemini's BuiltInCodeExecutor to run Python code blocks produced by agents
- Implement precise computation for complex tasks (financial calculations, data processing)
- Update agent instructions to strictly offload calculations to specialized agents
- Build robust multi-agent, multi-tool pipelines with error handling
- Explore tool types and orchestration patterns for real-world problems
- Understand best practices in agent communication, error management, and workflow design

**Key Concepts:**
- Sandboxed code execution
- Reliable computation patterns
- Multi-agent error handling
- Workflow orchestration at scale
- Production-ready agent architecture

### How to Access These Notebooks

1. **On GitHub:**
   - View the notebooks directly in this repository under the `notebooks/` folder
   - Download `.ipynb` files to run locally with Jupyter

2. **On Kaggle:**
   - Original notebooks: [Day 1a](https://www.kaggle.com/code/sujityalmar/day-1a-from-prompt-to-action) and [Day 1b](https://www.kaggle.com/code/sujityalmar/day-1b-agent-architectures), [Day 2a](https://www.kaggle.com/code/sujityalmar/day-2a-agent-tools), and [Day 2b](https://www.kaggle.com/code/sujityalmar/day-2b-agent-tools-best-practices)
   - Kaggle provides free compute and GPU access
   - All dependencies pre-installed

3. **Locally:**
   ```bash
   # Clone this repository
   git clone https://github.com/SujitYalmar/AI-Agent-Development-ADK.git
   cd AI-Agent-Development-ADK
   
   # Install dependencies
   pip install -r requirements.txt jupyter
   
   # Start Jupyter
   jupyter notebook notebooks/
   ```

### Running These Notebooks

**Prerequisites:**
- Python 3.11+
- Google API Key (get one at [Google AI Studio](https://aistudio.google.com/app/api-keys))
- Internet connection (for Google Search integration)

**Setup:**
1. Create a `.env` file with your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. For Kaggle Notebooks:
   - Go to Add-ons → Secrets
   - Add `GOOGLE_API_KEY` with your API key value

### Learning Progression

```
Day 1a: Foundations
├── Understanding agent basics
├── First agent with Google Search
└── Exploring Gemini models
        ↓
Day 1b: Advanced Architecture
├── Multi-agent orchestration
├── Workflow patterns
└── Real-world applications
```

### What You'll Build

- **Research Agents:** Automatically gather information from web sources
- **Summarization Agents:** Process and synthesize complex information  
- **Content Writers:** Generate structured articles and blog posts
- **Coordinators:** Manage workflows between multiple specialized agents
- **Iterative Refiners:** Improve outputs through feedback loops

### Next Steps

After completing these notebooks, you'll be ready to:
- Build production-grade agent systems
- Integrate agents into applications
- Deploy agents to cloud platforms
- Contribute to the AI agent ecosystem

### Resources

- [Google Agent Development Kit Docs](https://ai.google.dev/adk)
- [Kaggle Learn: Agents](https://www.kaggle.com/learn/agents)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Our Examples Folder](./examples)

## 📧 Contact

**Sujit Yalmar**
- GitHub: [@SujitYalmar](https://github.com/SujitYalmar)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

---

⭐ **If you find this project helpful, please consider giving it a star!** ⭐
