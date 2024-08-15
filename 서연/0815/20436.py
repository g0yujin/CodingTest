import sys

lefthand_keyboard = {
    'q':(0,0), 'w':(0,1), 'e':(0,2), 'r':(0,3), 't':(0,4), 
    'a':(1,0), 's':(1,1), 'd':(1,2), 'f':(1,3), 'g':(1,4), 
    'z':(2,0), 'x':(2,1), 'c':(2,2), 'v':(2,3)
}

righthand_keyboard = {
    'y':(0,5), 'u':(0,6), 'i':(0,7), 'o':(0,8), 'p':(0,9),
    'h':(1,5), 'j':(1,6), 'k':(1,7), 'l':(1,8),
    'b':(2,4), 'n':(2,5), 'm':(2,6)
}

left, right = sys.stdin.readline().split()

words = input()

cnt = 0

for word in words:

    if word == left or word == right:
        cnt += 1
        continue
    else:
        left_x, left_y = lefthand_keyboard[left] # 왼손의 위치
        right_x, right_y = righthand_keyboard[right] # 오른손의 위치

        try:
            word_left, word_right = righthand_keyboard[word] # 입력해야 할 단어의 위치
            move = abs(word_left - right_x) + abs(word_right - right_y) # 오른손이 움직여야 하는 횟수
            right = word
        except:
            word_left, word_right = lefthand_keyboard[word]
            move = abs(word_left - left_x) + abs(word_right - left_y) # 왼손이 움직여야 하는 횟수
            left = word
        cnt += (move + 1)

print(cnt)