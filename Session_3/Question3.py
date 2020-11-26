# Solution:

# Variables to store data in
Century = ""
Decade = ""

# Get user input
book_year = input("What year was your book written? ")

# Use int() function to check whether the year is within the library's book range
# Why don't we just use int() in the beginning when getting the input?
# This is because we need to index each value in book_year and can't do that if it's a string ...
if int(book_year) >= 1800 and int(book_year) <= 1950:

    # If within the range check if the 2nd number is an 8
    if book_year[1] == '8':
        Century = 'Nineteenth Century'

    # If not, then the only other option is that it's a 9 hence, the else statement and not an elif statement
    else:
        Century = 'Twentieth Century'

    # Now we'll run a different if statement, with a series of elif to check for the decade
    # We're putting this within the first if statement so that it only runs WHEN the century is within the correct range
    # This helps us avoid running it when the century is out of bounds, aka > 1950 or < 1800
    if book_year[2] == '0':
        Decade = 'Naughties'
    elif book_year[2] == '1':
        Decade = 'Teens'
    elif book_year[2] == '2':
        Decade = 'Twenties'
    elif book_year[2] == '3':
        Decade = 'Thirties'
    elif book_year[2] == '4':
        Decade = 'Fourties'
    elif book_year[2] == '5':
        Decade = 'Fifties'
    elif book_year[2] == '6':
        Decade = 'Sixties'
    elif book_year[2] == '7':
        Decade = 'Seventies'
    elif book_year[2] == '8':
        Decade = 'Eighties'
    elif book_year[2] == '9':
        Decade = 'Nineties'
    print("{}, {}".format(Century,Decade))

# If the input value is not within the range, inform the user.
else:
    print("Library doesn't have books within this range")