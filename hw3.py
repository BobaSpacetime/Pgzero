err={"400": "Bad Request - The server couldn't understand the request.", "401": "Unauthorized - You need to log in first.", "403": "Forbidden - Access denied.", "404": "Not Found - The page vanished into the void.", "500": "Internal Server Error - The server broke itself."}
code = input("Enter error code: ")
if code in err:
    print(err[code])
else:
    print("Even the internet is confused.")