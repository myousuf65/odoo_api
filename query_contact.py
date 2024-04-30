# include authentication.py

query = models.execute_kw(DB_NAME, uid , PASSWORD,  'res.partner', 'search', [
        [
            ['display_name', '=', 'Berlin Spa Limited'],
            ['company_type', '=', 'person' ]
        ]
    ])

partners_data = models.execute_kw(DB_NAME, uid, PASSWORD, 'res.partner', 'read', [[3583]])
print(partners_data)

