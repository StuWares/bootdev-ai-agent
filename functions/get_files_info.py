import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, directory)
    dir_abs = os.path.abspath(full_path)
    output_string = ""


    # Ensure that the target directory is within the working directory - prevents the LLM from going rogue!
    if not dir_abs.startswith(working_dir_abs):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if not os.path.isdir(dir_abs):
        return(f'Error: "{directory}" is not a directory')
    
    try:
        dir_list = os.listdir(dir_abs)
        for file in dir_list:
            output_string += f"- {file}: file_size={os.path.getsize(os.path.join(dir_abs,file))}, is_dir={os.path.isdir(os.path.join(dir_abs,file))}\n"
        
        return output_string
    except Exception as e:
        return f"Error listing files: {e}"
    
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
