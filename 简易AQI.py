print("本程序由御风工作室编写。")
x=int(input("请输入AQI数值:"))
if x<0:
    print("输入错误！")
else:
    if x<=50:
        s="一级，优，空气清新，参加户外活动。"
    elif x<=100:
        s="二级，良，可以正常进行户外活动。"
    elif x<=150:
        s="三级，极度污染，敏感人群减少体力消耗大的户外活动。"
    elif x<=200:
        s="四级，中度污染，对敏感人群影响较大，减少户外活动。"
    elif x<=300:
        s="五级，重度污染，所有人适当减少户外活动。"
    else:
        s="6级，严重污染，尽量不要留在户外。"
print("空气质量为"+s)