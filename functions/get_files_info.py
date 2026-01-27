import os 
def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir: 
        return print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n')
    
    if not os.path.isdir(target_dir): 
        return print(f'Error: "{directory}" is not a directory\n')
    
    for item in os.listdir(target_dir):

        try: 
            item_path = os.path.join(target_dir, item)
            print(f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n")
        except:
            return f'Error: cannot list items in the target directory\n'
