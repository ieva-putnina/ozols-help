import csv

#file_names = []
with open('ozols-help-csv.csv') as csvFile:
    rowsArray = list(csv.reader(csvFile))
    count = 0
    for row in rowsArray:
        if count != 0: 
            ozols_id = (str(row[:-5])[2:-2])   
            ssw_id = (str(row[2:-3])[2:-2]) 
            skf_id = (str(row[3:-2])[2:-2]) 
            parent_id = (str(row[1:-4])[2:-2])
            html_code = (str(row[5:])[2:-2])
            caption = (str(row[4:-1])[2:-2])
            
            ozols_id = ozols_id.strip()
            ssw_id = ssw_id.strip()
            skf_id = skf_id.strip()
            html_code = html_code.strip()
            caption = caption.strip()
            
            html_code = html_code.replace("_x000D_", "") #chr(13))
            html_code = html_code.replace("\\", "-=+=")
            html_code = html_code.replace("-=+=-=+=", "\\")
            html_code = html_code.replace("-=+=", "\\")
            
            #ozols_id = ozols_id.replace(" / ", "_")
            #ozols_id = ozols_id.replace(" \ ", "_")
            #ozols_id = ozols_id.replace("/", "_")
            #ozols_id = ozols_id.replace("\\" , "_")
            #ozols_id = ozols_id.replace(". ", "_")
            #ozols_id = ozols_id.replace(".", "_")
            #ozols_id = ozols_id.replace(":", "") 
            #ozols_id = ozols_id.replace("(", "")
            #ozols_id = ozols_id.replace(")", "")
            #ozols_id = ozols_id.replace(" ", "_")
            #ozols_id = ozols_id.lower()
            #file_names.append(s)
            #if file_names.count(s) > 1:
                #s = s + "_" + str(file_names.count(s))
                      
            print(ozols_id)
            
            f = open("rst_files/" + ozols_id + ".rst", "w+")
            f.write("ssw_id = " + ssw_id + chr(13))
            f.write("skf_id = " + skf_id + chr(13))
            f.write("parent_id = " + parent_id + chr(13))
            f.write(caption + ";" + chr(13))
            f.write(html_code)
            f.close()
        count += 1
        #if count > 3:
           # break
    #print(count)      
csvFile.close()          