def change(record,name):
    for i in range(len(record)):
        if record[i][0] == 'Enter':
            name[record[i][1]] = record[i][2]
        elif record[i][0] == 'Change':
            name[record[i][1]] = record[i][2]
def solution(record):
    for i in range(len(record)):
        record[i] = list(map(str, record[i].split(' ')))
        #record[i][1] = record[i][1].strip('uid')
    ans, res = [], ''
    name = dict()
    change(record, name)
    for i in range(len(record)):
        if record[i][0] == 'Enter':
            res = '%s님이 들어왔습니다.' %(name[record[i][1]])
            ans.append(res)
        elif record[i][0] == 'Leave':
            res= '%s님이 나갔습니다.' %(name[record[i][1]])
            ans.append(res)
    return ans
