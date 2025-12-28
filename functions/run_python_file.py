import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file with the given arguments, if the file exists and really is a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the python file you want to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="The array of itens to give as argument on the command to run the python file",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="The itens of args array"
                )
            ),
        },
        required=["file_path"]
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        wkg_dir_abs_path = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(wkg_dir_abs_path, file_path))

        if os.path.commonpath([wkg_dir_abs_path, target_file]) != wkg_dir_abs_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args != None:
            command.extend(args)

        cp = subprocess.run(command, stderr=True, stdout=True, text=True, timeout=30)
        
        result = f"STDOUT: {cp.stdout}\nSTDERR: {cp.stderr}"

        if cp.returncode != 0:
            result += f'\nProccess exited with code {cp.returncode}'

        if cp.stderr == None or cp.stdout == None:
            result += f'\nNo output produced'

        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"
