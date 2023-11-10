import sympy as sym

def dao_ham(f, var = 'x'):
    x = sym.symbols(var)
    try:
        result = sym.diff(f, x)
        return str(result)
    except Exception as e:
        return f"Lỗi: {str(e)}"
    
    
##fx = "x**2 +3*x+4"
#result = daoHam(fx)
#print(result)

    
def tich_phan(f, var = 'x', lower_limit = None, upper_limit  = None):
    x = sym.symbols(var)
    try:
        result = sym.integrate(f, (x, lower_limit, upper_limit))
        return str(result)
    except Exception as e:
        return f"Lỗi: {str(e)}"
    
    
def nguyen_ham(f, var = 'x'):
    x = sym.symbols(var)
    try:
        result = sym.integrate(f, x)
        return str(result)
    except Exception as e:
        return f"Lỗi: {str(e)}"
        
        
f_str = input("Nhập hàm số muốn tính toán; ")
try:
    f = sym.sympify(f_str)
except Exception as e:
    print(f"Lỗi: {str(e)}")
    
result = nguyen_ham(f)
print(result)
