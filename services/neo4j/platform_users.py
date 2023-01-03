users = [
    {  
        "name": "User1",
        "email": "jame@smith.com",
        "fb": "F1",
        "phone": "654321"
    },
    {
        "name": "User2",
        "email": "abc@gmail.com",
        "fb": "F2",
        "phone": "123098"
    },
    {
        "name": "User3",
        "email": "abc@gmail.com",
        "fb": "F3",
        "phone": "123456"
    },
    {
        "name": "User4",
        "email": "efg@gmail.com",
        "fb": "F3",
        "phone": "987654"
    },
    {
        "name": "User99",
        "email": "xyz@gmail.com",
        "fb": "F4",
        "phone": "123456"
    },
]

links = [   {"src": "User1", "target": "User2", "link": "email"},
            {"src": "User2", "target": "User3", "link": "email"},
             {"src": "User3", "target": "User4", "link": "facebook"},
             {"src": "User3", "target": "User99", "link": "phone"},
             ]
            
links_bulk = [(35,{"email":"REMI"}, 39)]

items =[{"type":"market place ",
          "platformn": "ebay",
          "url": "...",
          "collected for user": {}},
        {"type": "social media",
            "Platform": "instagram",
            "url": "...",
             "collected for user": {}},

        {}]
