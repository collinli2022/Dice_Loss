import os
import nibabel as nib


def openImage(fp):
    """
    Open up nifty image and convert to numpy arrays

    Paramaters
    ----------
    fp: string
        The file path to the nifty image

    Returns
    ----------
    img: numpy array
    """
    if (not fp) or ('nii' not in fp):
        return
    
    return nib.load(fp).get_fdata()

def organizeFiles(fp):
    """
    Organize nifty files into array
    
    Parameters
    ----------
    fp: string
        The file path to the folder containing nifty images

    Returns
    ----------
    arr: array of file paths to numpy images
    """

    arr = []
    for f in os.listdir(fp):
        if 'nii' in f:
            arr.append(os.path.join(fp, f))
    return arr

def organizeFolders(fp):
    """
    Organize folders into array
    
    Paramaters
    ----------
    fp: string
        The file path to the folder containing nifty images

    Returns
    ----------
    arr: array of file paths to folders
    """

    print('DEBUG: list directories -', os.listdir(fp))

    arr = []
    for f in os.listdir(fp):
        if os.path.isdir(os.path.join(fp, f)):
            arr.append(os.path.join(fp, f))
    return arr
