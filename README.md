# Swjtu 网上健康信息定时填报脚本
- 安装依赖  

    ```
    pip install -r requirements.txt
    ```

- 创建config文件  

    ```
    参考 config_template.json 与 config_demo.json
    ```

- 运行  

    ```
    python clockin.py
    ```

- tips：
    - 目前仅支持chrome浏览器，其他浏览器需要更改为对应的浏览器类型，并下载相应驱动，对应驱动参考https://www.jianshu.com/p/1b63c5f3c98e
    ```
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(r'.\chromedriver.exe', options=options)
    ```
    - 关闭程序直接关闭控制台窗口或kill
    - ctrl+c / ctrl break 只有在打卡期间有效，监听期间不响应
