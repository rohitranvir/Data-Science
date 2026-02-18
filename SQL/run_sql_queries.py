import sqlite3
import pandas as pd
import re
import os

# Define file paths
files = [
    r"d:\Data-Science\SQL\SQL-SUBQUERY.SQL",
    r"d:\Data-Science\SQL\office_DATA.sql",
    r"d:\Data-Science\SQL\rohit13.sql"
]

def setup_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # --- Standard Schema (EMP/DEPT) ---
    cursor.execute("CREATE TABLE DEPT (DEPTNO INTEGER, DNAME TEXT, LOCATION TEXT)")
    cursor.executemany("INSERT INTO DEPT VALUES (?, ?, ?)", [
        (10, 'ACCOUNTING', 'NEW YORK'),
        (20, 'RESEARCH', 'DALLAS'),
        (30, 'SALES', 'CHICAGO'),
        (40, 'OPERATIONS', 'BOSTON')
    ])
    
    cursor.execute('''CREATE TABLE EMP (
        EMPNO INTEGER, ENAME TEXT, JOB TEXT, MGR INTEGER, 
        HIREDATE TEXT, SAL REAL, COMM REAL, DEPTNO INTEGER
    )''')
    # Standard Scott/Tiger data
    employees = [
        (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, None, 20),
        (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 300, 30),
        (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 500, 30),
        (7566, 'JONES', 'MANAGER', 7839, '1981-04-02', 2975, None, 20),
        (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30),
        (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01', 2850, None, 30),
        (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09', 2450, None, 10),
        (7788, 'SCOTT', 'ANALYST', 7566, '1987-04-19', 3000, None, 20),
        (7839, 'KING', 'PRESIDENT', None, '1981-11-17', 5000, None, 10),
        (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08', 1500, 0, 30),
        (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23', 1100, None, 20),
        (7900, 'JAMES', 'CLERK', 7698, '1981-12-03', 950, None, 30),
        (7902, 'FORD', 'ANALYST', 7566, '1981-12-03', 3000, None, 20),
        (7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300, None, 10)
    ]
    cursor.executemany("INSERT INTO EMP VALUES (?,?,?,?,?,?,?,?)", employees)

    # --- ASHOKIT Schema ---
    cursor.execute("CREATE TABLE ASHOKIT_DEPT (dept_id INTEGER, dept_name TEXT)")
    cursor.executemany("INSERT INTO ASHOKIT_DEPT VALUES (?, ?)", [
        (101, 'Development'), (102, 'Testing'), (103, 'HR')
    ])
    
    cursor.execute("CREATE TABLE ASHOKIT_MANAGERS (manager_id INTEGER, manager_name TEXT)")
    cursor.executemany("INSERT INTO ASHOKIT_MANAGERS VALUES (?, ?)", [
        (1, 'Ashok'), (2, 'Suresh')
    ])
    
    cursor.execute("CREATE TABLE ASHOKIT_EMP (emp_id INTEGER, emp_name TEXT, dept_id INTEGER, manager_id INTEGER)")
    cursor.executemany("INSERT INTO ASHOKIT_EMP VALUES (?, ?, ?, ?)", [
        (1001, 'Raju', 101, 1),
        (1002, 'Rani', 102, 2),
        (1003, 'Ganesh', 101, 1)
    ])

    cursor.execute("CREATE TABLE ASHOKIT_PROJECTS (project_id INTEGER, project_name TEXT)")
    cursor.executemany("INSERT INTO ASHOKIT_PROJECTS VALUES (?, ?)", [
        (1, 'E-Commerce'), (2, 'Banking App')
    ])

    conn.commit()
    return conn

def clean_and_execute(conn, file_path):
    print(f"\n{'='*50}\nExecuting: {os.path.basename(file_path)}\n{'='*50}")
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # improved parsing
    current_query = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Handle comments
        if stripped.startswith('--') or stripped.startswith('//'):
            continue
            
        # Specific handling for SQL-SUBQUERY.SQL which uses "SQL >>"
        is_explicit_sql = False
        if 'SQL >>' in line:
            line = re.sub(r'SQL\s*>>', '', line, flags=re.IGNORECASE)
            is_explicit_sql = True
            
        # Clean // comments at end of line
        line = re.sub(r'//.*', '', line)
        
        # Check if it looks like a SQL start if not explicit (simplified check)
        # We accumulate lines until a semicolon
        
        # If it's just text like "Query-1...", skip it unless it's part of a query?
        # A simple heuristic: if it doesn't start with a keyword and wasn't explicit SQL >>
        # and we aren't in the middle of a query (this is hard to know perfectly without a parser)
        # But here, most queries are one-liners or split by ;
        
        # simpler approach: collect everything, split by ;, then check keywords
        pass

    # Re-read and split by ; to keep it simple, but we need to filter out the "garbage" chunks
    with open(file_path, 'r') as f:
        content = f.read()

    # Pre-clean
    content = re.sub(r'//', '--', content)
    
    # Split by ;
    raw_statements = content.split(';')
    
    for raw in raw_statements:
        # cleanup each statement
        stmt = raw.strip()
        
        # remove "SQL >>"
        stmt = re.sub(r'SQL\s*>>', '', stmt, flags=re.IGNORECASE)
        
        # remove lines that don't look like code
        lines = stmt.split('\n')
        clean_lines = []
        for l in lines:
            l = l.strip()
            if not l: continue
            if l.startswith('--'): continue
            
            # If line is just text like "Working With Sub Queries", skip it
            # Valid SQL usually starts with SELECT, INSERT, CREATE, WITH, UPDATE, DELTE, DROP
            # or is a continuation. 
            # If the *first* word of the statement isn't a keyword, it's likely text.
            clean_lines.append(l)
            
        if not clean_lines:
            continue
            
        final_sql = ' '.join(clean_lines)
        
        # Check first word
        first_word = final_sql.split()[0].upper()
        if first_word not in ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'DROP', 'WITH', 'PRAGMA']:
            # This is likely a text description chunk that was between semicolons (or start of file)
            continue
            
        print(f"\nQuery: {final_sql}")
        try:
            df = pd.read_sql_query(final_sql, conn)
            if df.empty:
                print("Result: [Empty DataFrame]")
            else:
                print(df.to_string(index=False))
        except Exception as e:
            print(f"Error: {e}")


def main():
    conn = setup_db()
    for file_path in files:
        if os.path.exists(file_path):
            clean_and_execute(conn, file_path)
        else:
            print(f"File not found: {file_path}")
    conn.close()

if __name__ == "__main__":
    main()
