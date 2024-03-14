class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort() # time O(nlogn)
        array_len = len(products)
        ans = []
        input_char = ""

        for chr in searchWord:
            tmp = []
            input_char += chr
            insertion_index = self.binary_search(products, input_char)
            for word_ind in range(insertion_index, min(array_len, insertion_index+3)):
                if products[word_ind].startswith(input_char):
                    tmp.append(products[word_ind])
            ans.append(tmp)
        return ans

    def binary_search(self, array, target):
        lo = 0
        hi = len(array)

        while lo < hi:
            mid = (lo + hi) //2
            if array[mid] < target: lo = mid + 1
            else: hi = mid
        return lo