from connect import get_api_response, get_credentials

def get_all_product_ids():
    # Get API credentials
    store_hash, _, _ = get_credentials()

    # API endpoint for fetching products
    url = f'https://api.bigcommerce.com/stores/{store_hash}/v3/catalog/products'
    
    # Initialize an empty list to store product IDs
    product_ids = []
    
    # Set the initial page
    page = 1
    
    while True:
        # Add the page parameter to the URL
        paginated_url = f'{url}?page={page}'
        
        # Make the API request
        response = get_api_response(paginated_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            
            # Extract product IDs from the response and add them to the list
            for product in data['data']:
                product_ids.append(product['id'])
            
            # Check if there are more pages
            if data['meta']['pagination']['current_page'] < data['meta']['pagination']['total_pages']:
                # Move to the next page
                page += 1
            else:
                # Exit the loop if there are no more pages
                break
        else:
            print(f'Failed to fetch products. Status code: {response.status_code}')
            break
    
    return product_ids

# Test the function
if __name__ == '__main__':
    product_ids = get_all_product_ids()
    print(f'Product IDs: {product_ids}')
