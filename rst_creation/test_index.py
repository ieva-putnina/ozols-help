import csv
from html2rest import html2rest
from io import BytesIO as StringIO
from bs4 import BeautifulSoup as bs
import time

param_array = {}
f = {}

#import bs4
start_time = time.time()
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
    
    def parse_csv(row):
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
        
        html_code = html_code.replace("_x000D_", "\n" + chr(13))
        html_code = html_code.replace("\\", "-=+=")
        html_code = html_code.replace("-=+=-=+=", "\\")
        html_code = html_code.replace("-=+=", "\\")   
        
        #print(html_code.find("IMG"))
       
       #soup = None
       #soup = bs(html_code, "html.parser")
        #print(soup)
        #images = None
        #images = soup.findAll('img')
        #print(skf_id)
        #for image in images:        
          #print(image["src"])
          #print("+++++++++++++++++++++++++++++++++++++++++++++")
        #print("===============================================")
        
        param_array[0] = ozols_id
        param_array[1] = ssw_id
        param_array[2] = skf_id
        param_array[3] = parent_id
        param_array[4] = html_code
        param_array[5] = caption
        param_array[6] = rst_name
        
        return(param_array)        
    
    for row in rowsArray:
        if count != 0:            
            param_array[1] = parse_csv(row)
            
            if param_array[1][3] == "0":
                index_file.write("   " + param_array[1][6] + ".rst" + chr(13))
                f[1] = open("rst_files/" + param_array[1][6] + ".rst", "w+")
                f[1].write(".. " + param_array[1][6] + chr(13))
                f[1].write(" " + chr(13))
                header_sep = ""
                for i in range(len(param_array[1][5])+4):
                    header_sep = header_sep + "="
                #f.write(header_sep + chr(13))
                f[1].write(param_array[1][5] + chr(13))
                f[1].write(header_sep + chr(13))
                f[1].write(" " + chr(13))              
                stream = StringIO()
                #soup = bs(param_array[4], "html.parser")
                #images = soup.findAll('img')
                #print(param_array[2])
                #for image in images:
                    #print(image["src"])
                    #print("+++++++++++++++++++++++++++++++++++++++++++++")
                
                #print("===============================================")                 
                html2rest(param_array[1][4], writer = stream)
                f[1].write(stream.getvalue().decode("utf8") + chr(13))
                f[1].write(" " + chr(13))
                
                for q in range(2,7,1):
                    isParent = False
                    for row_child in rowsArray:
                        param_array[q] = parse_csv(row_child)
                        maxdepth = 6-(q-2)
                        if param_array[q][3] == param_array[q-1][2]:                                    
                            isParent = True
                   
                    if isParent == True:
                        f[q-1].write(".. toctree::" + chr(13))
                        f[q-1].write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                        f[q-1].write(" " + chr(13))
                   
                    for row_child in rowsArray:                    
                        param_array[q] = parse_csv(row_child)
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
                        
                              
                               #f[q].close()
                   #f[q-1].close()
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

print(param_array)
print("Execution time: " + str(time.time() - start_time))