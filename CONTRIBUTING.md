# Contributing to AI Agent Development ADK

🎉 Thank you for your interest in contributing to our AI Agent Development project! We welcome contributions from the community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow. Please be respectful and constructive in all interactions.

### Our Standards

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the problem
- **Expected behavior** vs. actual behavior
- **Environment details** (OS, Python version, ADK version)
- **Code samples** or error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Clear use case** for the enhancement
- **Expected benefits** to users
- **Possible implementation** approach
- **Alternative solutions** you've considered

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

### Prerequisites

- Python 3.11 or higher
- Git
- Google API Key (for Gemini models)

### Local Setup

1. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Agent-Development-ADK.git
   cd AI-Agent-Development-ADK
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run examples:**
   ```bash
   python examples/simple_agent_example.py
   ```

## Pull Request Process

1. **Update documentation** for any new features
2. **Add tests** to maintain code coverage
3. **Follow coding standards** outlined below
4. **Update README.md** if needed
5. **One feature per PR** - keep changes focused
6. **Link related issues** in your PR description

### PR Title Format

Use conventional commits format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Maximum line length: 100 characters

### Code Formatting

```bash
# Format code with black
black .

# Check with flake8
flake8 .
```

### Documentation

- Add docstrings to all public functions
- Use type hints where appropriate
- Update README.md for user-facing changes
- Comment complex logic

### Testing

- Write unit tests for new features
- Ensure existing tests pass
- Aim for high code coverage
- Test edge cases

## Reporting Bugs

### Before Submitting

- Check [existing issues](https://github.com/SujitYalmar/AI-Agent-Development-ADK/issues)
- Try the latest version
- Collect relevant information

### Bug Report Template

```markdown
**Description**
A clear description of the bug.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Run '...'
3. See error

**Expected Behavior**
What should happen.

**Actual Behavior**
What actually happens.

**Environment**
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Python Version: [e.g., 3.11.5]
- ADK Version: [e.g., 0.1.0]

**Additional Context**
Add any other context, screenshots, or error logs.
```

## Suggesting Enhancements

### Enhancement Template

```markdown
**Feature Description**
Clear description of the proposed feature.

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should this work?

**Alternatives Considered**
Other approaches you've thought about.

**Additional Context**
Mockups, examples, or references.
```

## Questions?

If you have questions about contributing:

- Open a [Discussion](https://github.com/SujitYalmar/AI-Agent-Development-ADK/discussions)
- Check existing documentation
- Ask in issues

---

**Thank you for contributing! Your efforts help make this project better for everyone.** 🚀
