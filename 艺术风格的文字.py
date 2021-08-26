from pyfiglet import Figlet, FigletFont
"""
pip install pyfiglet
"""
# 所有字体样式
print(FigletFont().getFonts())

f = Figlet()
print(f.renderText("Andrew"))

f = Figlet(font="stellar")
print(f.renderText("Andrew"))

f = Figlet(font="advenger")
print(f.renderText("Andrew"))

f = Figlet(font="acrobatic")
print(f.renderText("Andrew"))

f = Figlet(font="alligator")
print(f.renderText("Andrew"))

f = Figlet(font="alligator2")
print(f.renderText("Andrew"))

f = Figlet(font="alphabet")
print(f.renderText("Andrew"))

f = Figlet(font="ascii___")
print(f.renderText("Andrew"))

f = Figlet(font="contessa")
print(f.renderText("Andrew"))
