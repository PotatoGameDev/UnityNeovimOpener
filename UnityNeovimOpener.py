import subprocess
import sys
import os

def is_neovim_running(pipe_name):
    return os.path.exists(pipe_name)

def open_file_in_neovim(pipe_name, file_path, line_number):
    try:
        open_command = ["nvim", "--server", pipe_name, "--remote", file_path]
        subprocess.run(open_command, check=True)

        # Second command to jump to line
        goto_line_command = ["nvim", "--server", pipe_name, "--remote-send", f":{line_number}G\r"]
        subprocess.run(goto_line_command, check=True)
    except Exception as e:
        print(f"Error occurred while opening file in Neovim: {e}")
        return False
    return True

def start_and_open_file_in_neovim(pipe_name, file_path, line_number):
    try:
        # Start Neovim and open the file
        command = ["nvim", "--listen", pipe_name, file_path, f"+{line_number}"]
        subprocess.run(command, check=True)
    except Exception as e:
        print(f"Failed to start Neovim: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python nvim_open.py <file_path> <line_number>")
        return

    file_path = sys.argv[1]
    line_number = sys.argv[2]

    pipe_name = r'\\.\pipe\MyUnityProjectNVIM'

    if not is_neovim_running(pipe_name):
        start_and_open_file_in_neovim(pipe_name, file_path, line_number)
    else:
        if not open_file_in_neovim(pipe_name, file_path, line_number):
            print("Failed to open file in existing Neovim instance.")

if __name__ == "__main__":
    main()

