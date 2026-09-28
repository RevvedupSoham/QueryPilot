from app.database import execute_query, get_engine, get_schema
from app.llm import get_llm
from app.prompts import SQL_PROMPT
from app.sql_validator import validate_sql


def main():
    print("\nQueryPilot")
    print("Natural-language SQL assistant powered by LangChain + Groq + MySQL")
    print("Type 'exit' to quit.\n")

    engine = get_engine()
    schema = get_schema(engine)
    llm = get_llm()
    chain = SQL_PROMPT | llm

    while True:
        question = input("QueryPilot> ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        if not question:
            continue
        try:
            response = chain.invoke({"schema": schema, "question": question})
            valid, result = validate_sql(response.content)
            if not valid:
                print("\nBlocked: " + result + "\n")
                continue
            print("\nGenerated SQL:\n" + result + "\n")
            rows = execute_query(engine, result)
            if not rows:
                print("No rows returned.\n")
                continue
            for row in rows:
                print(row)
            print()
        except Exception as exc:
            print("Error: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
