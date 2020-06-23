# Query: Create 3 new users   
User.objects.create(first_name="Michael", last_name="Choi", email_address="mchoi@foo.com", age=29)
User.objects.create(first_name="Dylan", last_name="Sharkey", email_address="dsharkey@foo.com", age=44)
User.objects.create(first_name="Devon", last_name="Newsom", email_address="sup@foo.com", age=99)

# Query: Retrieve all the users   
User.objects.all()

# Query: Retrieve the last user   
User.objects.last()

# Query: Retrieve the first user  
User.objects.first()

# Query: Change the user with id=3 so their last name is Pancakes.    
user_three = User.objects.get(id=3)
user_three.last_name = "Pancakes"
user_three.save()

# Query: Delete the user with id=2 from the database  
user_two = User.objects.get(id=2)
user_two.delete()

# Query: Get all the users, sorted by their first name    
User.objects.order_by('first_name')

# BONUS Query: Get all the users, sorted by their first name in descending order  
User.objects.order_by('-first_name')
