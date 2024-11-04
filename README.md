This is my first personal project repository.
After being introduced to Python in CS 417 - Topics in OOP, I wanted to be more comfortable with Python.
When I could, I added to this repo over the break between classes.

The Plan: 
>Recreate a budget tracking application similar to EveryDollar by Ramsey Solutions for my own personal use.
>To do so, I wanted to utilize Python and SQL to read and write to a database of planned income and expenses hosted on a raspberry pi 4.
>Every month has a budget with total income divided into planned expense cateories. 
>As money is spent, the user will add a record detailing the date, amount, category, and details (on what/where) of the expense.
>This is stored in the database so that the application can later read these records and calculated remaining funds, over/under amount and percentage, and export the record into different file formats.
>Once this is done, I could look into expanding support for devices other than my home PC- other computers, mobile devices, etc.

Current Implementation:
>The database is hosted on a raspberry pi and the development pc is authorized to access it.
>It is required that I authorize each device as a DB user by IP address, so local devices are ideal because they can be easily looked up on the router's DHCP client table.
>This seems like the largest roadblock for devices that are not on my local network; I have to know the IP address of each user device for the program to work with the database properly using this method.
>
>The current build has support to create a DB and insert categories and budgets into the respective tables within the database.
>There is no select-from or reading database information through the python scripts at the moment, but that is my next step.

Planned Outcome:
>+Python Experience
>
>+SQL Experience
>
>+Pi/Debian/Networking Experience - the raspberry pi would finally be put to use!
>
>Have a budget tracking app with the premium features for free
