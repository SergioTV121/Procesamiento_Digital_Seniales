%%Time specifications:
Fs = 8000;                   % samples per second
dt = 1/Fs;                   % seconds per sample
StopTime = 0.25;             % seconds
t = (0:dt:StopTime-dt)';     % seconds
%%Sine wave:
Fc = 60;                     % hertz
x = sin(2*pi*Fc*t);
% Plot the signal versus time:
figure;
plot(t,x);
xlabel('Tiempo (segundos)');
ylabel('Corriente');
title('Corriente/Tiempo');