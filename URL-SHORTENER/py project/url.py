import pyshorteners
from colorama import init, Fore, Style

# Initialize colorama to work on Windows terminals
init()

def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return shortened_url
    except pyshorteners.exceptions.ShorteningErrorException as e:
        return f"An error occurred: {e}"

def save_to_file(url, shortened_url):
    try:
        with open('shortened_urls.txt', 'a') as file:
            file.write(f"Original URL: {url}\nShortened URL: {shortened_url}\n\n")
            print(Fore.GREEN + "Shortened URL saved to 'shortened_urls.txt'")
    except IOError as e:
        print(Fore.RED + f"Error while saving to file: {e}")

def main():
    print(Fore.BLUE + "Welcome to URL Shortener")
    while True:
        url = input(Fore.YELLOW + 'Enter the URL to shorten (or "exit" to quit): ')
        
        if url.lower() == 'exit':
            print(Fore.CYAN + "Exiting the URL Shortener. Goodbye!")
            break
        
        shortened_url = shorten_url(url)
        if 'http' in shortened_url:
            print(Fore.GREEN + 'Shortened URL:', shortened_url)
            save_to_file(url, shortened_url)
        else:
            print(Fore.RED + shortened_url)

if __name__ == "__main__":
    main()
