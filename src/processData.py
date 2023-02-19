import pandas as pd
import traceback
import sys

def processData(filepath: str) -> pd.DataFrame:
  '''
  This function accepts a filepath to a csv file containing human
  tissue data at a certain resolution
  '''
  
  # Check whether filepath exists, if not, kill program
  try:
    data = pd.read_csv(filepath)
  except Exception:
    traceback.print_exc()
    sys.exit(0)
    
  return data