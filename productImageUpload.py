import csv
from connect import get_api_response, get_credentials

def upload_image_to_product(product_id, image_url):
    """Upload an image to a BigCommerce product."""
    store_hash, _, _ = get_credentials()
    url = f'https://api.bigcommerce.com/stores/{store_hash}/v3/catalog/products/{product_id}/images'
    payload = {
        "image_url": image_url
    }
    response = get_api_response(url, method='post', json=payload)
    if response.status_code == 201:
        print(f'Successfully uploaded image to product ID: {product_id}')
    else:
        print(f'Failed to upload image to product ID {product_id}: {response.text}')



def upload_images_from_csv(csv_file):
    """Upload images to BigCommerce products based on a CSV file."""
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            product_id = row[2]  # Assuming product ID is in the third column (index 2)
            for image_url in row[3:13]:  # Assuming image URLs are in columns 4 to 13
                if image_url:  # Check if the cell contains an image URL
                    upload_image_to_product(product_id, image_url)

# Test the function with your CSV file
if __name__ == '__main__':
    upload_images_from_csv('imageupload.csv')  # Replace 'path/to/your/file.csv' with the path to your CSV file
