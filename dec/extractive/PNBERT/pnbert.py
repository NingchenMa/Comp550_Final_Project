import os

# Absolute path of a file
old_name = r"0.dec"
new_name = r"loopsum_0.ref"

for index in range(50):
    # Absolute path of a file
    old_name = str(index)+".dec"
    new_name = "pnbert"+str(index)+".dec"
    # Renaming the file
    os.rename(old_name, new_name)
    
