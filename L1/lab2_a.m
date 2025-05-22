clear, clf, hold off;
theta = linspace(0, 2*pi, 100);
r = 3;

x = r*cos(theta);
y = r*sin(theta);

plot(x, y, 'LineWidth', 2);
axis equal;
grid on;