# Swjtu 网上健康信息定时填报脚本
- 支持 win 与 linux 建议通过tmux运行在VPS服务器上

- 安装依赖  

    ```
    pip install -r requirements.txt
    ```

- 创建config.json文件

    ```
    内容参考 config_template.json 与 config_demo.json
    ```

- linux下需安装chrome

    - 打开一个终端，使用下面的命令编辑sources.list源文件

        ```
        sudo nano /etc/apt/sources.list
        ```

    - 复制下面一行文字，将它粘贴到sources.list文件的末尾
        ```
        deb http://dl.google.com/linux/chrome/deb/ stable main
        ```

    - 保存文件，然后使用wget下载谷歌的公钥，用apt-key将公钥添加到Debian

        ```
        wget https://dl-ssl.google.com/linux/linux_signing_key.pub
        sudo apt-key add linux_signing_key.pub
        sudo apt-get update
        sudo apt-get install google-chrome-stable
        ```

- linux下需要给予chromedriver权限

    ```
    chmod 777 chromedriver
    ```

- 运行

    ```
    python clockin.py
    ```

- tips：

    - 目前仅支持chrome浏览器，其他浏览器需更改浏览器类型并安装相应驱动

    ```
    options = webdriver.ChromeOptions() # 你的浏览器
    self.driver = webdriver.Chrome(r'.\chromedriver.exe', options=options)  # 浏览器对应驱动
    ```

    - 对应驱动下载：
        - chrom：[link](http://npm.taobao.org/mirrors/chromedriver/)
        - firefox：[link](https://github.com/mozilla/geckodriver/releases)
        - Edge：[link](https://developer.microsoft.com/en-us/micrsosft-edage/tools/webdriver)
        - Safari：[link](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
        
    - win 关闭 Ctrl + Break 或者（虚拟键盘） Ctrl + Fn + Pause
    
    - linux 关闭 Ctrl + C
