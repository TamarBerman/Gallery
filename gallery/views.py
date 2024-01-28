from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Review, Category


def home(response):
    return render(response, 'gallery/home.html')


'''Galley page displays sorts categories and filterd gallery'''
def gallery(request):
    # Retrieves the selected category from the query parameters.
    selected_category=request.GET.get('category')
    
    # do not filter 'all' / None
    if selected_category is not None and not selected_category == "All":
        images= Image.objects.all().filter(categories__title = selected_category)
    else:
        images= Image.objects.all()
    categories= Category.objects.all().order_by('title')
    
    # Move the category with title "All" to the front
    all_category = categories.filter(title='All').first()
    if all_category:
        categories = [all_category] + [category for category in categories if category != all_category]

    context= {"images":images,"categories": categories, "selected_category":selected_category} 
    return render(request, 'gallery/gallery.html', context)


'''Image page display images and sorted reviews according to the selected reviews page'''
def image(request, image_id):
    # define num of reviews for each review's page
    limit=5
    # data from param
    image_details = get_object_or_404(Image, pk=image_id)
    # data from query string * calculate page and limit to get offset
    offset = (int(request.GET.get('offset', 0))-1)*limit
    type = request.GET.get('type')
    
    total_reviews_count = image_details.reviews.count()
    
    if type == 'prev':
        offset = max(offset - limit, 0)
    elif type == 'next':
        offset = min(offset + limit, total_reviews_count)
    else:
        offset=0
        
    #  handle the case where it goes beyond the total number of reviews.
    if offset == total_reviews_count:
        offset -= total_reviews_count%5
        
    reviews = image_details.reviews.all().order_by('-created_at')[offset:offset+limit]  # Get all reviews for the image
    
    # Create a string of stars based on the rate and Add a new attribute to the review object
    for review in reviews:
        rate = review.rate
        stars = '*' * rate
        review.star_rating = stars  
    
    context= {'imageDetails': image_details, 'reviews': reviews, "lastOffset":(int(offset/5)+1)}
    return render(request, 'gallery/image.html', context=context)


@login_required
def addreview(request, image_id):
    
    # Retrieves details from the request (form).
    if request.method == 'POST':
        image = Image.objects.get(pk=image_id)
        text = request.POST.get('review_text')
        rate=int(request.POST.get('rate'))
        user = request.user  
        
        if request.POST.get('anonymous')=="clicked":
            anonymous=True
        else:
            anonymous=False
            
        review = Review(image=image, text=text, user=user, anonymous=anonymous, rate=rate)
        review.save()   
        
    return redirect('Image', image_id=image_id)

