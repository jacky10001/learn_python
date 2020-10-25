# learn_python
 
這是將目前Pyhton所使用過的相關程式，做一個 Review
===============================================



Ananconda Conda Commands
===============================================
使用 Anaconda 管理多個的 Python 環境

1. 安裝 Anaconda
   根據OS，選擇合適版本
   windows 安裝過程中需注意勾選將軟體加至"環境變數 path"
   (即可在 cmd 運行 conda 指令)

2. 建立 Python 虛擬環境
   >  conda create -n "env_name" python="3.X.X"

3. 查看已建立的虛擬環境清單
   >  conda env list

4. 啟動\退出虛擬環境
   >  conda activate "env_name"
   >  conda deactivate

5. 在虛擬環境中安裝套件
   >  conda install "package_name"

6 .查看當前環境下已安裝的套件
   查看在conda中已經安裝的包，會顯示套件名字和版本
   >  conda list

7. 導出\導入某個環境用於共享
   >  conda env export > "env_name.yaml"
   導入虛擬環境
   >  conda env update -f="path/env_name.yaml"

   對使用 pip 套件
   >  pip freeze > "env_name.txt"
   >  pip install -r "path/env_name.txt"

8. 刪除某個虛擬環境
   >  conda env remove -n "env_name "


Jupyter
===============================================
   基於web的代碼編輯和數據分析工具jupyter notebook
   >  conda install jupyter notebook
   
   Jupyter NbExtensions Configurator
   >  conda install -c conda-forge jupyter_nbextensions_configurator
   >  jupyter nbextensions_configurator enable --user

   Advantage--在不同的 虛擬環境 使用 "jupyter"
   >  activate myenv
   >  conda install ipykernel # or pip install ipykernel

   新增 kernel (虛擬環境)
   >  python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
   移除 kernel (虛擬環境)
   >  jupyter kernelspec uninstall "unwanted-kernel"
===============================================
