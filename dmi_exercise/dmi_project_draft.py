import requests
import json
import tkinter as tk
import tkintermapview


def fetch_data(start, end, bbox, limit, offset, key):
    date = "datetime=" + start + "-01-01T00:00:00%2B02:00/" + end + "-01-01T00:00:00%2B02:00"
    print("Date: " + date)
    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?limit=" + limit + "&offset=" + offset + "&bbox=" + bbox + "&" + date + "&api-key=" + key
    print("URL: " + url)
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def save_data(data):
    with open("dmi_data.json", "w") as myfile:
        json.dump(data, myfile, indent=4)


def read_data():
    with open("dmi_data.json", "r") as myfile:
        return json.load(myfile)


def print_coordinates(data):
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


def plot_coordinates_on_map(coordinates):
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{1024}x768")
    root_tk.title("Lynnedslag på Kort")
    map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack(fill="both", expand=True)

    for coord in coordinates:
        lat, lon = coord[1], coord[0]
        map_widget.set_position(lat, lon, marker=True, marker_color_circle="yellow")

    map_widget.set_zoom(12)
    root_tk.mainloop()


def launch_gui():
    def save_and_close():
        nonlocal start_year, end_year
        start_year = start_year_entry.get()
        end_year = end_year_entry.get()
        gui.destroy()

    gui = tk.Tk()
    gui.title("Indstil Årstal")
    gui.geometry("300x150")

    tk.Label(gui, text="Start år:").pack(pady=5)
    start_year_entry = tk.Entry(gui)
    start_year_entry.pack(pady=5)

    tk.Label(gui, text="Slut år:").pack(pady=5)
    end_year_entry = tk.Entry(gui)
    end_year_entry.pack(pady=5)

    tk.Button(gui, text="Gem", command=save_and_close).pack(pady=10)

    gui.mainloop()
    return start_year, end_year


def main():
    KEY = "bf39b989-b47c-4557-abfd-5b3b492aca36"
    bbox = "12.2361824,55.6323748,12.3317978,55.6669539"
    limit = "1000"
    offset = "0"

    # Launch the GUI to set start and end year
    start_year, end_year = launch_gui()

    # Fetch and process data
    data = fetch_data(start_year, end_year, bbox, limit, offset, KEY)
    save_data(data)

    data = read_data()
    print_coordinates(data)

    coordinates = get_coordinates(data)
    plot_coordinates_on_map(coordinates)


if __name__ == "__main__":
    main()
