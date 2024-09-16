from basketapp.models import Basket

def basket(request):
   print(f'context processor basket works')
   basket = []

   if request.user.is_authenticated:
       basket = Basket.objects.filter(user=request.user)

   return {
       'basket': basket,
   }
