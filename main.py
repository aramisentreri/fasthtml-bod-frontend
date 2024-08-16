from fasthtml.fastapp import * 
from fasthtml.common import *
from fasthtml import *

css = Style(':root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))

minis = [{
    "title": "Elf Ranger", 
    "description": "A very cool elf.", 
    "img_url": "https://m.media-amazon.com/images/I/71U797kMc2L._AC_SL1500_.jpg"
    },
    {
    "title": "Elf Ranger", 
    "description": "A very cool elf.", 
    "img_url": "https://m.media-amazon.com/images/I/71U797kMc2L._AC_SL1500_.jpg"
    },
    {
    "title": "Elf Ranger", 
    "description": "A very cool elf.", 
    "img_url": "https://m.media-amazon.com/images/I/71U797kMc2L._AC_SL1500_.jpg"
    },
    {
    "title": "Elf Ranger", 
    "description": "A very cool elf.", 
    "img_url": "https://m.media-amazon.com/images/I/71U797kMc2L._AC_SL1500_.jpg"
    }
]

def mini_display(mini_dict):
    return Div(
        Card(
            H4(mini_dict["title"]), 
            P(mini_dict["description"]), 
            Img(src=mini_dict["img_url"], alt="Card image", cls="card-img-top"),
        )
    )


@app.get("/")
def home():
    return Titled("", Card(
            H1("Bazaar of Dragons"),
            H2("Rent Miniatures Inspire your players"),
            P("A marketplace for Dungeon Masters to connect and share miniatures that will enhance and add flavor to your game without breaking the bank!"),
            P("Let's do this!"),
        ),
        Div(*[mini_display(mini_dict) for mini_dict in minis],
            cls="grid"
        )
    )

serve()