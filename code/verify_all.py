# @Time    : 2023/2/28 下午 4:14
# @Author  : Tianfei Xu
# @Email   : tianfei8@outlook.com
# @Software: PyCharm
# @Project : CSCI406_Algorithm_Project2_AlgoBOWL
# @File    : verify_all

from verifier001 import Verifier
import os
from icecream import ic

if __name__ == '__main__':
    input_files_address=r"..\all_inputs\inputs"
    output_file_address=r"..\OUTPUTS"
    for root, dirs, files in os.walk(input_files_address):
        for input_file_name in files:
            output_file_name='output'+input_file_name
            vf001=Verifier(os.path.join(input_files_address, input_file_name), os.path.join(output_file_address, output_file_name))
            judgement=vf001.judge_inclusion()
            ic(input_file_name, output_file_name, judgement)
