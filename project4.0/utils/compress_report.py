# 压缩文件
import os
import zipfile


def zipDir(dirpath,outFullName):
    # dirpath为需要导出的文件夹路径
    # outFullName为导出的zip压缩包的路径（含压缩包名称）
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标根路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')
        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()
# zipDir(r"C:\Users\24113\ldproject\project3 .0\result",r"C:\Users\24113\ldproject\project3 .0\result.zip")