
import os
import cv2

olddir = 'images/slide1'
newdir = 'images/slide'
os.makedirs(newdir, exist_ok=True)
filelist = os.listdir(olddir)
count = 0
for file in filelist:
    try:
        count += 1
        if count % 100 == 0:
            print(count)

        filename = olddir+file

        img = cv2.imread(filename)
        target_img = cv2.resize(img, (1920, 1280))
        newpath = newdir+file
        cv2.imwrite(newpath, target_img)
    except:
        pass
