import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()
import cv2
from modules.utils import load_yaml, save_yaml
from glob import glob
from tqdm import tqdm
import shutil

if __name__ == '__main__':
    # Load Config
    prj_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(prj_dir, 'config', 'preprocess.yaml')
    config = load_yaml(config_path)

    train_dir = config['train_dir']
    test_dir = config['test_dir']
    resize_shape = (config['resize_width'], config['resize_height'])

    # Load Original Dataset
    train_x_images = sorted(glob(f'{train_dir}/x/*.jpg'))
    train_y_images = sorted(glob(f'{train_dir}/y/*.png'))
    test_x_images = sorted(glob(f'{test_dir}/x/*.jpg'))

    print(f'train | num x : {len(train_x_images)}, num y : {len(train_y_images)}')
    print(f'test | num x : {len(test_x_images)}')

    # Make directory for saving resized images
    serial_num = config['serial_num']
    save_dir = f'{prj_dir}/data/{serial_num}'
    if os.path.isdir(save_dir):
        shutil.rmtree(save_dir)
    os.makedirs(f'{save_dir}/train/x', exist_ok=True)
    os.makedirs(f'{save_dir}/train/y', exist_ok=True)
    os.makedirs(f'{save_dir}/test/x', exist_ok=True)
    save_yaml(f'{save_dir}/preprocess.yaml', config)

    print('Start resizing the train dataset')

    # for i in tqdm(range(len(train_x_images))):
    for i in tqdm(range(10)):
    

        train_x, train_y = train_x_images[i], train_y_images[i]

        image = cv2.imread(train_x, cv2.IMREAD_COLOR)
        image_f_name = os.path.basename(train_x)
        resize_image = cv2.resize(image, dsize=resize_shape)
        cv2.imwrite(f'{save_dir}/train/x/{image_f_name}',resize_image)

        del image, image_f_name, resize_image

        mask = cv2.imread(train_y, cv2.IMREAD_GRAYSCALE)
        mask_f_name = os.path.basename(train_y)
        resize_mask = cv2.resize(mask, dsize=resize_shape)
        cv2.imwrite(f'{save_dir}/train/y/{mask_f_name}',resize_mask)

        del mask, mask_f_name, resize_mask

    print('Start resizing the test dataset')

    # for i in tqdm(range(len(test_x_images))):
    for i in tqdm(range(10)):
    
        test_x = test_x_images[i]

        image = cv2.imread(test_x, cv2.IMREAD_COLOR)
        image_f_name = os.path.basename(test_x)
        resize_image = cv2.resize(image, dsize=resize_shape)
        cv2.imwrite(f'{save_dir}/test/x/{image_f_name}',resize_image)

        del image, image_f_name, resize_image

    