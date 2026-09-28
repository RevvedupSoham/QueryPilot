# QueryPilot

**A basic natural-language SQL assistant built with LangChain and Groq for querying a MySQL database.**

QueryPilot is a small learning-focused project that demonstrates how an LLM application can translate natural-language questions into SQL, validate the generated query, execute approved read-only queries against MySQL, and return a readable result.

The project is intentionally kept small so that each component can be understood and explained end-to-end.

## Project Goals

- Understand the basic LangChain application workflow.
- Use Groq as the LLM inference provider.
- Convert natural-language questions into SQL.
- Add a basic SQL safety and validation layer before execution.
- Execute read-only queries against MySQL.
- Keep the implementation simple and defendable.

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
MySQL
      |
      v
Formatted Result
```

## Tech Stack

- **Language:** Python
- **LLM Framework:** LangChain
- **LLM Provider:** Groq
- **Database:** MySQL
- **Database Access:** SQLAlchemy + PyMySQL
- **Configuration:** Python environment variables / `.env`
- **Version Control:** Git / GitHub

## Core Features

- Natural-language questions over structured data
- LangChain prompt templates and model invocation
- Groq-powered SQL generation
- MySQL connectivity
- SQL validation before execution
- Read-only query policy
- Separation between LLM generation and database execution
- Environment-based configuration for database credentials and API keys

## Project Structure

```text
QueryPilot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── llm.py
│   ├── prompts.py
│   └── sql_validator.py
├── sql/
│   └── schema.sql
├── tests/
│   └── test_sql_validator.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/RevvedupSoham/QueryPilot.git
cd QueryPilot
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a MySQL database named `querypilot` and run the schema file from:

```text
sql/schema.sql
```

The application expects a MySQL server to be available on the configured host and port.

### 5. Configure environment variables

Copy `.env.example` to `.env` and provide your local values:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_groq_model

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=querypilot
```

**Never commit `.env` or API keys to GitHub.**

### 6. Run QueryPilot

```bash
python -m app.main
```

## Example Questions

After the sample database is configured, QueryPilot can handle questions such as:

```text
Show all employees in the Engineering department.

What is the average salary by department?

Show the five highest-paid employees.

How many employees joined after 2024?
```

The application generates SQL, validates it, executes approved read-only SQL against MySQL, and displays the result.

## Safety Approach

QueryPilot does not directly execute every SQL statement returned by the LLM.

Before execution, the generated SQL passes through a validation layer. The initial implementation is intended to allow read-only queries and reject statements that modify database state, such as INSERT, UPDATE, DELETE, DROP, ALTER, and other administrative operations.

This is a learning project. The validator is a basic safety layer and is not a replacement for production-grade database security.

## Why LangChain?

LangChain is used to structure the interaction between the application and the LLM. QueryPilot uses it for reusable prompt templates and model invocation instead of building an advanced agent framework.

The project deliberately avoids RAG, vector databases, autonomous agents, and LangGraph because those are outside the scope of this basic implementation.

## Why Groq?

Groq provides the LLM inference layer used to generate SQL from natural-language questions. LangChain handles the application-level interaction with the model.

## Limitations

- Generated SQL depends on the model and schema supplied in the prompt.
- The SQL validator is a basic safety layer, not a complete SQL security system.
- MySQL credentials must be configured locally.
- The application is designed for read-only querying rather than database administration.

## Learning Scope

QueryPilot is intended to demonstrate practical understanding of:

- LangChain prompt templates
- LLM model invocation
- Natural-language-to-SQL workflows
- MySQL connectivity
- SQL validation
- Separation of AI generation from database execution

## Status

**MySQL implementation added. End-to-end local testing requires a configured MySQL instance and Groq API key.**

## Author

**Soham Dutta**  
GitHub: https://github.com/RevvedupSoham/QueryPilot
