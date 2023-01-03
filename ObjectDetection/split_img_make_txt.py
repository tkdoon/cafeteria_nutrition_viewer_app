import os
import random
import shutil
#什么都不用改 ,只需要改下面的划分比例

img_directory_path = ''
train_img_path = ''
valid_img_path = ''
train_txt_path = ''
valid_txt_path = ''
dish_list = []
img_list = []


for index, dish_name in enumerate(os.listdir(img_directory_path)):
    print(dish_name)
    dish_list.append(dish_name)
    dish_path = img_directory_path+dish_name
    for img_file_name in os.listdir(dish_path):
        if "augmented_9" in img_file_name:
            shutil.copy2(dish_path+"/"+img_file_name, valid_img_path)
            labelFile = open(valid_txt_path +
                             os.path.splitext(img_file_name)[0] + '.txt', 'w')

        else:
            shutil.copy2(dish_path+"/"+img_file_name, train_img_path)
            labelFile = open(train_txt_path +
                             os.path.splitext(img_file_name)[0] + '.txt', 'w')

        labelFile.write(str(index) + ' 0.500000 0.500000 1.000000 1.000000')
        labelFile.close()
