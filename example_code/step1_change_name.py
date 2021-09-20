import os
from os import listdir
from os.path import isfile, join
import argparse

"""
將 images, ground_truth 檔案拆分成： train, test 資料。

"""
parser = argparse.ArgumentParser()
parser.add_argument("--path",
                    type=str,
                    help="這是第 1 個引數，請給定路徑")
args = parser.parse_args()


print(os.getcwd())
# Set path :
imgpath = './step1_data/jpg/'
xmlpath = './step1_data/xml/'

# Set training name:
training_name = 'dbnet_data_' 

# get name
ori_imgname = [f for f in listdir(imgpath) if isfile(join(imgpath, f))]
ori_xmlname = [f for f in listdir(xmlpath) if isfile(join(xmlpath, f))]
imgname = [f.strip('.jpg') for f in ori_imgname]
xmlname = [f.strip('.xml') for f in ori_xmlname]

# Create dict for mapping
enum = enumerate(imgname)
dictionary = dict((i,j) for i,j in enum)



# rename img filename : 
for index ,content in enumerate(imgname):
    if content in dictionary.values():
        # print(index ,content)
        os.rename(imgpath + content + '.jpg', imgpath + training_name + str(index) + '.jpg')
    else:
        print('Wrong match')


# rename xml filename : 
for index ,content in enumerate(xmlname):
    if content in dictionary.values():
        # print(index ,content)
        os.rename(xmlpath + content+ '.xml', xmlpath + training_name + str(index) + '.xml')
    else:
        print('Wrong match')

print('[ Step1 Done  ]')







