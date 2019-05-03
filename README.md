### Python language translator

this simple python script allow you to translate text directly from the command line

### Usage

    $ translate --main_language it  --foreign_language en --content "corrente elettrica"
        electricity
        electric current
        electrical current
        electrical power
    $

for now it only translate from italian to english with no argument

    $ translate "corrente elettrica"
        electricity
        electric current
        electrical current
        electrical power
    $
    
### Arguments
    -m / --main_language      Language you would like to translate from
    -f / --foreign_languate   Language you would like to translate to
    -c /  --content           The text tp tramslate