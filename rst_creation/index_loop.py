                param_array = []
                f = []
                row_child = []
                
                for q in range(2,6):
                    isParent = False
                    for row_child[q-1] in rowsArray:
                        param_array[q] = parse_rst(row_child[q-1])
                        maxdepth = 6-(q-2)
                        if param_array[q][3] == param_array[q-1][2]:                                    
                            isParent = True
                    
                    if isParent == True:
                        f[q-1].write(".. toctree::" + chr(13))
                        f[q-1].write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                        f[q-1].write(" " + chr(13))
                    
                    for row_child[q-1] in rowsArray:                    
                        param_array[q] = parse_rst(row_child[q-1])
                        maxdepth = 6-(q-2)
                        isParent = False
                        if param_array[q][3] == param_array[q-1][2]:
                            isParent = True
                            maxdepth -= 1
                            if isParent == True:
                                f[q-1].write("   " + param_array[q][6] + ".rst" + chr(13))
                                f[q] = open("rst_files/" + param_array[q][6] + ".rst", "w+")
                                f[q].write(".. " + param_array[q][6] + chr(13))
                                f[q].write(" " + chr(13))
                                header_sep = ""
                                for i in range(len(param_array[q][5])+4):
                                    header_sep = header_sep + "="
                                f[q].write(header_sep + chr(13))
                                f[q].write(param_array[q][5] + chr(13))
                                f[q].write(header_sep + chr(13))
                                f[q].write(" " + chr(13))
                                f[q].write(param_array[q][4] + chr(13))
                                f[q].write(" " + chr(13))
                                
                                f[q].close()
                    f[q-1].close()