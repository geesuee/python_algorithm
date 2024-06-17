class SegmentTree:
    def __init__(self, arr):
        # 주어진 배열의 길이
        self.n = len(arr)
        # 주어진 배열의 길이에 따라 정해지는 세그먼트 트리의 크기
        size = 2 * (2 ** (self.n - 1).bit_length())
        self.tree = [0] * size
        # 배열을 사용하여 세그먼트 트리(=구간 합 트리) 생성
        self.build(arr=arr, node=1, start=0, end=self.n - 1)

    # 재귀 방식으로 구간 합 구하는 함수
    def build(self, arr, node, start, end):
        if start == end:
            # 구간 시작 값과 마지막 값이 같은 경우 = 구간 합 트리의 리프 노드
            # 해당 구간인 배열 값을 그대로 넣어줌
            self.tree[node] = arr[start]
        else:
            # 구간을 반으로 쪼개어 합을 구하고 자식 노드에 저장
            mid = (start + end) // 2
            # 재귀로 끝까지 내려가서 리프 노드들을 구하고 올라오는 구조
            self.build(arr, 2 * node, start, mid)
            self.build(arr, 2 * node + 1, mid + 1, end)
            # 올라오는 과정에서 왼쪽 자식 노드와 오른쪽 자식 노드를 더해서 부모 노드 값 저장
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    # 재귀 방식으로 구간 합 수정하는 함수
    def update(self, idx, val, node, start, end):
        if start == end:
            # 구간 시작 값과 마지막 값이 같은 경우 = 구간 합 트리의 리프 노드
            # 리프 노드에 있는 배열 값을 변경
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                # 변경 대상인 노드가 중간 값보다 적으면 -> 왼쪽 자식 노드 수정
                self.update(idx, val, 2 * node, start, mid)
            else:
                # 변경 대상인 노드가 중간 값보다 크면 -> 오른쪽 자식 노드 수정
                self.update(idx, val, 2 * node + 1, mid + 1, end)
            # 아래 자식 노드 값이 변경됨에 따라 그것의 합산인 부모 노드 값도 수정
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    # 재귀 방식으로 구간 합 트리를 탐색하여, 지정된 범위 내 구간 합을 찾아 합산하는 함수
    def query(self, L, R, node, start, end):
        # Case 1 : 현재 구간이 쿼리로 탐색 중인 구간에 없음
        if R < start or L > end:
            return 0
        
        # Case 2 : 현재 구간이 쿼리로 탐색 중인 구간에 완전히 겹침(=포함 상태)
        if L <= start and end <= R:
            return self.tree[node]
        
        # Case 3 : 현재 구간이 쿼리로 탐색 중인 구간에 부분적으로 겹침
        # 현재 구간을 반으로 쪼개어 탐색
        mid = (start + end) // 2
        # 재귀로 끝까지 내려가서 왼쪽, 오른쪽 노드 내 주어진 구간을 포함하는 부분의 합을 합산하여 올라옴
            # 왼쪽 자식 노드 인덱스 = 인덱스 * 2
            # 오른쪽 자식 노드 인덱스 = 인덱스 * 2 + 1
        left_sum = self.query(L, R, 2 * node, start, mid)
        right_sum = self.query(L, R, 2 * node + 1, mid + 1, end)
        # 왼쪽 자식 노드에서 끌어올려진 값과 오른쪽 자식 노드에서 끌어올려진 값을 합산하여 다음 레벨로 넘어감
        return left_sum + right_sum

    def update_value(self, idx, val):
        self.update(idx, val, 1, 0, self.n - 1)

    def range_query(self, L, R):
        return self.query(L, R, 1, 0, self.n - 1)


# ------------
# 사용 예시
# ------------
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

print(seg_tree.range_query(1, 3))  # Output: 15 (3 + 5 + 7)

seg_tree.update_value(1, 10)
print(seg_tree.range_query(1, 3))  # Output: 22 (10 + 5 + 7)