import os

class PCFG:
    def __init__(self, corpus):
        with open(file=os.getcwd() + "/upload/" + corpus, mode="r", encoding="utf-8") as corpus_reader:
            sentences = corpus_reader.readlines()
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
            tag = []
            for i in results:
                for j in results[i]:
                    if j != "" and len(j.split("*")) == 1:
                        tag.append(i + " -> " + j + " [" + str(results[i][j]) + "]")
            print(results)
            # rules = {}
            # with open(file=os.getcwd() + "/pcfg/tag.txt", mode="r", encoding="utf-8") as count_tag_reader:
            #     data = count_tag_reader.readlines()
            #     for i in data:
            #         symbol = i.split(" -> ")
            #         temp = symbol[1].split(" [")
            #         key = temp[0]
            #         value = int(temp[1].replace("]", ""))
            #         try:
            #             rules[symbol[0]][key] = value
            #         except KeyError:
            #             rules[symbol[0]] = {}
            #             rules[symbol[0]][key] = value
            # pcfg_temp = {}
            # for i in rules:
            #     total = 0
            #     for j in rules[i]:
            #         total += rules[i][j]
            #     for j in rules[i]:
            #         try:
            #             pcfg_temp[i][j] = float(rules[i][j] / total)
            #         except KeyError:
            #             pcfg_temp[i] = {}
            #             pcfg_temp[i][j] = float(rules[i][j] / total)
            # with open(file=os.getcwd() + "/pcfg/pcfg.txt", mode="w+", encoding="utf-8") as pcfg_writer:
            #     special_char = [":", "-", "&", '"', "'", "%", "+", "/", "?", ";", "$", "Γö£├⌐Γö¼├║"]
            #     for i in pcfg_temp['S']:
            #         pcfg_writer.write("S -> %s [%s]\n" % (i, pcfg_temp['S'][i]))
            #     for i in pcfg_temp:
            #         if i != "S":
            #             for j in pcfg_temp[i]:
            #                 v = "{:.5f}".format(pcfg_temp[i][j])
            #                 if j.islower() or j.isdigit() or len(j.split(',')) > 1 or len(
            #                         j.split('.')) > 1 or j in special_char:
            #                     if len(j.split("'")) > 1:
            #                         pcfg_writer.write("%s -> \"%s\" [%s]\n" % (i, j, v))
            #                     else:
            #                         pcfg_writer.write("%s -> \'%s\' [%s]\n" % (i, j, v))
            #                 else:
            #                     pcfg_writer.write("%s -> %s [%s]\n" % (i, j, v))
