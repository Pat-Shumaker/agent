import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))

        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

        if valid_target_dir == False:
            return (f'Error: Cannot list "{directory}" as it is outside the working directory')
        
        elif os.path.isdir(target_dir) == False:
            return (f'Error: Cannot list "{directory}" is not a directory')
        
        target_dir_contents = os.listdir(target_dir)
        
        contents_info = ""

        for item in target_dir_contents:
            item_path = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_path)
            item_is_dir = os.path.isdir(item_path)

            contents_info += f"- {item}: file_size={item_size}, is_dir={item_is_dir}\n"
        
        return contents_info

    except Exception as e:
        return f"Error: {e}"
