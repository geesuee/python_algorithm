# 반복문으로 세그먼트 트리 구현

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)
    
    def build(self, data):
        # 리프 노드 값 초기화
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # 자식 노드 값의 합으로 부모 노드 연산
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, pos, value):
        # 특정 원소만 값으로 갖는 리프 노드 찾아서 수정
        pos += self.n
        self.tree[pos] = value
        # 해당 노드가 영향을 주는 부모 노드 찾아서 수정
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
    
    def query(self, left, right):
        # 내부 구간 합 연산
        left += self.n
        right += self.n
        sum = 0
        while left < right:
            if left % 2 == 1:
                sum += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                sum += self.tree[right]
            left //= 2
            right //= 2
        return sum



# ------------
# 사용 예시
# ------------
data = [1, 2, 3, 4, 5]
seg_tree = SegmentTree(data)

print(seg_tree.query(1, 4))  # Output: 9 (2 + 3 + 4)

seg_tree.update(2, 10)
print(seg_tree.query(1, 4))  # Output: 16 (2 + 10 + 4)
