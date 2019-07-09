def main():
	ecofile = open("economy.csv", "r")
	ecolines = ecofile.readlines()
	ecofile.close()
	
	worthfile = open("worth.yml", "w+")
	for x in ecolines:
	  line = x
	  comma_index = line.find(",")
	  if comma_index != -1:
	    item = line[:comma_index]
	    worth = line[comma_index + 1:]
	    worthfile.write("%s: %s" % (item.upper(), worth))
	worthfile.close()

if __name__ == "__main__":
  main()