def build_order(projects, dependencies):
    build = []
    graph = create_dict(projects, dependencies)

    with_dependencies = project_dependencies(graph)
    no_dependencies = project_no_dependencies(graph, with_dependencies)

    if len(no_dependencies) == 0 and no_dependencies:
        return "Cycle found"

    for project in no_dependencies:
        build.append(project)

    for project in with_dependencies:
        build.append(project)

    return build


def project_dependencies(graph):
    with_dependencies = set()

    for project in graph:
        with_dependencies = with_dependencies.union(set(graph[project]))

    return with_dependencies


def project_no_dependencies(graph, projects_with):
    projects_without = set()

    for project in graph:
        if project not in projects_with:
            projects_without.add(project)

    return projects_without


def create_dict(projects, dependencies):
    graph = {}

    for project in projects:
        graph[project] = []

    for dependency in dependencies:
        graph[dependency[0]].extend(dependency[1])

    return graph


print(build_order(['A', 'B', 'C', 'D', 'E', 'F'],
                    [('A', 'D'), ('F', 'B'), ('B', 'D'), ('F', 'A'), ('D', 'C')]))