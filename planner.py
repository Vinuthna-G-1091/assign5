

from flight import Flight
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)][0] > self.heap[index][0]:
            # Swap if parent is greater than current node
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self.heapify_down(0)
        return root

    def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != index:
            # Swap and continue heapifying if needed
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

# Example usage

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:  # If queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:  # If queue becomes empty
            self.rear = None
        self.size -= 1
        return temp.value

    def is_empty(self):
        return self.front is None

    def front_element(self):
        if not self.is_empty():
            return self.front.value
        else:
            print("Queue is empty")

    def queue_size(self):
        return self.size

class Planner:
    def __init__(self, flights):
        """The Planner
        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        
        n=len(flights)
        m=0
        self.no_of_flights=n+1
        self.flight_adj=[[] for _ in range(n+1)]
        
        for i in range(n):
            m=max(m,flights[i].start_city,flights[i].end_city)
            
        self.s_city=[[] for _ in range(m+1)]
        
        for i in range(n):
            self.s_city[flights[i].start_city].append(flights[i])
            
        for f in flights:
            for af in self.s_city[f.end_city]:
                if f.arrival_time+20<=af.departure_time:
                    self.flight_adj[f.flight_no].append(af)
                    
        self.no_of_cities=m+1
        

        # pass
    
        
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        # correct code but taking 45 sec
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        n=self.no_of_flights
        parent=[-1]*(n+1)
        m=self.no_of_cities
        dist=[-1]*(m+1)
        visited=[-1]*(n+1)
        queue=Queue()
        d=1
        poss=[]
        queue.enqueue(0)
        
        if start_city==end_city:
            return []
        
        for f in self.s_city[start_city]:
            if f.departure_time>=t1 and f.arrival_time<=t2:
                queue.enqueue(f)
                parent[f.flight_no]=(None,0)
                visited[f.flight_no]=1
                if f.end_city==end_city:
                    if poss==[]:
                        poss.append(f)
                    else:
                        if(poss[0].arrival_time>f.arrival_time):
                            poss[0]=f
                if dist[f.end_city]==-1:
                    dist[f.end_city]=d
        
        # queue.enqueue(0)
        while queue:
            fl=queue.pop()
            # print(fl)
            if fl!=0:
                for f in self.flight_adj[fl.flight_no]:
                    if visited[f.flight_no]==-1:
                        visited[f.flight_no]=1
                        if f.departure_time>=t1 and f.arrival_time<=t2:
                            queue.enqueue(f)
                            if parent[f.flight_no]==-1:
                                parent[f.flight_no]=(fl,fl.arrival_time)
                            else:
                                if fl.arrival_time<parent[f.flight_no][1]:
                                    parent[f.flight_no]=(fl,fl.arrival_time)
                            if f.end_city==end_city:
                                # print(poss)
                                if poss==[]:
                                    poss.append(f)
                                else:
                                    if(poss[0].arrival_time>f.arrival_time):
                                        poss[0]=f
                                # print(poss)
                            if dist[f.end_city]==-1:
                                dist[f.end_city]=d
                    # else:
                        
            else:
                if poss!=[]:
                    ans=[None]*d
                    f=poss[0]
                    while f:
                        ans[d-1]=f
                        f=parent[f.flight_no][0]
                        d-=1
                    # print(ans)
                    return ans
                else:
                    d+=1
                    # print(queue.front_element())
                    if queue.front_element==0 or queue.is_empty():
                        # print("vinuthna")
                        # print(queue.front_element)
                        return []
                    else:
                        # print("vinuthna")
                        queue.enqueue(0)
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        heap=MinHeap()
        n=self.no_of_flights
        parent=[None]*(n+1)
        visited=[-1]*(n+1)
        
        if start_city==end_city:
            return []
        
        for f in self.s_city[start_city]:
            # print(f)
            if f.departure_time>=t1 and f.arrival_time<=t2:
                visited[f.flight_no]=0
                parent[f.flight_no]=None
                heap.insert((f.fare,f))
                
        last_flight=None
        while heap.size():
                top=heap.extract_min()
                if top[1].end_city==end_city:
                    last_flight=top[1]
                    break
                else:
                    for f in self.flight_adj[top[1].flight_no]:
                            if f.departure_time>=t1 and f.arrival_time<=t2:
                                # print(f.flight_no)
                                if visited[f.flight_no]==-1:
                                    visited[f.flight_no]=0
                                    parent[f.flight_no]=top[1]
                                    # 
                                    heap.insert((top[0]+f.fare,f))
                # visited[top[1].flight_no]=1
        ans=[]
        f=last_flight
        while f:
            ans.append(f)
            f=parent[f.flight_no]
        return ans[::-1]
        #   return []
                
        
        # pass
    
    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        # pass
        n=self.no_of_flights
        parent=[-1]*(n+1)
        m=self.no_of_cities
        dist=[-1]*(m+1)
        queue=Queue()
        # visited=[-1]*(n+1)
        d=1
        poss=[]
        queue.enqueue(0)
        if start_city==end_city:
            return []
        for f in self.s_city[start_city]:
            if f.departure_time>=t1 and f.arrival_time<=t2:
                queue.enqueue((f,f.fare))
                parent[f.flight_no]=None
                if f.end_city==end_city:
                    if poss==[]:
                        poss.append((f,f.fare))
                    else:
                        if(poss[0][1]>f.fare):
                            poss[0]=(f,f.fare)
                if dist[f.end_city]==-1:
                    dist[f.end_city]=d
        # queue.enqueue(0)
        while queue:
            fl=queue.pop()
            # print(fl)
            if fl!=0:
                for f in self.flight_adj[fl[0].flight_no]:
                    if f.departure_time>=t1 and f.arrival_time<=t2:
                        # if visited[f.flight_no]==-1:
                        #     visited[f.flight_no]=1
                            
                        if  parent[f.flight_no]==-1:
                            parent[f.flight_no]=(fl[0],f.fare+fl[1])
                            queue.enqueue((f,f.fare+fl[1]))
                        else:
                            if  parent[f.flight_no]:
                                if parent[f.flight_no][1]>f.fare+fl[1]:
                                    parent[f.flight_no]=(fl[0],f.fare+fl[1])
                                    queue.enqueue((f,f.fare+fl[1]))
                        if f.end_city==end_city:
                            
                            if poss==[]:
                                poss.append((f,f.fare+fl[1]))
                            else:
                                if(poss[0][1]>f.fare+fl[1]):
                                    poss[0]=(f,f.fare+fl[1])
                        if dist[f.end_city]==-1:
                            dist[f.end_city]=d
            else:
                if poss!=[]:
                    # print(poss[0][0].flight_no)
                    # print(parent[poss[0][0].flight_no])
                    # print(d)
                    ans=[None]*d
                    f=poss[0][0]
                    while f:
                        ans[d-1]=f
                        if parent[f.flight_no]:
                            f=parent[f.flight_no][0]
                        else :
                            f=None
                        d-=1
                    # print(ans)
                    return ans
                else:
                    d+=1
                    # print(queue.front_element())
                    if queue.front_element==0 or queue.is_empty():
                        # print("vinuthna")
                        # print(queue.front_element)
                        return []
                    else:
                        # print("vinuthna")
                        queue.enqueue(0)