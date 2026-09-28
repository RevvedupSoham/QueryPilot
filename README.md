# QueryPilot

**A basic natural-language SQL assistant built with LangChain and Groq.**

QueryPilot is a small learning-focused project that demonstrates how an LLM application can translate natural-language questions into SQL, validate the generated query, execute safe read-only queries against a relational database, and return a readable result.

The project is intentionally kept small so that each component can be understood and defended clearly.

## Project Goals

- Understand the basic LangChain application workflow.
- Use Groq as the LLM inference provider.
- Convert natural-language questions into SQL.
- Add a basic SQL safety/validation layer before execution.
- Execute read-only queries against a sample relational database.
- Keep the implementation simple enough to explain end-to-end.

## Architecture

```text
User Question
      |
      v
LangChain Prompt Template
      |
      v
Groq LLM
      |
      v
Generated SQL
      |
      v
SQL Validation / Safety Check
      |
      v
Read-only Database Execution
      |
      v
Formatted Result
```

## Tech Stack

- **Language:** Python
- **LLM Framework:** LangChain
- **LLM Provider:** Groq
- **Database:** SQLite for the initial implementation
- **Database Access:** SQLAlchemy
- **Configuration:** Python environment variables / `.env`
- **Version Control:** Git / GitHub

## Status

**Initial setup / development in progress.**

## Author

**Soham Dutta**  
GitHub: [RevvedupSoham](https://github.com/RevvedupSoham)
