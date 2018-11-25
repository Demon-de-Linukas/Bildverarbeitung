#############################
##
## montagepic.py
## Append sub pictures into one entire picture
##
##
#############################
import os
from PIL import Image



def montage(images, w_sub, h_sub, step):
    """
   Append Picture one after another, till all the picture in the folder ars used.

    Parameters
    ----------
    :param images: :class:`list`
        Input List of images.

    :param w_sub: Width of the sub picture.

    :param h_sub: Hight of the sub picture.

    :param step: Number of sub picture in one row or one column.

    Returns
    -------
    :returns: target : :class:`.PIL.Image.Image` : Generated picture set.

    """
    target = Image.new('RGB', (w_sub*step, h_sub*step))
    left = 0
    right = w_sub
    for i in range(len(images)):
        top=(i//step)*h_sub
        target.paste(images[i], (left, top, right, top+h_sub))
        if(i//step < (i+1)//step):#Check if this row is done
            left = 0#Reset the position in a row
            right = w_sub
        else: #Next picture
            left += w_sub
            right += w_sub
    quality_value = 100
    return target


def appendpics(pathofimg, w_sub, h_sub, step):
    """
       Append Picture one after another and save under a folder which will be new created to the same path of the images.

        Parameters
        ----------
        :param pathofimg: Path of the images

        :param w_sub: Width of the sub picture.

        :param h_sub: Hight of the sub picture.

        :param step: Number of sub picture in one row or one column.

        """
    num = 0
    dirlist = []
    images = []  # images in each folder
    for root, dirs, fileswer in os.walk(pathofimg):
        if len(dirs)!= 0:
            for dir in dirs:
                dirlist.append(dir)
                for rooert, dirwerwes, files in os.walk(pathofimg+'/'+dir):
                    for file in files:
                        if(file.endswith('.png')):
                            images.append(Image.open(pathofimg+'/'+dir+'/'+file))
                    if(len(images)==81):
                        break
                target = montage(images, w_sub, h_sub, step)
                target.save(pathofimg +'/'+ dir + '.png', quality=100)
        else:
            dir = 'Generated'
            for file in fileswer:
                if (file.endswith('.png')):
                    images.append(Image.open(pathofimg +'/'+ file))
            target1 = montage(images, w_sub, h_sub, step)
            savepath = pathofimg +'/'+ 'generated'
            os.makedirs(savepath)
            target1.save(savepath +'/'+ dir + '.png', quality=100)


appendpics(pathofimg = "",
            w_sub = 625,
            h_sub = 434,
            step = 15)
