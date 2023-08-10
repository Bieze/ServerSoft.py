import os

class Downloader:
    def __init__(self):
        self.DownloadPaper()
    
    def DownloadPaper(self):
        """Downloads the latest papermc.jar"""
    
        os.system("git clone https://github.com/PaperMC/Paper.git")
        os.chdir(f"{os.getcwd()}/Paper")
        os.system("./gradlew applyPatches")
        os.system("./gradlew createReobfBundlerJar")
        print("The built server can be found in the Paper/build/libs directory!")
        