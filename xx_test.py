from playsound import playsound
# list_num = "123432"
# root = "E:/HafetyHelmet/auido/"
# # # for i in list:
# playsound(root+"wpd.mp3")         # 未佩戴人员
# playsound(root+"gonghao.mp3")      # 工号
# l = list(list_num)
# for i in l:
#     playsound(root+i+".mp3")
# playsound(root+"xm.mp3")
# playsound(root+"xiaobai.mp3")

#原：E:/HafetyHelmet/auido/   C:/python-project/HafetyHelmet/auido/
def broadcast_mp3(Warning_signs,root = "C:/python-project/HafetyHelmet/auido/"):
    """
    :param list: 直接那个Warning_signs-->"[[id_img_path, name, id],[xxx, xxx, xxx],...]"
    :return:
    """
    for i in Warning_signs:
        id = i[2]
        print(id)
        # # for i in list:
        playsound(root + "wpd.mp3")  # 未佩戴人员
        playsound(root + "gonghao.mp3")  # 工号
        id_list = list(id)
        for j in id_list:
            playsound(root + j + ".mp3")
            print(j)
        if i[1] == "杨玥":
            playsound(root + "xm.mp3")
            playsound(root + "yangyue.mp3")

if __name__ == '__main__':
    broadcast_mp3([[".ada/ds/","杨玥","201824050341"]])
    