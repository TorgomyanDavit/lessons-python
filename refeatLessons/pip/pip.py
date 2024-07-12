
import camelcase

c = camelcase.CamelCase()
hello = "hello code"
# print(hello.endswith("e"))

print(c.hump(hello))
