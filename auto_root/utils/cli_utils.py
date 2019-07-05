import subprocess


def run_console_command(command):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE, shell=True)
    proc.wait()
    return proc.stdout.read()
