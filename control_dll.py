from ctypes import *
import os

#原：E:\HafetyHelmet\idcard   C:\python-project\HafetyHelmet\idcard
def file_name(file_dir="C:\python-project\HafetyHelmet\idcard"):
    """
    :func ：得到file_dir下所有符合条件的文件的路径列表
    :param file_dir:
    :return: list,如：['E:\\HafetyHelmet\\idcard\\WIN_20200512_09_52_26_Pro.jpg']
    """
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(root, file))
    return L

def one_vs_one(path1, path2):
    """
    :func 1：1的人脸比对函数
    :param path1:图像存储的地址1
    :param path2: 图像存储的地址2（必须是绝对路径）
    :return: 返回两张图片的相似度（置信度，最大为1）
    """
    dll = CDLL("Dll2.dll")
    demo = dll.demo_samplecode
    demo.restype = c_float
    a = dll.demo_samplecode(c_char_p(bytes(path1, 'utf-8')),
                            c_char_p(bytes(path2, 'utf-8')))
    return float(str(a))

#原：E:\HafetyHelmet\idcard 修改时间：2022.4.12
def one_vs_n(path_img, path_idcard="C:\python-project\HafetyHelmet\idcard"):
    """
    :func 实现1：N的人脸比对，如果最后匹配到的最大人脸置信度>0.5就返回最大那个图片，如果<0.5认为没有这个人，此次比对无效
    :param path_img:待比对人脸图片
    :param path_idcard:人脸库
    :return:id 也就是工人的工号，【类型】str
        比如最后匹配到E:\\HafetyHelmet\\idcard\\12223.jpg--》返回的id就是12223
    """
    L = file_name(file_dir=path_idcard)
    score = -1
    max_socre_id = 0.0
    for i in L:
        now_socre = one_vs_one(path_img, i)
        if score < now_socre:
            score = now_socre
            max_socre_id = i

    if score < 0.5:
        id = ""
    else:
        id = str(max_socre_id.split("\\")[-1]).split(".")[0]
    return id

if __name__ == '__main__':
    import datetime
    starttime = datetime.datetime.now()
    #原：E:\\HafetyHelmet\\20200512175507.png 修改时间：2022.4.12
    print(one_vs_n("C:\\python-project\\HafetyHelmet\\20200512175507.png"))
    # long running
    endtime = datetime.datetime.now()
    print((endtime-starttime).seconds)
