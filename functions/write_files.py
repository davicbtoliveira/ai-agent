import os

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
 
