"""
Author: Gang Liu, 1725443381@qq.com

Question:
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Examples:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def main(list_num, obj_num):
    sum = [i+j for i in list_num for j in list_num if i != j]
    pos = [(i, j) for i in range(len(list_num)) for j in range(len(list_num)) if i != j]
    print(list([i for i in dict(zip(pos, sum)).keys() if dict(zip(pos, sum))[i] == obj_num][0]))
    
    # out: [0, 3]

if __name__ == "__main__":
  list_num = [1, 2, 4, 7, 9]
  obj_num = 8
  main(list_num, obj_num)

