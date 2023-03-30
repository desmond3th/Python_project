from sys import maxsize
from itertools import permutations
from tkinter import *
V = 5
minPath=()
def travellingSalesmanProblem(graph, s):
    global minPath;
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        tempMinPath = i
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        if current_pathweight<min_path:
            minPath=tempMinPath
        min_path = min(min_path, current_pathweight)    
    return min_path



print("Enter the names of all the cities that you want to travel");
a=input("Enter the name of place one : ");
b=input("Enter the name of place two : ");
c=input("Enter the name of place three : ")
d=input("Enter the name of place four : ");
e=input("Enter the name of place five : ")

ab=int(input(f"Enter the distance between {a} and {b} : "));
ac=int(input(f"Enter the distance between {a} and {c} : "));
ad=int(input(f"Enter the distance between {a} and {d} : "));
ae=int(input(f"Enter the distance between {a} and {e} : "));
bc=int(input(f"Enter the distance between {b} and {c} : "));
bd=int(input(f"Enter the distance between {b} and {d} : "));
be=int(input(f"Enter the distance between {b} and {e} : "));
cd=int(input(f"Enter the distance between {c} and {d} : "));
ce=int(input(f"Enter the distance between {c} and {e} : "));
de=int(input(f"Enter the distance between {d} and {e} : "));


graph=[[0,ab ,ac ,ad , ae] , [ab , 0 , bc , bd , be],[ac , bc , 0,cd , ce] , [ad , bd , cd , 0 , de],[ae, be, ce , de,0]];


print(graph)

print(f"0.{a}")
print(f"1.{b}")
print(f"2.{c}")
print(f"3.{d}")
print(f"4.{e}")
answer='YES'
while(answer=='YES' or answer=='yes'):
    s=int(input("Select from given options (enter a number) that from where you want to start your journey : "));
    answer=travellingSalesmanProblem(graph, s);
    answer=str(answer)+' KM'
    resulter="The distance of the shortest path is : "+ answer;
    cities=[a,b,c,d,e]
    window=Tk()
    window.geometry('500x500')
    Label(text=resulter,font = "Verdana 10 bold",fg = "white", bg = "black").pack()
    Label(text=cities).pack()
    Label(text="The Path is : ",font = "Verdana 15 bold").pack()
    Label(text=cities[s],font = "Verdana 10 bold",fg = "white", bg = "black").pack()
    Label(text='↓',font = "Verdana 10 bold").pack()
    for x in minPath:
        Label(text=cities[x],font = "Verdana 10 bold",fg = "white", bg = "black",borderwidth=5).pack()
        Label(text='↓',font = "Verdana 10 bold").pack()

    Label(text=cities[s],font = "Verdana 10 bold",fg = "white", bg = "black").pack()
    B1=Button (window,text='Do YOU WANT TO CHANGE YOUR LOCATION',command=window.destroy,borderwidth=5).pack()
    window.mainloop()
    answer=input("DO you want to change the starting point(YES/NO)?")
