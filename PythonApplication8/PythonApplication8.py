import os
from tqdm import tqdm
from xml.dom.minidom import Document


def make_xml_from_txt(path, save_path):
    """把标准txt标签文件转化为标准xml格式标签文件

    :param path: txt文件所在路径，以'\\'或者'/'结尾
    :param save_path: 生成的xml文件路劲，以'\\'或者'/'结尾
    :return: 无返回
    """
    path = 'C:\\Users\\flash\\source\\repos\\PythonApplication8\\PythonApplication8\\100030101.txt'
    save_path = 'C:\\Users\\flash\\Desktop\\std\\'
    files = os.listdir(path)
    n = 0
    for file_name in tqdm(files):
        n += 1
        # print('begin :', n)
        img_id = file_name.split('.')[0]
        lines = []
        for line in open(path + file_name):
            lines.append(line)

        doc = Document()  # 创建DOM文档对象
        annotation = doc.createElement('annotation')  # 创建根元素

        folder = doc.createElement('folder')
        folder.appendChild(doc.createTextNode('VOC'))
        annotation.appendChild(folder)

        filename = doc.createElement('filename')
        filename.appendChild(doc.createTextNode(img_id))
        annotation.appendChild(filename)

        object_num = doc.createElement('object_num')
        object_num.appendChild(doc.createTextNode(str(len(lines))))
        annotation.appendChild(object_num)

        size = doc.createElement('size')
        width = doc.createElement('width')
        width.appendChild(doc.createTextNode(str(548)))
        height = doc.createElement('height')
        height.appendChild(doc.createTextNode(str(408)))
        depth = doc.createElement('depth')
        depth.appendChild(doc.createTextNode(str(3)))
        size.appendChild(width)
        size.appendChild(height)
        size.appendChild(depth)
        annotation.appendChild(size)

        for line in lines:
            lines_list = line.split(' ')
            x = int(float(lines_list[1]))
            y = int(float(lines_list[2]))
            width = int(float(lines_list[3]))-int(float(lines_list[1]))
            height = int(float(lines_list[4]))-int(float(lines_list[2]))
            c = int(float(lines_list[0])) # 种类

            object_d = doc.createElement('object')
            name = doc.createElement('name')
            name.appendChild(doc.createTextNode(str(c)))
            object_d.appendChild(name)
            difficult = doc.createElement('difficult')
            difficult.appendChild(doc.createTextNode(str(0)))
            object_d.appendChild(difficult)
            pose = doc.createElement('pose')
            pose.appendChild(doc.createTextNode('Frontal'))
            object_d.appendChild(pose)
            truncated = doc.createElement('truncated')
            truncated.appendChild(doc.createTextNode(str(0)))
            object_d.appendChild(truncated)
            bndbox = doc.createElement('bndbox')
            xmin = doc.createElement('xmin')
            xmin.appendChild(doc.createTextNode(str(x)))
            ymin = doc.createElement('ymin')
            ymin.appendChild(doc.createTextNode(str(y)))
            xmax = doc.createElement('xmax')
            xmax.appendChild(doc.createTextNode(str(x + width)))
            ymax = doc.createElement('ymax')
            ymax.appendChild(doc.createTextNode(str(y + height)))
            bndbox.appendChild(xmin)
            bndbox.appendChild(ymin)
            bndbox.appendChild(xmax)
            bndbox.appendChild(ymax)
            object_d.appendChild(bndbox)
            annotation.appendChild(object_d)
        doc.appendChild(annotation)
        f = open(save_path + img_id + '.xml', 'w')
        # print(savePath + img_id + '.xml', 'w')
        doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()


def make_xml_from_output_txt(path, save_path):
    """ 把以c和i分隔的字符串的txt文件转化为标准xml格式标签文件

    :param path: txt文件路径, *.txt
    :param save_path: 生成的xml文件路劲，以'\\'或者'/'结尾
    :return: 无返回
    """
    n = 0
    for line in tqdm(open(path)):
        n += 1
        print('begin :', n)
        picName = line.split(' ')[1].split('c')  # 原图名称以C间隔标签
        P_name = picName[0]

        doc = Document()  # 创建DOM文档对象
        annotation = doc.createElement('annotation')  # 创建根元素

        folder = doc.createElement('folder')
        folder.appendChild(doc.createTextNode('VOC'))
        annotation.appendChild(folder)

        filename = doc.createElement('filename')
        filename.appendChild(doc.createTextNode(P_name))
        annotation.appendChild(filename)

        object_num = doc.createElement('object_num')
        object_num.appendChild(doc.createTextNode(str(len(picName) - 1)))
        annotation.appendChild(object_num)

        size = doc.createElement('size')
        width = doc.createElement('width')
        width.appendChild(doc.createTextNode(str(544)))
        height = doc.createElement('height')
        height.appendChild(doc.createTextNode(str(416)))
        depth = doc.createElement('depth')
        depth.appendChild(doc.createTextNode(str(3)))
        size.appendChild(width)
        size.appendChild(height)
        size.appendChild(depth)
        annotation.appendChild(size)

        for j in range(1, len(picName)):

            x = int(picName[j].split('i')[1])
            y = int(picName[j].split('i')[2])
            width = int(picName[j].split('i')[3])
            height = int(picName[j].split('i')[4])
            c = int(picName[j].split('i')[0])
         
            object_d = doc.createElement('object')
            name = doc.createElement('name')
            name.appendChild(doc.createTextNode(str(c)))
            object_d.appendChild(name)
            difficult = doc.createElement('difficult')
            difficult.appendChild(doc.createTextNode(str(0)))
            object_d.appendChild(difficult)
            pose = doc.createElement('pose')
            pose.appendChild(doc.createTextNode('Frontal'))
            object_d.appendChild(pose)
            truncated = doc.createElement('truncated')
            truncated.appendChild(doc.createTextNode(str(0)))
            object_d.appendChild(truncated)
            bndbox = doc.createElement('bndbox')
            xmin = doc.createElement('xmin')
            xmin.appendChild(doc.createTextNode(str(x)))
            ymin = doc.createElement('ymin')
            ymin.appendChild(doc.createTextNode(str(y)))
            xmax = doc.createElement('xmax')
            xmax.appendChild(doc.createTextNode(str(x + width)))
            ymax = doc.createElement('ymax')
            ymax.appendChild(doc.createTextNode(str(y + height)))
            bndbox.appendChild(xmin)
            bndbox.appendChild(ymin)
            bndbox.appendChild(xmax)
            bndbox.appendChild(ymax)
            object_d.appendChild(bndbox)
            annotation.appendChild(object_d)
        doc.appendChild(annotation)
        f = open(save_path + P_name + '.xml', 'w')
        doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()

path = 'C:\\Users\\flash\\Desktop\\100030104.txt'
save_path = 'C:\\Users\\flash\\Desktop\\std\\'
make_xml_from_output_txt(path,save_path)