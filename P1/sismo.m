A = 16;
F = 55;
Fm = 1000;
n = 0:1/F:1;
Fase = 0;
X = A *sin(2*pi*F*n+Fase);
figure(),plot(n,X)
xlabel("Tiempo")
ylabel("Escala Ritchter")
title("Sismo")