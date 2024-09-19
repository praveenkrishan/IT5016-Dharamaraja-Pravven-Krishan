class RequestSystem:

    request_counter = 1

    def __init__(self):

        self.requests = {}
        self.user_details = {}

    def user_info(self):

        name = input("Enter your name")
        date = int(input("Enter the date"))
        staffID = int(input("Enter the ID"))
        requisitionID = input("Enter your requisitionID")
        self.user_details = {'name': name, 'date': date, 'staffID': staffID, 'requisitionID': requisitionID}
        print("user information collected succesfully.\n")

    def request_details(self):

        items = []
        total = 0
        while True:
            item_name = input("Enter item name (or type 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            cost = float(input(f"Enter cost for{item_name}: "))
            items.append((item_name, cost))
            total += cost
        print(f"\nTotal amount for request is: ${total:.2f}")
        return total, items

    def request_approval(self, total_amount):

        status = "approved" if total_amount < 500 else "pending"
        requestID = RequestSystem.request_counter
        RequestSystem.request_counter += 1
        request = {
            'id' : requestID,
            'user' : self.staff_info,
            'total' : total_amount,
            'status' : status,

        }
        self.requst.append(request)
        print(f"Request Submitted with ID {request_id} and status '{status}'.\n")

    def respond_request(self):

        request_id = int(input("enter the request ID to respond to: "))
        for request in self.requests:
            if request['id'] == "pending":
                response = input("approve or not approve? (A/N): ").strip().upper()
                request ['status'] = "approved" if response == "A" else "not approved"
                print(f"Request {request_id} has been updated to '{request['status']}'.\n")
            else:
                print("this request is not pending; no action needed.\n")
            return
        print("Request ID not found.\n")


    def display_request(self):

        print("\nRequest Details:")
        for request in self.requests:
            print(f"ID: {request['id']}, user: {request['user']['name']}, "
                  f"Total: ${request['total']:.2f}, status: {request['status']}")

    def request_statistic(self):

        total_submitted = len(self.requests)
        approved = sum(1 for req in self.requests if req ['status'] == 'approved')
        pending = sum(1 for req in self.requests if req ['status'] == 'pending')
        not_approved = sum(1 for req in self.requests if req ['status'] == 'not approved')

        print("\nRequest Statistics:")
        print(f"total number of requests submitted: {total_submitted}")
        print(f"total number of approved requests: {approved}")  
        print(f"total number of pending requests: {pending}")  
        print(f"total number of not approved requests: {not_approved}")


request_system = RequestSystem()
request_system.user_info()
total, items = Request_system.request.details()
Request_system.request.approval(total)
Request_system.respond.request()
Request_system.display.request()
Request_system.request.statistics()                                       


                


      