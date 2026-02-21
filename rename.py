import os
import fileinput

OLD = "cljtempl"
NEW = "stratchpad"

def rename_paths(root_dir):
    # Rename files and dirs bottom-up to avoid path issues
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for name in filenames + dirnames:
            if OLD in name:
                old_path = os.path.join(dirpath, name)
                new_name = name.replace(OLD, NEW)
                new_path = os.path.join(dirpath, new_name)
                os.rename(old_path, new_path)

def replace_in_file(file_path):
    try:
        with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(OLD, NEW), end='')
        os.remove(file_path + '.bak')
    except UnicodeDecodeError:
        pass  # skip binary files

def replace_in_contents(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            replace_in_file(filepath)

if __name__ == "__main__":
    ROOT_DIR = "."  # or specify your template dir
    rename_paths(ROOT_DIR)
    replace_in_contents(ROOT_DIR)
