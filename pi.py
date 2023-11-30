class Ticket:
    def __init__(self, staffID, name, email, description):
        self.staffID = staffID
        self.name = name
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def __str__(self):
        return f"Ticket Number: {self.ticketNumber} Name: {self.name} Staff ID: {self.staffID} Email: {self.email} Description: {self.description} Response: {self.response} Status: {self.status}"


class HelpDesk:
    ticketNumber = 2000
    openTickets = 0
    closedTickets = 0

    def __init__(self):
        self.tickets = []

    def submitTicket(self, staffID, name, email, description):
        newTicket = Ticket(staffID, name, email, description)
        self.tickets.append(newTicket)
        newTicket.ticketNumber = HelpDesk.ticketNumber
        HelpDesk.ticketNumber += 1
        HelpDesk.openTickets += 1
        if "Password Change" in description:
            newTicket.response = f"New Password: {staffID[:2]}{name[:3]}"
            HelpDesk.closedTickets += 1
            HelpDesk.openTickets -= 1
            newTicket.status = "Closed"
        return newTicket

    def respondToTicket(self, ticketNumber, response):
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                ticket.response = response
                HelpDesk.closedTickets += 1
                HelpDesk.openTickets -= 1
                ticket.status = "Closed"

    def reopenTicket(self, ticketNumber):
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                ticket.status = "Reopened"
                HelpDesk.openTickets += 1
                HelpDesk.closedTickets -= 1

    def display_ticket(self, ticketNumber):
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                print(ticket)

    def displayStatistics(self):
        print(
            f"Number of tickets submitted: {HelpDesk.ticketNumber - 2000} Number of open tickets: {HelpDesk.openTickets} Number of closed tickets: {HelpDesk.closedTickets}")


def main():
    while True:
        print("Select the following choices\n")
        print("(1) Submit helpdesk ticket")
        print("(2) Show all tickets")
        print("(3) Respond to ticket by number")
        print("(4) Re open resolved ticket")
        print("(5) Display ticket statistics")
        print("(6)  Exit\n")
        choice = (input("Enter menu selection 1-6 : "))
        if choice == "1":
            display_ticket()
        elif choice == "2":
            show_all_tickets()
        elif choice == "3":
            respond_to_ticket()
        elif choice == "4":
            reopen_resolved_ticket()
        elif choice == "5":
            total_tickets, resolved_tickets, open_tickets = Ticket.ticket_stats()
            print(f"\n Number of total tickets: {total_tickets}")
            print(f" Number of resolved tickets: {resolved_tickets}")
            print(f"Number of tickets to solve: {open_tickets}")
        else:
            print("Please enter the right option")

main()
