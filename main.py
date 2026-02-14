import os
while True:
    print('''
          ---------------------
          1. Create File & Write
          2. Read your file
          3. Update your file
          4. Delete your file
          5. Exit
          ---------------------''')
    user =input('Enter Your Choice:')
    
    # Main Logic
    if user == '1' : # user can create file and write there task
        file_name = input('Enter Your File Name with Extension:')
        user_activity = input('Your Task:')
        file = open(file_name, 'x')
        file.write(user_activity)
        file.close()
        print(f'Your Task is save Successfully in {file_name} file')


    elif user == '2':# User can read there task.
        Rfile_name = input('Enter your file name with extension :')
        if os.path.exists(Rfile_name):
            FileData = open(Rfile_name)
            print(FileData.readline())
            FileData.close()
        else:
            print(f'The {Rfile_name} file are no Available .')

    elif user == '3':# User update there task. 
        Ufile_name = input('Enter your file name with extension :')
        updateText = input('Update Your Task :')
        if os.path.exists(Ufile_name):
            UpdateFile = open(Ufile_name, 'a', encoding='utf-8')
            text =UpdateFile.write(updateText)
            UpdateFile.close()
            print('Updated Successfully')
        else:
            print(f'{Ufile_name} file are no Available . ')

    elif user == '4' : # User can delete there file
        Dfile = input('Enter your file name with extension:')
        if os.path.exists(Dfile):
            os.remove(Dfile)
            print(f'{Dfile} Deleted Successfully.')

    elif user == '5':# exit
        break
