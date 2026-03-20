from faker import Faker
fgen=Faker()
name=fgen.name()
print(name)
print(fgen.last_name())
print(fgen.first_name())
print(fgen.email())
print(fgen.city())
print(fgen.random_int(min=0,max=99))