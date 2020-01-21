import os

os.chdir('videos')

# print(os.getcwd())

for f in os.listdir():
    # print(f)
    # print(os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)

    f_title, f_course, f_num = f_name.split('-')

    f_name = f_name.strip()
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    # print(f_title)
    # print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))#
    new_name = '{}-{}-{}{}'.format(f_num, f_title, f_course, f_ext)
    #print(new_name)
    os.rename(f, new_name)

