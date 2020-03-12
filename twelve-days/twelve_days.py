def recite(start_verse, end_verse):
    gifts = [ 
        "a Partridge in a Pear Tree",
        "two Turtle Doves",  
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings", 
        "six Geese-a-Laying", 
        "seven Swans-a-Swimming", 
        "eight Maids-a-Milking", 
        "nine Ladies Dancing", 
        "ten Lords-a-Leaping", 
        "eleven Pipers Piping",
        "twelve Drummers Drumming" 
    ]

    days = [ 
        "first", 
        "second", 
        "third", 
        "fourth", 
        "fifth", 
        "sixth", 
        "seventh",
        "eighth", 
        "ninth", 
        "tenth", 
        "eleventh", 
        "twelfth"
    ]

    output = []

    for i in range(start_verse-1, end_verse,1):
        verse_day = days[i]
        verse_gift_list = gifts[i:: -1]

        if len(verse_gift_list) > 1:
            verse_gift_list[-1] = "and {}".format(verse_gift_list[-1])
        
        verse_gift_list = ", ".join(verse_gift_list)
        output.append("On the {} day of Christmas my true love gave to me: {}.".format(verse_day, verse_gift_list))
   
    return output
