#mossyhorn 12.6.19
import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
import urllib.request

HEIGHT = 700
WIDTH = 800
request = 'none'

def create_search():
    frame.destroy()
    lower_frame.destroy()

    global return_button
    return_button = tk.Button(root, text='Return',
                            font=('Small Fonts', 20),
                            command=lambda: create_main(),)
    return_button.place(relx=0.75, rely=0.025, relwidth=0.15, relheight=0.05)

    searchbar_frame = tk.Frame(root, bg='#C0C0C0', bd=5)
    searchbar_frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1,
                        anchor='n')

    search_entry = tk.Entry(searchbar_frame, font=('Small Fonts', 20))
    search_entry.place(relwidth=0.7, relheight=1)

    search_button = tk.Button(searchbar_frame, text='Search',
                            font=('Small Fonts', 20),
                            command=lambda: search(search_entry.get()))
    search_button.place(relx=0.75, relwidth=0.25, relheight=1)

    global result_frame
    result_frame = tk.Frame(root, bg='#C0C0C0', bd=5)
    result_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.6,
                        anchor='n')

def search(entry):
    print('You are searching for:', entry)

    print(request)
    if request == 'pokemon':
        try:
            x = entry.replace(' ', '-')
            response = requests.get('https://pokeapi.co/api/v2/pokemon/' +
                                    x.lower() + '/')
            pyresponse = response.json()

            name = pyresponse['forms'][0]['name'].title()
            img_url = pyresponse['sprites']['front_default']
            image = Image.open(requests.get(img_url, stream=True).raw)
            ph = ImageTk.PhotoImage(image)
            type = pyresponse['types'][0]['type']['name'].title()
            #Given in decimetres
            height = pyresponse['height']
            height = int(height) / 10
            #Given in hectograms
            weight = pyresponse['weight']
            weight = int(weight) / 10
            id = pyresponse['id']

            output = 'ID: %s \nName: %s \nType: %s \nHeight: %s m\nWeight: %s kg' % (id, name, type, height, weight)
            label = tk.Label(result_frame, font=('Small Fonts', 20),
                            anchor='nw', justify='left', bd=5)
            label.place(relwidth=1, relheight=1)
            label['text'] = output

            label = tk.Label(result_frame, image=ph, bd=5)
            label.image=ph
            label.place(relx=0.95, rely=0, relwidth=0.25, relheight=0.25, anchor='ne')
        except:
            label = tk.Label(result_frame, font=('Small Fonts', 20),
                            anchor='nw', justify='left', bd=5)
            label.place(relwidth=1, relheight=1)
            output = ('There was a problem retreiving that information.\n' +
                    'Try searching another key term.')
            label['text'] = output
    elif request == 'berry':
        try:
            response = requests.get('https://pokeapi.co/api/v2/berry/' +
                                    entry.lower() + '/')
            pyresponse = response.json()

            firmness = pyresponse['firmness']['name'].title()
            name = pyresponse['name'].title()
            size = pyresponse['size']
            max_harvest = pyresponse['max_harvest']
            natural_gift_type = pyresponse['natural_gift_type']['name'].title()
            id = pyresponse['id']

            output = 'ID: %s \nName: %s \nFirmness: %s \nSize: %s mm \nMax Harvest: %s \nNatural Gift Type: %s' % (id, name, firmness, size, max_harvest, natural_gift_type)

            label = tk.Label(result_frame, font=('Small Fonts', 20),
                            anchor='nw', justify='left', bd=5)
            label.place(relwidth=1, relheight=1)
            label['text'] = output
        except:
            label = tk.Label(result_frame, font=('Small Fonts', 20),
                            anchor='nw', justify='left', bd=5)
            label.place(relwidth=1, relheight=1)
            output = ('There was a problem retreiving that information.\n' +
                    'Try searching another key term.')
            label['text'] = output
    elif request == 'item':
        try:
            x = entry.replace(' ', '-')
            response = requests.get('https://pokeapi.co/api/v2/item/' +
                                x.lower() + '/')
            pyresponse = response.json()

            category = pyresponse['category']['name'].replace('-', ' ').title()
            short_effect = pyresponse['effect_entries'][0]['short_effect']
            name = pyresponse['name'].replace('-', ' ').title()
            id = pyresponse['id']

            img_url = pyresponse['sprites']['default']
            image = Image.open(requests.get(img_url, stream=True).raw)
            ph = ImageTk.PhotoImage(image)

            output = 'ID: %s \nName: %s \nCategory: %s \nEffect: %s' % (id, name, category, short_effect)

            label = tk.Label(result_frame, font=('Small Fonts', 20),
                            anchor='nw', justify='left', bd=5)
            label.place(relwidth=1, relheight=1)
            label['text'] = output

            label = tk.Label(result_frame, image=ph, bd=5)
            label.image=ph
            label.place(relx=0.95, rely=0, relwidth=0.25, relheight=0.25, anchor='ne')
        except:
            label = tk.Label(result_frame, font=('Small Fonts', 20),
                            anchor='nw', justify='left', bd=5)
            label.place(relwidth=1, relheight=1)
            output = ('There was a problem retreiving that information.\n' +
                    'Make sure there are no unnecessary whitespaces\n and try '
                    + 'searching another key term.')
            label['text'] = output
    elif request == 'location':
        try:
            x = entry.replace(' ', '-')
            response = requests.get('https://pokeapi.co/api/v2/location/' +
                                    x.lower() + '/')
            pyresponse = response.json()

            name = pyresponse['name'].replace('-', ' ').title()
            id = pyresponse['id']
            region = pyresponse['region']['name'].title()

            output = 'ID: %s \nName: %s \nRegion: %s' % (id, name, region)

            label = tk.Label(result_frame, font=('Small Fonts', 20),
                            anchor='nw', justify='left', bd=5)
            label.place(relwidth=1, relheight=1)
            label['text'] = output
        except:
            label = tk.Label(result_frame, font=('Small Fonts', 20),
                            anchor='nw', justify='left', bd=5)
            label.place(relwidth=1, relheight=1)
            output = ('There was a problem retreiving that information.\n' +
                    'Make sure there are no unnecessary whitespaces\n and try '
                    + 'searching another key term.')
            label['text'] = output

#query api on 'https://pokeapi.co/api/v2/pokemon/[id or name]'
def pokemon_press():
    create_search()

    print('Pokemon button pressed')
    global request
    request = 'pokemon'

def berry_press():
    create_search()

    print('Berry button pressed!')
    global request
    request = 'berry'

def item_press():
    create_search()

    print('Item button pressed!')
    global request
    request = 'item'

def location_press():
    create_search()

    print('Location button pressed!')
    global request
    request = 'location'

#Create app
root = tk.Tk()
root.title('Pokedex')


#Define how large app window is
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#FF0000')
canvas.pack()

#Create main menu
def create_main():
    try:
        return_button.destroy()
    except:
        pass

    global frame
    frame = tk.Frame(root, bg='#C0C0C0', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor='n')

    label = tk.Label(frame, text='Welcome to the Pokedex!\n Choose an item to sea' +
                    'rch:', font=('Small Fonts', 20))
    label.place(relwidth=1, relheight=1)

    global lower_frame
    lower_frame = tk.Frame(root, bg='#C0C0C0', bd=5)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.6, anchor='n')

    button1 = tk.Button(lower_frame, text='Pokemon', font=('Small Fonts', 20),
                    command=lambda: pokemon_press())
    button1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.2)

    button2 = tk.Button(lower_frame, text='Berries', font=('Small Fonts', 20),
                    command=lambda: berry_press())
    button2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.2)

    button3 = tk.Button(lower_frame, text='Items', font=('Small Fonts', 20),
                    command=lambda: item_press())
    button3.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.2)

    button4 = tk.Button(lower_frame, text='Locations', font=('Small Fonts', 20),
                    command=lambda: location_press())
    button4.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.2)

create_main()

#Runs what is in the app
root.mainloop()
