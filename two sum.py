class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        #loop que adicona os numeros ao mapa e faz a verificação simultanea de qual deles da o complemento 
        for i, num in enumerate(nums):
            # ex: se num = 7 e target = 9 o complemento sera 2 que fara a busca no mapa
            # o mesmo vale para caso o num = 2 target = 9, o complemento sera 7 
            complemento = target - num
            if complemento in mapa:
                # retorno da posições dos numeros
                #a chave do mapa seria o valor de nums, e o valor da chave seria a posição
                return[mapa[complemento], i]
            mapa[num]=i


