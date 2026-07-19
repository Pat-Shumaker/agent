import os

def write_file(working_directory: str, file_path: str, content: str) -> str:    
        try:
            abs_path = os.path.abspath(working_directory)
            target_file = os.path.normpath(os.path.join(abs_path, file_path))

            valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path

            if valid_target_file == False:
                return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
            elif os.path.isdir(target_file) == True:
                return (f'Error: Cannot write to "{file_path}" as it is a directory')
            
            os.makedirs(abs_path, exist_ok=True)

            with open(target_file, "w") as f:
                f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        except Exception as e:
            return f"Error: {e}"