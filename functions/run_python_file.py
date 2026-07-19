import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
        try:
            abs_path = os.path.abspath(working_directory)
            abs_file_path = os.path.normpath(os.path.join(abs_path, file_path))

            valid_abs_file_path = os.path.commonpath([abs_path, abs_file_path]) == abs_path

            if valid_abs_file_path == False:
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
            elif os.path.isfile(abs_file_path) == False:
                return f'Error: "{file_path}" does not exist or is not a regular file'
            
            elif file_path.split(".")[1] != "py":
                 return f'Error: "{file_path}" is not a Python file'
            
            command = ["python", abs_file_path]

            if args:
                command.extend(args)

            run_command = subprocess.run(command, capture_output=True, text=True, timeout=30)

            cmd_output = ""
            cmd_stdout = run_command.stdout
            cmd_stderr = run_command.stderr 

            if run_command.returncode != 0:
                 cmd_output += f'Process exited with code {run_command.returncode}'

            elif cmd_stderr == "" and cmd_stdout == "":
                 cmd_output += "No output produced"

            else:
                 if cmd_stdout != "":
                    cmd_output += f"STDOUT: {cmd_stdout}"
                 
                 if cmd_stderr != "":
                    cmd_output+= f"\nSTDERR: {run_command.stderr}"

            return cmd_output

        except Exception as e:
            return f"Error: executing Python file {e}" 