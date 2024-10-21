# 방법 1
# def solution(genres, plays):
#     answer = []
    
#     genre_dic = {}
#     for genre in set(genres):
#         genre_dic[genre] = {}
        
#     for i in range(len(plays)):
#         genre_dic[genres[i]][i] = plays[i]
        
#     # print(genre_dic) # {'pop': {1: 600, 4: 2500}, 'classic': {0: 500, 2: 150, 3: 800}}
    
#     sum_genre = []
    
#     for genre in genre_dic.keys(): # 'pop', 'classic'
#         sum_genre.append([genre, sum(genre_dic[genre].values())])
#         genre_dic[genre] = sorted(genre_dic[genre].items(), key=lambda x:(-x[1], x[0]))
    
#     sum_genre.sort(key=lambda x: -x[1])
#     # print(sum_genre) # [['pop', 3100], ['classic', 1450]]
#     # print(genre_dic) # {'pop': [(4, 2500), (1, 600)], 'classic': [(3, 800), (0, 500), (2, 150)]}
    
#     for genre, play in sum_genre:
#         if len(genre_dic[genre]) >= 2:
#             answer.append(genre_dic[genre][0][0])
#             answer.append(genre_dic[genre][1][0])
#         else:
#             answer.append(genre_dic[genre][0][0])
#     return answer

# 방법 2
def solution(genres, plays):
    answer = []
    
    d = {e:[] for e in set(genres)}
    # print(d) # {'pop': [], 'classic': []}
    
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    # print(d) # {'classic': [[500, 0], [150, 2], [800, 3]], 'pop': [[600, 1], [2500, 4]]}
    
    # print(list(d.keys())) # ['classic', 'pop']
    genreSort =sorted(list(d.keys()), key= lambda x: sum(map(lambda y: y[0], d[x]) ), reverse = True)
    # print(genreSort) # ['pop', 'classic']
    
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    
    return answer
