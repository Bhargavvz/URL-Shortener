import tkinter as tk
import pyshorteners

def shorten_url():
    url = url_entry.get()
    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        result_label.config(text=f"Shortened URL: {shortened_url}")
        save_to_file(url, shortened_url)
    except pyshorteners.exceptions.ShorteningErrorException as e:
        result_label.config(text=f"An error occurred: {e}")

def save_to_file(url, shortened_url):
    try:
        with open('shortened_urls.txt', 'a') as file:
            file.write(f"Original URL: {url}\nShortened URL: {shortened_url}\n\n")
            result_label.config(text="Shortened URL saved to 'shortened_urls.txt'")
    except IOError as e:
        result_label.config(text=f"Error while saving to file: {e}")

# Create GUI
root = tk.Tk()
root.title("URL Shortener")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

url_label = tk.Label(frame, text="Enter the URL:")
url_label.pack()

url_entry = tk.Entry(frame, width=40)
url_entry.pack()

shorten_button = tk.Button(frame, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

result_label = tk.Label(frame, text="")
result_label.pack()

root.mainloop()
