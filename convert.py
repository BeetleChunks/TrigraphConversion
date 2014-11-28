def trigraph(fileInName, fileOutName):
	triSymbols = {"|": "??!", "^": "??'", "[": "??(",
	              "]": "??)", "~": "??-", "\\": "??/", 
                  "{": "??<", "#": "??=", "}": "??>"}
	with open(fileInName, "r+") as fileIn:
		symbols = fileIn.read()

	with open(fileOutName, "w") as fileOut:
		for sym in symbols:
			if sym in triSymbols.keys():
				sym = triSymbols[sym]
				fileOut.write(sym)
			else:
				fileOut.write(sym)

def main():
	trigraph("hashRev.c", "out2.c")

if __name__ == '__main__':
	main()
