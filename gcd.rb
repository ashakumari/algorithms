def gcd(a, b)
	if (a == b)
		return a
	elsif a > b
		return gcd(a-b, b)
	else
		return gcd(a, b-a)
	end		
end

print gcd(24,8) == 8
print "\n"
print gcd(1362, 1407) == 3
print "\n"
print gcd(1875, 1907) == 1
print "\n"
print gcd(45,116) == 1