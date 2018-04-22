# Box Office Agent

The application uses "cmd" module to imitate a command line style interaction.

Start the app by `./agent.py`

Help on operation
---
Type `?` or `help` for an overview of all possible commands.

Specific instruction of an operation can be viewed by `help <command>` or `?buy`

### buy:
Buy a ticket. e.g.`buy 20180412 n 3 6`

    Input: buy <date> <showtime> <auditorium>
    <date> format: yyyymmdd
    <showtime>: m for matinee, n for night
    <auditorium>: 1 - 5
    <number_of_tickets>: number of tickets you want to buy, 
    cannot exceed over 10.

The buy function now suffices limiting to 10 tickets, and checking whether the date is valid to buy a ticket.  
The function now can check whether your input is valid or not.  
When 200 tickets is filled up for an event, no more will be able to be sold. But it could accept refund.  
Price will be given based on inputs. 
There are four tiers and operator could dive in the code to set actual price in `event_class.py`  

### refund
Refund with specific serial number. (given by "buy" command) e.g. `refund`
    
    Input: refund <serial_number>
    <serial_number> is provided when you buy the ticket.
    
Only generated tickets could be refund.  
Your refund price will be given when you initiate a refund.


### report_day
Report of a certain day. e.g. `report_day 20180412`

    Generate a report of the total number of tickets sold on any given date
    Input: <date>
    Print: ticket sale for the day.
    <date> format: yyyymmdd
    
If no event is found, report will have 0 on that day.
    
### report_event
Report of an event. e.g. `report_event 20180412 n 3`

    Generate a report of the number of tickets sold and number of vacant seats
    for any given showtime, past or future
    Input: r_event <date> <showtime> <auditorium>
    Print: ticket sale for the specific event, if exists.
    <date> format: yyyymmdd
    <showtime>: m for matinee, n for night
    <auditorium>: 1 - 5
    
An event is not created if no one is buying a ticket, thus will not have reports for that day.


### Additional instructions
You could find some more introductions by both running the `agent` script, 
or going into the `.py` scripts and read its documents.