import subprocess
import psutil

BoxSize = 40

class LoadViewer:
    
    def PrintInformation(Information):
        EmptySpace = BoxSize - len("* " + Information + " *")
        print("* " + Information + " "*EmptySpace + " *")

    def SeperatingLine():
        Count = 1

        print("*", end="")
        while(Count != BoxSize-1):
            print("-", end="")
            Count += 1
        print("*")

    def InitBox(Length):
        box = "\n".join(["*"*(2*Length)] + ["*%s*" % (" "*(2*Length-2))]*(Length-2) + ["*"*(int(Length>1)*2*Length)])
        print("*"*Length)
        
        CPUInformation.CPUInfo()

        print("*"*Length)

class CPUInformation:
    def GetCPUName():
        CPUName = subprocess.check_output(["wmic", "cpu", "get", "name"], shell=True)
        return CPUName

    def CPUInfo():
        SystemCPUUsage = "CPU Usage: " + str(psutil.cpu_percent(interval=1))
        CMDCPUName = subprocess.check_output(["wmic", "cpu", "get", "name"], shell=True)
        CPUName = "CPU Name: " + str(CPUInformation.GetCPUName())
        CPUFrequency = psutil.cpu_freq()
        MaxCPUFrequency = "Max CPU Frequency: " + str(CPUFrequency.max)
        CurCPUFrequency = "Current CPU Frequency: " + str(CPUFrequency.current)
        


        TitleLength = len("* CPU Information:" + " *")
        EmptySpace = BoxSize - TitleLength
        print("* CPU Information:" + " "*EmptySpace + " *")
        LoadViewer.SeperatingLine()
        LoadViewer.PrintInformation(SystemCPUUsage)
        LoadViewer.PrintInformation(CPUName)
        LoadViewer.PrintInformation(MaxCPUFrequency)
        LoadViewer.PrintInformation(CurCPUFrequency)
        LoadViewer.SeperatingLine()


LoadViewer.InitBox(BoxSize)