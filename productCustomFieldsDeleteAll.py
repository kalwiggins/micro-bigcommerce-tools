from connect import get_api_response, get_credentials
from products import get_all_product_ids

def delete_product_custom_fields(product_id):
    """Delete all custom fields for a given product."""
    store_hash, _, _ = get_credentials()
    base_url = f'https://api.bigcommerce.com/stores/{store_hash}/v3/catalog/products/{product_id}/custom-fields'
    
    # Fetch the product custom fields
    response = get_api_response(base_url)
    if response.status_code == 200:
        custom_fields = response.json()['data']
        if not custom_fields:
            print(f'No custom fields to delete for product ID: {product_id}')
            return True
        # Delete each custom field individually
        for custom_field in custom_fields:
            delete_url = f'{base_url}/{custom_field["id"]}'
            delete_response = get_api_response(delete_url, method='delete')
            if delete_response.status_code == 204:
                print(f'Deleted custom field {custom_field["id"]} for product ID: {product_id}')
            else:
                print(f'Error deleting custom field {custom_field["id"]} for product ID {product_id}: {delete_response.text}')
                return False
        return True
    else:
        print(f'Error fetching custom fields for product ID {product_id}: {response.text}')
        return False

def productCustomFieldsDelete(product_id=None):
    """Delete all custom fields for a given product or all products."""
    if product_id:
        product_ids = [product_id]
    else:
        product_ids = get_all_product_ids()
    
    for product_id in product_ids:
        if delete_product_custom_fields(product_id):
            print(f'Deleted all custom fields for product ID: {product_id}')
        else:
            print(f'Failed to delete some custom fields for product ID: {product_id}')

# Test the function with a single product ID
if __name__ == '__main__':
    # productCustomFieldsDelete(product_id="48050")  # Replace "48050" with your product ID or remove it to run for all products
    productCustomFieldsDelete()
