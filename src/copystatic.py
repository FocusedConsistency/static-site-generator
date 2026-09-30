import os
import shutil

import os
import shutil

def copy_files_recursive(source_dir, dest_dir):
    for filename in os.listdir(source_dir):
        from_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            os.mkdir(dest_path)
            copy_files_recursive(from_path, dest_path)
