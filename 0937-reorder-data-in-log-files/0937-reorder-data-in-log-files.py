class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        # def weirdOrder(log):
        #     all_parts = log.split()
        #     key, rest = all_parts[0], all_parts[1:]
        #     return [' '.join(rest) , key]
        letter_logs.sort(key = lambda x: [x.split(' ')[1:],x[0]])
        return letter_logs + digit_logs
        
        
        