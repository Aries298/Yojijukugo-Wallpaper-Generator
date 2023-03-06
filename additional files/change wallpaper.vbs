Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c ""PATH_TO_BAT_FILE"""
oShell.Run strArgs, 0, false