import random
import time
import numpy as np

# 定义两支球队的属性
team1 = {
    "name": "ManCity",
    "attack": 90,
    "defense": 90,
    "midfield": 95
}

team2 = {
    "name": "ManUnited",
    "attack": 65,
    "defense": 35,
    "midfield": 60
}

score_list = [0, 0, 0]

# 初始化比分
score_team1 = 0
score_team2 = 0

#时间
match_time = 90
injury_time = 0

#球权
possession = True

#函数
def IniMatch():
    global match_time, possession, score_team1, score_team2
    match_time = 90
    possession = True
    score_team1 = 0
    score_team2 = 0

def MidfieldAttack(t1, t2):
    global match_time, possession, score_team1, score_team2
    # 组织
    print(t1['name'] + "中场组织进攻")
    if(t1["midfield"] > random.gauss(0, 1)*100 and t2["midfield"] < random.gauss(0, 1)*100):
        match_time -= 2
        print(t1["name"] + "中场突破！")

        #进攻
        if(t1["attack"] > random.gauss(0, 1)*100 and t2["defense"] < random.gauss(0, 1)*100):
                match_time -= 1
                print(t1["name"] + "进入禁区！")

                #射门
                if(t1["attack"] > (random.gauss(0, 1))):
                    if(possession):
                        score_team1 += 1
                    else:
                        score_team2 += 1
                    print(t1["name"] + "进球得分！！！")
                    print(f"现在比分！{team1['name']} {score_team1} - {score_team2} {team2['name']}")
                    possession = not possession
                else:
                    print(t1["name"] + "射门偏出。")
                    possession = True if random.gauss(0, 1)>0.5 else False
        else:
            match_time -= 1
            possession =  not possession
            print("球权转换。")
    else:
        match_time -= 2
        possession = not possession
        print("球权转换。")


# 模拟比赛
def MatchSim(speed):
    while match_time > 0:
    # 计算比赛事件的概率
        if(possession):
            MidfieldAttack(team1, team2)
        else:
            MidfieldAttack(team2, team1)
        if(match_time >=0):
            print("比赛时间：" + str(match_time))

for i in range(100):
    IniMatch()
    MatchSim(5)
    score_str = (str(score_team1)+ " - " + str(score_team2))
    if(score_team1>score_team2):
        score_list[0] += 1
    elif(score_team1 == score_team2):
        score_list[1] += 1
    else:
        score_list[2] += 1
    ## score_list.append(score_str)

print(score_list)
# 输出比赛结果
# print(f"比赛结束！{team1['name']} {score_team1} - {score_team2} {team2['name']}")
