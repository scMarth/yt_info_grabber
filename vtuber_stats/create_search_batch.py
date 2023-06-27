import os

# start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" "https://www.youtube.com/playlist?list=WL"

# get the path to the directory that this script resides in
script_dir = os.path.dirname(os.path.abspath(__file__))

output_filename = 'search_vtubers.bat'
output_filepath = script_dir + '\\' + output_filename

# delete output file if it exists
if os.path.exists(output_filepath):
    os.remove(output_filepath)

files = [
    ['nijisanji_en.txt', 'nijisanji en'],
    ['nijisanji_en_retired.txt', 'nijisanji en'],
    ['nijisanji_main_branch.txt', 'nijisanji'],
    ['nijisanji_main_branch_retired.txt', 'nijisanji'],
    ['virtuareal.txt', 'virtuareal'],
    ['virtuareal_retired.txt', 'virtuareal']
]

vtubers = []

for filename, org in files:

    file_path = script_dir + '\\' + filename
    print(file_path)

    with open(file_path, "r") as file:
        for line in file:
            if line.split():
                vtubers.append(line.split() + org.split())


for vtuber in vtubers:
    with open(output_filepath, 'a') as file:
        # command_str = 'start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" "https://www.youtube.com/results?search_query={}"'.format('+'.join(vtuber))
        command_str = 'start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.youtube.com/results?search_query={}"'.format('+'.join(vtuber))
        file.write(command_str + '\n')

