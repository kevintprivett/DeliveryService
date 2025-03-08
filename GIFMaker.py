from PIL import Image
im_list = []

im1 = Image.open("test0000.png")

for i in range(5):
    file_number_string = "{:04d}".format(i)
    im_list.append(Image.open(f'test{file_number_string}.png'))

for i in range(15):
    im_list.append(Image.open('test0004.png'))

im1.save("out.gif", save_all=True,
         append_images=im_list,
         duration=200, loop=0)
