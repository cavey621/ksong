n = 180;
N = 3;
z = 1;
v = 1;
w = 1;
R = 0;
L = n/6;
count = 1;
simnum = 100;
y = [1:simnum];
he=0; 
nA = 12;
Ti = [];
Tmax = 0;
Tmin = 5000;
smax = 0;
smin = 0;

while count <= simnum
    st = 0;
    stA = 0;
    xA = ceil(nA.*rand(nA,1));
    sA = zeros(1, nA);
    timeA = zeros(1,1000);
    timeB = zeros(1,100000);
for i = 1:12 
    a = xA(i);
    r = R;
    R = floor(a/4);
    k = mod(a, 4);
    sA(a) = 1;
    b = rand(100,1);
    if b <= 80
        timeA(2*R + 2*i + stA: 2*R + 2*i + stA + 30) = 1; %first class wide 2
        stA = stA + 30;
    end 
    if k == 1
            if sA(a+1) == 1
                stA = stA + 5;
                timeA(2*R + 2*i + stA: 2*R + 2*i + stA + 5) = 1;
            end
    else if k == 0
            if sA(a-1) == 1
                stA = stA + 5;
                timeA(2*R + 2*i + stA: 2*R + 2*i + stA + 5) = 1;             
            end
        end
            
    end

    stA = sum(timeA~=0);
end
    TA = R + w*nA + stA;
for j = 1:N
    x = ceil(n/N.*rand(n,1));
    s = zeros(1, n/N);
for i = 1:n/N
    a = x(i);
    r = R;
    R = floor(a/2);
    s(a) = 1;
    b = rand(100,1);
    if b <= 80
        timeB(R + i + st: R + i + st + 15) = 1;
        st = st + 15;
    end 
    st = sum(timeB~=0);
end
end
    T = R + w*n + st;
    he = he + T + TA;
    Time = T + TA;
    Ti = [Ti Time];  
    if Time>Tmax
        Tmax = Time;
        smax = count;
    else if Time < Tmin
        Tmin = Time;
        smin = count;
        end
    end
    count = count + 1;
end

average = he / simnum;
Min = floor(average/60);
Second = average - Min*60;
print = ['N=',num2str(N),' n=',num2str(n),' average=',num2str(average),'=', num2str(Min),'min',num2str(Second),'sec',' Tmax=',num2str(Tmax),' Tmin=',num2str(Tmin)];
disp(print)
plot(y,Ti,'o')
hold on
plot(smax,Tmax,'r+',smin,Tmin,'r+')
hline = refline(0,average);
set(hline,'Color','r');
xlabel('simulations');
ylabel('seconds');
title('OI time vs simulations')





    
    
                    