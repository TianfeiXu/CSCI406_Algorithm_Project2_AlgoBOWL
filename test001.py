# @Time    : 2023/2/13 下午 6:36
# @Author  : Tianfei Xu
# @Email   : tianfei8@outlook.com
# @Software: PyCharm
# @Project : Project2Programming
# @File    : test001
import sys 

class AlgoBOWL:
    def __init__(self, n, target_list):
        """
        input n, and target_list.
        :param n:
        :param target_list:
        """
        self.n=n    #number of targets. Have not used.
        self.target_list=target_list    #list of some intergers.
        self.addends=[1]
        self.result=[]

    def select_addend(self, first_addend, target):
        """
        Find the most suitable addend in the optimal addends list.
        :param first_addend: the first addends of the add, which should be the max of the existing addends list.
        :param target: target of sum.
        :return: optional addend, which is the largest int in the addends list but less or equal than a perfect matched addend.
        """
        range= target - first_addend
        for i in self.addends[::-1]:
            if i <= range:
                return i
        return None


    def finder(self):
        """
        Get the result for target list. Superior rather than optimal.
        :return: the result list of the class, is a 2 layer nested list, the inner list is a two-int-element list, which are the two addends of one addition operation.
        """
        int_max=1
        for target in self.target_list:
            while True:
                sum1=int_max * 2
                if sum1 > target:
                    select_addend=self.select_addend(int_max, target)
                    sum2=select_addend + int_max
                    self.result.append([int_max, select_addend])
                    self.addends.append(sum2)
                    int_max=sum2
                    if sum2==target:
                        break
                elif sum1 == target:
                    self.result.append([int_max, int_max])
                    self.addends.append(sum1)
                    int_max=sum1
                    break
                elif sum1 < target:
                    self.result.append([int_max, int_max])
                    self.addends.append(sum1)
                    int_max=sum1


        return self.result


if __name__ == '__main__':

    target_list = [] #array to store points 
    file = sys.argv[1]
    with open(file) as f: # read in input file 
        n = int(f.readline())
        values = f.readline()
    
    for value in values.split(' '):
        target_list.append(int(value))

    if(len(target_list) != n): # self check on input 
        print('Input error')

    AB1=AlgoBOWL(n, target_list)
    print(AB1.finder())

    totalComputations = len(AB1.result)
    with open('output.txt', 'w') as file:
        file.writelines(f'{totalComputations} \n')
        i = 0
        for computation in AB1.result:
            if(i == len(AB1.result)-1):
                file.writelines(f'{computation[0]} {computation[1]}')
                continue
            file.writelines(f'{computation[0]} {computation[1]} \n')
            i = i+1
