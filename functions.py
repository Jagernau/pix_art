import os

def check_directories(in_dir, out_dir):
    """
    Checks the existence of directories 'in_pic' and 'out_pic'.
    If the directories do not exist, creates them.
    """
    try:
        if not os.path.isdir(in_dir):
            os.makedirs(in_dir)
            print(f'Directory "{in_dir}" was successfully created.')

        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
            print(f'Directory "{out_dir}" was successfully created.')
    
    except Exception:
        print("Directories cannot be created.")

def check_in_dir_empty(in_dir):
    """
    Raises a SystemExit if the specified input directory is empty.
    """
    if len(os.listdir(in_dir)) == 0:
        raise FileNotFoundError(f"Directory {in_dir} is empty")
    else:
        pass


