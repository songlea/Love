# Rose

## 玫瑰

> 打包

* pyinstall + python3.8

1. 先执行 `pyinstaller -F -w rose.py`, 会生成rose.spec文件
2. 修改rose.spec文件， Analysis中的datas 修改为`datas=[('res', 'res')]`, EXE中添加一行 `console=False , icon='res/rose.ico')`
3. 再次打包 `pyinstaller -F -w rose.spec`