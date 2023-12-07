class Ticket:
    ticket_counter = 1
    ticket_list = []
    open_tickets = 0
    closed_tickets = 0

    def __init__(self, staff_id, staff_name, email_id, description):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.email_id = email_id
        self.description = description
        self.ticket_number = Ticket.ticket_counter + 2000
        self.status = 'Open'
        self.response = 'Not Yet Provided'
        Ticket.ticket_counter += 1
        Ticket.ticket_list.append(self)

    def password_change_requested(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.staff_name[:3]
            self.response = {new_password}
            print(f"New password is :{new_password}")
            self.status = "Closed"

    def resolve_ticket(self):
        self.status = "Closed"

    def reopen_ticket(self):
        if self.status == "Closed":
            self.status = "Reopened"

    def update_response(self, response):
        self.response = response
        self.status = "Closed"

    @staticmethod
    def ticket_stats():
        total_tickets = len(Ticket.ticket_list)
        resolved_tickets = len([ticket for ticket in Ticket.ticket_list if ticket.status == "Closed"])
        open_tickets = len([ticket for ticket in Ticket.ticket_list if ticket.status != "Closed"])
        return total_tickets, resolved_tickets, open_tickets

    @staticmethod
    def display_ticket_info():
        for ticket in Ticket.ticket_list:
            print("Ticket Information:")
            print(f"Ticket Number: {ticket.ticket_number}")
            print(f"Creator Name: {ticket.staff_name}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Email Address: {ticket.email_id}")
            print(f"Issue Description: {ticket.description}")
            print(f"Response: {ticket.response}")
            print(f"Status: {ticket.status}")


def submit_ticket():
    staff_id = input(" Enter your staff id")
    staff_name = input("Enter your name")
    email_id = input("Enter your email")
    description = input("Enter description of problem")
    ticket = Ticket(staff_id, staff_name, email_id, description)
    print(f"Ticket {ticket.ticket_number} created successfully")


def show_all_tickets():
    Ticket.display_ticket_info()


def respond_to_ticket():
    ticket_number = int(input("Enter ticket number: "))
    response = input("Enter response: ")
    for ticket in Ticket.ticket_list:
        if ticket.ticket_number == ticket_number:
            ticket.update_response(response)
            print(f"Ticket {ticket_number} updated successfully")
            Ticket.closed_tickets += 1
            Ticket.open_tickets -= 1
            ticket.status = "Closed"


def reopen_resolved_ticket():
    ticket_number = int(input('Enter ticket number: '))
    for ticket in Ticket.ticket_list:
        if ticket.ticket_number == ticket_number:
            ticket.status = "Reopened"
        Ticket.closed_tickets -= 1
        Ticket.open_tickets += 1
        print(f"Ticket is reopened")


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
            submit_ticket()
            Ticket.ticket_list[len(Ticket.ticket_list) - 1].password_change_requested()
            another_prob = input("is there another problem that you are having? (Y/N) /n")
            while another_prob == "Y":
                submit_ticket()
                Ticket.ticket_list[len(Ticket.ticket_list) - 1].password_change_requested()
                another_prob = input("is there another problem that you are having? (Y/N) /n")
            else:
                main()

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
