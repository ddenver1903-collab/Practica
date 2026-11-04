"""class PriorityQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value, priority):
        self.queue.append((value, priority))
    def dequeue(self):
        highest = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][1] > self.queue[highest][1]:
                highest = i
        return self.queue.pop(highest)[0]
    def peek(self):
        highest = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][1] > self.queue[highest][1]:
                highest = i
        return self.queue[highest][0]
    def is_empty(self):
        return len(self.queue) == 0
pq = PriorityQueue()
pq.enqueue("Task A",2)
pq.enqueue("Task B",5)
pq.enqueue("Task C",1)
pq.enqueue("Task D",4)
print("Peek:",pq.peek())
print("Removed:",pq.dequeue())
print("Removed:",pq.dequeue())
print("Peek:",pq.peek())
print("Is empty:",pq.is_empty())"""
"""import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value, priority):
        heapq.heappush(self.queue, (priority, value))
    def dequeue(self):
        return heapq.heappop(self.queue)[1]
    def peek(self):
        return self.queue[0][1]
    def is_empty(self):
        return len(self.queue) == 0
pq = PriorityQueue()
pq.enqueue("Task A",2)
pq.enqueue("Task B",5)
pq.enqueue("Task C",1)
pq.enqueue("Task D",4)
print("Peek:",pq.peek())
print("Removed:",pq.dequeue())
print("Removed:",pq.dequeue())
print("Peek:",pq.peek())
print("Is empty:",pq.is_empty())"""
"""import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value, priority):
        heapq.heappush(self.queue, (-priority, value))
    def dequeue(self):
        return heapq.heappop(self.queue)[1]
    def peek(self):
        return self.queue[0][1]
    def is_empty(self):
        return len(self.queue) == 0
pq = PriorityQueue()
pq.enqueue("Task A",5)
pq.enqueue("Task B",9)
pq.enqueue("Task C",2)
pq.enqueue("Task D",7)
pq.enqueue("Task E",1)
pq.enqueue("Task F",10)
pq.enqueue("Task G",4)
pq.enqueue("Task H",8)
pq.enqueue("Task I",3)
pq.enqueue("Task J",6)
print("Peek:",pq.dequeue())
while not pq.is_empty():
    print("Removed:",pq.dequeue())"""
"""import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0
    def enqueue(self, value, priority):
        heapq.heappush(self.queue, (-priority, self.counter, value))
    def dequeue(self):
        return heapq.heappop(self.queue)[2]
    def peek(self):
        return self.queue[0][2]
    def is_empty(self):
        return len(self.queue) == 0
pq = PriorityQueue()
pq.enqueue("Task A",2)
pq.enqueue("Task B",2)
pq.enqueue("Task C",2)
pq.enqueue("Task D",1)
pq.enqueue("Task E",3)
pq.enqueue("Task F",2)
pq.enqueue("Task G",1)
pq.enqueue("Task H",3)
pq.enqueue("Task I",1)
pq.enqueue("Task J",1)
print("Peek:",pq.dequeue())
while not pq.is_empty():
    print("Removed:",pq.dequeue())"""
"""import heapq
class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.counter = 0
    def add_task(self, name, priority, time):
        task = (priority, self.counter, name, time)
        heapq.heappush(self.tasks, task)
        self.counter += 1
    def next_task(self):
        if not self.tasks:
            return None
        task = heapq.heappop(self.tasks)
        return task[2], task[3]
    def display_tasks(self):
        if not self.tasks:
            print("No tasks")
            return
        print("Tasks:")
        for priority, counter, name, time in sorted(self.tasks):
            print(name,"Priority:",priority,"Time:",time,"min")
scheduler = TaskScheduler()
scheduler.add_task("Complete homework", 1, 30)
scheduler.add_task("Read a book", 4, 45)
scheduler.add_task("Prepare presentation", 3, 90)
scheduler.add_task("Practice math", 2, 40)
scheduler.add_task("Write report", 1, 120)
scheduler.add_task("Review notes", 3, 20)
scheduler.add_task("Do exercises", 2, 35)
scheduler.display_tasks()
print("Next task:",scheduler.next_task())
print("After completing the task:")
scheduler.display_tasks()"""
"""import heapq
class HospitalTriage:
    def __init__(self):
        self.patients = []
        self.counter = 0
    def add_patient(self, name, symptoms, urgency):
        patient = (-urgency, self.counter, name, symptoms)
        heapq.heappush(self.patients, patient)
        self.counter += 1
    def treat_patient(self):
        if not self.patients:
            return None
        patient = heapq.heappop(self.patients)
        return patient[2], patient[3], -patient[0]
    def display_patients(self):
        if not self.patients:
            print("No patients waiting")
            return
        print("Waiting patients:")
        for urgency, counter, name, symptoms in sorted(self.patients):
            print(name, "Symptoms:", symptoms, "Urgency:", -urgency)
hospital = HospitalTriage()
hospital.add_patient("Biba","Headache",3)
hospital.add_patient("Allan","Chest pain",10)
hospital.add_patient("Yelaman","Fever",5)
hospital.add_patient("Max","Broken arm",7)
hospital.add_patient("Damir","Cough",2)
hospital.add_patient("Akerke","Difficulty breathing",10)
hospital.add_patient("Yelaman2","Stomach pain",4)
hospital.add_patient("Zerde","Severe bleeding",9)
hospital.add_patient("Nurzat","Back pain",3)
hospital.add_patient("Daniyar","Allergic reaction",7)
hospital.display_patients()
print("Treating patients:")
while hospital.patients:
    print(hospital.treat_patient())"""
"""import heapq
class Printer:
    def __init__(self):
        self.jobs = []
        self.counter = 0
    def add_job(self, name, priority, pages):
        job = (-priority, self.counter, name, pages)
        heapq.heappush(self.jobs, job)
        self.counter += 1
    def process_job(self):
        if not self.jobs:
            return None
        job = heapq.heappop(self.jobs)
        return job[2], job[3]
    def jobs_remaining(self):
        return len(self.jobs)
printer = Printer()
printer.add_job("Document A", 3, 10)
printer.add_job("Document B", 5, 20)
printer.add_job("Document C", 1, 5)
printer.add_job("Document D", 4, 15)
printer.add_job("Document E", 5, 8)
printer.add_job("Document F", 2, 12)
printer.add_job("Document G", 3, 7)
printer.add_job("Document H", 1, 25)
printer.add_job("Document I", 4, 6)
printer.add_job("Document J", 2, 18)
print("Jobs remaining:", printer.jobs_remaining())
while printer.jobs_remaining() > 0:
    print("Printing:", printer.process_job())
    print("Jobs remaining:", printer.jobs_remaining())"""
"""import heapq
class NetworkRouter:
    def __init__(self):
        self.packets = []
        self.counter = 0
        self.total_bytes = 0
    def packet_arrival(self, packet_id, size, priority):
        packet = (-priority, self.counter, packet_id, size)
        heapq.heappush(self.packets, packet)
        self.counter += 1
    def transmit_packet(self):
        if not self.packets:
            return None
        packet = heapq.heappop(self.packets)
        self.total_bytes += packet[3]
        return packet[2], packet[3]
    def inspect_queue(self):
        if not self.packets:
            print("No packets waiting")
            return
        print("Packets in queue:")
        for priority, counter, packet_id, size in sorted(self.packets):
            print("id:",packet_id,"Size:",size,"bytes  Priority:",-priority)
    def get_total_bytes(self):
        return self.total_bytes
router = NetworkRouter()
router.packet_arrival(101,500,3)
router.packet_arrival(102,1200,5)
router.packet_arrival(103,800,2)
router.packet_arrival(104,1500,8)
router.packet_arrival(105,300,5)
router.packet_arrival(106,2000,1)
router.inspect_queue()
print("Transmitting packets:")
while router.packets:
    print("Transmitted:",router.transmit_packet())
    print("Total bytes:",router.get_total_bytes())
print("Final total bytes:",router.get_total_bytes())"""
"""import heapq
class CPUScheduler:
    def __init__(self):
        self.processes = []
        self.counter = 0
        self.total_time = 0
    def add_process(self, process_id, priority, burst_time):
        process = (-priority, self.counter, process_id, burst_time)
        heapq.heappush(self.processes, process)
        self.counter += 1
    def execute_process(self):
        if not self.processes:
            return None
        process = heapq.heappop(self.processes)
        self.total_time += process[3]
        return process[2], process[3]
    def execute_all(self):
        order = []
        while self.processes:
            process = self.execute_process()
            order.append(process)
        print("Execution order:")
        for process in order:
            print("Process:", process[0], "Burst time:", process[1])
        print("Total processing time:", self.total_time)
scheduler = CPUScheduler()
scheduler.add_process("P1", 3, 10)
scheduler.add_process("P2", 5, 20)
scheduler.add_process("P3", 2, 15)
scheduler.add_process("P4", 8, 5)
scheduler.add_process("P5", 1, 12)
scheduler.execute_all()"""
"""import heapq
def top_k_frequent(nums, k):
    frequency = {}
    first_position = {}
    for i, num in enumerate(nums):
        if num not in frequency:
            frequency[num] = 0
            first_position[num] = i
        frequency[num] += 1
    queue = []
    for num in frequency:
        heapq.heappush(queue, (-frequency[num], first_position[num], num))
    result = []
    for i in range(min(k, len(queue))):
        item = heapq.heappop(queue)
        result.append(item[2])
    return result
numbers = [1,1,1,2,2,3]
print("Top 2:", top_k_frequent(numbers,2))
numbers = [4,4,2,2,3,3,3,5,5,5]
print("Top 3:", top_k_frequent(numbers,3))"""
"""import heapq
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
def merge_k_lists(lists):
    heap = []
    counter = 0
    for head in lists:
        if head:
            heapq.heappush(heap, (head.key, counter, head))
            counter += 1
    dummy = Node(0)
    current = dummy
    while heap:
        key, index, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.key, counter, node.next))
            counter += 1
    current.next = None
    return dummy.next
def display(head):
    current = head
    while current:
        print(current.key, end=" ")
        current = current.next
    print()
list1 = Node(1)
list1.next = Node(4)
list1.next.next = Node(7)
list2 = Node(2)
list2.next = Node(5)
list2.next.next = Node(8)
list3 = Node(3)
list3.next = Node(6)
list3.next.next = Node(9)
lists = [list1, list2, list3]
result = merge_k_lists(lists)
print("Merged list:")
display(result)"""
"""import heapq
def dijkstra(graph, start):
    distances = {}
    for vertex in graph:
        distances[vertex] = float('inf')
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        distance, vertex = heapq.heappop(queue)
        if distance > distances[vertex]:
            continue
        for neighbor, weight in graph[vertex].items():
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
    return distances
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}
start = 'A'
result = dijkstra(graph, start)
print("Shortest distances from", start, ":")
for vertex, distance in result.items():
    print(vertex, ":", distance)"""
"""import heapq
class EventSimulation:
    def __init__(self):
        self.events = []
        self.counter = 0
    def add_event(self, name, time):
        event = (time, self.counter, name)
        heapq.heappush(self.events, event)
        self.counter += 1
    def process_event(self):
        if not self.events:
            return None
        event = heapq.heappop(self.events)
        return event[0], event[2]
    def display_events(self):
        if not self.events:
            print("No pending events")
            return
        print("Pending events:")
        for time, counter, name in sorted(self.events):
            print(name,"Time:",time)
simulation = EventSimulation()
simulation.add_event("Event A",10)
simulation.add_event("Event B",5)
simulation.add_event("Event C",15)
simulation.add_event("Event D",3)
simulation.add_event("Event E",12)
simulation.add_event("Event F",8)
simulation.add_event("Event G",20)
simulation.add_event("Event H",6)
simulation.add_event("Event I",18)
simulation.add_event("Event J",9)
simulation.display_events()
print("Processing events:")
while simulation.events:
    event = simulation.process_event()
    print("Processed:", event)
    if event[1] == "Event D":
        simulation.add_event("Event K",4)
        simulation.add_event("Event L",7)
        print("New events added: Event K and Event L")"""
"""import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.tasks = {}
        self.counter = 0
    def add_task(self, name, priority):
        self.tasks[name] = priority
        self.counter += 1
        heapq.heappush(self.heap, (priority, self.counter, name))
    def update_priority(self, name, new_priority):
        if name in self.tasks:
            self.tasks[name] = new_priority
            self.counter += 1
            heapq.heappush(self.heap, (new_priority, self.counter, name))
            print(name, "priority updated to", new_priority)
        else:
            print("Task not found")
    def execute_task(self):
        while self.heap:
            priority, counter, name = heapq.heappop(self.heap)
            if name in self.tasks and self.tasks[name] == priority:
                del self.tasks[name]
                print("Executing:", name, "Priority:", priority)
                return name
        print("Queue is empty")
    def display(self):
        print("Current tasks:")
        for name, priority in sorted(self.tasks.items(), key=lambda x: x[1]):
            print(name, "-", priority)
pq = PriorityQueue()
pq.add_task("Task A", 5)
pq.add_task("Task B", 3)
pq.add_task("Task C", 7)
pq.update_priority("Task A", 1)
pq.display()
pq.execute_task()
pq.execute_task()
pq.execute_task()"""
"""import heapq
class HelpDesk:
    def __init__(self):
        self.heap = []
        self.tickets = {}
        self.counter = 0
    def create_ticket(self, ticket_id, description, priority, submission_time):
        if ticket_id in self.tickets:
            print("Ticket already exists")
            return
        self.counter += 1
        self.tickets[ticket_id] = {
            "description": description,
            "priority": priority,
            "submission_time": submission_time,
            "order": self.counter
        }
        heapq.heappush(self.heap, (priority, self.counter, ticket_id))
        print("Ticket", ticket_id, "created")
    def process_ticket(self):
        while self.heap:
            priority, order, ticket_id = heapq.heappop(self.heap)
            if ticket_id in self.tickets:
                ticket = self.tickets[ticket_id]
                if ticket["priority"] == priority and ticket["order"] == order:
                    del self.tickets[ticket_id]
                    print("Processing ticket:", ticket_id)
                    print("Description:", ticket["description"])
                    print("Priority:", priority)
                    return
        print("No pending tickets")
    def view_next_ticket(self):
        while self.heap:
            priority, order, ticket_id = self.heap[0]
            if ticket_id in self.tickets:
                ticket = self.tickets[ticket_id]
                if ticket["priority"] == priority and ticket["order"] == order:
                    print("Next ticket:", ticket_id)
                    print("Description:", ticket["description"])
                    print("Priority:", priority)
                    print("Submission time:", ticket["submission_time"])
                    return
            heapq.heappop(self.heap)
        print("No pending tickets")
    def update_priority(self, ticket_id, new_priority):
        if ticket_id not in self.tickets:
            print("Ticket not found")
            return
        ticket = self.tickets[ticket_id]
        self.counter += 1
        ticket["priority"] = new_priority
        ticket["order"] = self.counter
        heapq.heappush(self.heap, (new_priority, self.counter, ticket_id))
        print("Ticket", ticket_id, "priority updated")
    def cancel_ticket(self, ticket_id):
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            print("Ticket", ticket_id, "cancelled")
        else:
            print("Ticket not found")
    def display_tickets(self):
        print("\nPending tickets:")
        if not self.tickets:
            print("No pending tickets")
            return
        for ticket_id, ticket in sorted(
            self.tickets.items(),
            key=lambda x: (x[1]["priority"], x[1]["order"])):
            print(ticket_id,"|",ticket["description"],"Priority:",ticket["priority"]," Time:",ticket["submission_time"])
helpdesk = HelpDesk()
helpdesk.create_ticket(101, "Wi-Fi problem", 3, "09:00")
helpdesk.create_ticket(102, "Cannot access exam", 1, "09:05")
helpdesk.create_ticket(103, "Password reset", 4, "09:10")
helpdesk.create_ticket(104, "Student portal error", 2, "09:15")
helpdesk.create_ticket(105, "Payment problem", 2, "09:20")
helpdesk.create_ticket(106, "Email not working", 3, "09:25")
helpdesk.create_ticket(107, "Registration problem", 1, "09:30")
helpdesk.create_ticket(108, "Library account issue", 4, "09:35")
helpdesk.update_priority(103, 1)
helpdesk.cancel_ticket(108)
helpdesk.view_next_ticket()
helpdesk.process_ticket()
helpdesk.process_ticket()
helpdesk.display_tickets()"""