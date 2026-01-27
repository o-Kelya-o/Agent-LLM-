import os 
import subprocess
from google.genai import types

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
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file from a file_path and optionnal args, provides the execution of that said file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file that will get executed",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY.STRING, 
                description="List of arguments (type string) that will be called upon executing the file (default value is None)",
            )
        },
        required=["file_path"]
    ),
)
