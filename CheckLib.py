import sys, subprocess

def checklib():
    pip_download_ = []
    try:
        import tk
    except ImportError:
        print("tk not found")
        pip_download_.append('tk')

    if not pip_download_ == []:

        try:
            for package in pip_download_:
                print("Installing " + package)
                subprocess.call([sys.executable, "-m", "pip", "install", package, "--user"])
        except:
            print("Installation failed")
            sys.exit(-1)
        subprocess.call([sys.executable, sys.argv[0]])
        sys.exit(0)