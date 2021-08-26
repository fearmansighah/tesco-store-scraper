import csv


def extractNames(line):
    line = str(line)
    index = 0
    for char in line:
        if char == '"':
            start = index + 1
            index = 0
            break

        index += 1

    for char in line:
        if (char == '"') and (start == index):
            continue
            index += 1
        if char == '"':
            end = index - 1

        index += 1

    store_name = line[int(start): int(end+1)]

    return store_name


def main():
    # get file object
    f = open("tesco_stores.txt", "r")

    csvfile = open("store_names.csv", "w", newline="")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Store Name'])

    while (True):
        # read next line
        line = f.readline()
        # if line is empty, you are done with all lines in the file
        if not line:
            break
        # you can access the line
        store_name = extractNames(line.strip())

        print(store_name)
        csvwriter.writerow([store_name])

    # close file
    f.close()
    csvfile.close()


if __name__ == "__main__":
    main()
