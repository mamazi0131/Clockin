# Swjtu 网上健康信息定时填报脚本
## 已跟随信息填报系统更新并完成测试
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

    - VPS长时间运行后可能出现如下错误解决防范
    报错：
    ```
    Message: unknown error: session deleted because of page crash
    from unknown error: cannot determine loading status
    from tab crashed
    (Session info: headless chrome=81.0.4044.138)
    ```
    原因：内存泄漏造成的程序崩溃
    解决方案：
    ```
    1.更改配置，放弃使用内存，转而使用硬盘，执行速度略微下降
    options.add_argument('--disable-dev-shm-usage')
    ```
    ```
    2.更改VPS系统配置，加大内容容量
    sudo mount -t tmpfs -o rw,nosuid,nodev,noexec,relatime,size=512M tmpfs /dev/shm
    ```
    
 - ![log](https://github.com/swjtuer0/Clockin/blob/master/log.png)
