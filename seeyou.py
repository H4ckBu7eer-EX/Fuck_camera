
import argparse
from cv2 import VideoCapture, imwrite

parser = argparse.ArgumentParser(description="I can SEE YOU!")
parser.add_argument("-c", "--check", help="获取摄像头数目", action="store_true")
parser.add_argument("-u", "--use", help="选择使用的摄像头", type=int)
parser.add_argument("-f", "--folder", help="选择保存目录")

args = parser.parse_args()


if args.check:
    camera = VideoCapture(0)
    num_cameras = 0
    if camera.isOpened():
        num_cameras += 1
        camera.release()
        camera = VideoCapture(num_cameras)
        print(f"检测到{num_cameras}个摄像头!")
    else:
        print("没有检测到摄像头!")
        exit()


if args.use: 
    cap = VideoCapture(args.use if args.use else 0)
    save_path = args.folder if args.folder else "."
    ret, frame = cap.read()
    imwrite(f'{save_path}/shot.png', frame)

    # 打印最终保存目录
    print(f"照片保存至{save_path}目录!")


else:
    print("先看看-h吧")