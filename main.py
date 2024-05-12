import PySimpleGUI as ps

ps.theme('Dark')
title = ps.Text('FILE COMPRESSOR', font=('Copperplate Gothic Bold', 20), text_color='green')
dev_credits = ps.Text('by: anasanchesdev', font=('Courier', 8), text_color='lime green', pad=((6, 0), (0, 15)))

# line 1
archive_label = ps.Text('Select the archive:')
archive_input = ps.Input()
archive_button = ps.FileBrowse('Select', key='archive_button')

# line 2
dest_label = ps.Text('Select the destination folder:')
dest_input = ps.Input()
dest_button = ps.FolderBrowse('Select', key="dest_button")

# line 3
extract_button = ps.Button('Extract', key='extract_button')
action_text = ps.Text(key='action_text')

layout = [
    [title],
    [dev_credits],
    [archive_label],
    [archive_input, archive_button],
    [dest_label],
    [dest_input, dest_button],
    [extract_button, action_text]
]

window = ps.Window('File Decompressor', layout=layout)

while True:
    events, values = window.read()
    print(events, values)

window.close()
