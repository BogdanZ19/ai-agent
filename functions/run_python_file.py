import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_dir_abs = os.path.abspath(working_directory)
    file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    if os.path.commonpath([file_abs, working_dir_abs]) != working_dir_abs:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_abs):
        return f'Error: File "{file_path}" not found.'
        
    if not file_abs.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cmd = ["python3", file_abs] + args
        result = subprocess.run(cmd, timeout=30, capture_output=True, cwd=working_directory)           
    
        if result.stdout is None:
            return "No output produced"

        return_message = f'STDOUT: {result.stdout} STDERR:{result.stderr}'
        if result.returncode != 0:
            return_message += result.returncode
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    return return_message