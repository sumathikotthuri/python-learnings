def process_text(text: str):
    print(text.split())


def process_texts(texts: list):
    print(texts.insert(2,"three"))    


process_text('Hello world')    
texts = ["one","two"]
process_texts(texts)


value = 10

print(f"Value {value}")
print('Value',value)


video_specs = (1920,1080, 60)
width = video_specs[0]
height = video_specs[1]
fps = video_specs[2]

print('width',width)
print('height',height)
print('fps',fps)

#Instead we can do this way

video_specs_alt = (1920,1080, 60)
width_alt,height_alt,fps_alt = video_specs_alt

print('width_alt',width_alt)
print('height_alt',height_alt)
print('fps_alt',fps_alt)

# multi assignments in single line
x,y,z = 1,2,3

print('x',x)
print('y',y)
print('z',z)


numbers = [1,2,3,4,5,6,7]

# if we want to filter even numbers from above list

filered_a = []

for num in numbers:
    if num%2==0:
        filered_a.append(num)

print("filtered a",filered_a)

# but there is more comprehenced way
# of doing it using list comprehension
filered_b=[i for i in numbers if i % 2 == 0 ] 
print("filered_b",filered_b)

filered_c=[i for i in numbers if not i % 2 == 0 ] #not means inverse operator
print("filered_c",filered_c)


a,b = 15,20

if a > 10 and a < b:
    print("yay!!")

#the same can be written as

if 10 < a < b:
    print("Big yay!!")



internet = False

if internet:
    is_connected = 'Connected'
else:
    is_connected = 'Not Connected'


print(is_connected)  

# the same code can be used using ternery operator

is_connected_alt = 'Connected' if internet else 'Not Connected'

print(is_connected_alt)  

people = ['Sumathi','Roopa','Swapna','Soujanya','Shyam']

for i,person in enumerate(people):
    print(i,':', person)
    #print("{} : {}".format((i+1), person))


decimal:float = 120_000.1234567

fmt_dec:str = '{0:.2f}'.format(decimal)
print(fmt_dec)
round_dec:float = round(decimal,2)
print(round_dec)
fmt_com:str = f'{decimal:,}'
print(fmt_com)
fmt_decimal_com:str = f'{round_dec:,}'
print(fmt_decimal_com)