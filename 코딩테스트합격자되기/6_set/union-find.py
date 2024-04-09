# 유니온-파인드 알고리즘
# 배열 기반 트리로 집합을 구현한 상태에서
# 파인드 연산
	# 두 개 집합 간, 교집합이 있는지 루트 노드 탐색
	# 재귀를 통해 부모 노드를 타고 타고 올라가서 탐색하는 것은 최악의 경우 O(N)
	# 트리의 경로를 압축해서 찾으면, 더 빠르게 루트 노드 접근 가능
# 유니온 연산
	# 두 개 집합을 하나로 합침
	# 두 개 집합의 루트 노드를 파인드 연산으로 찾고
	# 두 집합의 루트 노드를 동일하게 해서 합침
    # 랭크 값이 더 작은 루트 노드의 부모 노드를 랭크가 큰 루트 노드로 바꿔 합침
    # 랭크 : 현재 노드를 기준으로 가장 깊은 노드까지의 경로 길이

class UnionFind:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

    def find(self, node):
        if self.parent[node] != node:
            # Path compression
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

if __name__ == "__main__":
    # Example usage:
    parent = [i for i in range(5)]
    rank = [0] * 5
    uf = UnionFind(parent, rank)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(0, 2)

    print(uf.find(0))  # Output: 2 (or 3, as path compression may vary)
    print(uf.find(3))  # Output: 2
