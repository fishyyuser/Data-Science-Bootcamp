from mypackage import add, multi
print(add(3,7))
print (multi(2,5))

try:
    from mypackage import div

except ImportError:
    print("Are u blind but gracefully")