'''
Тема: Построение плоских полиномиальных кривых.
Задание: Написать программу, строящую полиномиальную кривую по заданным точкам. Обеспечить возможность
изменения позиции точек.

NURB-кривая. n = 5, k = 3. Узловой вектор неравномерный. Веса точек различны и модифицируются
'''
import tkinter as tk
from geomdl import NURBS
from geomdl import utilities
from geomdl.visualization import VisMPL

win = tk.Tk()
win.title("Борисов Я.А. lab 7 NURB-кривая. n = 5, k = 3.")
win.geometry("400x400")

a = tk.Entry(win, width=30)
tk.Label(text="Point a x= ") \
    .grid(row=0, column=0)
a.grid(row=0, column=1)

b = tk.Entry(win, width=30)
tk.Label(text="Point a y= ") \
    .grid(row=1, column=0)
b.grid(row=1, column=1)

c = tk.Entry(win, width=30)
tk.Label(text="Point b x= ") \
    .grid(row=2, column=0)
c.grid(row=2, column=1)

d = tk.Entry(win, width=30)
tk.Label(text="Point b y= ") \
    .grid(row=3, column=0)
d.grid(row=3, column=1)

e = tk.Entry(win, width=30)
tk.Label(text="Point c x= ") \
    .grid(row=4, column=0)
e.grid(row=4, column=1)

f = tk.Entry(win, width=30)
tk.Label(text="Point c y= ") \
    .grid(row=5, column=0)
f.grid(row=5, column=1)

g = tk.Entry(win, width=30)
tk.Label(text="Point d x= ") \
    .grid(row=6, column=0)
g.grid(row=6, column=1)

h = tk.Entry(win, width=30)
tk.Label(text="Point d y= ") \
    .grid(row=7, column=0)
h.grid(row=7, column=1)

i = tk.Entry(win, width=30)
tk.Label(text="Point e x= ") \
    .grid(row=8, column=0)
i.grid(row=8, column=1)

j = tk.Entry(win, width=30)
tk.Label(text="Point e y= ") \
    .grid(row=9, column=0)
j.grid(row=9, column=1)


def main():
    curve = NURBS.Curve()

    curve.degree = 3
    curve.ctrlpts = [[float(a.get()), float(b.get()), 0],
                     [float(c.get()), float(d.get()), 0],
                     [float(e.get()), float(f.get()), 0],
                     [float(g.get()), float(h.get()), 0],
                     [float(i.get()), float(j.get()), 0]]

    # вектор узлов
    curve.knotvector = utilities.generate_knot_vector(curve.degree,
                                                      len(curve.ctrlpts))

    # гладкость кривой
    curve.delta = 0.0001

    curve.vis = VisMPL.VisCurve2D()
    curve.render()


button = tk.Button(win, text="Показать фигуру", command=main)
button.grid(row=12, column=1)
win.mainloop()
