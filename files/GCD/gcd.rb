def gcd(a, b)
  while b > 0
    a, b = b, a % b
  end
  a
end

