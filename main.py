import PySimpleGUI as sg
from zip import extractor

label1=sg.Text("Select file to Unzip:")
input1=sg.Input()
choose_button1=sg.FileBrowse("Choose", key="file")

label2=sg.Text("Select export location:")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose", key="folder")

Unzip_button = sg.Button("Unzip")
output_label=sg.Text(key="output")

window = sg.Window("File Unzipper", layout=[[label1,input1,choose_button1],
                                              [label2,input2,choose_button2],
                                              [Unzip_button,output_label]])
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Unzip":
            archivepath = values["file"]
            dest_dir = values["folder"]
            extractor(archivepath, dest_dir)
            window["output"].update(value="Extraction Completed!")
        case sg.WIN_CLOSED:
            break
window.close()