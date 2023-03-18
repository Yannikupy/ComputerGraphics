'''
Разработать формат представления многогранника и процедуру его каркасной отрисовки
в ортографической и изометрической проекциях. Обеспечить удаление невидимых линий
и возможность пространственных поворотов и масштабирования многогранника.
Обеспечить автоматическое центрирование и изменение размеров изображения при изменении
размеров окна.
Вариант 2: Правильный октаэдр

'''
import math

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons
import tkinter as tk

win = tk.Tk()
win.geometry("400x400")

a = tk.Entry(win, width=30)
tk.Label(text="Длина ребра = ") \
    .grid(row=0, column=0)
a.grid(row=0, column=1)


def main():
    b = int(a.get())
    fig = plt.figure('лабораторная работа № 2, Борисов Я.А. Вариант 2: Правильный октаэдр')
    ax = fig.add_subplot(111, projection='3d')

    # вершины пирамиды
    v = np.array([[0, 0, b / math.sqrt(2)], [0, 0, -b / math.sqrt(2)], [0, b / math.sqrt(2), 0],
                  [0, -b / math.sqrt(2), 0], [b / math.sqrt(2), 0, 0], [-b / math.sqrt(2), 0, 0]])

    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

    # построение сторон
    verts = [[v[0], v[4], v[2]],
             [v[0], v[5], v[3]],
             [v[1], v[4], v[2]],
             [v[1], v[5], v[3]],
             [v[0], v[5], v[3]],
             [v[0], v[5], v[2]],
             [v[0], v[4], v[3]],
             [v[1], v[5], v[2]],
             [v[1], v[4], v[3]],
             ]

    # отрисовка
    ax.add_collection3d(
        Poly3DCollection(verts, facecolors='pink', linewidths=1, edgecolors='purple', alpha=0.25))  # 0.25

    def iButton(event):
        ax.view_init(28, -136)
        plt.draw()

    axes_ibutton_add = plt.axes([0.55, 0.05, 0.4, 0.075])
    ibutton_add = Button(axes_ibutton_add, 'Изометрическая')
    ibutton_add.on_clicked(iButton)

    def oButton(event):
        ax.view_init(-2, -36)
        plt.draw()

    axes_obutton_add = plt.axes([0.06, 0.05, 0.4, 0.075])
    obutton_add = Button(axes_obutton_add, 'Ортографическая')
    obutton_add.on_clicked(oButton)

    lines_visibility = plt.axes([0.02, 0.85, 0.5, 0.11], facecolor='lavenderblush')
    radio = RadioButtons(lines_visibility, ('Каркасная отрисовка', 'Убрать невидимые линии'))

    def lines(a):
        condition = {'Каркасная отрисовка': 0.20, 'Убрать невидимые линии': 1}
        alpha = condition[a]
        # print(a)
        ax.add_collection3d(Poly3DCollection(verts, facecolors='pink', linewidths=1, edgecolors='purple', alpha=alpha))
        plt.draw()

    radio.on_clicked(lines)

    plt.show()


button = tk.Button(win, text="Показать фигуру", command=main)
button.grid(row=1, column=1)
win.mainloop()
