# Map Navigator

A simple map navigator application with a graphical user interface (GUI) built using Tkinter in Python. This application allows users to search for locations and view them on an interactive map using Folium.

## Features

- **Search for Locations**: Enter a location name to find and view it on a map.
- **Interactive Map**: Displays the location on an interactive map with a marker.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python installations)
- `folium` (for generating interactive maps)
- `geopy` (for geocoding and reverse geocoding)
- `webbrowser` (to open the generated HTML map)

## Installation

1. **Clone the repository or download the script**:
    ```bash
    git clone https://github.com/yourusername/map-navigator.git
    cd map-navigator
    ```

2. **Install the required Python libraries**:
    ```bash
    pip install folium geopy
    ```

3. **Run the Script**:
    ```bash
    python map_navigator.py
    ```

## Usage

1. **Start the Application**: Run the script to open the Map Navigator application.
2. **Enter Location**: Type a location name (e.g., "Eiffel Tower, Paris, France") into the input field.
3. **Click "Search"**: The application will generate a map centered on the entered location and open it in your default web browser.

## Code Structure

- **MapNavigator Class**: Handles the GUI and map display logic.
  - `create_widgets()`: Initializes the GUI components.
  - `search_location()`: Geocodes the entered location and triggers map display.
  - `display_map()`: Generates and saves the map, then opens it in a web browser.

## Example

When you run the script and enter a location like "Statue of Liberty, New York, USA," the application will display a map centered on the Statue of Liberty with a marker.

## License

This project is licensed under the MIT License.

