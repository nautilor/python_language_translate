### Python language translator

this simple python script allow you to translate text directly from the command line

### Usage

    $ translate --language en --content "corrente elettrica"
        electricity
        electric current
        electrical current
        electrical power
    $

### Arguments
    -l / --language           The language you want to translate to
    -c /  --content           The text to translate

>The language must be the 2 letter country code (EX: en, de, it)
>

# NOTE
To translate you need a Yandex api_key
Right now it does not have a configuration file where to store the key (coming soon) and you have to place the key inside `libs/yandex.py`
