from PIL import Image
import os
def resize_multiple_images(src_path, dst_path):
    
    for filename in os.listdir(src_path):
        try:
            img = Image.open(src_path+filename)
            new_img = img.resize((120, 65))
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
            new_img.save(dst_path+filename)
            print('Resized and saved {} successfully.'.format(filename))
        except:
            continue
src_path = '/Users/hyuno/LG_webos/train_dataset/wallet/'
dst_path = '/Users/hyuno/LG_webos/train_dataset/wallet/'
resize_multiple_images(src_path, dst_path)
