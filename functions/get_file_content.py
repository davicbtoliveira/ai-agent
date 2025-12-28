import os
from config import MAX_CHAR_TO_READ

def get_file_content(working_directory, file_path):
    try:
        wkg_dir_abs_path = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(wkg_dir_abs_path, file_path))

        if os.path.commonpath([wkg_dir_abs_path, target_file]) != wkg_dir_abs_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        f = open(target_file)

        content = f.read(MAX_CHAR_TO_READ)
        
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHAR_TO_READ} characters]'

        return content
    except Exception as e:
        return f"Error: {e}"
