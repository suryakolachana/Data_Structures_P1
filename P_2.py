import os 
arr = []
arr1 = [] 
def find_files(suffix,path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == '':
      return
    
    if path == '':
      return
    
    if os.path.isfile(path):
         if path.endswith(suffix):
           filepath = os.path.join(path)
           arr1.append(filepath)
           return arr1
    else:
        directory = os.path.dirname(path)

        if os.path.isdir(directory) is not True:
            return

        l = os.listdir(directory)

        for d in l:
            if os.path.isdir(directory + '/' + d):
                find_files(suffix, os.path.join(directory + '/',d) + '/')
            else:
                if os.path.isfile(directory + '/' + d):
                    if d.endswith(suffix):
                        filepath = os.path.join(directory + '/',d)
                        arr.append(filepath)
        
        if len(arr) == 0:
            return None

    return arr 

def main():
 print(find_files(".c","c:/Users/"))  # Directory path
 print(find_files(".c","c:/Users/vamsi/a.c"))  # Exact filepath
 print(find_files(".c",""))  # empty path 
 print(find_files(".c","p:/")) # Invalid path

if __name__ == "__main__":
  main()

