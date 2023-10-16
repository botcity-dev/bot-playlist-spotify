$exclude = @("venv", "BotPlaylistSpotify.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotPlaylistSpotify.zip" -Force