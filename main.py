from copy import copy

graph = {
    "Seattle": {"San Francisco": 1306, "Denver": 2161, "Minneapolis": 2661},
    "San Francisco": {"Los Angeles": 629, "Las Vegas": 919},
    "Los Angeles": {"Las Vegas": 435},
    "Las Vegas": {"Denver": 1225, "Dallas": 1983},
    "Denver": {"Dallas": 1258, "Minneapolis": 1483},
    "Minneapolis": {"Dallas": 1532, "Chicago": 661},
    "Dallas": {"Wash DC": 2113, "Miami": 2161},
    "Chicago": {"Wash DC": 1709, "Boston": 1613},
    "Wash DC": {"Boston": 725, "New york": 383, "Miami": 1709},
    "Boston": {"Wash DC": 725, "New york": 338},
    "New york": {"Boston": 338, "Wash DC": 383, "Miami": 2145},
    "Miami": {"Wash DC": 1709, "New york": 2145, "Dallas": 2161}
}


def get_min_distance(vertices, distancia, key, previous):
    new_val = {"min_distance": distancia, "previous": previous}
    if vertices.get(key) is None:
        return new_val

    min_distance = vertices.get(key).get("min_distance")

    return vertices.get(key) if min_distance is not None and min_distance < distancia else new_val


def dijkistra_graph(graph, source="Seattle", destiny="Miami"):
    vertices = [{source: graph.remove(source)}]
    visitados = {source: {"min_distance": 0.}}


def dijkistra(cities, source, destination):
    vertices = [{source: cities.pop(source)}]
    visitados = {source: {"min_distance": 0.}}

    for name, edge in cities.items():
        vertices.append({name: edge})

    while vertices:
        for city in vertices:
            for name, edges in city.items():
                if visitados.get(name) is None:
                    continue
                for edge, weight in edges.items():
                    if visitados.get(edge) is None:
                        visitados.update({edge: {"min_distance": float("inf")}})
                    total_wight = visitados.get(name).get("min_distance") + weight
                    if total_wight < visitados.get(edge).get("min_distance"):
                        min_distancia = get_min_distance(visitados, total_wight, edge, name)
                        visitados.update({edge: min_distancia})
                vertices.remove(city)

    # for v in visitados.items():

    peso_total = visitados.get(destination).get("min_distance")
    caminho = ["total: " + str(peso_total), destination]
    key = destination
    while visitados:
        previous = visitados.pop(key).get("previous")
        if previous:
            key = previous
            caminho.append(key)
        else:
            break


    caminho.reverse()

    return caminho


if __name__ == '__main__':
    print " --> ".join(dijkistra(graph, "Seattle", "Wash DC"))

