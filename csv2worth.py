def main():
    print("------------------------")
    print("csv2worth Utility | jstnf")
    print("Phoenix Origins")
    print("------------------------")
	
    print("Grabbing economy.csv...")
    ecofile = open("economysurvival.csv", "r")
    ecolines = ecofile.readlines()
    ecofile.close()

    print("Generating worth.yml file...\n")
    worthfile = open("worthsurvival.yml", "w+", newline="")
    worthfile.write("worth:\n")
    for x in ecolines:
      line = x
      comma_index = line.find(",")
      if comma_index != -1:
        item = line[:comma_index].lower()
        worth = line[comma_index + 1:]
        print("Found item %s worth %s" % (item, worth), end="")
        worthfile.write("  %s: %s" % (item, worth))
    worthfile.close()
    print("\nFinished conversion! Goodbye!")

if __name__ == "__main__":
  main()
