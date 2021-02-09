import os
import os.path

def replace_text (file_name, old_string, new_string):
    if os.path.exists ( file_name ):
        # open file in read mode
        file = open ( file_name, "r" )
        replaced_content = ""
        # looping through the file
        for line in file:
            # stripping line break
            line = line.strip ()
            # replacing the texts
            new_line = line.replace ( old_string, new_string )
            # concatenate the new string and add an end-line break
            replaced_content = replaced_content + new_line + "\n"

        # close the file
        file.close ()
        # Open file in write mode
        write_file = open ( file_name, "w" )
        # overwriting the old file contents with the new/replaced content
        write_file.write ( replaced_content )
        # close the file
        write_file.close ()
    else:
        print("An error occurred")


def delete_file(name):
    try:
        os.remove ( name )
    except:
        return  False
    return True


while True:
    line = input()
    if line == "End":
        break
    command, *other = line.split('-')
    file_name = other[0]
    if command=='Create':
        with open ( file_name, 'w' ) as f:
            f.write ( '' )
    elif command=='Add':
        content = other[1]
        with open ( file_name, 'a' ) as f:
            f.write ( content +'\n')
    elif command=='Replace':
        old_string = other[1]
        new_string= other[2]
        replace_text ( file_name, old_string, new_string )
        # if os.path.exists(file_name):
        #     with open ( file_name, 'r+' ) as f:
        #         for line in f:
        #             # current_line = str(line)
        #             print(line)

    elif command=='Delete':
        if not delete_file(file_name):
            print("An error occurred")