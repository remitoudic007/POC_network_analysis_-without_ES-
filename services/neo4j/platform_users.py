users = [
    {
        "name": "User1",
        "email": "abc@gmail.com",
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
        "phone": "fgh@gmail.com"
    },
    {
        "name": "User99",
        "email": "abc@gmail.com",
        "fb": "F1",
        "phone": "123456"
    },
]

relations = [{"src": "User1", "target": "User2", "relation": "email"},
             {"src": "User2", "target": "User3", "relation": "email"},
             {"src": "User3", "target": "User4", "relation": "facebook"},
             {"src": "User3", "target": "User99", "relation": "phone"},
             ]
