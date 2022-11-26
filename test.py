import os
import sys
import re

if __name__ == "__main__":
    for (root, dirs, files ) in os.walk('test'):
        match_files = [f for f in files if re.search(r'.*\.cpp$', f)]
        for f in match_files:
            path = os.path.join(root, f)
            
            ret_value = os.system("python main.py " + path)
            if(ret_value != 0):
                print("failed: " + path)
                sys.exit(1)