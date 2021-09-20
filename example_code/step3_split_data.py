import os
import shutil
from os import walk
import argparse

"""
將 images, ground_truth 檔案拆分成： train, test 資料。

"""
parser = argparse.ArgumentParser()
parser.add_argument("--path",
                    type=str,
                    help="這是第 1 個引數，請給定路徑")
args = parser.parse_args()

# Set path:
default_path = args.path #'/Users/datanny/Desktop/'
src_path = default_path + 'step3_data/'
dst_path = default_path + 'datasets/'
dst_train_img = dst_path + 'train/' + 'img'
dst_train_gt = dst_path + 'train/' + 'gt'
dst_test_img = dst_path + 'test/' + 'img'
dst_test_gt = dst_path + 'test/' + 'gt'
if not os.path.exists(dst_path + 'train') or not os.path.exists(dst_path + 'test'):
    os.makedirs(dst_train_img)
    os.makedirs(dst_train_gt)
    os.makedirs(dst_test_img)
    os.makedirs(dst_test_gt)

# Set file name [source files]: 
img_path =  src_path + '/img/'
gt_path = src_path + '/gt/'

# Set file name [distination files]: 
train_txt_path = dst_path + 'train.txt'
test_txt_path = dst_path + 'test.txt'
train_txt = open(train_txt_path,'a+')
test_txt = open(test_txt_path,'a+')

# Set percentage:
train_percent = 0.8
test_percent = 1 - train_percent 

# Ignore .ds_store files:
img_names = [i for i in sorted(next(walk(img_path), (None, None, []))[2]) if not i.startswith('.') ]
gt_names = [i for i in sorted(next(walk(gt_path), (None, None, []))[2]) if not i.startswith('.') ]



count = 0.1
total_round = len(img_names)
for count_down in range(total_round):
    if round(count_down/total_round, 1) == count:
        print(' --- Step3 Split data process : [  {}%  ]'.format(count*100))

        # Split data: 
        train_img = img_names[ : int(len(img_names) * train_percent)]
        test_img = img_names[int(len(img_names) * train_percent):]

        train_gt = gt_names[ : int(len(gt_names) * train_percent)]
        test_gt = gt_names[int(len(gt_names) * train_percent):]

        # Copy data to train, test folder: 
        for name in train_img:
            shutil.copy2(src_path + 'img/' + name, dst_train_img)
        for name in train_gt:
            shutil.copy2(src_path + 'gt/' + name, dst_train_gt)
        for name in test_img:
            shutil.copy2(src_path + 'img/' + name, dst_test_img)
        for name in test_gt:
            shutil.copy2(src_path + 'gt/' + name, dst_test_gt)
            
        if len(train_img) == len(train_gt):
            with open(train_txt_path, 'w') as f:
                for i in range(len(train_img)):
                    if not train_img[i].startswith('.') and not train_gt[i].startswith('.'):
                        f.write(dst_path + 'train/img/' + train_img[i]+ ' ')
                        f.write(dst_path + 'train/gt/' + train_gt[i]+ '\n')
        else: 
            print('[Train]image and ground truth quantity not match!')


        if len(test_img) == len(test_gt):
            with open(test_txt_path, 'w') as f:
                for i in range(len(test_img)):
                    if not test_img[i].startswith('.') and not test_gt[i].startswith('.'):
                        f.write(dst_path + 'test/img/' + test_img[i]+ ' ')
                        f.write(dst_path + 'test/gt/' + test_gt[i]+ '\n')
        else: 
            print('[Test] image and ground truth quantity not match!')


        count += 0.1
        count = round(count, 1) 
    if count_down == total_round - 1:
        print('[  Step3 Done  ]')



