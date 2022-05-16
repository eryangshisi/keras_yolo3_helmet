from playsound import playsound
#原：E:/HafetyHelmet/auido/         C:/python-project/HafetyHelmet/auido/
def broadcast_mp3(Warning_signs,root = "C:/python-project/HafetyHelmet/auido/"):
    """
    :param list: 直接用给陈豪的那个Warning_signs-->"[[id_img_path, name, id],[xxx, xxx, xxx],...]"
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
    #原：E:\\HafetyHelmet\\idcard\\20200303003.jpg     C:\python-project\HafetyHelmet
    broadcast_mp3([['C:\\python-project\\HafetyHelmet\\20200303003.jpg', '杨玥', '20200303003']])