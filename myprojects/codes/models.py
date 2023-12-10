# from django.db import models

# from myprojects import settings
# from user.models import CustomUser

# import random
# class Code(models.Model):
#     number=models.CharField(max_length=5,blank=True)
#     user =models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     def __str__(self):
#         return str(self.number)
    
#     def save(self, *args, **kwargs):

#         number_list=[x for x in range(10)]
#         code_items = []
#         for i in range(5):
#             num = random.choice(number_list)
#             code_items.append(num)
#         code_string = "".join(str(item) for item in code_items)
#         self.number = code_string
        
#         print(f"Verification code for user {self.user.email}: {self.number}")


#         super().save(*args, **kwargs)





from django.db import models
from user.models import CustomUser
import random

class Code(models.Model):
    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        if not self.number:
            number_list = [x for x in range(10)]
            code_items = []

            for i in range(5):
                num = random.choice(number_list)
                code_items.append(num)

            code_string = "".join(str(item) for item in code_items)
            self.number = code_string

            # Print the verification code to the terminal
            print(f"Verification code for user {self.user.email}: {self.number}")

        super().save(*args, **kwargs)

