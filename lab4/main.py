import math
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



light_pos = (20, 30, 30)
light_intensity = 5
reflection = 115
ambient = [0.8, 0.0, 0.0, 0.5]

diffuse = [1.0, 0.0, 0.0, light_intensity]

specular = [1.0, 0.0, 0.0, light_intensity]


x_rot = 0
y_rot = -40
z_rot = 0


approximation = 35
size = 1
a, b, c = 2, 4, 4


def init():
    glClearColor(255, 255, 255, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_NORMALIZE)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)

def paraboloid():
    global a, b, c, approximation
    longitude_delta = 2 * math.pi / approximation
    vertices = []

    for i in range(approximation + 1):
        for j in range(approximation + 1):
            lon = j * longitude_delta
            x = a * i
            z = a * i
            y = (x * x + z * z) / 2*a
            x1 = math.cos(lon) * x
            y1 = 0.5 * i * i
            z1 = math.sin(lon) * x
            vertices.append([x1, y1, z1])
    for i in range(approximation + 1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(approximation + 1):
            glVertex3fv(vertices[j + i * approximation])
            glVertex3fv(vertices[j + (i + 1) * approximation])
        glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 0, 2)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glTranslatef(size, size, size)
    init_lighting()
    glRotatef(x_rot, 1, 0, 0)
    glRotatef(y_rot, 0, 0, 1)
    glRotatef(z_rot, 0, 1, 0)

    glPushMatrix()
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128 - reflection)
    paraboloid()
    glPopMatrix()
    glutSwapBuffers()


def init_lighting():
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    l_dif = (2.0, 2.0, 3.0, light_intensity)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, l_dif)
    l_dir = (light_pos[0], light_pos[1], light_pos[2], 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, l_dir)


    attenuation = float(101 - light_intensity) / 25.0
    distance = math.sqrt(pow(light_pos[0], 2) + pow(light_pos[1], 2) + pow(light_pos[2], 2))
    constant_attenuation = attenuation / 3.0
    linear_attenuation = attenuation / (3.0 * distance)
    quadratic_attenuation = attenuation / (3.0 * distance * distance)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, constant_attenuation)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, linear_attenuation)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, quadratic_attenuation)


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, float(width) / float(height), 1.0, 60.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1, 0)


def specialkeys(key, x, y):
    global x_rot, y_rot, z_rot, size, approximation, light_intensity
    if key == b'w':
        x_rot += 5
    if key == b's':
        x_rot -= 5
    if key == b'a':
        y_rot += 5
    if key == b'd':
        y_rot -= 5
    if key == b'q':
        z_rot += 5
    if key == b'e':
        z_rot -= 5
    if key == b'=':
        size += 1
    if key == b'-':
        size -= 1
    if key == b'p':
        approximation += 1
    if key == b'o':
        approximation -= 1
        approximation = max(10, approximation)
    if key == b'l':
        light_intensity += 5
        light_intensity = min(100, light_intensity)
    if key == b'k':
        light_intensity -= 5
        light_intensity = max(-100, light_intensity)

    glutPostRedisplay()


def main():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInit(sys.argv)
    glutCreateWindow("lab 4-5")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(specialkeys)
    init()
    glutMainLoop()


if __name__ == "__main__":
    print("Rotation:")
    print("OX: W S")
    print("OY: A D")
    print("OZ: Q E")
    print()
    print("Change figure size: - +")
    print("Change approximation: o p")
    print("Change light intensity: k l")
    main()