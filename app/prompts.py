from langchain_core.prompts import ChatPromptTemplate

SQL_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You convert natural-language questions into MySQL SQL.\n\nUse only the tables and columns provided in the schema.\nReturn only one read-only SQL statement.\nDo not use INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, TRUNCATE, GRANT, REVOKE, or other database-changing/admin operations.\nDo not wrap the SQL in markdown code fences.\n\nDatabase schema:\n{schema}"),
    ("human", "Question: {question}"),
])
