import numpy as np
import pandas as pd
import traceback
import os
from PIL import Image

def processImages(dirpath: str) -> np.array:
  '''
  This function accepts a path to a directory of png files containing human lung tissue data at a certain resolution. Returns a dataframe containing data at filepath. Creates a lung.csv file under the data folder
  '''
  
  # Check whether filepath exists, if not, return
  dir = []
  try:
    dir = os.listdir(dirpath)
  except Exception:
    traceback.print_exc()
    return None
  
  # First image to compress into the first row 
  firstImage = Image.open(dirpath + "/" + "1.png")
  
  # Read image into np array and sum the columsn and divide by 255
  lungData = np.asarray(firstImage).sum(axis=0) / 255
  firstImage.close()
  
  # 2nd to Nth image in array to compress into 2nd to Nth row
  for i in range(2, len(dir)):
    with Image.open(dirpath + "/" + str(i) + ".png") as image:
      imageArray = np.asarray(image)
      newSlice = imageArray.sum(axis=0) / 255
      lungData = np.vstack((lungData, newSlice))
  
  ## Map to 2D image for thickness visualization
  # Image.fromarray(lungData).show()
  
  pd.DataFrame(lungData).to_csv("../data/lung.csv")
  
  return lungData

# processImages("../data/images")