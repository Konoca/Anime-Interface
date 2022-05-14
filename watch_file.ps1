Function RunMyStuff {
    # this is the bit we want to happen when the file changes
    # Clear-Host # remove previous console output
    # & 'C:\Program Files\erl7.3\bin\erlc.exe' 'program.erl' # compile some erlang
    # erl -noshell -s program start -s init stop # run the compiled erlang program:start()
    $path = Get-Content -path ./pipe/file.txt
    Write-Host $path
    Invoke-Item -LiteralPath $path

    Clear-Content ./pipe/file.txt -Force
}

Function Watch {    
    $global:FileChanged = $false
    $folder = "$(Get-Location)\pipe"
    $filter = "*.txt"
    $watcher = New-Object IO.FileSystemWatcher $folder, $filter -Property @{ 
        IncludeSubdirectories = $false 
        EnableRaisingEvents = $true
    }

    Register-ObjectEvent $Watcher "Changed" -Action {$global:FileChanged = $true} > $null

    while ($true){
        while ($global:FileChanged -eq $false){
            Start-Sleep -Milliseconds 100
        }

        RunMyStuff

        $global:FileChanged = $false
    }
}

RunMyStuff
Watch

# D:/PicturesVideos/Anime/[Erai-raws] Tomodachi Game - 05 [1080p][Multiple Subtitle][06D5D073].mkv