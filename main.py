import os
import base64 as base

def design():
	os.system("figlet -f standard ANTI-SCRIPT-KIDDIES")

def Base_64(file, output):
	en_1 = open(file, "r").read().encode()
	en = base.b64encode(en_1)
	out = en
	t = open(output, "wb")
	t.write(b"import base64\nexec(base64.b64decode(b\"")
	t.write(out)
	t.write(b"\"))")
    
	
def Base_32(file, output):
	en_1 = open(file, "r").read().encode()
	en = base.b32encode(en_1)
	out = en
	t = open(output, "wb")
	t.write(b"import base64\nexec(base64.b32decode(b\"")
	t.write(out)
	t.write(b"\"))")
	
def Base_16():
	en_1 = open(file, "r").read().encode()
	en = base.b16encode(en_1)
	out = en
	t = open(output, "wb")
	t.write(b"import base64\nexec(base64.b16decode(b\"")
	t.write(out)
	t.write(b"\"))")
	
#def Mars_Hal(file, output):
#	en_1 = open(file, "r").read().encode()
#	en = mars.dumps(en_1)
#	out = en
#	t = open(output, "wb")
#	t.write(b"import marshal\nexec(marshal.loads(b\"")
#	t.write(out)
#	t.write(b"\"))")
	
def main():
	design()
	print("Tool starting")
	print("select an option")
	option = input("""
		{1} Base64
		{2} Base32
		{3} Base16
		μ~> """)
	file = input("file μ~> ")
	output = input("output μ~> ")
	test = file.split(".")
	if test[1] == "py":
		if option == "1":
			Base_64(file, output)
			print(f"test the script by typing: python {output}")
		elif option == "2":
			Base_32(file, output)
			print(f"test the script by typing: python {output}")
		elif option == "3":
			Base_16(file, output)
			print(f"test the script by typing: python {output}")
		else:
			print("Choose from the given option")
	else:
			print("only .py(python file and program are supported)")
		#elif option == "4":
#			Mars_Hal(file, output)
#			print(f"test the script by typing: python {output}")
	
main()