from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import  Reviews_and_Ratings

def rate(request):
    if request.method == 'POST':
        user = request.user  
        item_id = request.POST.get('item_id')
        rating_value = request.POST.get('rating')

    
        existing_rating = Reviews_and_Ratings.objects.filter(user=user, item_id=item_id).first()

        if existing_rating:
            existing_rating.rating = rating_value
            existing_rating.save()
        else:
            Reviews_and_Ratings.objects.create(user=user, item_id=item_id, rating=rating_value)

       
        update_average_rating(item_id)

        return redirect('item_detail', item_id=item_id)  

    return redirect('home')  

def update_average_rating(item_id):
    ratings = Reviews_and_Ratings.objects.filter(item_id=item_id)
    total_ratings = ratings.count()
    total_rating_value = sum(rating.rating for rating in ratings)

    if total_ratings > 0:
        average_rating = total_rating_value / total_ratings
    else:
        average_rating = 0

    item = Reviews_and_Ratings.objects.get(pk=item_id)
    item.average_rating = average_rating
    item.save()

def get_average_rating(request, item_id):
    item = Reviews_and_Ratings.objects.get(pk=item_id)
    average_rating = item.average_rating

    return JsonResponse({'average_rating': average_rating})
