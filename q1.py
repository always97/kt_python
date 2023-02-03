# Q1 Answer template
def rank(match):
    if match == 6 : return 1
    elif match == 5: return 2
    elif match ==4 : return 3
    elif match == 3 : return 4
    elif match == 2 : return 5
    else : return 6
    
    
def solution(lottos, win_nums):
    match_num = 0
    anynum = 0
    for i in lottos:
        if i in win_nums:
            match_num+=1
        elif i == 0 : anynum+=1
            
    return rank(match_num+anynum), rank(match_num)

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)
