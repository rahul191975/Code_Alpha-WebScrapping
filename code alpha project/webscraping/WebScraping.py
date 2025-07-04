import requests
from bs4 import BeautifulSoup
import pandas as pd

def Extract_DetailsOf_Product(URL):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9"
    }

    Send_request = requests.get(URL, headers=headers)

    if Send_request.status_code != 200:

        print("The webpage could not be retrieved.")
        return

    soup = BeautifulSoup(Send_request.content, 'html.parser')


    # Extract product details
    title = soup.find("span", {"id": "productTitle"})

    price = soup.find("span", {"class": "a-price-whole"})

    rating = soup.find("span", {"class": "a-icon-alt"})

    review_count = soup.find("span", {"id": "acrCustomerReviewText"})

    availability = soup.find("div", {"id": "availability"})

    description = soup.find("div", {"id": "feature-bullets"})


    # Clean and format data
    product_data_Collect = {
        "Product_Title": title.get_text(strip=True) 
            if title else "Not available",

        "Price of Product": price.get_text(strip=True) 
            if price else "Not available",
        
        "Overall Rating ": rating.get_text(strip=True) 
            if rating else "Not available",

        "Number of Reviews": review_count.get_text(strip=True) 
            if review_count else "Not available",

        "Product_Availability": availability.get_text(strip=True) 
            if availability else "Not available",

        "Description": description.get_text(strip=True).replace('\n', ' ') 
            if description else "Not available"
    }


    # Shows Product details in terminal

    print("\n Extracted Product Details From The Given Link :\n")
    for key, value in product_data_Collect.items():
        print(f"{key}: {value}")

    # Save to CSV

    Data_table = pd.DataFrame([product_data_Collect])
    Data_table.to_csv("product_details.csv", index=False)
    print("\n Product details saved to 'product_details.csv'\n")

# Start point

if __name__ == "__main__":
    Product_Link = input("Paste the Link of Amazon Product : ").strip()
    Extract_DetailsOf_Product(Product_Link)