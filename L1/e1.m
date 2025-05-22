% Constantes
G = 6.67430e-11; % constante gravitatoria
M = 5.972e24;    % masa de la Tierra (kg)
R = 6.371e6;     % radio de la Tierra (m)

% Condiciones iniciales
r0 = [0; R + 1e6];      % posición inicial (100 km sobre la Tierra)
v0 = [7500; 1000];         % velocidad inicial (m/s) - ajusta esto para ver diferentes trayectorias

% Tiempo
dt = 1;                 % paso de tiempo (s)
t_max = 10000;          % duración total (s)
n_steps = floor(t_max/dt);

% Inicializar arrays
r = zeros(2, n_steps);
v = zeros(2, n_steps);
r(:,1) = r0;
v(:,1) = v0;

% Simulación (método de Euler)
for i = 1:n_steps-1
    r_norm = norm(r(:,i));
    a = -G * M * r(:,i) / r_norm^3; % aceleración
    v(:,i+1) = v(:,i) + a * dt;
    r(:,i+1) = r(:,i) + v(:,i+1) * dt;
    
    if norm(r(:,i+1)) < R
        fprintf('Impacto en la Tierra en t = %f s\n', i*dt);
        r = r(:,1:i+1); % cortar el array hasta el impacto
        break;
    end
end
%theta = atan2(v(2, :), v(1, :)); % ángulo en radianes

% Dibuja una flecha que representa el vector de velocidad inicial
scale = 1e2; % ajusta para que la flecha no sea demasiado grande
quiver(r0(1), r0(2), v0(1)*scale, v0(2)*scale, 0, 'r', 'LineWidth', 2, 'MaxHeadSize', 2);
hold on;

% Gráfica
plot(r(1,:), r(2,:))
hold on
rectangle('Position',[-R, -R, 2*R, 2*R], 'Curvature',[1,1], 'EdgeColor','k', 'LineStyle','--'); % mostrar la Tierra
% plot((0:length(theta)-1)*dt, rad2deg(theta));
axis equal
xlabel('x (m)')
ylabel('y (m)')
title('Trayectoria bajo gravedad terrestre')
