import csv
from html2rest import html2rest
from io import BytesIO as StringIO

#file_names = []
with open('ozols-help-csv.csv') as csvFile:
    rowsArray = list(csv.reader(csvFile))
    count = 0
    maxdepth = 6
    index_file = open("rst_files/index.rst", "w")
    index_file.write(".. Ozols-help documentation master file, created by" + chr(13))
    index_file.write("   sphinx-quickstart on Fri Jun 26 09:37:44 2020." + chr(13))
    index_file.write("   You can adapt this file completely to your liking, but it should at least" + chr(13))
    index_file.write("   contain the root `toctree` directive." + chr(13))
    index_file.write(" " + chr(13))
    index_file.write("=============================" + chr(13))
    index_file.write("OZOLS palīdzības sistēma" + chr(13))
    index_file.write("=============================" + chr(13))
    index_file.write("Programma OZOLS izmanto klientservera datu apstrādes tehnoloģiju. Datu bāzes vadību veic SQL serveris, nodrošinot efektīvu datu apstrādi un drošību. Datu bāzi nevar nesankcionēti kopēt vai sabojāt, un dati nav pakļauti vīrusu uzbrukumiem. Sistēmas darbam nav nepieciešams nepārtraukts savienojums ar serveri, jo programma automātiski atjauno savienojumu, ja tas uz laiku ir bijis pārtraukts." + chr(13))
    index_file.write(" " + chr(13))
    index_file.write(".. toctree::" + chr(13))
    index_file.write("   :maxdepth: " + str(maxdepth) + chr(13))    
    index_file.write(" " + chr(13))
    
    def parse_rst(row):
        param_array = ["","","","","","", ""]
        
        ozols_id = str(row[0])   
        ssw_id = str(row[2]) 
        skf_id = str(row[3]) 
        parent_id = str(row[1])
        html_code = str(row[5])
        caption = str(row[4])
        
        ozols_id = ozols_id.strip()
        ssw_id = ssw_id.strip()
        skf_id = skf_id.strip()
        parent_id = parent_id.strip()
        html_code = html_code.strip()
        caption = caption.strip()
        
        rst_name = skf_id
        #rst_name = rst_name.replace(" / ", "_")
        #rst_name = rst_name.replace(" \ ", "_")
        #rst_name = rst_name.replace("/", "_")
        #rst_name = rst_name.replace("\\" , "_")
        #rst_name = rst_name.replace(". ", "_")
        #rst_name = rst_name.replace(".", "_")
        #rst_name = rst_name.replace(":", "") 
        #rst_name = rst_name.replace("(", "")
        #rst_name = rst_name.replace(")", "")
        #rst_name = rst_name.replace(" ", "_")
        #rst_name = rst_name.lower()
        
        html_code = html_code.replace("_x000D_", "") #chr(13))
        html_code = html_code.replace("\\", "-=+=")
        html_code = html_code.replace("-=+=-=+=", "\\")
        html_code = html_code.replace("-=+=", "\\")   
    
        param_array[0] = ozols_id
        param_array[1] = ssw_id
        param_array[2] = skf_id
        param_array[3] = parent_id
        param_array[4] = html_code
        param_array[5] = caption
        param_array[6] = rst_name
        
        return(param_array)    
    
    #def rst_hierachy(param_array, param_array2):
        
    
    
    for row in rowsArray:
        if count != 0:            
            param_array = parse_rst(row)
            
            if param_array[3] == "0":
                index_file.write("   " + param_array[6] + ".rst" + chr(13))
                f = open("rst_files/" + param_array[6] + ".rst", "w+")
                f.write(".. " + param_array[6] + chr(13))
                f.write(" " + chr(13))
                header_sep = ""
                for i in range(len(param_array[5])+4):
                    header_sep = header_sep + "="
                f.write(header_sep + chr(13))
                f.write(param_array[5] + chr(13))
                f.write(header_sep + chr(13))
                f.write(" " + chr(13))              
                stream = StringIO()
                html2rest(param_array[4], writer = stream)
                f.write(stream.getvalue().decode("utf8") + chr(13))
                f.write(" " + chr(13))
                
                isParent = False
                for row_child in rowsArray:
                    param_array2 = parse_rst(row_child)
                    maxdepth = 6
                    if param_array2[3] == param_array[2]:                                    
                        isParent = True
                
                if isParent == True:
                    f.write(".. toctree::" + chr(13))
                    f.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                    f.write(" " + chr(13))
                
                for row_child in rowsArray:                    
                    param_array2 = parse_rst(row_child)
                    maxdepth = 6
                    isParent = False
                    if param_array2[3] == param_array[2]:
                        isParent = True
                        maxdepth -= 1
                        if isParent == True:
                            f.write("   " + param_array2[6] + ".rst" + chr(13))
                            f2 = open("rst_files/" + param_array2[6] + ".rst", "w+")
                            f2.write(".. " + param_array2[6] + chr(13))
                            f2.write(" " + chr(13))
                            header_sep = ""
                            for i in range(len(param_array2[5])+4):
                                header_sep = header_sep + "="
                            f2.write(header_sep + chr(13))
                            f2.write(param_array2[5] + chr(13))
                            f2.write(header_sep + chr(13))
                            f2.write(" " + chr(13))            
                            stream2 = StringIO()
                            html2rest(param_array2[4], writer = stream2)
                            f2.write(stream2.getvalue().decode("utf8") + chr(13))
                            f2.write(" " + chr(13))
                            
                            isParent = False
                            for row_child2 in rowsArray:
                                param_array3 = parse_rst(row_child2)
                                maxdepth = 5
                                if param_array3[3] == param_array2[2]:                                    
                                    isParent = True
                            
                            if isParent == True:
                                f2.write(".. toctree::" + chr(13))
                                f2.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                                f2.write(" " + chr(13))
                            for row_child2 in rowsArray:                    
                                param_array3 = parse_rst(row_child2)
                                maxdepth = 5
                                isParent = False
                                if param_array3[3] == param_array2[2]:
                                    isParent = True
                                    maxdepth -= 1
                                    if isParent == True:
                                        f2.write("   " + param_array3[6] + ".rst" + chr(13))
                                        f3 = open("rst_files/" + param_array3[6] + ".rst", "w+")
                                        f3.write(".. " + param_array3[6] + chr(13))
                                        f3.write(" " + chr(13))
                                        header_sep = ""
                                        for i in range(len(param_array3[5])+4):
                                            header_sep = header_sep + "="
                                        f3.write(header_sep + chr(13))
                                        f3.write(param_array3[5] + chr(13))
                                        f3.write(header_sep + chr(13))
                                        f3.write(" " + chr(13))              
                                        #if param_array3[6] != "14066" and param_array3[6] != "721": 
                                        stream3 = StringIO()
                                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++" + chr(13))
                                        print(param_array3[6] + chr(13))
                                        print(param_array3[4] + chr(13))
                                        html2rest(param_array3[4], writer = stream3)
                                        f3.write(stream3.getvalue().decode("utf8") + chr(13))
                                        f3.write(" " + chr(13))
                                        
                                        isParent = False
                                        for row_child3 in rowsArray:
                                            param_array4 = parse_rst(row_child3)
                                            maxdepth = 4
                                            if param_array4[3] == param_array3[2]:                                    
                                                isParent = True
                                        
                                        if isParent == True:
                                            f3.write(".. toctree::" + chr(13))
                                            f3.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                                            f3.write(" " + chr(13))
                                           
                                        for row_child3 in rowsArray:                    
                                            param_array4 = parse_rst(row_child3)
                                            maxdepth = 4
                                            isParent = False
                                            if param_array4[3] == param_array3[2]:
                                                isParent = True
                                                maxdepth -= 1
                                                if isParent == True:
                                                    f3.write("   " + param_array4[6] + ".rst" + chr(13))
                                                    f4 = open("rst_files/" + param_array4[6] + ".rst", "w+")
                                                    f4.write(".. " + param_array4[6] + chr(13))
                                                    f4.write(" " + chr(13))
                                                    header_sep = ""
                                                    for i in range(len(param_array4[5])+4):
                                                        header_sep = header_sep + "="
                                                    f4.write(header_sep + chr(13))
                                                    f4.write(param_array4[5] + chr(13))
                                                    f4.write(header_sep + chr(13))
                                                    f4.write(" " + chr(13))           
                                                    stream4 = StringIO()
                                                    html2rest(param_array4[4], writer = stream4)
                                                    f4.write(stream4.getvalue().decode("utf8") + chr(13))
                                                    f4.write(" " + chr(13))                                        

                                                    isParent = False
                                                    for row_child4 in rowsArray:
                                                        param_array5 = parse_rst(row_child4)
                                                        maxdepth = 3
                                                        if param_array5[3] == param_array4[2]:                                    
                                                            isParent = True
                                                    
                                                    if isParent == True:
                                                        f4.write(".. toctree::" + chr(13))
                                                        f4.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                                                        f4.write(" " + chr(13))
                                                    for row_child4 in rowsArray:                    
                                                        param_array5 = parse_rst(row_child4)
                                                        maxdepth = 3
                                                        isParent = False
                                                        if param_array5[3] == param_array4[2]:
                                                            isParent = True
                                                            maxdepth -= 1
                                                            if isParent == True:
                                                                f4.write("   " + param_array5[6] + ".rst" + chr(13))
                                                                f5 = open("rst_files/" + param_array5[6] + ".rst", "w+")
                                                                f5.write(".. " + param_array5[6] + chr(13))
                                                                f5.write(" " + chr(13))
                                                                header_sep = ""
                                                                for i in range(len(param_array5[5])+4):
                                                                    header_sep = header_sep + "="
                                                                f5.write(header_sep + chr(13))
                                                                f5.write(param_array5[5] + chr(13))
                                                                f5.write(header_sep + chr(13))
                                                                f5.write(" " + chr(13))
                                                                stream5 = StringIO()
                                                                html2rest(param_array5[4], writer = stream5)
                                                                f5.write(stream5.getvalue().decode("utf8") + chr(13))
                                                                f5.write(" " + chr(13)) 
                                                                
                                                                
                                                                isParent = False
                                                                for row_child5 in rowsArray:
                                                                    param_array6 = parse_rst(row_child5)
                                                                    maxdepth = 2
                                                                    if param_array5[3] == param_array5[2]:                                    
                                                                        isParent = True
                                                                
                                                                if isParent == True:
                                                                    f5.write(".. toctree::" + chr(13))
                                                                    f5.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                                                                    f5.write(" " + chr(13))
                                                                for row_child5 in rowsArray:                    
                                                                    param_array6 = parse_rst(row_child5)
                                                                    maxdepth = 2
                                                                    isParent = False
                                                                    if param_array6[3] == param_array5[2]:
                                                                        isParent = True
                                                                        maxdepth -= 1
                                                                        if isParent == True:
                                                                            f5.write("   " + param_array6[6] + ".rst" + chr(13))
                                                                            f6 = open("rst_files/" + param_array6[6] + ".rst", "w+")
                                                                            f6.write(".. " + param_array6[6] + chr(13))
                                                                            f6.write(" " + chr(13))
                                                                            header_sep = ""
                                                                            for i in range(len(param_array6[5])+4):
                                                                                header_sep = header_sep + "="
                                                                            f6.write(header_sep + chr(13))
                                                                            f6.write(param_array6[5] + chr(13))
                                                                            f6.write(header_sep + chr(13))
                                                                            f6.write(" " + chr(13))              
                                                                            stream6 = StringIO()
                                                                            html2rest(param_array6[4], writer = stream6)
                                                                            f6.write(stream6.getvalue().decode("utf8") + chr(13))
                                                                            f6.write(" " + chr(13))                                                                 
                                                                
                                                                            f6.close()
                                                                f5.close()
                                                    f4.close()            
                                        f3.close()                            
                            f2.close()
                f.close()
          
        count += 1
        #if count > 3:
           # break
    #print(count)   
    #index_file.write(" " + chr(13))
    #index_file.write("Indices and tables" + chr(13))
    #index_file.write("==================" + chr(13))
    #index_file.write(" " + chr(13))
    #index_file.write("* :ref:`genindex`" + chr(13))
    #index_file.write("* :ref:`modindex`" + chr(13))
    #index_file.write("* :ref:`search`" + chr(13))
    #index_file.close()    
csvFile.close()          