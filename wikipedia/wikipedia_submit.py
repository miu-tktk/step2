import sys
import collections
#宿題１
#queueにidだけでなく、それまでの通ってきたid全てを持つリストを作る。
#ゴールに辿り着いた時、経路をprintすることができる。

class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # Read the pages file into self.titles.
        with open(pages_file) as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ") #src: source, dst: destination
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()


    # Find the longest titles. This is not related to a graph algorithm at all
    # though :)
    def find_longest_titles(self):
        titles = sorted(self.titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()


    # Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.titles.keys():
            link_count[id] = 0

        for id in self.titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.titles[dst], link_count_max)
        print()


    # Find the shortest path.
    # |start|: The title of the start page.
    # |goal|: The title of the goal page.
    def find_shortest_path(self, start, goal):
            ## Get the IDs of start and goal as they are given as strings
        for item, title in titles.items():
            if title == start:
                start_id = item
            if title == goal:
                goal_id = item
        
        # BFS
        queue = collections.deque()  #queue
        visited = {}                 #Explored nodes
        visited[start_id] = True                  #mark start as explored
        queue.appendleft((start_id, [start_id]))  #enqueue start_id
        while len(queue) > 0:  # end when the queue is empty
            (node, path) = queue.pop() # dequeue (node, list of nodes traversed from the start) 

            # If the goal is reached
            if node == goal_id:
                print("Found path:")
                order = 1
                for id in path:
                    print(str(order) +":"+ titles[id])
                    order += 1
                return
            
            # If the goal is not reached, add the linked nodes to the queue
            for child in links[node]:
                if not child in visited:  # If child is unexplored
                    visited[child] = True                    # Mark child as explored
                    queue.appendleft((child, path+[child]))  # Enqueue child, # By creating a new list with path+[child], it prevents mixing with other routes due to overwriting
                    print(queue)
        print("Path not found")
        #------------------------#


    # Calculate the page ranks and print the most popular pages.
    def find_most_popular_pages(self):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass


    # Do something more interesting!!
    def find_something_more_interesting(self):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass


# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("usage: %s pages_file links_file" % sys.argv[0])
#         exit(1)

#     wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
#     wikipedia.find_shortest_path("渋谷", "パレートの法則")

titles = {}
links = {}
# Read the pages file into self.titles.
with open("pages_medium.txt", mode="r") as file:
    for line in file:
        (id, title) = line.rstrip().split(" ")
        id = int(id)
        assert not id in titles, id
        titles[id] = title
        links[id] = []
print("Finished reading %s" % "pages_medium.txt")

# Read the links file into links.
with open("links_medium.txt", mode="r") as file:
    for line in file:
        (src, dst) = line.rstrip().split(" ") #src: source, dst: destination
        (src, dst) = (int(src), int(dst))
        assert src in titles, src
        assert dst in titles, dst
        links[src].append(dst)
print("Finished reading %s" % "links_medium.txt")
print()
def find_shortest_path(start, goal):
        ## Get the IDs of start and goal as they are given as strings
        for item, title in titles.items():
            if title == start:
                start_id = item
            if title == goal:
                goal_id = item
        
        # BFS
        queue = collections.deque()  #queue
        visited = {}                 #Explored nodes
        visited[start_id] = True                  #mark start as explored
        queue.appendleft((start_id, [start_id]))  #enqueue start_id
        while len(queue) > 0:  # end when the queue is empty
            (node, path) = queue.pop() # dequeue (node, list of nodes traversed from the start) 

            # If the goal is reached
            if node == goal_id:
                order = 1
                for id in path:
                    print(str(order) +":"+ titles[id])
                    order += 1
                return
            
            # If the goal is not reached, add the linked nodes to the queue
            for child in links[node]:
                if not child in visited:  # If child is unexplored
                    visited[child] = True                    # Mark child as explored
                    queue.appendleft((child, path+[child]))  # Enqueue child, # By creating a new list with path+[child], it prevents mixing with other routes due to overwriting
        print("Path not found")
find_shortest_path("渋谷", "パレートの法則")