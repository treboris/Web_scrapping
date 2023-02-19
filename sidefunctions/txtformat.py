


text = ""
with open("txt/jobline_job_1_2023-02-07.txt") as f:
    file = f.readlines()
    for line in file:
        if(line.strip()):
            text += line
open("txt/jobline_job_1_2023-02-07.txt", 'w').close()
print(text)
with open("txt/jobline_job_1_2023-02-07.txt", 'w') as new_file:
    new_file.write(text)
