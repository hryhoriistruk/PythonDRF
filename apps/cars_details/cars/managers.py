from django.db import models


class CarManager(models.Manager):
    def all_cars_with_price(self):
        return self.prefetch_related('price').all()  # як приклад відфільтрувати щось і зменшити навантаження на API

    def all_cars_by_premium_seller_id(self, pk):
        return self.prefetch_related('cars').filter(premium_seller_id=pk)

    # def description_increment_attempts(self):
    #     self.attempts += 1
    #     if self.attempts >= 3:
    #         self.blocked = True
    #         self.save()

    # def save(self, *args, **kwargs):
    #     if self.attempts >= 3:
    #         self.attempts = 0
    #         messages.warning('Ad creation car blocked. Contact manager to unblocked')
    #         return super(CarModel, self).save(*args, **kwargs)

# def check_description(self):
#     obscene_words = [
#         'FUCK',
#         'asshole',
#         'fucking'
#     ]
#     description_lower = self.description.lower()
#     if any(word in description_lower for word in obscene_words):
#         self.attempts += 1
#         self.save()
#         if self.attempts >= 3:
#             self.block_car()
#             return "Your carModel blocked"
#         return "Obscene language is defined in description, Please revise it"
#     return None
