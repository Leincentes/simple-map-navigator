import tkinter as tk
from tkinter import messagebox
import folium
import webbrowser
from geopy.geocoders import Nominatim
import os

class MapNavigator:
    def __init__(self, root):
        self.root = root
        self.root.title("Map Navigator")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Search Section
        tk.Label(self.root, text="Enter Location:").grid(row=0, column=0, padx=10, pady=10)
        
        self.location_entry = tk.Entry(self.root, width=40)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Button(self.root, text="Search", command=self.search_location).grid(row=0, column=2, padx=10, pady=10)
        
        # Map Section
        self.map_frame = tk.Frame(self.root, width=800, height=600)
        self.map_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.map_label = tk.Label(self.map_frame, text="Map will be displayed here")
        self.map_label.pack()
        
    def search_location(self):
        location_name = self.location_entry.get()
        if not location_name:
            messagebox.showwarning("Input Error", "Please enter a location.")
            return
        
        geolocator = Nominatim(user_agent="map_navigator")
        try:
            location = geolocator.geocode(location_name)
            if location:
                self.display_map(location.latitude, location.longitude, location.address)
            else:
                messagebox.showerror("Location Error", "Could not find the location.")
        except Exception as e:
            messagebox.showerror("Geocoding Error", str(e))
    
    def display_map(self, lat, lon, address):
        map_ = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], popup=address).add_to(map_)
        
        map_file = "map.html"
        map_.save(map_file)
        
        # Open the map in the default web browser
        webbrowser.open(f"file://{os.path.abspath(map_file)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MapNavigator(root)
    root.mainloop()
