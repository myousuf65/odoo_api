
# include everything from authentication.py here

newContact = {
    'name' : 'test-contact-bad',
    'street' : 'test-address',
    'email' : 'email@example.com',
    'mobile' : '97111233',
    'phone' : '3134144442',
    'type' : 'contact',
    'company_type' : 'person', 
    'parent_id' : '1975',                         # id of parent company
	# 'x_personincharger' : 'Steve Wong',
    'x_salesperson' : 'Steve Wong',
    'x_studio_approved_1' : True,
}

new_id = models.execute_kw(DB_NAME, uid, PASSWORD, 'res.partner', 'create', [newContact])
print(new_id)

