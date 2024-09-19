class RequestSystem:
   
    request_counter = 1
 
    def __init__(self):
     
        self.requests = []
        self.user_details = {}  
 
    def user_info(self):
       
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        self.user_details = {'name': name, 'age': age, 'email': email}
        print("User information collected successfully.\n")
 
    def request_details(self):
       
        items = []
        total = 0
        while True:
            item_name = input("Enter item name (or type 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            cost = float(input(f"Enter cost for {item_name}: "))
            items.append((item_name, cost))
            total += cost
        print(f"\nTotal amount for the request is: ${total:.2f}")
        return total, items
 
    def request_approval(self, total_amount):
        
        status = "approved" if total_amount < 150 else "pending"
        request_id = RequestSystem.request_counter
        RequestSystem.request_counter += 1
        request = {
            'id': request_id,
            'user': self.user_details,
            'total': total_amount,
            'status': status,
        }
        self.requests.append(request)
        print(f"Request submitted with ID {request_id} and status '{status}'.\n")
 
    def respond_request(self):
       
        request_id = int(input("Enter the request ID to respond to: "))
        for request in self.requests:
            if request['id'] == request_id:
                if request['status'] == "pending":
                    response = input("Approve or Not Approve? (A/N): ").strip().upper()
                    request['status'] = "approved" if response == "A" else "not approved"
                    print(f"Request {request_id} has been updated to '{request['status']}'.\n")
                else:
                    print("This request is not pending; no action needed.\n")
                return
        print("Request ID not found.\n")
 
    def display_request(self):
   
        print("\nRequest Details:")
        for request in self.requests:
            print(f"ID: {request['id']}, User: {request['user']['name']}, "
                  f"Total: ${request['total']:.2f}, Status: {request['status']}")
 
    def request_statistics(self):
 
        total_submitted = len(self.requests)
        approved = sum(1 for req in self.requests if req['status'] == 'approved')
        pending = sum(1 for req in self.requests if req['status'] == 'pending')
        not_approved = sum(1 for req in self.requests if req['status'] == 'not approved')
 
        print("\nRequest Statistics:")
        print(f"Total number of requests submitted: {total_submitted}")
        print(f"Total number of approved requests: {approved}")
        print(f"Total number of pending requests: {pending}")
        print(f"Total number of not approved requests: {not_approved}")
 
 
request_system = RequestSystem()
request_system.user_info()              
total, items = request_system.request_details()  
request_system.request_approval(total)  
request_system.respond_request()        
request_system.display_request()         
request_system.request_statistics()  