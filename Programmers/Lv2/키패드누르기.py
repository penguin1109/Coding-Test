def solution(numbers, hand):
    answer = ''
    """
    1. 왼손 엄지는 '*' 오른손 엄지는 '#'에서 시작
    2. 엄지 손가락은 4개의 방향으로만 이동이 가능
    3. 1, 4, 7입력 할 떄는 왼손 / 3,6,9 입력 할때는 오른손 / 2,5,8,0입력 할때는 더 가까운 (거리가 같으면 "hand"에 따라 다르게)
    4. 각 번호를 누른 손가락이 왼 -> L 오 -> R
    """
    user = 'L'

    if hand == 'right':
        user = 'R'

    def change(n):
        if n in [int(i) for i in range(1, 10)]:
            return n
        elif n == '*':return 10
        elif n == 0:return 11
        else:return 12

    def get_dist(l, r, num):
        l,r = change(l)-1, change(r)-1
        num = change(num)-1
        lx,ly,rx,ry = l//3,l%3,r//3,r%3
        nx, ny = num//3, num%3
        dl = abs(nx-lx) + abs(ny-ly)
        dr = abs(nx-rx) + abs(ny-ry)
        return dl, dr

    def get_hand(l, r, num):
        if num in [1,4,7]:
            return 'L'
        elif num in [3,6,9]:
            return 'R'
        else:
            dl, dr = get_dist(l, r, num)
            if (dl == dr):return user
            elif (dl < dr):return 'L'
            else:return 'R'
    l,r = '*', '#'
    for n in numbers:
        ans = get_hand(l,r,n)
        if (ans == 'L'):
            l = n
        else:
            r = n
        answer += ans


    return answer

if __name__ == "__main__":
    numbers = [7,0,8,2,8,3,1,5,7,6,2]
    hand = "left"
    print(solution(numbers, hand))