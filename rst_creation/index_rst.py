import csv
from html2rest import html2rest
from io import BytesIO as StringIO
from bs4 import BeautifulSoup as bs
import time
import os.path

#import bs4
start_time = time.time()
img_dir = "images_ozols/"
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
            param_array = parse_csv(row)
            
            if param_array[3] == "0":
                index_file.write("   " + param_array[6] + ".rst" + chr(13))
                f = open("rst_files/" + param_array[6] + ".rst", "w+")
                f.write(".. " + param_array[6] + chr(13))
                f.write(" " + chr(13))
                header_sep = ""
                for i in range(len(param_array[5])+4):
                    header_sep = header_sep + "="
                #f.write(header_sep + chr(13))
                f.write(param_array[5] + chr(13))
                f.write(header_sep + chr(13))
                f.write(" " + chr(13))         
                stream = StringIO()
                soup = None
                soup = bs(param_array[4], "html.parser")
                images = soup.findAll('img')
                print(param_array[2])
                
                for image in images:
                    img_start_pos =  param_array[4].find(image["src"]) - 10
                    img_end_pos  =  param_array[4].find(">", img_start_pos)  
                    img_id = image["src"][image["src"].find("=") + 1:]
                    print("IMAGE ID:  " + str(img_id))        
                    img_file = img_dir + img_id + ".png"
                    if os.path.isfile(img_file) == False:
                        img_file = img_dir + img_id + ".jpg"    
                        if os.path.isfile(img_file) == False:
                            img_file = img_dir + img_id + ".gif"  
                            if os.path.isfile(img_file) == False:
                                img_file = img_dir + img_id + ".PNG"    
                                if os.path.isfile(img_file) == False:
                                    img_file = img_dir + img_id + ".JPG"
                                    if os.path.isfile(img_file) == False:
                                        img_file = img_dir + img_id + ".GIF"                            
                    param_array[4] = param_array[4] + "<br> .. " + "|" + img_file + "|  image:: " + img_file + " <br /> :scale: 100%<br />" 
                    param_array[4] = param_array[4].replace(param_array[4][ img_start_pos : img_end_pos+1 ], " |" + img_file + "| ", 1)
                    #param_array[4] = param_array[4].replace(param_array[4][ img_start_pos : img_end_pos+1 ], ".. image:: " + img_file + " <br /> :scale: 100% <br />", 1)                                          
                html2rest(param_array[4], writer = stream)
                rst_code = stream.getvalue().decode("utf8")
                rst_code = rst_code.replace(".. image:: " , chr(13) +"" + chr(13) +"  .. image:: ")                 
                rst_code = rst_code.replace(":scale: 100%" , "       :scale: 100%") 
                f.write(rst_code + chr(13))
                f.write(" " + chr(13))
                
                isParent = False
                for row_child in rowsArray:
                    param_array2 = parse_csv(row_child)
                    maxdepth = 6
                    if param_array2[3] == param_array[2]:                                    
                        isParent = True
                
                if isParent == True:
                    f.write(".. toctree::" + chr(13))
                    f.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                    f.write(" " + chr(13))
                
                for row_child in rowsArray:                    
                    param_array2 = parse_csv(row_child)
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
                            soup = None
                            soup = bs(param_array2[4], "html.parser")
                            images = soup.findAll('img')
                            print(param_array2[2])
                            if param_array2[2] == "14033":
                                print(images)    
                            for image in images:
                                img_start_pos =  param_array2[4].find(image["src"]) - 10
                                img_end_pos  =  param_array2[4].find(">", img_start_pos) 
                                img_id = image["src"][image["src"].find("=") + 1:]
                                print("IMAGE ID:  " + str(img_id))        
                                img_file = img_dir + img_id + ".png"
                                if os.path.isfile(img_file) == False:
                                    img_file = img_dir + img_id + ".jpg"    
                                    if os.path.isfile(img_file) == False:
                                        img_file = img_dir + img_id + ".gif" 
                                        if os.path.isfile(img_file) == False:
                                            img_file = img_dir + img_id + ".PNG"    
                                            if os.path.isfile(img_file) == False:
                                                img_file = img_dir + img_id + ".JPG"
                                                if os.path.isfile(img_file) == False:
                                                    img_file = img_dir + img_id + ".GIF"


                                param_array2[4] = param_array2[4] + "<br> .. " + "|" + img_file + "|  image:: " + img_file + " <br /> :scale: 100% <br />"        
                                param_array2[4] = param_array2[4].replace(param_array2[4][ img_start_pos : img_end_pos+1 ], " |" + img_file + "| ", 1)                                          
                                #param_array2[4] = param_array2[4].replace(param_array2[4][ img_start_pos : img_end_pos+1 ], ".. image:: " + img_file + " <br /> :scale: 100% <br />", 1)                                          
                            html2rest(param_array2[4], writer = stream2)
                            rst_code = stream2.getvalue().decode("utf8") 
                            rst_code = rst_code.replace(".. image:: " , chr(13) +"" + chr(13) +"  .. image:: ") 
                            rst_code = rst_code.replace(":scale: 100%" , "       :scale: 100%") 
                            f2.write(rst_code + chr(13))
                            f2.write(" " + chr(13))
                            
                            isParent = False
                            for row_child2 in rowsArray:
                                param_array3 = parse_csv(row_child2)
                                maxdepth = 5
                                if param_array3[3] == param_array2[2]:                                    
                                    isParent = True
                            
                            if isParent == True:
                                f2.write(".. toctree::" + chr(13))
                                f2.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                                f2.write(" " + chr(13))
                            for row_child2 in rowsArray:                    
                                param_array3 = parse_csv(row_child2)
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
                                            header_sep = header_sep + "*"
                                        #f3.write(header_sep + chr(13))
                                        f3.write(param_array3[5] + chr(13))
                                        f3.write(header_sep + chr(13))
                                        f3.write(" " + chr(13))              
                                        #if param_array3[6] != "14066" and param_array3[6] != "721": 
                                        stream3 = StringIO()
                                        soup = None
                                        soup = bs(param_array3[4], "html.parser")
                                        images = soup.findAll('img')
                                        print(param_array3[2])
                                        for image in images:
                                            img_start_pos =  param_array3[4].find(image["src"]) - 10
                                            img_end_pos  =  param_array3[4].find(">", img_start_pos)
                                            img_id = image["src"][image["src"].find("=") + 1:]
                                            print("IMAGE ID:  " + str(img_id))        
                                            img_file = img_dir + img_id + ".png"
                                            if os.path.isfile(img_file) == False:
                                                img_file = img_dir + img_id + ".jpg"    
                                                if os.path.isfile(img_file) == False:
                                                    img_file = img_dir + img_id + ".gif" 
                                                    if os.path.isfile(img_file) == False:
                                                        img_file = img_dir + img_id + ".PNG"    
                                                        if os.path.isfile(img_file) == False:
                                                            img_file = img_dir + img_id + ".JPG"
                                                            if os.path.isfile(img_file) == False:
                                                                img_file = img_dir + img_id + ".GIF"
                                            param_array3[4] = param_array3[4] + "<br> .. " + "|" + img_file + "|  image:: " + img_file + " <br />:scale: 100% <br />"        
                                            param_array3[4] = param_array3[4].replace(param_array3[4][ img_start_pos : img_end_pos+1 ], " |" + img_file + "| ", 1)                                          
                                            #param_array3[4] = param_array3[4].replace(param_array3[4][ img_start_pos : img_end_pos+1 ], ".. image:: " + img_file + " <br /> :scale: 100% <br />", 1)  
                                        html2rest(param_array3[4], writer = stream3)
                                        rst_code = stream3.getvalue().decode("utf8") 
                                        rst_code = rst_code.replace(".. image:: " , chr(13) +"" + chr(13) +"  .. image:: ") 
                                        rst_code = rst_code.replace(":scale: 100%" , "       :scale: 100%") 
                                        f3.write(rst_code + chr(13))
                                        f3.write(" " + chr(13))
                                        
                                        isParent = False
                                        for row_child3 in rowsArray:
                                            param_array4 = parse_csv(row_child3)
                                            maxdepth = 4
                                            if param_array4[3] == param_array3[2]:                                    
                                                isParent = True
                                        
                                        if isParent == True:
                                            f3.write(".. toctree::" + chr(13))
                                            f3.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                                            f3.write(" " + chr(13))
                                           
                                        for row_child3 in rowsArray:                    
                                            param_array4 = parse_csv(row_child3)
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
                                                        header_sep = header_sep + "*"
                                                  #  f4.write(header_sep + chr(13))
                                                    f4.write(param_array4[5] + chr(13))
                                                    f4.write(header_sep + chr(13))
                                                    f4.write(" " + chr(13))           
                                                    stream4 = StringIO()
                                                    soup = None
                                                    soup = bs(param_array4[4], "html.parser")
                                                    images = soup.findAll('img')
                                                    print(param_array4[2])
                                                    for image in images:
                                                        img_start_pos =  param_array4[4].find(image["src"]) - 10
                                                        img_end_pos  =  param_array4[4].find(">", img_start_pos)
                                                        img_id = image["src"][image["src"].find("=") + 1:]
                                                        print("IMAGE ID:  " + str(img_id))        
                                                        img_file = img_dir + img_id + ".png"
                                                        if os.path.isfile(img_file) == False:
                                                            img_file = img_dir + img_id + ".jpg"    
                                                            if os.path.isfile(img_file) == False:
                                                                img_file = img_dir + img_id + ".gif"
                                                                if os.path.isfile(img_file) == False:
                                                                    img_file = img_dir + img_id + ".PNG"    
                                                                    if os.path.isfile(img_file) == False:
                                                                        img_file = img_dir + img_id + ".JPG"
                                                                        if os.path.isfile(img_file) == False:
                                                                            img_file = img_dir + img_id + ".GIF"                                                                
                                                        param_array4[4] = param_array4[4] + "<br> .. " + "|" + img_file + "|  image:: " + img_file + " <br /> :scale: 100% <br />"        
                                                        param_array4[4] = param_array4[4].replace(param_array4[4][ img_start_pos : img_end_pos+1 ], " |" + img_file + "| ", 1)                                          
                                                        #param_array4[4] = param_array4[4].replace(param_array4[4][ img_start_pos : img_end_pos+1 ], ".. image:: " + img_file + " <br /> :scale: 100% <br />", 1)                                                                 
                                                    html2rest(param_array4[4], writer = stream4)
                                                    rst_code = stream4.getvalue().decode("utf8") 
                                                    rst_code = rst_code.replace(".. image:: " , chr(13) +"" + chr(13) +"  .. image:: ") 
                                                    rst_code = rst_code.replace(":scale: 100%" , "       :scale: 100%") 
                                                    f4.write(rst_code + chr(13))
                                                    f4.write(" " + chr(13))                                        

                                                    isParent = False
                                                    for row_child4 in rowsArray:
                                                        param_array5 = parse_csv(row_child4)
                                                        maxdepth = 3
                                                        if param_array5[3] == param_array4[2]:                                    
                                                            isParent = True
                                                    
                                                    if isParent == True:
                                                        f4.write(".. toctree::" + chr(13))
                                                        f4.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                                                        f4.write(" " + chr(13))
                                                    for row_child4 in rowsArray:                    
                                                        param_array5 = parse_csv(row_child4)
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
                                                                    header_sep = header_sep + "*"
                                                                #f5.write(header_sep + chr(13))
                                                                f5.write(param_array5[5] + chr(13))
                                                                f5.write(header_sep + chr(13))
                                                                f5.write(" " + chr(13))
                                                                stream5 = StringIO()
                                                                soup = None
                                                                soup = bs(param_array5[4], "html.parser")
                                                                images = soup.findAll('img')
                                                                print(param_array5[2])
                                                                for image in images:
                                                                    img_start_pos =  param_array5[4].find(image["src"]) - 10
                                                                    img_end_pos  =  param_array5[4].find(">", img_start_pos)
                                                                    img_id = image["src"][image["src"].find("=") + 1:]
                                                                    print("IMAGE ID:  " + str(img_id))        
                                                                    img_file = img_dir + img_id + ".png"
                                                                    if os.path.isfile(img_file) == False:
                                                                        img_file = img_dir + img_id + ".jpg"    
                                                                        if os.path.isfile(img_file) == False:
                                                                            img_file = img_dir + img_id + ".gif"
                                                                            if os.path.isfile(img_file) == False:
                                                                                img_file = img_dir + img_id + ".PNG"    
                                                                                if os.path.isfile(img_file) == False:
                                                                                    img_file = img_dir + img_id + ".JPG"
                                                                                    if os.path.isfile(img_file) == False:
                                                                                        img_file = img_dir + img_id + ".GIF"
                                                                    param_array5[4] = param_array5[4] + "<br> .. " + "|" + img_file + "|  image:: " + img_file + " <br /> :scale: 100%<br />"        
                                                                    param_array5[4] = param_array5[4].replace(param_array5[4][ img_start_pos : img_end_pos+1 ], " |" + img_file + "| ", 1)                                          
                                                                    #param_array5[4] = param_array5[4].replace(param_array5[4][ img_start_pos : img_end_pos+1 ], ".. image:: " + img_file + " <br /> :scale: 100% <br />", 1)   
                                                                html2rest(param_array5[4], writer = stream5)
                                                                rst_code = stream5.getvalue().decode("utf8") 
                                                                rst_code = rst_code.replace(".. image:: " , chr(13) +"" + chr(13) +"  .. image:: ") 
                                                                rst_code = rst_code.replace(":scale: 100%" , "       :scale: 100%") 
                                                                f5.write(rst_code + chr(13))
                                                                f5.write(" " + chr(13)) 
                                                                
                                                                
                                                                isParent = False
                                                                for row_child5 in rowsArray:
                                                                    param_array6 = parse_csv(row_child5)
                                                                    maxdepth = 2
                                                                    if param_array5[3] == param_array5[2]:                                    
                                                                        isParent = True
                                                                
                                                                if isParent == True:
                                                                    f5.write(".. toctree::" + chr(13))
                                                                    f5.write("   :maxdepth: "+ str(maxdepth) + chr(13)) 
                                                                    f5.write(" " + chr(13))
                                                                for row_child5 in rowsArray:                    
                                                                    param_array6 = parse_csv(row_child5)
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
                                                                                header_sep = header_sep + "*"
                                                                            #f6.write(header_sep + chr(13))
                                                                            f6.write(param_array6[5] + chr(13))
                                                                            f6.write(header_sep + chr(13))
                                                                            f6.write(" " + chr(13))              
                                                                            stream6 = StringIO()
                                                                            soup = None
                                                                            soup = bs(param_array6[4], "html.parser")
                                                                            images = soup.findAll('img')
                                                                            print(param_array6[2])
                                                                            for image in images:
                                                                                img_start_pos =  param_array6[4].find(image["src"]) - 10
                                                                                img_end_pos  =  param_array6[4].find(">", img_start_pos)
                                                                                img_id = image["src"][image["src"].find("=") + 1:]
                                                                                print("IMAGE ID:  " + str(img_id))        
                                                                                img_file = img_dir + img_id + ".png"
                                                                                if os.path.isfile(img_file) == False:
                                                                                    img_file = img_dir + img_id + ".jpg"    
                                                                                    if os.path.isfile(img_file) == False:
                                                                                        img_file = img_dir + img_id + ".gif"
                                                                                        if os.path.isfile(img_file) == False:
                                                                                            img_file = img_dir + img_id + ".PNG"    
                                                                                            if os.path.isfile(img_file) == False:
                                                                                                img_file = img_dir + img_id + ".JPG"
                                                                                                if os.path.isfile(img_file) == False:
                                                                                                    img_file = img_dir + img_id + ".GIF"
                                                                                        
                                                                                param_array6[4] = param_array6[4] + "<br> .. " + "|" + img_file + "|  image:: " + img_file + " <br /> :scale: 100% <br />"        
                                                                                param_array6[4] = param_array6[4].replace(param_array6[4][ img_start_pos : img_end_pos+1 ], " |" + img_file + "| ", 1)                                          
                                                                                #param_array6[4] = param_array6[4].replace(param_array6[4][ img_start_pos : img_end_pos+1 ], ".. image:: " + img_file + " <br /> :scale: 100% <br />", 1)  
                                                                            html2rest(param_array6[4], writer = stream6)
                                                                            rst_code = stream6.getvalue().decode("utf8") 
                                                                            rst_code = rst_code.replace(".. image:: " , chr(13) +"" + chr(13) +"  .. image:: ") 
                                                                            rst_code = rst_code.replace(":scale: 100%" , "       :scale: 100%") 
                                                                            f6.write(rst_code + chr(13))
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
print("Execution time: " + str(time.time() - start_time))