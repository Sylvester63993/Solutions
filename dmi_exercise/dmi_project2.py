import requests
import json
import tkinter
import tkintermapview

KEY = "bf39b989-b47c-4557-abfd-5b3b492aca36"
start = "2020"
end = "2021"
bbox = "7,54,16,58"

def fetch_data(start, end, bbox, key=KEY):
    # start = input("Indtast start kalenderår: ")
    # end = input("Indtast slut kalenderår: ")
    date = "datetime=" + start + "-01-01T00:00:00%2B02:00/" + end + "-01-01T00:00:00%2B02:00"
    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?limit=10&bbox=" + bbox + "&" + date + "&api-key=" + key
    response = requests.get(url)
    data = json.loads(response.text)
    print(f'{data=}')
    # print(data)
    print("URL: " + url)
    print("Date: " + date)

def generate_map():
    # create tkinter window
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{800}x{600}")
    root_tk.title("map_view_example.py")

    # create map widget
    map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # set current widget position and zoom
    # map_widget.set_position(55.613133, 12.356829, marker=True)  # Ishøj Bycenter, Denmark
    # map_widget.set_position(55.9396761, 9.5155848)  # Hele DK, zoom: 7
    # map_widget.set_zoom(7)

    # Gadekæret sø: 55.6174754 12.3482867
    # Jægerbuen sø: 55.6109373 12.3611426
    map_widget.fit_bounding_box((55.6174754, 12.3482867), (55.6109373, 12.3611426))

    root_tk.mainloop()


if __name__ == "__main__":  # Executed when invoked directly
    print(fetch_data(start, end, bbox, KEY))
    generate_map()

