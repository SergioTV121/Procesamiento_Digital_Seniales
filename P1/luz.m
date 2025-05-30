clc; close all; clear all;

%Generar una senal de amplitud de 12, frecuencia de 7 hz, fase de 0 y Fm
%variable
A=5;    %Amplitud
F=2;    %Frecuencia de 7Hz
Fm=1000 %Frecuencia de muestreo, 1000 muestras por segundo
n=0:1/Fm:1;     %Declaracion de mi tiempo discreto
Fase=0; %Fase
X=A*sin(2*pi*F*n+Fase); %Se genera la senal senoidal
figure(),plot(n,X)
xlabel("Tiempo")
ylabel("Amplitud / voltaje")
title("Onda de Luz")