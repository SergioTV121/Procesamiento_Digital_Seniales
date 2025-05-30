A=.2;    %Amplitud
F=.5;    %Frecuencia de 7Hz
Fm=1000 %Frecuencia de muestreo, 1000 muestras por segundo
n=0:2/Fm:2;     %Declaracion de mi tiempo discreto
Fase=0; %Fase
X=A*sin(2*pi*F*n+Fase); %Se genera la senal senoidal
figure(1),plot(n,X)
hold on;
xlabel("Tiempo")
title("Onda Movimiento Manecillas de Reloj")