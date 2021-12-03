import redis
from django.conf import settings
from .models import Product

# Connect to redis
conn = redis.Redis(host=settings.REDIS_HOST, 
                   port=settings.REDIS_PORT, 
                   db=settings.REDIS_DB)

class Recommend(object):
    
    def get_product_id(self, id):
        return f'product:{id}:pruchased_with'
    
    def products_bought(self, products):
        product_ids = [product.id for product in products]
        for product_id in product_ids:
            for with_id in product_ids:
                # get the other products bought with each product
                if product_id != with_id:
                    # Increment score for product purchased together
                    conn.zincrby(self.get_product_id(product_id), 1, with_id)
    
    def suggest_products_for(self, products, max_results=5):
        product_ids = [product.id for product in products]
        if len(products) == 1:
            #only a product
            suggestions = conn.zrange(
                self.get_product_id(product_ids[0]), 0, -1, desc=True)[:max_results]
            
        else:
            # Not a single product, generate a temporary key
            flat_ids = ''.join([str(id) for id in product_ids])
            temp_key = f'temp_{flat_ids}'
            # Store the resulting sorted set in a temporary_key
            keys = [self.get_product_id(id) for id in product_ids]
            conn.zunionstore(temp_key, keys)
            # Remove ids for the products the recommendation is for
            conn.zrem(temp_key, *product_ids)
            # get the product ids by their score, descendant sort
            suggestions = conn.zrange(temp_key, 0, -1, desc=True)[:max_results]
            
            #remove the temporary key
            conn.delete(temp_key)
        suggested_products_ids = [int(id) for id in suggestions]
        #get suggested products and sort by order of appearance
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products
    
    def clear_purchases(self):
        for id in Product.objects.values_list('id', flat=True):
            conn.delete(self.get_product_id(id))