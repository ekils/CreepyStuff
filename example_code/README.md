# 標註轉檔操作

### 1. (需手動設定) 先設定檔案資料夾路徑: 
* 此資料夾為執行轉檔的程式碼資料夾

        export DATAPATH='/your/path/of/convert/codes/'

</br>

### 2. (需手動自建) 在此資料夾底下創建一個資料夾 src_data: 
* 然後把標注檔案與圖檔放置到該資料夾底下,格式如下： </br>
    src_data</br>
    &emsp;&emsp;&emsp;|__jpg </br>
    &emsp;&emsp;&emsp;|__xml

    
        mkdir src_data
 </br>

### 3. 將 src_data 複製到 step1_data 資料夾底下進行檔名調整:

        # Copy source data to step1: 
        cp -a $DATAPATH'src_data/.' './step1_data'
        # # step1:
        python3 step1_change_name.py --path $DATAPATH
</br>

### 4. 將 step1_data 複製到 step2_data 資料夾底下進行xml to txt 轉換:
* 此操作裡面兩個參數：</br>
&emsp;&emsp;&emsp;--txt_folder : 將xml檔案轉成txt後存放的目錄</br>
&emsp;&emsp;&emsp;--img_folder : txt轉好後,對應的圖檔存放目錄</br>

        cp -a $DATAPATH'step1_data/.' './step2_data'
        rm -R $DATAPATH'step1_data'
        # step2:
        mkdir ./step2_data/img
        mkdir ./step2_data/gt
        mkdir ./step3_data
        python3 step2_totxt.py --txt_folder ./step3_data/gt/ --img_folder ./step3_data/img/
</br>

### 5. 將 step2_data 複製到 step3_data 資料夾底下進行DBNet的資料轉換:

        # Copy source data to step3:
        rm -R $DATAPATH'step2_data'
        # step3:  Split data into train, test dataset
        python3 step3_split_data.py --path $DATAPATH  # Modify the path according to your situation
        rm -R $DATAPATH'step3_data'