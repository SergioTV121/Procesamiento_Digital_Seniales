
A=1;    %Amplitud
F=1;    %Frecuencia de 7Hz
Fm=1000 %Frecuencia de muestreo, 1000 muestras por segundo
n=0:2/Fm:2;     %Declaracion de mi tiempo discreto
Fase=0; %Fase
X=A*sin(2*pi*F*n+Fase); %Se genera la senal senoidal
figure(1),plot(n,X)
hold on;
xlabel("Tiempo")
ylabel("Amplitud / voltaje")
title("Onda Sen Cos")

A1=1;    
F1=1.5;    
Fase1=0;
X1=A1*sin(2*pi*F1*n+Fase1);
figure(1),plot(n,X1)