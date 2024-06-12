H = int(input());
M = int(input());
S = int(input());
T = int(input());

totalS = (H * 3600) + (M * 60) + S + T;
sRestantes = totalS % 3600;
totalS = totalS // 3600;
while totalS > 23:
  totalS = totalS - 24;

print(totalS);
print(sRestantes // 60);
print(sRestantes % 60);

