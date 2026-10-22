# Task graph contract

A task graph has a destination, nodes, dependency edges, ownership, checks, and a stop condition. A node is ready only when its inputs and contract are stable.

Parallelize only disjoint work. Integrate in small slices. When a worker discovers a missing dependency or wrong assumption, update the graph before continuing instead of silently changing the product.
