def change(data):
    time = list(map(float, data[1].split(':')))
    spent = float(data[2][:-1])
    alltime = 0
    for i in range(2, -1,-1):
        alltime += time[i] * (60**(2-i))
    alltime = '%0.3f' %(float(alltime))
    start = '%0.3f' %(float(alltime) - spent+0.001)
    return([start, alltime])
def solution(lines):
    file = []
    for j in range(len(lines)):
        lines[j] = list(map(str, lines[j].split(' ')))
    for i in range(len(lines)):
        file.append(change(lines[i]))
        file[i][0] , file[i][1] = float(file[i][0]), float(file[i][1])
    answer = 0
    for i in range(len(file)):
        count1, count2 = 0,0
        a,b = file[i][0], file[i][1]
        for j in range(len(file)):
            if not (file[j][1] <= a or file[j][0] > a+1): 
                count1 += 1
            if not (file[j][1] <= b or file[j][0] > b+1): 
                count2 += 1
        answer = max(answer, count1, count2)
    return answer
