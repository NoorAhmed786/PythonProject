import requests
from bs4 import BeautifulSoup as bs

# Prompt the user for their GitHub username
github_user = input('Enter your GitHub username: ')

# Construct the GitHub profile URL
url = 'https://github.com/' + github_user

try:
    # Send a GET request to the profile page
    r = requests.get(url)
    r.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    # Parse the HTML content using BeautifulSoup
    soup = bs(r.content, 'html.parser')

    # Find the profile image element (adjust selector based on actual page structure)
    profile_img_tag = soup.find('img', {'alt': f'@{github_user}'})

    # Ensure the element exists before accessing its 'src' attribute
    if profile_img_tag:
        profile_img = profile_img_tag['src']
        print(f"Profile Image URL: {profile_img}")
    else:
        print("Profile image not found. The page structure might have changed.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the GitHub profile: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
