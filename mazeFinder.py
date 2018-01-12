

maze_str="111110111011100100010000011011111111111100000001010011111111101010010000010001111110101011110100010001001011111111111"
width=13
height=9

#if you want some other maze of different dimensions just change the maze_str and it properties variables named width and height to its respective value!

visited_array=[]
path_array=[]
junction_array=[]
maze=[]
temp=[]
ind=1

for x in maze_str:
    if (ind % width==0):
        temp.append(str(x))
        maze.append(temp)
        temp=[]
    else:
        temp.append(str(x))
    ind=ind+1


def display(m):
    itr=iter(m)
    print("\n")
    for y in itr:
        print(y)
    print("\n")


def isPath(maze,pos):
    return maze[pos[0]][pos[1]]=='1'

def setMaze(maze,pos,char):
    maze[pos[0]][pos[1]]=char
    
def getMaze(maze,pos):
    return maze[pos[0]][pos[1]]


def nextPath(maze,pos):
    new_pos={'l':[pos[0],pos[1]-1],'r':[pos[0],pos[1]+1],'u':[pos[0]-1,pos[1]],'d':[pos[0]+1,pos[1]]}
    available_path={}
    for x in new_pos:
        if((not(new_pos[x][1]<0) and not(new_pos[x][1]>(width-1))) and (not((new_pos[x][0])<0) and not((new_pos[x][0])>(height-1)))):
            if(isPath(maze,new_pos[x])==True):
                available_path[x]=new_pos[x]

    return available_path

def noOfPaths(maze,pos):
    count=0
    p=nextPath(maze,pos)
    for x in list(p.values()):
        if(not(x in visited_array)):
            count+=1
    return count


def solveMaze(maze,entry_point,exit_point):
    path=nextPath(maze,entry_point)
    
    if(entry_point==exit_point):
        path_array.append(entry_point)
        return 1
    
    if(noOfPaths(maze,entry_point)==0):
        visited_array.append(entry_point)
        return 0
        
    if(noOfPaths(maze,entry_point)==1):
        for x in list(path.values()):
                if(not(x in visited_array)):
                    new_pos=x
        
        if(not(new_pos in visited_array)):
            visited_array.append(entry_point)
            path_array.append(entry_point)
            flag=solveMaze(maze,new_pos,exit_point)
            if (flag==1 or flag=='x'):
                return 1
            else:
                path_array.remove(entry_point)
                return 0
        else:
            return 0
        
    if(noOfPaths(maze,entry_point)>1):
        junction_array.append(entry_point)
        visited_array.append(entry_point)
        paths=nextPath(maze,entry_point)
        for new_pos in list(paths.values()):
    
            path_array.append(entry_point)
            flag=solveMaze(maze,new_pos,exit_point)
            if(flag==1):
                return 1
            else:
                path_array.remove(entry_point)
           
                
def display_solved_maze(maze,path_array):
    solved_maze=maze
    for x in path_array:
        solved_maze[x[0]][x[1]]='*'
    entry=path_array[0]
    exit=path_array[len(path_array)-1]
    solved_maze[entry[0]][entry[1]]='e'
    solved_maze[exit[0]][exit[1]]='E'
    display(solved_maze)
    
def direction(maze,path_array):
    new_maze=maze
    direction_array=[]
    for x in range(0,len(path_array)-1):
        pos1=path_array[x]
        pos2=path_array[x+1]
        x1=pos1[1]
        y1=pos1[0]
        x2=pos2[1]
        y2=pos2[0]
        if((y1-y2)==0 and (x1-x2)==-1):
            new_maze[pos1[0]][pos1[1]]='>'
            direction_array.append('r')
        if((y1-y2)==0 and (x1-x2)==1):
            new_maze[pos1[0]][pos1[1]]='<'
            direction_array.append('l')
        if((x1-x2)==0 and (y1-y2)==-1):
            new_maze[pos1[0]][pos1[1]]='v'
            direction_array.append('d')
        if((x1-x2)==0 and (y1-y2)==1):
            new_maze[pos1[0]][pos1[1]]='^'
            direction_array.append('u')
    entry=path_array[0]
    exit=path_array[len(path_array)-1]
    new_maze[entry[0]][entry[1]]='e'
    new_maze[exit[0]][exit[1]]='E'
    string=''
    count=1
    for z in range(0,len(direction_array)):
            if(z<len(direction_array)-1):
                ind1=direction_array[z]
                ind2=direction_array[z+1]
                if(ind1==ind2):
                    count=count+1
                else:
                    string=string+str(count)+str(ind1)+" "
                    count=1
            else:
                ind1=direction_array[z]
                ind2=direction_array[z-1]
                if(ind1==ind2):
                    string=string+str(count)+str(ind1)+" "
                else:
                    count=1
                    string=string+str(count)+str(ind1)+" "
    display(new_maze)

    return string
            
        
    
def solve(maze,entry_point,exit_point):
 
    flag=solveMaze(maze,entry_point,exit_point)
    if(flag==1):
        print("\nThe maze is solved!\n")
        print("PATH ARRAY: {}\n".format(path_array))
        direction_array=direction(maze,path_array)
        print("DIRECTIONS : {}\n".format(direction_array))
#         display_solved_maze(maze,path_array)
    else:
        print("There is no path for the given exit point!")
       
            


solve(maze,[0,0],[8,12]) #use this method to solve the maze.But only one intance at a time!



# In[343]:





# print(junction_array)

