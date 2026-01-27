import os 
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try: 
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        output_str = ""

        if not valid_target_dir: 
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file): 
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if target_file.split(".")[-1] != "py": 
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args != None: 
            command.extend(args)

        process = subprocess.run(command, text=True, capture_output=True, timeout=30)

        if process.check_returncode() != 0: 
            output_str += f"Process exited with code {process.check_returncode()}\n"

        if process.stdout == "" and process.stderr == "":
            output_str += "No output produced\n"

        output_str += f"STDOUT: {process.stdout}\nSTDERR: {process.stderr}\n"
            
        return output_str
    
    except Exception as e:
        return f"Error: executing Python file: {e}"