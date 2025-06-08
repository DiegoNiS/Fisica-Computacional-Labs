import numpy as np
import matplotlib.pyplot as plt

class Masa:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def dibujar_masa(self):
        theta = np.linspace(0, 2 * np.pi, 200)
        xc = self.r * np.cos(theta) + self.x
        yc = self.r * np.sin(theta) + self.y
        plt.plot(xc, yc, color='blue', linewidth=2)

    def calcularDistancia(self, x, y):
        return np.sqrt((x - self.x)**2 + (y - self.y)**2)

    def colapso(self, x, y):
        return self.calcularDistancia(x, y) <= self.r

def ax(x, y, cuerpo1, cuerpo2, cuerpo3, cuerpo4):
    ax1 = -(x - cuerpo1.x) / (((x - cuerpo1.x)**2 + (y - cuerpo1.y)**2)**(3/2))
    ax2 = -(x - cuerpo2.x) / (((x - cuerpo2.x)**2 + (y - cuerpo2.y)**2)**(3/2))
    ax3 = -(x - cuerpo3.x) / (((x - cuerpo3.x)**2 + (y - cuerpo3.y)**2)**(3/2))
    ax4 = -(x - cuerpo4.x) / (((x - cuerpo4.x)**2 + (y - cuerpo4.y)**2)**(3/2))
    return ax1 + ax2 + ax3 + ax4

def ay(x, y, cuerpo1, cuerpo2, cuerpo3, cuerpo4):
    ay1 = -(y - cuerpo1.y) / (((x - cuerpo1.x)**2 + (y - cuerpo1.y)**2)**(3/2))
    ay2 = -(y - cuerpo2.y) / (((x - cuerpo2.x)**2 + (y - cuerpo2.y)**2)**(3/2))
    ay3 = -(y - cuerpo3.y) / (((x - cuerpo3.x)**2 + (y - cuerpo3.y)**2)**(3/2))
    ay4 = -(y - cuerpo4.y) / (((x - cuerpo4.x)**2 + (y - cuerpo4.y)**2)**(3/2))
    return ay1 + ay2 + ay3 + ay4

if __name__ == "__main__":
    plt.figure(figsize=(7, 7))
    cuerpo1 = Masa(x=0, y=10, r=2)
    cuerpo2 = Masa(x=10, y=0, r=2)
    cuerpo3 = Masa(x=-10, y=0, r=2)
    cuerpo4 = Masa(x=0, y=-10, r=2)

    cuerpo1.dibujar_masa()
    cuerpo2.dibujar_masa()
    cuerpo3.dibujar_masa()
    cuerpo4.dibujar_masa()

    # condiciones iniciales
    max_vx = 0.8
    k = 0.001
    v0 = 0.7
    tfin = 300
    h = 1

    for vx in np.arange(v0, max_vx + k, k):
        vy = 0
        x = cuerpo3.x
        y = cuerpo3.y + cuerpo3.r + 1
        px = []
        py = []
        estado = "orbitando"

        for t in np.arange(0, tfin + h, h):
            vx += ax(x, y, cuerpo1, cuerpo2, cuerpo3, cuerpo4) * h
            vy += ay(x, y, cuerpo1, cuerpo2, cuerpo3, cuerpo4) * h
            x += vx * h
            y += vy * h

            # colapso
            if (cuerpo1.colapso(x, y) or cuerpo2.colapso(x, y) or
                cuerpo3.colapso(x, y) or cuerpo4.colapso(x, y)):
                estado = "colapso"
                break

            # escape
            if np.abs(x) > 30 or np.abs(y) > 30:
                estado = "escapo"
                break

            py.append(y)
            px.append(x)

        if estado == "orbitando":
            plt.plot(px, py)

    plt.axis('equal')
    plt.grid(True)
    plt.show()