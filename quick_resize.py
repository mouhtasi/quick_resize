from PIL import Image
import sys

def resize(original_path, imgnum):
    '''Resize an image and save in the same same path as the source.'''
    img = Image.open(original_path)
    
    max_width = 250    # the width of the resized image will not exceed this
    max_height = 250   # the height of the resized image will not exceed this
    
    img.thumbnail((max_width, max_height), Image.ANTIALIAS)
   
    temp_path = original_path[::-1]
    
    for c in temp_path:
        if(c == '\\'):
            temp_path = temp_path[::-1]
            break
        else:
            temp_path = temp_path[1:]
    print imgnum;
            
    if(imgnum != 0):
        newpath = temp_path + 'cover' + str(imgnum) + '.jpg'
    else:
        newpath = temp_path + 'cover.jpg'
    img.save(newpath, quality=85)
    

if __name__ == '__main__':
    imgnum = 0
    ctr = 1
    
    while ctr < len(sys.argv):
        resize(sys.argv[ctr], imgnum)
        ctr += 1
        imgnum += 1
        