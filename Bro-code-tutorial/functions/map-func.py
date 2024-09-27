 # map() = applies a function to each item in an iterable (list, tuple etc.)
# syntax:
# map(function, iterable)

# assume prices are in dollars
store_usd = [("shirt",20.0),
         ("pant",28.0),
         ("tie",3.0),
         ("cap",6.0),
         ("socks",2.0)]

to_inr = lambda  data : (data[0],data[1]*83.5)

store_inr = list(map(to_inr,store_usd)) # casting map object being created into a list object
print(store_inr,"\n",type(store_inr[1]))
