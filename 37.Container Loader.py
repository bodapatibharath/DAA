def container_loader(capacity, items):
    items.sort(reverse=True)
    containers = [[]]
    remaining_capacity = [capacity]

    for item in items:
        for i, remaining in enumerate(remaining_capacity):
            if remaining >= item:
                containers[i].append(item)
                remaining_capacity[i] -= item
                break
        else:
            containers.append([item])
            remaining_capacity.append(capacity - item)

    return containers

# Example usage:
if __name__ == "__main__":
    capacity = 10
    items = [8, 5, 3, 2, 2, 1, 1]
    containers = container_loader(capacity, items)
    for i, container in enumerate(containers, 1):
        print(f"Container {i}: {container}")
