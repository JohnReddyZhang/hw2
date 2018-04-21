# Movie Box Office Ticket Window

_NOTE: This a draft and subject to change._

<img width="600px" src="https://loyoladigitaladvertising.files.wordpress.com/2014/04/box-office-1.jpg">


In this scenario, you will build an application for
an box office ticket agent at a movie theater.  
Customers arrive at the theater and expect to be
able to perform the following transactions:

* Buy tickets for a movie up to 7 days in advance
* Get a refund for a ticket whose movie has not yet been shown

Therefore, a ticket agent needs to:

* Sell tickets for any movie for an upcoming showtime
* Refund a ticket when presented at the counter, if the movie
has not started yet
* Generate a report of the number of tickets sold and number of vacant
seats for any given showtime, past or future
* Generate a report of the total number of tickets sold on
any given date

Business Rules:

* Make sure every ticket has a unique serial number
* Up to 10 tickets can be purchased at once.
* Refunds can only be given if the movie hasn't started yet.
* Each theater has 200 seats.
* Each theater has five screens, so it can show five movies at
  the same time.
* Each movie is shown twice a day, at 2pm (the matinee) and 8pm.
* Ticket prices have four tiers.
* Movies shown on Mondays thru Thursdays are always cheaper than
  those shown on Friday, Saturdays, and Sundays.
* Matinee showtimes are alway cheaper than the evening showtime on the same day.
