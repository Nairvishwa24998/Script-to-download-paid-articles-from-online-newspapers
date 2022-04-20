# Script-to-download-paid-articles-from-online-newspapers

Libraries Used:
The script relies on the urllib library in Python 3.

Works for:(Not exhaustive)

New York Times
Bloomberg (Multiple tries in a short span of time might fail since Bloomberg understands that the requests are automated)
Economist
Washington Post
Los Angeles Times
Reuters(The formatting becomes a bit off but the text is very much readable)
Athletic
Guardian

Doesn't work for:(Ones identified so far)
USA Today
WSJ

Working:
1) Obtains the link of the concerned article as input.
2)  Uses a function to return the characters between the first slash and html(if it is present in the link) which is then later added with the .html extension to be used as the name of the file which would be created
3) write to the above file in UTF-8 encoding format.
