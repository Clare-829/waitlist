class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time
     
    def __repr__(self):
        return str([self.item, self.priority])

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time

class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"


    

class Waitlist:
    def __init__(self):
        self._entries = []
    
    def len(self):
        len(self._entries)

    def add_customer(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._upheap(len(self._entries) - 1)

    def peek(self):
        if len(self.entries) == 0:
            return None
        else:
            return (self._entries[0].name, self._entries[0].time)
        

    def seat_customer(self):
        L = self._entries
        item = L[0].name
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        return item
    
    def _parent(self, item):
        return (item - 1) // 2
    
    def _children(self, item):
        left = 2 * item + 1
        right = 2 * item + 2
        return range(left, min(len(self._entries), right + 1)) 
   
    def print_reservation_list(self):
        self._entries.sort()
        results = []
        for entry in self._entries:
            results.append((entry.name, entry.time))
            print(entry.name, entry.time)
        return results
    
    def _upheap(self, item):
        all_entries = self._entries
        parent = self._parent(item)
        if item> 0 and all_entries[item] < all_entries[parent]:
            self._swap(item, parent)
            self._upheap(parent)
    
    def change_reservation(self, name, new_priority):
        all_entries = self._entries
        results = []
        for entry in all_entries:
            if entry.name == name:
                # update with new time
                entry.time = new_priority
                results.append((entry.name, entry.time))

if __name__ == "__main__":
    new_waitlist = Waitlist()
    new_waitlist.add_customer('Mary Willow', '10:55')
    new_waitlist.add_customer('Collins Ponds', '08:30')
    new_waitlist.add_customer('Michelle Rice', '18:45')
    print(new_waitlist.print_reservation_list())
    print([('Collins Ponds 08:30'), ('Mary Willow 10:55'), ('Michelle Rice 18:45')])
