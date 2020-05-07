# Swjtu 网上健康信息定时填报脚本
- 安装依赖  

    ```
    pip install -r requirements.txt
    ```

- 创建config.json文件

    ```
    内容参考 config_template.json 与 config_demo.json
    ```

- 运行  

    ```
    python clockin.py
    ```

- tips：
    - 目前仅支持chrome浏览器，其他浏览器需更改浏览器类型并安装相应驱动
    ```
    options = webdriver.ChromeOptions() # 你的浏览器
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(r'.\chromedriver.exe', options=options)  # 浏览器对应驱动
    ```
    - 对应驱动下载：
        - chrom：[link](http://npm.taobao.org/mirrors/chromedriver/)
        - firefox：[link](https://github.com/mozilla/geckodriver/releases)
        - Edge:[link](https://developer.microsoft.com/en-us/micrsosft-edage/tools/webdriver)
        - Safari:[link](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
    - 关闭程序直接关闭控制台窗口或kill
    - ctrl+c / ctrl break 只有在打卡期间有效，监听期间不响应
