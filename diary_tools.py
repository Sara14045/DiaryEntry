#ave the  l made this function to save adiary entry in afile.  
def save_entry(file_name, entry_date, entry_text):
    #l use "a" to add new notes without deleting old notes.
    with open(file_name, "a") as file:
        #l use write to save the date and text in the file. file.write(entry_date +" -" + entry_text + "\n")
        file.write(entry_date + ":"+ entry_text + "\n")


#This function searches for diary entries by data.1
def search_entries(file_name, search_date):
     try:
          with open(file_name, "r") as file:
               found =False
               for line in file:
                 if line. startswith(search_date + ":"):
                     print(line.strip()) 
                     found = True
               if not found:          
                   print("No entries found.")  
     except FileNotFoundError:
        print("File not found.")                           
                