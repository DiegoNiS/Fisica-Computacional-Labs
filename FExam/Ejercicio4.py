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

def ax(x, y, *cuerpos):
    return sum(-(x - c.x) / (((x - c.x)**2 + (y - c.y)**2)**(3/2)) for c in cuerpos)

def ay(x, y, *cuerpos):
    return sum(-(y - c.y) / (((x - c.x)**2 + (y - c.y)**2)**(3/2)) for c in cuerpos)

if __name__ == "__main__":
    plt.figure(figsize=(8, 8))
    cuerpo1 = Masa(x=0, y=10, r=2)
    cuerpo2 = Masa(x=10, y=0, r=2)
    cuerpo3 = Masa(x=-10, y=0, r=2)
    cuerpo4 = Masa(x=0, y=-10, r=2)
    cuerpos = [cuerpo1, cuerpo2, cuerpo3, cuerpo4]
    for c in cuerpos:
        c.dibujar_masa()
    v0 = 0.7
    tfin = 300
    h = 1
    ángulos = np.linspace(0, 2 * np.pi, 16)
    colores_estado = {"orbitando": "green", "colapso": "red", "escapo": "orange"}
    contador = {"orbitando": 0, "colapso": 0, "escapo": 0}
    for angle in ángulos:
        vx = v0 * np.cos(angle)
        vy = v0 * np.sin(angle)
        x = cuerpo3.x
        y = cuerpo3.y + cuerpo3.r + 1
        px, py = [], []
        estado = "orbitando"
        for t in np.arange(0, tfin + h, h):
            vx += ax(x, y, *cuerpos) * h
            vy += ay(x, y, *cuerpos) * h
            x += vx * h
            y += vy * h
            if any(c.colapso(x, y) for c in cuerpos):
                estado = "colapso"
                break
            if np.abs(x) > 40 or np.abs(y) > 40:
                estado = "escapo"
                break
            px.append(x)
            py.append(y)
        contador[estado] += 1
        plt.plot(px, py, color=colores_estado[estado], label=estado if contador[estado] == 1 else "")
    plt.title("Simulación de órbitas con múltiples direcciones iniciales")
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    print("== RESULTADOS DE LA SIMULACIÓN ==")
    for estado in contador:
        print(f"{estado.capitalize()}: {contador[estado]} trayectorias")
    plt.show()