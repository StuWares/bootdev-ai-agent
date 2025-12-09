import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    output_string = "No output produced"
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'

    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(["uv","run", target_file] + args, timeout=30, stdout=True, stderr=True, cwd=working_directory)

        if completed_process.returncode == 0:
            output_string = f'STDOUT: {completed_process.stdout} STDERR: {completed_process.stderr}'
        else:
            output_string = f'STDOUT: {completed_process.stdout} STDERR: {completed_process.stderr} Process exited with code {completed_process.check_returncode}'
        

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    return output_string
