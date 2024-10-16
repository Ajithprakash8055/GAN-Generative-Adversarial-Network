# import opendatasets as od
# dataset_url = 'https://www.kaggle.com/datasets/jessicali9530/celeba-dataset'
# od.download(dataset_url)


import os
import random

# Path to the folder containing images
folder_path = '/home/madmax/GAN/celeba-dataset/img_align_celeba'

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg', '.bmp', '.gif'))]

# Check if there are more than 100 images
if len(image_files) > 2000:
    # Randomly select 100 images to keep
    images_to_keep = random.sample(image_files, 2000)
    
    # Delete the rest of the images
    for image in image_files:
        if image not in images_to_keep:
            os.remove(os.path.join(folder_path, image))
    print(f"Deleted")
else:
    print("Folder contains 100 or fewer images. No images were deleted.")