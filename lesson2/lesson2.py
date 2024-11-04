a, b, c = input().split()
print(f'{a}, {b} and c is {c}')
if a.isdigit() or b.isdigit():
  print(f"A or B is digit")
  if c.isdigit():
    print(f"C is digit")
else:
  print(f"Var A and B is not digit")


a, b, c = input().split()
if not a.isdigit() or not b.isdigit() or not c.isdigit():
    print('Input numbers!')
else:
    a, b, c = map(int, (a, b, c))
    if a < b and a < c:
        print(f"Variable a is minimal")
    else:
        if b < c:
            print(f"Variable b is minimal")
        else:
            print(f"Variable c is minimal")