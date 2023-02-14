class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        freq = defaultdict(int)
        for response in responses: 
            words = set(response.split())
            for feature in features: 
                if feature in words: freq[feature] += 1
        return sorted(features, key=lambda x: freq.get(x, 0), reverse=True)
    
# from collections import Counter

# class Solution:

#     def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
#         stats = Counter(features)
#         features_set = set(features)
#         for response in responses:
#             response_features = set(response.split()) & features_set
#             stats += Counter(response_features)
#         sorted_features = sorted(stats.keys(), key=stats.get, reverse=True)
#         return sorted_features
            
                    
        