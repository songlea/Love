# Confess

##表白

> 打包

* pyinstall + python3.8

1. 先执行 `pyinstaller -F main.py`, 会生成main.spec文件
2. 修改main.spec文件， Analysis中的datas 修改为`datas=[('res', 'res')]`, EXE中添加一行 `console=False , icon='res/heart.ico')`
3. 再次打包 `pyinstaller -F main.spec` (加上-w杀毒软件会误报)
