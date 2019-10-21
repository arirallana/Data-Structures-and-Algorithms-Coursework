'''
progrm to fid mediam of a list of integers using threshold values. A threshold (1 or 0)
indicates whether the number in list is greater or less than the index. Median is found by summing
all threshold values. 
'''

def threshold_median(list_):
    scores_list = []
    for i in range(1, max(list_)+1):
        score = []
        for j in range(len(list_)):
            if list_[j] >= i:
                score.append(1)
            else:
                score.append(0)
        if score.count(1)>=score.count(0):
            scores_list.append(1)
        else:
            scores_list.append(0)
    median = sum(scores_list)
    print(median)
    return median

list_ = [1,3,2,6,4,7,5,8,9]
threshold_median(list_)
            
        
