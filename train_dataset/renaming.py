#renaming
import os


def rename_multiple_files(path, obj):
    i = 0
    for filename in os.listdir(path):
        print(path+filename, '->', path+str(obj)+str(i)+'.jpg')
        os.rename(path+'/'+filename, path+'/'+str(obj)+str(i)+'.jpg')
        i += 1


path = '/Users/hyuno/LG_webos/train_dataset/wallet'
obj = 'wallet'

rename_multiple_files(path, obj)
