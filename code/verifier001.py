# @Time    : 2023/2/28 下午 2:36
# @Author  : Tianfei Xu
# @Email   : tianfei8@outlook.com
# @Software: PyCharm
# @Project : test001.py
# @File    : verifier001
from icecream import ic

class Verifier:
    def __init__(self, input_file, output_file):
        self.input_file=input_file
        self.outpit_file=output_file
        self.n=0
        self.target_list=[] # array to store points
        self.add_operations_list=[]

    def read_input_file(self):
        with open(self.input_file) as f:  # read in input file
            self.n = int(f.readline())
            values = f.readline()

        for value in values.split(' '):
            self.target_list.append(int(value))

        if (len(self.target_list) != self.n):  # self check on input
            print('Input error')

        return self.target_list

    def read_output_file(self):
        with open(self.outpit_file) as f:  # read in input file
            n = int(f.readline())
            output_list = f.readlines()[1:]

        for output_line in output_list:
            self.add_operations_list.append(list(map(int,output_line.strip().split())))
        #ic(self.add_operations_list)
        return self.add_operations_list

    def do_addition(self):
        self.read_output_file()
        sum_list=list(map(sum, self.add_operations_list))
        return sum_list

    def judge_inclusion(self):
        self.read_input_file()
        sum_list=self.do_addition()
        print(set(self.target_list)<= set(sum_list))




if __name__ == '__main__':
    vf001=Verifier("input_group592.txt",'output.txt')
    vf001.judge_inclusion()


