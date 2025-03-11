# list of email addresses and you want to extract the domain part
# Given email adresses
emails = ["alice@example.com", "bob@sample.org", "charlie@mydomain.net"]
# Using list comprehension split function
domains = [email.split('@')[1] for email in emails]

print(domains)

'''     OUTPUT
['example.com', 'sample.org', 'mydomain.net']
'''
