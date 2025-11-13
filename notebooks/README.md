# 📚 Kaggle 5-Day Agents Course Notebooks

## Overview

This folder contains references and guides for the Kaggle "5 Days of Agents" course notebooks using Google's Agent Development Kit (ADK).

## Available Notebooks

### Day 1a - From Prompt to Action  
**Kaggle Link:** [Day 1a - From Prompt to Action](https://www.kaggle.com/code/sujityalmar/day-1a-from-prompt-to-action)

Your introduction to AI agents. Learn:
- Building your first agent with Google ADK
- Integrating Gemini LLM for intelligent responses
- Using Google Search as an agent tool
- Understanding the Think → Act → Observe loop

**Topics Covered:**
- Single-agent architecture
- Tool integration (Google Search)
- Prompt engineering for agents
- API key management
- Running agents on Kaggle Notebooks

**Duration:** ~30 minutes

---

### Day 1b - Agent Architectures  
**Kaggle Link:** [Day 1b - Agent Architectures](https://www.kaggle.com/code/sujityalmar/day-1b-agent-architectures)

Advance to multi-agent systems. Explore:
- Building teams of specialized agents
- Sequential workflows (one agent after another)
- Parallel execution (concurrent agents)
- Loop agents (iterative refinement)
- Real-world applications

**Topics Covered:**
- Multi-agent orchestration
- Agent specialization and roles
- Workflow patterns (Sequential, Parallel, Loop)
- Agent communication
- Practical examples:
  - Research and content generation
  - Multi-domain executive briefings
  - Iterative story refinement
  - Blog writing pipelines

**Duration:** ~45 minutes

---

## How to Use These Resources

### Option 1: On Kaggle (Recommended)
1. Visit the Kaggle links above
2. Click "Copy & Edit" to create your own version
3. Enable internet access (if needed for tools)
4. Add your Google API key to Kaggle Secrets
5. Run the cells and follow along

### Option 2: Locally
1. Download the notebook files from Kaggle
2. Install Jupyter: `pip install jupyter`
3. Install dependencies: `pip install -r ../requirements.txt`
4. Create `.env` file with your API key
5. Run: `jupyter notebook`

### Option 3: Google Colab
1. Open the Kaggle notebooks
2. Look for "Open in Colab" button
3. Run in free cloud environment

## Prerequisites

- Python 3.11+ (for local setup)
- Google API Key (get free at [Google AI Studio](https://aistudio.google.com/app/api-keys))
- Internet connection (for Google Search integration)
- Basic Python knowledge

## Key Concepts to Learn

### From Day 1a:
```
Agent = Instruction + Tools + Memory + Reasoning
```

### From Day 1b:
```
Multi-Agent System = Orchestrated Agents + Workflow + Communication
```

## Project Structure

```
notebooks/
├── README.md (this file)
├── day-1a-from-prompt-to-action.ipynb (download from Kaggle)
└── day-1b-agent-architectures.ipynb (download from Kaggle)
```

## Next Steps After These Notebooks

1. **Experiment:** Modify agent prompts and tools
2. **Create:** Build your own agent applications
3. **Deploy:** Use these skills in real projects
4. **Contribute:** Share your agent implementations

## Useful Resources

- [Google ADK Documentation](https://ai.google.dev/adk)
- [Gemini API Reference](https://ai.google.dev/docs)
- [Kaggle Learn: Agents](https://www.kaggle.com/learn/agents)
- [Agent Examples in Examples Folder](../examples)

## Troubleshooting

### API Key Issues
- Verify key is set in `.env` or Kaggle Secrets
- Check key has proper permissions
- Try creating a new key from Google AI Studio

### Notebook Won't Run
- Ensure internet access is enabled
- Check all dependencies are installed
- Verify Python version (3.11+)

### Google Search Not Working
- Enable "Search the web" in tool settings
- Check internet connection
- Verify API key permissions

## Questions or Issues?

- Check [GitHub Issues](../../issues)
- Review the main [README](../) for more info
- Look at [Examples](../examples) for reference code

---

**Last Updated:** November 2025  
**Course:** Kaggle 5-Day Agents  
**Maintained by:** Sujit Yalmar
