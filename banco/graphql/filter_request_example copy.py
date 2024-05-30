# client_gql.py
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def get_clients_named(name):
    transport = RequestsHTTPTransport(
        url='http://localhost:8000/graphql',
        use_json=True,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql("""
    query ($name: String) {
      allClientes(nombre: $name) {
        id
        cedula
        nombre
        apellido
      }
    }
    """)

    params = {"name": name}
    result = client.execute(query, variable_values=params)
    return result['allClientes']

if __name__ == "__main__":
    name_to_search = "Eduardo"
    clientes = get_clients_named(name_to_search)
    for cliente in clientes:
        print(f"ID: {cliente['id']}, Cedula: {cliente['cedula']}, Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}")
