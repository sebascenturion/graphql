# client_requests.py
import requests

def get_clients_named(name):
    url = "http://localhost:8000/graphql"
    query = """
    query ($name: String) {
      allClientes(nombre: $name) {
        id
        cedula
        nombre
        apellido
      }
    }
    """
    
    variables = {"name": name}
    response = requests.post(url, json={'query': query, 'variables': variables})
    if response.status_code == 200:
        result = response.json()
        return result['data']['allClientes']
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {response.text}")

if __name__ == "__main__":
    nombre = "Luis"
    clientes = get_clients_named(nombre)
    for cliente in clientes:
        print(f"ID: {cliente['id']}, Cedula: {cliente['cedula']}, Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}")
