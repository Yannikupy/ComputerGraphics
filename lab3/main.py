'''
Используя результаты Л.Р. №2, аппроксимировать заданное тело выпуклым многогранником.
Точность аппроксимации задается пользователем. Обеспечить возможность вращения и масштабирования многогранника
и удаление невидимых линий и поверхностей. Реализовать простую модель закраски для случая одного источника света.
Параметры освещения и отражающие свойства материала задаются пользователем в диалоговом режиме

Вариант 6: Параболоид

'''
import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib.widgets import Button

fig = plt.figure('лабораторная работа № 3, Борисов Я.А. Вариант 6: Параболоид')
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
X, Y = np.meshgrid(x, y)
Z = (X * X + Y * Y) / 2

ax.contour3D(X, Y, Z, levels=100, cmap='binary')

with open('camera.xml', 'r+') as f:
    data = f.read()
f.close()
bs_data = BeautifulSoup(data, 'xml')
ax.elev = float(bs_data.find('Camera')['axlevel'])
ax.azim = float(bs_data.find('Camera')['axazim'])


def deapprox_button(event):
    ax.cla()
    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
    X, Y = np.meshgrid(x, y)
    Z = (X * X + Y * Y) / 2
    ax.contour3D(X, Y, Z, levels=100, cmap='binary')
    plt.draw()
    plt.show()


def approx_button(event):
    ax.cla()
    x = np.linspace(-100, 100, 5)
    y = np.linspace(-100, 100, 5)
    X, Y = np.meshgrid(x, y)
    Z = (X * X + Y * Y) / 2
    ax.contour3D(X, Y, Z, levels=100, cmap='binary')
    plt.draw()
    plt.show()


def save_camera(event):
    with open('camera.xml', 'r+') as f:
        data = f.read()
    bs_data = BeautifulSoup(data, 'xml')
    bs_data.find('Camera')['axlevel'] = str(ax.elev)
    bs_data.find('Camera')['axazim'] = str(ax.azim)
    f.close()
    with open('camera.xml', 'w') as f:
        f.seek(0)
        f.truncate()
        f.write(bs_data.prettify())
    f.close()


axes_ibutton_add = plt.axes([0.55, 0.05, 0.4, 0.075])
axes_ibutton_add2 = plt.axes([0.15, 0.05, 0.4, 0.075])
axes_ibutton_add3 = plt.axes([0.05, 0.9, 0.4, 0.075])
ibutton_add = Button(axes_ibutton_add, 'Аппроксимировать')
ibutton_add2 = Button(axes_ibutton_add2, 'Деаппроксимировать')
ibutton_add3 = Button(axes_ibutton_add3, 'Сохранить положение камеры')
ibutton_add.on_clicked(approx_button)
ibutton_add2.on_clicked(deapprox_button)
ibutton_add3.on_clicked(save_camera)
print(ax.elev)
plt.show()
