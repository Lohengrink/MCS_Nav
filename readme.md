# fid2Nav in Window
- "fid2Nav_in_Window"(後續簡稱為f2n) 這是一個由python寫成的小工具。
其功能是將fid的檔案格式轉換成nav的檔案格式。同時，能夠抓出fid檔案之中，ffid有跳號，或是炸測秒數不規律的地方。
(註：兩者皆為文字格式，僅是副檔名與內容排列方式不同而已)

<!-- - 如果已經安裝了python，那麼您可以試試直接滑鼠左鍵兩下run.bat這個檔案。理論上應該就可以執行。 -->

- 如果尚未安裝python的話，建議參考以下方式安裝python，以及相關的軟體。(見## 軟體安裝需求)

## 如何操作f2n呢？
1. input資料夾：將欲轉換的fid檔案，放置於此資料夾中。程式將會讀取副檔名為".fid"的檔案，進行轉換。支援一次執行轉多個fid檔案。若副檔名不是fid，則不會被轉換。(預設已經存放一個demo123.fid的檔案，作為範例檔案)

2. output資料夾：轉換之後的nav檔案，將會存放於此處。若沒有此資料夾的話，可以自行創建，但名稱必須為"output"。也可以在第一次執行時，程式會自行創建output資料夾。

3. source_code資料夾：此資料夾存放原始程式碼，如有客製化的需求，可以自行打開程式碼進行調整與編輯。如有發現bug，請和新jack聯絡(k8813940518@gmail.com)。原則上，不建議隨意打開此資料夾與更動其中的內容。

4. 一般情境下，僅需要點兩下run.bat即可以執行。而terminal視窗將會顯示出，fid檔案中有ffid跳號、炸點間距有誤的地方。

## 下載需要的軟體與相關操作
需要的軟體概念上：

1. python本身
2. python相關的套件

實務上：
1. VScode (Strongly recommend) link: https://code.visualstudio.com/download
2. Anaconda link: https://www.anaconda.com/products/individual

- 當Anaconda下載好之後，開始安裝。注意在安裝過程中[環境變數]的地方，強烈建議勾選起來，避免之後其他問題。(如圖)

    - ![This is a alt text. Links of image: https://miro.medium.com/max/496/1*02VfY6TA12kzmwmaCs1YFQ.png](/image/EnvVariable.png "Click the first checkbox, please.")

- 下載且安裝完畢後，可從"開始"打開Anaconda，並打開power shell。
    
    - ![This is a alt text. Start Anaconda](/image/StartAnaconda.png "Start Anaconda")
    - ![This is a alt text. Start Anaconda](/image/OpenPowerShell.png "Open powershell")

#

在power shell中
```
pwd
```
取得目前所在路徑之後，將fid2nav_Env.yml這個檔案移到上述路徑之下，
並執行下面的指令。(fid2nav_Env.yml在下載後的資料夾之中。)

```
conda env create --file fid2nav_Env.yml --name fid2nav_Env
```

![This is a alt text. createEnvSuccessfully](/image/createEnvSuccessfully.png "createEnvSuccessfully")

出現上圖表示執行成功！
#
接著請執行下面指令：


```
conda activate fid2nav_Env
```
![This is a alt text. activateEnvSuccessfully](/image/activateEnvSuccessfully.png "activateEnvSuccessfullyn")

當前方出現fid2nav_Env字樣，表示環境已切換成功。
可以關閉power shell。

到run.bat資料夾底下，點兩下執行f2n的主程式。
![This is a alt text. activateEnvSuccessfully](/image/runSuccessfully.png "activateEnvSuccessfullyn")
出現上方頁面，表示執行成功了！
## Library Requirement
1. numpy
2. scipy

## Important ref
https://medium.com/datainpoint/python-essentials-conda-quickstart-1f1e9ecd1025