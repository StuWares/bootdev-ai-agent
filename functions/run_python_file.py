import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'

    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(["uv","run", target_file] + args, timeout=30, capture_output=True, text=True, cwd=working_directory)
        output = []
        
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
            
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")
        
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        if output:
            output_string = "\n".join(output)
        else:
            output_string = "No output produced."

        return output_string

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
name="run_python_file",
description="Executes a specified Python file within the working directory and returns the output from the interpreter.",
parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "file_path": types.Schema(
            type=types.Type.STRING,
            description="The Python file to execute, relative to the working directory.",
        ),
        "args": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(
                type=types.Type.STRING,
                description="Optional arguments to pass to the Python file."
            ),
            description="Optional arguments to pass to the Python file."      
        ),
    },
    required=["file_path"],
),
)    
