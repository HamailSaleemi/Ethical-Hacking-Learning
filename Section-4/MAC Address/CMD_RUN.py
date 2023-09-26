import subprocess

def run_bash_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        # If you want to capture the output and error messages, you can access them using result.stdout and result.stderr respectively.
        print("Command Successful {0} executed!".format(command))
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}.")
        print("Error message:")
        print(e.stderr)
        return None