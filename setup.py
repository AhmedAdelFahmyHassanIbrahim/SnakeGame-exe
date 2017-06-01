from cx_Freeze import setup , Executable

setup(name='Snake Game' ,
      version = '0.1' ,
      description='A simple snake game',
      executables=[Executable("Snake_Game.py")])
