import os
def get_files_info(working_directory, directory="."):

    full_path = os.path.join(working_directory, directory)
    dir_abs = os.path.abspath(full_path)
    output_string = ""

    #print(f"full path: {full_path}")
    #print(f"Working dir: {working_directory}")
    #print(f"dir abs : {dir_abs}")

    # Ensure that the target directory is within the working directory - prevents the LLM from going rogue!
    if working_directory not in dir_abs:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if not os.path.isdir(dir_abs):
        return(f'Error: "{directory}" is not a directory')
    
    try:
        dir_list = os.listdir(dir_abs)
        for file in dir_list:
            output_string += f"- {file}: file_size={os.path.getsize(os.path.join(dir_abs,file))}, is_dir={os.path.isdir(os.path.join(dir_abs,file))}\n"
        
        #print(output_string)
        return output_string
    except Exception as e:
        return f"Error listing files: {e}"

get_files_info("calculator", "pkg")