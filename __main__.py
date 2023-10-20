import os
from difflib import SequenceMatcher
import Levenstein
dir1_name = "dir1"    
dir2_name = "dir2"

def read_directories():
    dir1_path = os.getcwd() + "/1C-otbor/" + dir1_name
    dir2_path = os.getcwd() + "/1C-otbor/" + dir2_name
    _, _, files1_names = next(os.walk("{}".format(dir1_path)))
    _, _, files2_names = next(os.walk("{}".format(dir2_path)))

    files_count1 = len(files1_names)
    files_count2 = len(files2_names)

    files1 = [open("{dir_path}/{file_name}".format(dir_path=dir1_path, file_name=files1_names[i])).read() for i in range(files_count1)]
    files2 = [open("{dir_path}/{file_name}".format(dir_path=dir2_path, file_name=files2_names[i])).read() for i in range(files_count2)]

    return files1, files2, files1_names, files2_names

def remove_from_unique(file1, file2, unique_files1, unique_files2):
    if (file1 in unique_files1):
        unique_files1.remove(file1)

    if (file2 in unique_files2):
        unique_files2.remove(file2)

if __name__ == "__main__":    

    files1, files2, files1_names, files2_names = read_directories()

    files_count1 = len(files1)
    files_count2 = len(files2)

    percentage = int(input("Write the percentage number like \"33\"\n"))
    target_accuracy = percentage / 100

    same_files = []
    similar_files = []
    unique_files1 = set(files1_names)
    unique_files2 = set(files2_names)
    for i in range(files_count1):
        for j in range(files_count2):
            l1 = files1[i]
            l2 = files2[j]
            size1 = len(l1) 
            size2 = len(l2)
            if (size1 < size2):
                l1, l2 = l2, l1
                size1, size2 = size2, size1

            matcher = SequenceMatcher(None, l1, l2)
            matches = sum(triple[-1] for triple in matcher.get_matching_blocks())
            accuracy_between_files = matches / size1
            if accuracy_between_files == 1:
                    same_files.append([files1_names[i], files2_names[j]])
                    remove_from_unique(files1_names[i], files2_names[j], unique_files1, unique_files2)

            elif accuracy_between_files >= target_accuracy:
                    similar_files.append([files1_names[i], files2_names[j]])
                    remove_from_unique(files1_names[i], files2_names[j], unique_files1, unique_files2)

    print("same files are:")
    for i in range(len(same_files)):
        print(
              "{dir_path}/{file_name}".format(dir_path=dir1_name, file_name=same_files[i][0]),
              " --- ", 
              "{dir_path}/{file_name}".format(dir_path=dir2_name, file_name=same_files[i][1])
              )
    print("\nsimilar files are:")
    for i in range(len(similar_files)):
        print(
              "{dir_path}/{file_name}".format(dir_path=dir1_name, file_name=similar_files[i][0]),
              " --- ", 
              "{dir_path}/{file_name}".format(dir_path=dir2_name, file_name=similar_files[i][1])
        )
    
    print("\nunique files for dir1 are:")
    for name_file in unique_files1:
        print(
              "{file_name}".format(file_name=name_file)
        )
    print("\nunique files for dir2 are:")
    for name_file in unique_files2:
        print(
              "{file_name}".format(file_name=name_file)
        )
