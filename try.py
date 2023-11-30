class Ticket:
    counter = 1
    ticket_list = []

    def __init__(self, staff_id, creator_name, email, description):
        self.ticket_number = Ticket.counter + 2000
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.email = email
        self.description = description
        self.status = 'Open'
        self.response = 'Not Yet Provided'
        Ticket.counter += 1
        Ticket.ticket_list.append(self)

    def resolve_password_change(self):
        if 'Password Change' in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f'New password generated: {new_password}'
            self.status = 'Closed'

    def resolve_ticket(self):
        self.status = 'Closed'

    def reopen_ticket(self):
        self.status = 'Reopened'

    def provide_response(self, response):
        self.response = response

    @staticmethod
    def ticket_stats():
        created = len(Ticket.ticket_list)
        resolved = len([ticket for ticket in Ticket.ticket_list if ticket.status == 'Closed'])
        to_solve = len([ticket for ticket in Ticket.ticket_list if ticket.status != 'Closed'])
        return (created, resolved, to_solve)

    @staticmethod
    def print_tickets():
        for ticket in Ticket.ticket_list:
            print(f'Ticket Number: {ticket.ticket_number}\n'
                  f'Ticket Creator: {ticket.creator_name}\n'
                  f'Staff ID: {ticket.staff_id}\n'
                  f'Email Address: {ticket.email}\n'
                  f'Description: {ticket.description}\n'
                  f'Response: {ticket.response}\n'
                  f'Ticket Status: {ticket.status}\n')


def create_ticket():
    staff_id = input('Enter staff ID: ')
    creator_name = input('Enter creator name: ')
    email = input('Enter contact email: ')
    description = input('Enter description: ')
    ticket = Ticket(staff_id, creator_name, email, description)
    print(f'Ticket {ticket.ticket_number} created successfully.')


def see_all_tickets():
    Ticket.print_tickets()


def respond_to_ticket():
    ticket_number = int(input('Enter ticket number: '))
    response = input('Enter response: ')
    for ticket in Ticket.ticket_list:
        if ticket.ticket_number == ticket_number:
            ticket.provide_response(response)
            print(f'Ticket {ticket_number} updated successfully.')
            return
    print(f'Ticket {ticket_number} not found.')


def submit_ticket():
    ticket_number = int(input('Enter ticket number: '))
    for ticket in Ticket.ticket_list:
        if ticket.ticket_number == ticket_number:
            ticket.resolve_password_change()
            print(f'Ticket {ticket_number} resolved successfully.')
            return
    print(f'Ticket {ticket_number} not found.')


def exit_menu():
    print('Exiting program...')
    exit()


def main_menu():
    while True:
        print('\n===== Ticket System Menu =====')
        print('1. Create a new ticket')
        print('2. See all tickets')
        print('3. Respond to a ticket')
        print('4. Submit a resolved ticket')
        print('5. View ticket statistics')
        print('6. Exit program')
        choice = input('\nEnter your choice: ')
        if choice == '1':
            create_ticket()
        elif choice == '2':
            see_all_tickets()
        elif choice == '3':
            respond_to_ticket()
        elif choice == '4':
            submit_ticket()
        elif choice == '5':
            created, resolved, to_solve = Ticket.ticket_stats()
            print(f'\nNumber of created tickets: {created}')
            print(f'Number of resolved tickets: {resolved}')
            print(f'Number of tickets to solve: {to_solve}')
        elif choice == '6':
            exit_menu()
            break
        else:
            print('Invalid choice. Please try again.')


main_menu()
