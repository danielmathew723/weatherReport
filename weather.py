from tkinter import *
import requests
import json

root = Tk()
root.title("Air Quality")
root.geometry("235x100")

labelArea = Label(root, text="")
labelAqi = Label(root, text="")
labelCategory = Label(root, text="")

labelArea.grid(row=1, column=0, columnspan=2)
labelAqi.grid(row=2, column=0, columnspan=2)
labelCategory.grid(row=3, column=0, columnspan=2)


def zipcode():
    try:
        code = entry.get()
        api_request = requests.get(
            f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={code}&distance=5&API_KEY=905DB6A5-F716-41B8-9469-04C78639107D')
        api = json.loads(api_request.content)
        area = api[1]["ReportingArea"]
        aqi = api[1]["AQI"]
        category = api[1]["Category"]["Name"]

        if category == "Good":
            color = "#00e400"
        elif category == "Moderate":
            color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups (USG)":
            color = "#ff7e00"
        elif category == "Unhealthy":
            color = "#FF0000"
        elif category == "Very Unhealthy":
            color = "#8F3F97"
        else:
            color = "#7e0023"

        labelArea.config(text=f"Reporting Area: {area}")
        labelAqi.config(text=f"Air Quality: {aqi}")
        labelCategory.config(text=f"Category: {category}", background=color)

        entry.delete(0, 'end')

    except:
        labelArea.config(text="Error: invalid code.")
        labelAqi.config(text="")
        labelCategory.config(text="", background="SystemButtonFace")


entry = Entry(root)
buttonZip = Button(root, text="Enter zip code", width=12, command=zipcode)

entry.grid(row=0, column=0, padx=10)
buttonZip.grid(row=0, column=1)

root.mainloop()
