import PySimpleGUI as ps
import pathlib
from functions import extract_archive

DEFAULT_FONT = ('Segoe UI Black', 10)
ACTION_FONT = ('Segoe UI', 10)

ps.theme('Dark')
title = ps.Text('FILE COMPRESSOR', font=('Copperplate Gothic Bold', 20), text_color='green')
dev_credits = ps.Text('by: anasanchesdev', font=('Courier', 8), text_color='lime green', pad=((6, 0), (0, 15)))

# line 1
archive_label = ps.Text('Select the archive:', font=DEFAULT_FONT)
archive_input = ps.Input()
archive_button = ps.FilesBrowse('Select', key='archive_path', font=DEFAULT_FONT)

# line 2
dest_label = ps.Text('Select the destination folder:', font=DEFAULT_FONT)
dest_input = ps.Input()
dest_button = ps.FolderBrowse('Select', key="dest_dir", font=DEFAULT_FONT)

# line 3
extract_button = ps.Button('Extract', key='extract_button', font=DEFAULT_FONT)
exit_button = ps.Button('Exit', key='exit_button', font=DEFAULT_FONT)
action_text = ps.Text(key='action_text', font=ACTION_FONT)

layout = [
    [title],
    [dev_credits],
    [archive_label],
    [archive_input, archive_button],
    [dest_label],
    [dest_input, dest_button],
    [extract_button, exit_button, action_text]
]

window = ps.Window('File Decompressor', layout=layout)


while True:
    events, values = window.read()
    print(events, values)
    archive_path = values['archive_path']
    archive_name = pathlib.Path(archive_path).name
    print(archive_name)
    dest_dir = values['dest_dir']
    inputs = [archive_path, dest_dir]
    print(archive_path, dest_dir)

    if events == 'extract_button':
        if not all(inputs):
            window['action_text'].update(value=f'Please, fill in all the input fields before submitting.',
                                         text_color='red', font=ACTION_FONT)
            continue
        extract_archive(archive_path, dest_dir)
        window['action_text'].update(value=f'"{archive_name}.zip" was decompressed successfully.',
                                     text_color='lime green', font=ACTION_FONT)

    elif events == 'exit_button' or events == ps.WIN_CLOSED:
        break

window.close()
