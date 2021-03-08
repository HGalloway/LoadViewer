import subprocess
psutilProcess = subprocess.Popen(["pip","install","psutil"], shell=True)
psutilProcess.wait()