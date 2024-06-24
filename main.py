import os
print('Welcome to robo speaker, created by parveez \n Type exit to terminate the program')
while(True):
    x = input("Enter what you want me to speak")
    if x == 'exit':
        break
    command = f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"'''
    os.system(command)

