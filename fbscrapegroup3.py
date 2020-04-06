#https://github.com/kevinzg/facebook-scraper


from facebook_scraper import get_posts

grp = input('what do you want to search?: ')
pg = input('how many pages of posts?: ')
pgs = int(pg)
count = 0
for post in get_posts(grp, pages=pgs):
    print(post['text'])
    print('Likes: ', post['likes'])
    print('Shares: ', post['shares'])
    print('Image: ', post['image'])
    print('Post URL: ', post['post_url'])
    print('Link: ', post['link'])
    print('Date and Time: ', post['time'])
    print('Post ID: ', post['post_id'])
    count = count+1
    print()
print("Count: ", count)
