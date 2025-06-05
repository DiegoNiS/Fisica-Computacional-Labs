clear, clf, hold off; 
n = 0; 
h = 0.01;
% Constantes del sistema
g = 9.81;       
tfin = 2;     
v0 = 10;         
theta = 60;     
phi = 30; %
theta_rad = deg2rad(theta);
phi_rad = deg2rad(phi);
vx = v0 * cos(theta_rad) * cos(phi_rad);
vy = v0 * cos(theta_rad) * sin(phi_rad);
vz = v0 * sin(phi_rad);
% Posiciones iniciales
x = 0;
y = 0;
z = 0;
% Vectores
pt(1) = 0; 
px(1) = x; 
py(1) = y;
pz(1) = z;
pvx(1) = vx; 
pvy(1) = vy;
pvz(1) = vz;
for t = 0:h:tfin
    n = n + 1;
    ax = 0;
    ay = 0;
    az = -g
    vx = vx + h * ax;   
    vy = vy + h * ay;
    vz = vz + h * az;
    x = x + h * vx;
    y = y + h * vy;
    z = z + h * vz;
    pt(n+1) = t;
    px(n+1) = x;
    py(n+1) = y;
    pz(n+1) = z;
    pvx(n+1) = vx;
    pvy(n+1) = vy;
    pvz(n+1) = vz;
end
% Gráficos
plot3(pt, px, pz), grid on