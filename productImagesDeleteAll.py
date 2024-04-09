from connect import get_api_response, get_credentials
from products import get_all_product_ids

def delete_product_images(product_id):
    """Delete all images for a given product."""
    store_hash, _, _ = get_credentials()
    base_url = f'https://api.bigcommerce.com/stores/{store_hash}/v3/catalog/products/{product_id}/images'
    
    # Fetch the product images
    response = get_api_response(base_url)
    if response.status_code == 200:
        images = response.json()['data']
        if not images:
            print(f'No images to delete for product ID: {product_id}')
            return True
        # Delete each image individually
        for image in images:
            delete_url = f'{base_url}/{image["id"]}'
            delete_response = get_api_response(delete_url, method='delete')
            if delete_response.status_code == 204:
                print(f'Deleted image {image["id"]} for product ID: {product_id}')
            else:
                print(f'Error deleting image {image["id"]} for product ID {product_id}: {delete_response.text}')
                return False
        return True
    else:
        print(f'Error fetching images for product ID {product_id}: {response.text}')
        return False



def productImagesDelete(product_id=None):
    """Delete all product images for a given product or all products."""
    if product_id:
        product_ids = [product_id]
    else:
        product_ids = get_all_product_ids()
    
    for product_id in product_ids:
        if delete_product_images(product_id):
            print(f'Deleted images for product ID: {product_id}')
        else:
            print(f'Failed to delete images for product ID: {product_id}')

# Test the function with a single product ID
if __name__ == '__main__':
    # productImagesDelete(product_id="8999")
    productImagesDelete()
