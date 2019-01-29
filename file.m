x = zeros(1,100)
for i= 1:length(x)
x(i)= power(i,2)
end
save('file','x')

