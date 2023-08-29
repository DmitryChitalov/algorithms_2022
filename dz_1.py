
# class Solution:
#     """
#     Попытка опереться на непересекающиеся множества к успеху не привела, один из тест-кейсов проваливается:
#     n = 100
#     l = [[17, 51], [33, 83], [53, 62], [25, 34], [35, 90], [29, 41], [14, 53], [40, 84], [41, 64], [13, 68],
#         [44, 85], [57, 58], [50, 74], [20, 69], [15, 62], [25, 88], [4, 56], [37, 39], [30, 62], [69, 79], [33, 85],
#         [24, 83], [35, 77], [2, 73], [6, 28], [46, 98], [11, 82], [29, 72], [67, 71], [12, 49], [42, 56], [56, 65],
#         [40, 70], [24, 64], [29, 51], [20, 27], [45, 88], [58, 92], [60, 99], [33, 46], [19, 69], [33, 89], [54, 82],
#         [16, 50], [35, 73], [19, 45], [19, 72], [1, 79], [27, 80], [22, 41], [52, 61], [50, 85], [27, 45], [4, 84],
#         [11, 96], [0, 99], [29, 94], [9, 19], [66, 99], [20, 39], [16, 85], [12, 27], [16, 67], [61, 80], [67, 83],
#         [16, 17], [24, 27], [16, 25], [41, 79], [51, 95], [46, 47], [27, 51], [31, 44], [0, 69], [61, 63], [33, 95],
#         [17, 88], [70, 87], [40, 42], [21, 42], [67, 77], [33, 65], [3, 25], [39, 83], [34, 40], [15, 79], [30, 90],
#         [58, 95], [45, 56], [37, 48], [24, 91], [31, 93], [83, 90], [17, 86], [61, 65], [15, 48], [34, 56], [12, 26],
#         [39, 98], [1, 48], [21, 76], [72, 96], [30, 69], [46, 80], [6, 29], [29, 81], [22, 77], [85, 90], [79, 83],
#         [6, 26], [33, 57], [3, 65], [63, 84], [77, 94], [26, 90], [64, 77], [0, 3], [27, 97], [66, 89], [18, 77],
#         [27, 43]]
#     Output: 12
#     Expected: 13
#     """
#
#     def makeConnected(self, n: int, connections: List[List[int]]) -> int:
#         if len(connections) < n - 1:
#             return -1
#         net = set()
#         extra_conns = 0
#         for conn_1, conn_2 in sorted(connections, key=lambda x: (x[0], x[1])):
#             if conn_1 in net and conn_2 in net:
#                 extra_conns += 1
#             else:
#                 if conn_1 not in net:
#                     net.add(conn_1)
#                 if conn_2 not in net:
#                     net.add(conn_2)
#         not_connected = len(set(range(n)) - net)
#         if not_connected <= extra_conns:
#             return not_connected
#         return -1

class Solution:
    """
    В обсуждении задачи нашла рабочее решение на графах
    """

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def depth_first_search(current_node, adj_list, visited):
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in adj_list[current_node]:
                    depth_first_search(neighbor, adj_list, visited)

        if len(connections) < n - 1:
            return -1

        visited = set()
        counter = 0
        adjacency_list = {i: set() for i in range(n)}
        for conn_1, conn_2 in connections:
            adjacency_list[conn_1].add(conn_2)
            adjacency_list[conn_2].add(conn_1)
        while len(visited) < n:
            for node in range(n):
                if node not in visited:
                    depth_first_search(node, adjacency_list, visited)
                    counter += 1
        return counter - 1
