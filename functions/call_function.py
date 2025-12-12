from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    working_dir = "./calculator"
    function_args = ({**function_call_part})
    function_args.pop("name")
    #print(f"Function args: {function_args}")
    function_name = function_call_part["name"]


    function_dict = {
        "get_files_info" : get_files_info,
        "get_file_content" : get_file_content,
        "run_python_file" : run_python_file,
        "write_file" : write_file,
    }

    if function_name not in function_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    

    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    func_to_call = function_dict[function_name]
    function_result = func_to_call(working_dir, **function_args)


    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )


    

    



    return