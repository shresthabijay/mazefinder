

maze_str="1111111110101010101111101111111011100000010101010101010000000001000001111111101011101111111011101110101110000000010100000000010101000101000111111110101111111111101011111010101101000101010101010100000001000101011010101110101010101011101011111011110001000100010000010001010001010100111011101110101110101111111110111010000100000101000100000100000000010110111111111110111111111010111110111100000000000100000100000100000100011110111111111011111011111111101011100100000100000000010001000001010001111111101111101111101011101010111110010000000001000001010001010001000110111010111011111111111011111011101101010100010001000000010101000100011010111110111110101111111010101011110000010001000001000101010001010100101111111010101111111010101010101011010001010001010101010001010101000111101110111111101010101111111011111"
width=35
height=23

#if you want some other maze of different dimensions just change the maze_str and it properties variables named width and height to its respective value!

visited_array=[]
path_array=[]
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
    solved_maze=[ a[:] for a in maze]
    for x in path_array:
        solved_maze[x[0]][x[1]]='#'
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
            direction_array.append('R')
        if((y1-y2)==0 and (x1-x2)==1):
            new_maze[pos1[0]][pos1[1]]='<'
            direction_array.append('L')
        if((x1-x2)==0 and (y1-y2)==-1):
            new_maze[pos1[0]][pos1[1]]='v'
            direction_array.append('D')
        if((x1-x2)==0 and (y1-y2)==1):
            new_maze[pos1[0]][pos1[1]]='^'
            direction_array.append('U')
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
                    string=string+str(count)+str(ind1)
                    count=1
            else:
                ind1=direction_array[z]
                ind2=direction_array[z-1]
                if(ind1==ind2):
                    string=string+str(count)+str(ind1)
                else:
                    count=1
                    string=string+str(count)+str(ind1)
    display(new_maze)

    return string
            
        
    
def solve(maze,entry_point,exit_point):
 
    flag=solveMaze(maze,entry_point,exit_point)
    if(flag==1):
        print("\nThe maze is solved!\n")
        print("PATH ARRAY: {}\n".format(path_array))
        m=[a[:] for a in maze]
        direction_array=direction(m,path_array)
        print("DIRECTIONS : {}\n".format(direction_array))

     
    else:
        print("There is no path for the given exit point!")
    path_array.clear()
    visited_array.clear()




solve(maze,[0,34],[0,0])

solve(maze,[22,34],[0,0])

solve(maze,[22,0],[0,0])




