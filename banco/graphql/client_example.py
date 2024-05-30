import requests

def get_clients():
    url = "http://localhost:8000/graphql"
    query = """
    query {
      allClientes {
        id
        cedula
        nombre
        apellido
      }
    }
    """
    
    response = requests.post(url, json={'query': query})
    if response.status_code == 200:
        result = response.json()
        clientes = result['data']['allClientes']
        return clientes
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {response.text}")

if __name__ == "__main__":
    clients = get_clients()
    for cliente in clients:
        print(f"ID: {cliente['id']}, Cedula: {cliente['cedula']}, Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}")
