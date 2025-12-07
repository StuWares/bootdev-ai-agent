import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    #print(f"target file: {target_file}")

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(target_file, "r") as f:
        all_content = f.read()
        num_chars = len(all_content)
        file_content_string = all_content[:MAX_CHARS]
        if num_chars > MAX_CHARS:
            #print(f'File {file_path} is length {num_chars}')
            return f'{file_content_string} [...File "{file_path}" truncated at {MAX_CHARS} characters]'
        #print(f"finished. File {file_path} is length {num_chars}")
        return file_content_string

# Below is for quick debugging! 
#get_file_content("calculator", "main.py")
    