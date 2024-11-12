class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        max_beauty = []
        beauty = 0
        for query in queries:
            for item in items:
                if item[0] <= query:
                    # price below max price
                    if item[1] > beauty:
                        beauty = item[1]    # pick the most beautiful item
            # add it to max_beauty
            max_beauty.append(beauty)
            beauty = 0
        return max_beauty
