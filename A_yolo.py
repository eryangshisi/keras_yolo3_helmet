from PIL import Image
import yolo
from timeit import default_timer as timer
import os
import cv2
import numpy as np

def detect_video(yolo, video_path, output_path=""):
    vid = cv2.VideoCapture(video_path)
    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video")
    video_FourCC    = int(vid.get(cv2.CAP_PROP_FOURCC))
    video_fps       = vid.get(cv2.CAP_PROP_FPS)
    video_size      = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    isOutput = True if output_path != "" else False
    if isOutput:
        print("!!! TYPE:", type(output_path), type(video_FourCC), type(video_fps), type(video_size))
        print("!!! TYPE:", output_path, video_FourCC, video_fps, video_size)
        out = cv2.VideoWriter(output_path, video_FourCC, video_fps, video_size)
    accum_time = 0
    curr_fps = 0
    fps = "FPS: ??"
    prev_time = timer()
    while True:
        return_value, frame = vid.read()
        image = Image.fromarray(frame)
        image = yolo.detect_image(image)
        result = np.asarray(image)
        curr_time = timer()
        exec_time = curr_time - prev_time
        prev_time = curr_time
        accum_time = accum_time + exec_time
        curr_fps = curr_fps + 1
        if accum_time > 1:
            accum_time = accum_time - 1
            fps = "FPS: " + str(curr_fps)
            curr_fps = 0
        cv2.putText(result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.imshow("result", result)
        if isOutput:
            out.write(result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    yolo.close_session()

def get_class(path= 'model_data/safe_hat_project_classes_for_hhhh_h5.txt',):
        classes_path = os.path.expanduser(path)
        with open(classes_path) as f:
            class_names = f.readlines()
        class_names = [c.strip() for c in class_names]
        return class_names

def num_pic(image, out_boxes, out_classes, out_scores,class_names):
    """
    :param image:img_PIL
    :param out_boxes:
    :param out_classes:
    :param out_scores:
    :return:
    """

    for i, c in reversed(list(enumerate(out_classes))):
        predicted_class = class_names[c]
        box = out_boxes[i]
        score = out_scores[i]

        label = '{} {:.2f}'.format(predicted_class, score)
        # draw = ImageDraw.Draw(image)
        # label_size = draw.textsize(label, font)

        top, left, bottom, right = box
        top = max(0, np.floor(top + 0.5).astype('int32'))
        left = max(0, np.floor(left + 0.5).astype('int32'))
        bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
        right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
        print(label, (left, top), (right, bottom))

        # if top - label_size[1] >= 0:
        #     text_origin = np.array([left, top - label_size[1]])
        # else:
        #     text_origin = np.array([left, top + 1])

        # My kingdom for a good redistributable image drawing library.
        # for i in range(thickness):
        #     draw.rectangle(
        #         [left + i, top + i, right - i, bottom - i],
        #         outline=self.colors[c])
        # draw.rectangle(
        #     [tuple(text_origin), tuple(text_origin + label_size)],
        #     fill=self.colors[c])
        # draw.text(text_origin, label, fill=(0, 0, 0), font=font)
        # del draw


if __name__ == '__main__':
    yolo = yolo.YOLO()
    is_show = True
    test_video = False
    # 比赛测试文件的格式：标签 置信度 Left Top Right Buttom
    # hat/person socres Left Top Right Buttom
    """
    annotation_path = "F:/safe_hat_project/labels_test.txt"
    with open(annotation_path) as f:
        lines = f.readlines()
    """
    if test_video:
        detect_video(yolo, 0)
    else:
        #原：F:/JPEGImages/wu
        for (root, dirs, files) in os.walk('C:/python-project/HafetyHelmet/JPEGImages/wu'):
            if files:
               for f in files:
                   path = os.path.join(root, f)
                   image = cv2.imread(path)
                   # f: test_000121.jpg(文件名)
                   # cv2转化为PIL
                   img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                   f_ = f.split(".")[0]
                   print("f_:",f_)
                   flag, r_image, out_boxes,  out_scores, out_classes = yolo.detect_image_for_write_testdata(img_PIL, f_)

                   ir_mg = cv2.cvtColor(np.asarray(r_image), cv2.COLOR_RGB2BGR)
                   cv2.imshow("OpenCV", ir_mg)
                   # if have_box:
                   #     cv2.imwrite('images/20200325/' + filename, ir_mg)
                   cv2.waitKey(2)

    # 从文件中读取：
    # annotation_path = 'F:/safe_hat_project/labels_test.txt'
    # with open(annotation_path) as f:
    #     lines = f.readlines()
    # # print(lines)
    # for a_line in lines:
    #     a_line = a_line.replace("\\", "/")
    #     a_line = a_line.replace("\n", "")
    #     filename = a_line.split("/")[3]
    #     image = cv2.imread(str(a_line))
    #     img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #     # ======一步搞定版========
    #     # have_box, r_image, out_boxes, out_classes, out_scores= yolo.detect_image(image=img_PIL)
    #
    #     # ========
    #     have_box, r_image, out_boxes_, out_scores, out_classes = yolo.detect_image_no_draw(image=img_PIL)
    #     out_boxes = yolo.get_box(r_image, out_boxes_)
    #     r_image = yolo.draw_img(r_image, out_boxes, out_scores, out_classes)
    #     hat_num, per_num = yolo.get_num_class(out_classes)
    #     print("hat_num:", hat_num, "per_num:", per_num)
    #     ir_mg = cv2.cvtColor(np.asarray(r_image), cv2.COLOR_RGB2BGR)
    #     cv2.imshow("OpenCV", ir_mg)
    #     # if have_box:
    #     #     cv2.imwrite('images/20200325/' + filename, ir_mg)
    #     cv2.waitKey(2)




    # 视频读取
    # detect_video(yolo, './videos/test/last2_x264.mp4', './videos/res/car_res.avi')
    # ./ videos / test / car_video.mp4
    # 读取帧图像
    # class_names = get_class()
    #
    # cap = cv2.VideoCapture(0)
    # while(1):
    #     ret, frame = cap.read()
    #     #show a frame
    #     cv2.imshow("capture", frame)
    #     img_PIL = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    #     print("img_PIL", type(img_PIL))
    #     is_ok, r_image, out_boxes, out_classes, out_scores = yolo.detect_image(image=img_PIL)
    #
    #     # PIL转化为cv2
    #     ir_mg = cv2.cvtColor(np.asarray(r_image), cv2.COLOR_RGB2BGR)
    #     cv2.imshow("OpenCV", ir_mg)
    #     cv2.waitKey(1)