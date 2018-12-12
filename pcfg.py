import sys
from os import getcwd
from optparse import OptionParser


def pcfg(argv):
    print("Probabilistic Context-Free Grammar (Ajie Pangestu | Made with ❤ using Python 3.6.6)")
    parser = OptionParser()
    parser.add_option("-d", "--data=", dest="data",
                      help="PATH of Data File", metavar="PATH of Data File")

    (options, args) = parser.parse_args(argv)
    if options.data:
        with open(file=options.data, mode="r", encoding="utf-8") as data_reader:
            sentences = data_reader.readlines()
            s = []
            current = []
            results = {}
            temp_string = ''
            for line in sentences:
                count = 0
                for char in line:
                    count += 1
                    if char == '(':
                        if len(temp_string):
                            current.append(temp_string)
                            temp_string = ''
                        s.append(current)
                        current = []
                    elif char == ')':
                        if len(temp_string):
                            current.append(temp_string)
                            temp_string = ''
                        left = current[0]
                        if len(current) == 2:
                            right = current[1]
                        else:
                            right = ' '.join(current[1:])
                        if left not in results:
                            results[left] = {}
                        if right not in results[left]:
                            results[left][right] = 0
                        results[left][right] += 1
                        tmp = current[0]
                        current = s.pop()
                        current.append(tmp)
                    elif char == ' ':
                        if len(temp_string):
                            current.append(temp_string)
                            temp_string = ''
                    else:
                        temp_string += char

            with open(file=getcwd() + "/pcfg/tag.txt", mode="w+", encoding="utf-8") as count_tag_writer:
                for i in results:
                    for j in results[i]:
                        if j != "" and len(j.split("*")) == 1:
                            count_tag_writer.write(i + " -> " + j + " [" + str(results[i][j]) + "]\n")
            rules = {}
            with open(file=getcwd() + "/pcfg/tag.txt", mode="r", encoding="utf-8") as count_tag_reader:
                data = count_tag_reader.readlines()
                print("PCFG Total\t\t: " + str(len(data)))
                log = "PCFG Total\t\t: " + str(len(data))
                for i in data:
                    symbol = i.split(" -> ")
                    temp = symbol[1].split(" [")
                    key = temp[0]
                    value = int(temp[1].replace("]\n", ""))
                    try:
                        rules[symbol[0]][key] = value
                    except KeyError:
                        rules[symbol[0]] = {}
                        rules[symbol[0]][key] = value
            pcfg_temp = {}
            for i in rules:
                total = 0
                for j in rules[i]:
                    total += rules[i][j]
                for j in rules[i]:
                    try:
                        pcfg_temp[i][j] = float(rules[i][j] / total)
                    except KeyError:
                        pcfg_temp[i] = {}
                        pcfg_temp[i][j] = float(rules[i][j] / total)
            with open(file=getcwd() + "/pcfg/pcfg.txt", mode="w+", encoding="utf-8") as pcfg_writer:
                special_char = [":", "-", "&", '"', "'", "%", "+", "/", "?", ";", "$", "Γö£├⌐Γö¼├║"]
                for i in pcfg_temp['S']:
                    pcfg_writer.write("S -> %s [%s]\n" % (i, pcfg_temp['S'][i]))
                for i in pcfg_temp:
                    if i != "S":
                        for j in pcfg_temp[i]:
                            v = "{:.5f}".format(pcfg_temp[i][j])
                            # v = f'pcfg[i][j]:.5f'
                            if j.islower() or j.isdigit() or len(j.split(',')) > 1 or len(
                                    j.split('.')) > 1 or j in special_char:
                                if len(j.split("'")) > 1:
                                    pcfg_writer.write("%s -> \"%s\" [%s]\n" % (i, j, v))
                                else:
                                    pcfg_writer.write("%s -> \'%s\' [%s]\n" % (i, j, v))
                            else:
                                pcfg_writer.write("%s -> %s [%s]\n" % (i, j, v))
            with open(file=getcwd() + "/log/pcfg_log.txt", mode="w+", encoding="utf-8") as log_writer:
                log_writer.write(log)
    else:
        print("Usage : pcfg.py -d <PATH of Data File>")
        sys.exit()


if __name__ == '__main__':
    pcfg(sys.argv[1:])
