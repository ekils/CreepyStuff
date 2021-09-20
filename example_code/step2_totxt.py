import re
import os
import shutil
import argparse
from xml.dom import minidom

def init_args():
    args = argparse.ArgumentParser()
    # args.add_argument('--file_folder',
    #                   type=str,
    #                   required=True,
    #                   help='Folder which contains xml files')
    args.add_argument('--txt_folder',
                      type=str,
                      required=True,
                      help='Folder which will save generated txt files')
    args.add_argument('--img_folder',
                      type=str,
                      required=True,
                      help='Extract images from xml folder whos file name is matched.')

    # args.add_argument('--image_folder',
    #                   type=str,
    #                   required=True,
    #                   help='Image folder')                      
    return args.parse_args()


def xml2txt(filefolder, xml_2_txt_folder):
    """
    把 xml 轉txt
    """
    for file in os.listdir(filefolder):
        if not file.startswith('.'):
            xml_src = filefolder + '/' + file
            file_name = file.split('.xml')[0]
            labelXML = minidom.parse(xml_src)

            # 原始信息
            xmins = []
            ymins = []
            xmaxs = []
            ymaxs = []
            tmpArrays = labelXML.getElementsByTagName("xmin")
            for elem in tmpArrays:
                xmins.append(int(elem.firstChild.data))   
            tmpArrays = labelXML.getElementsByTagName("xmax")
            for elem in tmpArrays:
                xmaxs.append(int(elem.firstChild.data))
            tmpArrays = labelXML.getElementsByTagName("ymin")
            for elem in tmpArrays:
                ymins.append(int(elem.firstChild.data))
            tmpArrays = labelXML.getElementsByTagName("ymax")
            for elem in tmpArrays:
                ymaxs.append(int(elem.firstChild.data))

            obj_list = []
            text_list = []
            for i in range(len(xmins)):
                # x1,y1
                text_list.append(xmins[i])
                text_list.append(ymins[i])
                # x2,y2
                text_list.append(xmaxs[i])
                text_list.append(ymins[i])
                # x3,y3
                text_list.append(xmaxs[i])
                text_list.append(ymaxs[i])
                # x4,y4
                text_list.append(xmins[i])
                text_list.append(ymaxs[i])
                # add all
                obj_list.append(text_list)
                text_list = []

            f=open(xml_2_txt_folder + '/' + file_name + '.txt', "w")
            for line in obj_list:
                q = ','.join(map(str, line))
                q += ',0' # label 0 
                _ = f.write(q)
                _ = f.write('\n')#換行 
            f.close()
    return 


def get_image(imagefolder, filefolder2):
    """
    把 txt 對應到的 image複製出來, 算是double check
    """
    txt_list = []        
    for filename in name_list('txt'):
        txt_list.append(filename)
        
    image_list = []        
    for filename in name_list('image'):
        image_list.append(filename)

    matchs = list(set(txt_list).intersection(image_list))
    # print('matchs',matchs)
    if not os.path.exists(filefolder2):
        _ = os.makedirs(filefolder2)
    for match in matchs:
        try:
            _ = shutil.copyfile(imagefolder+ '/' + match + '.jpg', filefolder2 + '/' + match + '.png')
        except:
            _ = shutil.copyfile(imagefolder + '/' + match + '.png', filefolder2 + '/' + match + '.png')
    return 


def name_list(format_name):
    if format_name == 'txt':
        for file in os.listdir(xml_2_txt_folder):
            if not file.startswith('.'):
                filename = re.split('.txt',file)
                # print(filename)
            yield filename[0]
    elif format_name =='image':
        for file in os.listdir(imagefolder):
            if not file.startswith('.'):
                if '.jpg'in file :
                    filename = file.split('.jpg')
                elif '.JPG'in file:
                    filename = file.split('.JPG')
                elif '.png'in file or ('.PNG'in file):
                    filename = file.split('.png')
                elif '.PNG'in file:
                    filename = file.split('.PNG')         
            yield filename[0]
    


args = init_args()

filefolder = './step2_data/xml/'# args.file_folder # xml資料夾
xml_2_txt_folder = args.txt_folder # 轉txt資料夾
imagefolder = './step2_data/jpg/' #args.image_folder  # image資料夾
filefolder2 = args.img_folder # xml的檔名對應到image資料夾的檔案撈出來 存放的資料夾位置


if not os.path.exists(xml_2_txt_folder):
    _ = os.makedirs(xml_2_txt_folder)

try:
    _ = xml2txt(filefolder, xml_2_txt_folder)
    print(' --- Step2: Done with : xml2txt ')
    _ = get_image(imagefolder, filefolder2)
    print(' --- Step2: Done with : get_image ')
    print('[ Step2 Done ]')
except:
    print('[ Step2 Wong ! ] ')
