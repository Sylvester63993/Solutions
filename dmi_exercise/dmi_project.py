import requests
import json
import tkinter
import tkintermapview


def fetch_data(start, end, bbox, limit, offset, key):
    # start = input("Indtast start kalenderår: ")
    # end = input("Indtast slut kalenderår: ")
    date = "datetime=" + start + "-01-01T00:00:00%2B02:00/" + end + "-01-01T00:00:00%2B02:00"
    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?limit=" + limit + "&offset=" + offset + "&bbox=" + bbox + "&" + date + "&api-key=" + key
    # url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?limit=100&bbox=" + bbox + "&" + date + "&api-key=" + key
    response = requests.get(url)
    data = json.loads(response.text)
    return data
    # print(f'{data=}')
    # print(data)
    print("URL: " + url)
    print("Date: " + date)

def save_data(data):
    myfile = "dmi_data.json"  # the name of the file. Note the / (slash) instead of a \ (backslash) in the file path!

    # Writing to a file (.json)
    with open(myfile, "w") as myfile:  # 'w' stands for "write"
        json.dump(data, myfile, indent=4)

def read_data():
    myfile = "dmi_data.json"

    # Reading file
    with open(myfile, "r") as myfile:
        data = json.load(myfile)

        return data

def print_coordinates(data):  # AI generated
    features = data.get("features", [])
    for feature in features:
        coordinates = feature.get("geometry", {}).get("coordinates", [])
        if coordinates:
            print(f'Koordinater: {coordinates}')

def get_coordinates(data):
    features = data.get("features", [])
    coordinates = []
    for feature in features:
        coord = feature.get("geometry", {}).get("coordinates", [])
        if coord:
            coordinates.append(coord)
    return coordinates


def plot_coordinates_on_map(coordinates):  # AI generated
    # create tkinter window
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{1024}x{768}")
    root_tk.title("map_view_example.py")

    # create map widget
    map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack(fill="both", expand=True)

    for coord in coordinates:
        lat, lon = coord[1], coord[0]  # Reorder coordinates for latitude, longitude
        map_widget.set_position(lat, lon, marker=True, marker_color_circle="yellow")  # marker_color_outline="yellow"

    map_widget.set_zoom(7)  # Adjust zoom level as necessary

    root_tk.mainloop()


def main():
    KEY = "bf39b989-b47c-4557-abfd-5b3b492aca36"
    start = "2020"
    end = "2021"
    # bbox = "7,54,16,58"  # DMIs bbox-koordinater for hele Danmark (format: [lon, lat])
    bbox = "12.2361824,55.6323748,12.3317978,55.6669539"
    limit = "1000"
    offset = "0"

    # Taastrup bbox
    # top right: 55.6669539 12.3317978
    # bottom left: 55.6323748 12.2361824

    # data = fetch_data(start, end, bbox, KEY)
    data = fetch_data(start, end, bbox, limit, offset, KEY)
    print(data)
    save_data(data)

    data = read_data()
    print_coordinates(data)

    # generate_map()
    # plot_coordinates_on_map()

    # Get coordinates from data
    coordinates = get_coordinates(data)

    # Plot coordinates on map
    plot_coordinates_on_map(coordinates)


if __name__ == "__main__":  # Executed when invoked directly
    main()
