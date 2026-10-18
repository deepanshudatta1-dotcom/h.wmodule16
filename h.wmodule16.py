
n = int(input("How many characters to preview?"))

file = open("class-name.txt", "r")
print(file.read(n))
file.close()
print()

file = open("class-name.txt", "r")
lines = file.readlines()
file.close()

print("total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

word = input("Skip lines starting with:")
file = open("class-name.txt", "r")

for line in file:
    if line.startswith(word):
        print("skip->", line.strip())
    else:
        print("keep->", line.strip())

file.close()
print()

file = open("class-name.txt", "r")
lines = file.readlines()
file.close()

out = open("odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()

print("odd lines saved to odd-lines.txt")
print()

file = open("class-name.txt", "r")
lines = file.readlines()
file.close()

out = open("programming-notes.txt", "w")
for line in lines:
    if line.startswith("programming:"):
        out.write(line)

out.close()
print("programming notes saved to programming-notes.txt")
