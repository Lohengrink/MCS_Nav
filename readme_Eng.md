# fid2Nav in Window
## Introduction
- "fid2Nav_in_Window" (hereinafter referred to as f2n) is a small tool written in python. Its function is to convert the file format of fid to the file format of nav. At the same time, in the fid file, f2n can figure out where the fid has a skip number, or the firing rate is irregular. (Note: Both of them are in text format, only the extension and content arrangement are different.)

- If python has not been installed, it is recommended to install python and related software by referring to the following methods. (See ## Software Installation Requirements)

<!-- - 如果已經安裝了python，那麼您可以試試直接滑鼠左鍵兩下run.bat這個檔案。理論上應該就可以執行。 -->

## How to operate the tool, f2n?
1. For input folder: You can put the fid file which need to be converted into this folder. The program will read the file with the extension ".fid" and convert it. Supports transferring multiple fid files in one execution. If the extension is not fid, it will not be converted. (By default, a demo123.fid file has been stored as an example file)

2. For output folder: The converted nav file will be stored here. If you don't have this folder, you can create it by yourself. (Note: the name must be "output".) Alternatively, the program will create it by itself when it is excuted for the first time.

3. For source_code folder：This folder stores the source code.If there is a need for customization, you can open the code for adjustment and editing. If you find bugs, please feel free to contact the author, New jack.(k8813940518@gmail.com)
In principle, it is not recommanded to open this folder and change its contents at will.

4. Before executing the program, we need to rename the file which is named run.cat to run.bat.

5. Under normal circumstance, you only need to double-click run.bat to execute. The terminal windows will show in the fid file where the wrong place for fid skip number and firing rate irregular are.

## Download the required software and related operations
1. VScode (Strongly recommend) link: https://code.visualstudio.com/download
 (Strongly recommend for code editing)

2. Anaconda link: https://www.anaconda.com/products/individual
 (including python)

Once Anaconda is downloaded, start the installation. 
Pay attention to the place of [Environment Variables] during the installation process, it is strongly recommended to check it to avoid other problems in the future. (picture)

    - ![This is a alt text. Links of image: https://miro.medium.com/max/496/1*02VfY6TA12kzmwmaCs1YFQ.png](/image/EnvVariable.png "Click the first checkbox, please.")

Once downloaded and installed, you can open Anaconda from window-Start and open a power shell.
    
    - ![This is a alt text. Start Anaconda](/image/StartAnaconda.png "Start Anaconda")
    - ![This is a alt text. Start Anaconda](/image/OpenPowerShell.png "Open powershell")



In power shell: 
```
pwd
```

After obtaining the current path, move the file, fid2nav_Env.yml to the above path, and execute the following command. (fid2nav_Env.yml is in the downloaded folder.)


```
conda env create --file fid2nav_Env.yml --name fid2nav_Env
```

![This is a alt text. createEnvSuccessfully](/image/createEnvSuccessfully.png "createEnvSuccessfully")


The above picture appears to indicate that the execution was successful!

Then execute the following command:

```
conda activate fid2nav_Env
```
![This is a alt text. activateEnvSuccessfully](/image/activateEnvSuccessfully.png "activateEnvSuccessfullyn")

The word fid2nav_Env appears on the front side, indicating that the environment has been switched successfully. Power shell can be closed.

In the run.bat folder, double-click to execute the main program of f2n.
![This is a alt text. activateEnvSuccessfully](/image/runSuccessfully.png "activateEnvSuccessfullyn")
The above page appears, indicating that the execution was successful!

## Library Requirement
1. numpy
2. scipy

## Important ref
https://medium.com/datainpoint/python-essentials-conda-quickstart-1f1e9ecd1025