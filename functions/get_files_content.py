import os

def get_files_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path, file_path))

        valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path

        if valid_target_file == False:
            return (f'Error: Cannot read "{file_path}" as it is outside the working directory')
        
        elif os.path.isfile(target_file) == False:
            return (f'Error: File not found or is not a regular file: "{file_path}"')     
        
        f = open(target_file)
        file_contents = f.read(10000)

        if f.read(1):
            file_contents += f'[...File "{file_path}" truncated at 10000 characters]'



        return file_contents

    except Exception as e:
        return f"Error: {e}"