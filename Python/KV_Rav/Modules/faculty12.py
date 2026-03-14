# import faculty1
# import faculty2
# print(faculty1.name,faculty1.sub)
# print(faculty2.name,faculty2.sub)
# faculty1.teach()
# faculty2.teach()


from faculty2 import name,sub,teach
from faculty1 import name,sub,teach
print(name,sub)
teach()