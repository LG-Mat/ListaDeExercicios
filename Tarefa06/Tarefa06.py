import sqlite3
import requests
import random
from typing import List, Tuple, Any

DATABASE_NAME = 'northwind_aula.db'
CHICAGO_TERRITORY_CODE = '60601'

def create_connection(db_file: str) -> sqlite3.Connection:
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao SQLite: {e}")
        if conn:
            conn.close()
        raise e


def execute_query(conn: sqlite3.Connection, query: str, params: tuple = ()) -> None:
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao executar a query: {e}\nQuery: {query}")


def fetch_query(conn: sqlite3.Connection, query: str, params: tuple = ()) -> List[Tuple[Any, ...]]:
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao buscar resultados: {e}\nQuery: {query}")
        return []


def setup_northwind_tables(conn: sqlite3.Connection):
    # Tabela 1: Territories (Territórios)
    create_territories_table = """
    CREATE TABLE IF NOT EXISTS Territories (
        TerritoryID TEXT PRIMARY KEY,
        TerritoryDescription TEXT NOT NULL,
        RegionID INTEGER
    );
    """

    # Tabela 2: Employees (Funcionários)
    create_employees_table = """
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY,
        LastName TEXT NOT NULL,
        FirstName TEXT NOT NULL
    );
    """

    # Tabela 3: EmployeeTerritories (Funcionários-Territórios - Relacionamento N:M)
    create_employee_territories_table = """
    CREATE TABLE IF NOT EXISTS EmployeeTerritories (
        EmployeeID INTEGER,
        TerritoryID TEXT,
        PRIMARY KEY (EmployeeID, TerritoryID),
        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
        FOREIGN KEY (TerritoryID) REFERENCES Territories(TerritoryID)
    );
    """

    # Tabela 4: Orders (Pedidos)
    create_orders_table = """
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY,
        EmployeeID INTEGER,
        OrderDate TEXT,
        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
    );
    """

    execute_query(conn, create_territories_table)
    execute_query(conn, create_employees_table)
    execute_query(conn, create_employee_territories_table)
    execute_query(conn, create_orders_table)
    print("Tabelas Northwind simplificadas criadas.")

def populate_northwind_data(conn: sqlite3.Connection):
    # Territórios
    territories = [
        ('12345', 'Boston'),
        (CHICAGO_TERRITORY_CODE, 'Chicago'),
        ('78787', 'New York')
    ]
    for id, desc in territories:
        execute_query(conn, "INSERT OR IGNORE INTO Territories (TerritoryID, TerritoryDescription) VALUES (?, ?)",
                      (id, desc))

    # Funcionários
    employees = [
        (1, 'Davolio', 'Nancy'),
        (2, 'Fuller', 'Andrew'),
        (3, 'Leverling', 'Janet')
    ]
    for id, last, first in employees:
        execute_query(conn, "INSERT OR IGNORE INTO Employees (EmployeeID, LastName, FirstName) VALUES (?, ?, ?)",
                      (id, last, first))

    # Funcionários e Territórios
    employee_territories = [
        (1, '12345'),
        (1, CHICAGO_TERRITORY_CODE),  # Nancy atende Chicago
        (2, CHICAGO_TERRITORY_CODE),  # Andrew atende Chicago
        (3, '78787')
    ]
    for emp_id, terr_id in employee_territories:
        execute_query(conn, "INSERT OR IGNORE INTO EmployeeTerritories (EmployeeID, TerritoryID) VALUES (?, ?)",
                      (emp_id, terr_id))

    # Pedidos (Orders)
    orders = [
        (101, 1, '2025-10-29'),
        (102, 2, '2025-10-30'),
        (103, 3, '2025-10-30'),
    ]
    for order_id, emp_id, date in orders:
        execute_query(conn, "INSERT OR IGNORE INTO Orders (OrderID, EmployeeID, OrderDate) VALUES (?, ?, ?)",
                      (order_id, emp_id, date))

    print("Dados de exemplo inseridos.")

def run_task_1(conn: sqlite3.Connection):
    print("\n--- 1) Territórios e Códigos ---")
    query = "SELECT TerritoryID, TerritoryDescription FROM Territories"
    results = fetch_query(conn, query)
    print(f"| {'Território':<20} | {'Código':<8} |")
    print("|" + "-" * 22 + "|" + "-" * 10 + "|")
    for id, desc in results:
        print(f"| {desc:<20} | {id:<8} |")


def run_task_2(conn: sqlite3.Connection):
    print("\n--- 2) Funcionários que atendem Chicago ---")

    query = """
    SELECT 
        E.FirstName, E.LastName
    FROM 
        Employees E
    JOIN 
        EmployeeTerritories ET ON E.EmployeeID = ET.EmployeeID
    WHERE 
        ET.TerritoryID = ?
    """

    results = fetch_query(conn, query, (CHICAGO_TERRITORY_CODE,))
    print(f"| {'Nome':<10} | {'Sobrenome':<10} |")
    print("|" + "-" * 12 + "|" + "-" * 12 + "|")
    for first, last in results:
        print(f"| {first:<10} | {last:<10} |")


def run_task_3(conn: sqlite3.Connection):
    print("\n--- 3) Pedidos de Funcionários de Chicago ---")
    query = """
    SELECT 
        O.OrderID, O.OrderDate, E.FirstName, E.LastName
    FROM 
        Orders O
    JOIN 
        Employees E ON O.EmployeeID = E.EmployeeID
    JOIN 
        EmployeeTerritories ET ON E.EmployeeID = ET.EmployeeID
    WHERE 
        ET.TerritoryID = ?
    """

    results = fetch_query(conn, query, (CHICAGO_TERRITORY_CODE,))
    print(f"| {'Pedido ID':<10} | {'Data':<10} | {'Funcionário':<20} |")
    print("|" + "-" * 12 + "|" + "-" * 12 + "|" + "-" * 22 + "|")
    for order_id, date, first, last in results:
        print(f"| {order_id:<10} | {date:<10} | {first} {last:<18} |")

# --- Tarefa 4

def run_task_4(conn: sqlite3.Connection):

    print("\n--- 4) Criação e População de Novas Tabelas ---")

    # A) Criação das Tabelas
    create_customers_table = """
    CREATE TABLE IF NOT EXISTS Clientes (
        ClienteID INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Email TEXT,
        Pais TEXT
    );
    """
    create_suppliers_table = """
    CREATE TABLE IF NOT EXISTS Fornecedores (
        FornecedorID INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Empresa TEXT,
        Pais TEXT
    );
    """
    create_products_table = """
    CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY,
        NomeProduto TEXT NOT NULL,
        CodigoProduto TEXT UNIQUE NOT NULL
    );
    """
    create_new_orders_table = """
    CREATE TABLE IF NOT EXISTS Pedidos_V2 (
        PedidoID INTEGER PRIMARY KEY,
        ClienteID INTEGER,
        FornecedorID INTEGER,
        ProdutoID INTEGER,
        Quantidade INTEGER NOT NULL,
        FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
        FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID),
        FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
    );
    """
    execute_query(conn, create_customers_table)
    execute_query(conn, create_suppliers_table)
    execute_query(conn, create_products_table)
    execute_query(conn, create_new_orders_table)
    print("Tabelas 'Clientes', 'Fornecedores', 'Produtos' e 'Pedidos_V2' criadas.")

    # B) População de Clientes e Fornecedores com dados da API RandomUser
    print("Buscando dados aleatórios...")
    try:
        # Pega 10 usuários aleatórios
        response = requests.get('https://randomuser.me/api/?results=10&nat=us,gb')
        response.raise_for_status()  # Lança exceção para status ruins
        data = response.json()

        customers_to_insert = []
        suppliers_to_insert = []

        # Popula Clientes e Fornecedores
        for i, user in enumerate(data['results']):
            # Cliente
            full_name = f"{user['name']['first']} {user['name']['last']}"
            email = user['email']
            country = user['location']['country']
            customers_to_insert.append((i + 1, full_name, email, country))

            # Fornecedor (usa o mesmo nome, mas simula uma empresa)
            company_name = f"Supra {user['name']['last']} Ltda."
            suppliers_to_insert.append((i + 1, full_name, company_name, country))

        # Insere Clientes
        for id, name, email, country in customers_to_insert:
            execute_query(conn, "INSERT INTO Clientes (ClienteID, Nome, Email, Pais) VALUES (?, ?, ?, ?)",
                          (id, name, email, country))
        print(f"{len(customers_to_insert)} Clientes inseridos.")

        # Insere Fornecedores
        for id, name, company, country in suppliers_to_insert:
            execute_query(conn, "INSERT INTO Fornecedores (FornecedorID, Nome, Empresa, Pais) VALUES (?, ?, ?, ?)",
                          (id, name, company, country))
        print(f"{len(suppliers_to_insert)} Fornecedores inseridos.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}. População de clientes/fornecedores ignorada.")

    products = [
        (1, 'Notebook Pro X1', 'NBX1'),
        (2, 'Mouse Gamer RGB', 'MGRB'),
        (3, 'Monitor Ultra HD', 'MUHD')
    ]
    for id, name, code in products:
        execute_query(conn, "INSERT INTO Produtos (ProdutoID, NomeProduto, CodigoProduto) VALUES (?, ?, ?)",
                      (id, name, code))
    print(f"{len(products)} Produtos inseridos.")

    customer_ids = list(range(1, 11))
    supplier_ids = list(range(1, 11))
    product_ids = [p[0] for p in products]

    orders_v2_to_insert = []
    for i in range(1, 16):  # 15 pedidos de exemplo
        c_id = random.choice(customer_ids)
        s_id = random.choice(supplier_ids)
        p_id = random.choice(product_ids)
        qty = random.randint(1, 10)
        orders_v2_to_insert.append((i, c_id, s_id, p_id, qty))

    for order_id, c_id, s_id, p_id, qty in orders_v2_to_insert:
        execute_query(conn,
                      "INSERT INTO Pedidos_V2 (PedidoID, ClienteID, FornecedorID, ProdutoID, Quantidade) VALUES (?, ?, ?, ?, ?)",
                      (order_id, c_id, s_id, p_id, qty))
    print(f"{len(orders_v2_to_insert)} Pedidos_V2 inseridos (com IDs de 1 a 15).")


# --- Função Principal ---

def main():
    try:
        # Conecta-se ao banco de dados (e cria o arquivo se não existir)
        conn = create_connection(DATABASE_NAME)

        # ⚠️ Assegura que o script começa com um estado limpo para as tarefas 1-3
        # Exclui as tabelas antigas antes de configurar as novas (opcional, para testes)
        execute_query(conn, "DROP TABLE IF EXISTS Territories")
        execute_query(conn, "DROP TABLE IF EXISTS Employees")
        execute_query(conn, "DROP TABLE IF EXISTS EmployeeTerritories")
        execute_query(conn, "DROP TABLE IF EXISTS Orders")

        # 1. Configura as tabelas Northwind e insere dados de exemplo
        setup_northwind_tables(conn)
        populate_northwind_data(conn)

        # 2. Executa as tarefas de consulta
        run_task_1(conn)
        run_task_2(conn)
        run_task_3(conn)

        # 3. Executa a tarefa de criação e população de novas tabelas
        run_task_4(conn)

    except Exception as e:
        print(f"\nOcorreu um erro no programa principal: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("\nConexão com o banco de dados fechada.")


if __name__ == '__main__':
    main()