import os 
from google.genai import types

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_dir: 
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory\n'
    
    if(os.path.isdir(target_file)): 
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    with open(target_file, "w") as f: 
        try:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except:
            return "Error: Cannot write in file '{target_file}'"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write in a python file at file_path the content given",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file that will get written uppon, if the file does not exists, it will create it with its parent directories",
            ),
            "content": types.Schema(
                type=types.Type.STRING, 
                description="Content that will get written in the said file",
            )
        },
        required=["file_path", "content"]
    ),
)
