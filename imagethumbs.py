import os
from multiprocessing import Pool, Process
from PIL import Image
import time

SAVE_DIRECTORY = 'thumbs'

def get_image_paths(folder):
    return (os.path.join(folder, f)
            for f in os.listdir(folder)
            if 'JPG' in f)

def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail((75, 75), Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, 'thumbs', fname)
    im.save(save_path)


def create_thumbnail_child_process(filename_list):
    for image in filename_list:
        create_thumbnail(image)


if __name__ == '__main__':
    folder = "F:\\000DCIM\\104APPLE"
    thumbs_folder = "F:\\000DCIM\\104APPLE\\thumbs"

    if not os.path.exists(thumbs_folder):
        os.mkdir(os.path.join(folder, 'thumbs'))

    images = get_image_paths(folder)

    """
    #for loop
    #48.64235806465149
    time_begin = time.clock()
    for image in images:
        print(image)
        create_thumbnail(image)
    time_end = time.clock()
    print(time_end - time_begin)
    """

    #pool
    #796
    #7.114084243774414
    time_begin = time.clock()

    pool = Pool()
    pool.map(create_thumbnail, images)
    pool.close()
    pool.join()

    time_end = time.clock()
    print(time_end - time_begin)


    #pool
    for i in range(4, 33):
        time_begin = time.clock()

        pool = Pool(i)
        pool.map(create_thumbnail, images)
        pool.close()
        pool.join()

        time_end = time.clock()
        print(i)
        print(time_end - time_begin)
        print("****")





    """
    #process
    #784
    #16.6739182472229
    images_list = list(images)

    time_begin = time.clock()

    processes = []
    step = 49
    start = 0
    for i in range(16):
        stop = start + step
        p_name = "process_no" +str(i)
        p = Process(name = p_name, target = create_thumbnail_child_process, args = (images_list[start:stop], ) )
        p.start()
        processes.append(p)
        start = stop

    for p in processes:
        p.join()

    time_end = time.clock()
    print(time_end - time_begin)

    """

#end
