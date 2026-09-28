import re

BLOCKED_KEYWORDS = {"INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "CREATE", "TRUNCATE", "REPLACE", "GRANT", "REVOKE", "EXEC", "EXECUTE", "CALL", "SET", "USE", "SHOW", "DESCRIBE", "DESC", "LOAD", "OUTFILE", "DUMPFILE"}

def validate_sql(sql):
    cleaned = sql.strip()
    if cleaned.startswith("```") and cleaned.endswith("```"):
        cleaned = re.sub(r"^```(?:sql)?\s*", "", cleaned, flags=re.I)
        cleaned = re.sub(r"\s*```$", "", cleaned).strip()
    if not cleaned:
        return False, "The generated SQL is empty."
    statements = [part.strip() for part in cleaned.split(";") if part.strip()]
    if len(statements) > 1:
        return False, "Multiple SQL statements are not allowed."
    query = statements[0]
    if not re.match(r"^(SELECT|WITH)\b", query, flags=re.I):
        return False, "Only SELECT or WITH queries are allowed."
    tokens = set(re.findall(r"\b[A-Z_]+\b", query.upper()))
    blocked = tokens.intersection(BLOCKED_KEYWORDS)
    if blocked:
        return False, "Blocked SQL operation: " + ", ".join(sorted(blocked)) + "."
    return True, query
