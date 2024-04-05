class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        resposta = ['']
        if len(digits)==0:
            return []
        number = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz",    
        }
        # list_digits = [number[digits[i]] for i in range(len(digits))]
        # print(list_digits)
        # return list_digits
        # for i in range(len(list_digits[0])):
        #     if len(list_digits) < 2:
        #         resposta.append(list_digits[0][i])
        #         continue
        #     sub_lista = []
        #     for j in range(len(list_digits[i])):
        #         sub_lista = sub_lista + [r + c for r in resposta]
        #     resposta = sub_lista
        for i in digits:
            # if len(list_digits) < 2:
            #     resposta.append(list_digits[0][i])
            #     continue
            sub_lista = []
            for j in number[i]:
                sub_lista = sub_lista + [k + j for k in resposta]
            resposta = sub_lista
        
            
        return resposta

