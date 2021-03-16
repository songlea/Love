# Finger Heart

## 比心

> 打包

* pyinstall + python3.8

1. 先执行 `pyinstaller -F -w finger_heart.py`, 会生成finger_heart.spec文件
2. 修改finger_heart.spec文件， Analysis中的datas 修改为`datas=[('res', 'res')]`, EXE中添加一行 `console=False , icon='res/heart.ico')`
3. 再次打包 `pyinstaller -F -w finger_heart.spec`