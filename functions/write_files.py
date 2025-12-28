import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content on the file specified by the given path if it exists",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file you want to write the content",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the content to be write to the specified file"
            )
        },
        required=["file_path", "content"]
    ),
)

def write_file(working_directory, file_path, content):
    try:
        wkg_dir_abs_path = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(wkg_dir_abs_path, file_path))

        if not os.path.isdir(os.path.dirname(target_file)):
            os.makedirs(target_file, exist_ok=True)

        if os.path.commonpath([wkg_dir_abs_path, target_file]) != wkg_dir_abs_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
 
