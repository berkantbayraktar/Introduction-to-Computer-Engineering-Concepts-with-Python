def help_michael(mafia_tree,savings):

    def datum(mafia_tree):

        return mafia_tree[0]

    def children(mafia_tree):

        return mafia_tree[1:]

    def isLeaf(mafia_tree):

        return len(children(mafia_tree)) == 0

    def collect(mafia_tree):

        if isLeaf(mafia_tree):

            return datum(mafia_tree)[1]

        else:

            total_collect = datum(mafia_tree)[1]

            for child in children(mafia_tree):

                total_collect += collect(child)

            return total_collect

    def wage(mafia_tree):

        if isLeaf(mafia_tree):

            return datum(mafia_tree)[2]

        else:
            
            total_wage = datum(mafia_tree)[2]

            for child in children(mafia_tree):

                total_wage += wage(child) 
                
            return total_wage

    x = collect(mafia_tree)
    y = wage(mafia_tree)

    global money

    money = x + savings - y

    if money >= 0:

        return "Yes"
    
    else:
        
        def find_list_depth(mafia_tree,depth): #This function finds each member in empire and sorts [Name,Collect,Wage,Depth]

            def datum(mafia_tree):

                return mafia_tree[0]

            def children(mafia_tree):

                return mafia_tree[1:]

            def isLeaf(mafia_tree):

                return len(children(mafia_tree)) == 0

            def makenode(datum,children = []):

                return [datum] + children

            lst = [[datum(mafia_tree)[0],datum(mafia_tree)[1],datum(mafia_tree)[2],depth]]

            for child in children(mafia_tree):

                lst +=  find_list_depth(child,depth+1)

            return lst

        member_list = find_list_depth(mafia_tree,0)

        def member_reducer(member_list):  #This function finds member who can be reducable wage and sorts [Name,Collect,Wage,Depth]

            reduced_list = []

            for member in member_list:

                if member[3] >1:

                    if member[1] < member[2]:

                        reduced_list += [member]

                    else:
                        reduced_list += []
                else:
                    reduced_list += []
                    
            return reduced_list        

        reduced_list = member_reducer(member_list)
        reduced_list = sorted(reduced_list, key= lambda reduced_list: reduced_list[3] , reverse=True)

        def possibility(member_list):

            result = 0

            for member in member_list:
                
                if member[3]>1:

                    if member[1] < member[2]:

                        if member[2] - (member[3] * 100) > 0:

                            result += member[1] - ( member[2] - 100* member[3])

                        else:

                            result += member[1] + 1

                    else:
                        result += member[1] - member[2]

                else:

                    result += member[1] - member[2]

            return result

        new = possibility(member_list)

        wages = new + savings
        
        def helper(money, reduced_list):  #This function finds members who have reduced and sorts [Name,Reduced Wage] 

            reduced_member_list = []

            for member in reduced_list:

                while money<0:                   

                    if member[2]-member[3]*100 > 0:

                        money += member[3] * 100

                        if money >0:

                            reduced_member_list += [[member[0],member[2]-member[3]*100 + money]]

                            break

                        else:

                            reduced_member_list += [[member[0],member[2]-member[3]*100]]

                            break

                    else:

                        money += member[2]-1

                        if money >0:
                            
                            reduced_member_list += [[member[0],1+money]]

                            break

                        else:

                            reduced_member_list += [[member[0],1]]

                            break

                    
            return reduced_member_list

        x = helper(money, reduced_list)

        x.insert(0,"Possible")
                       
        if wages >= 0:

            return x

        else:

            return "No"

print help_michael([["Michael", 0, 10000], \
[["Jack", 6000, 5000], [["Fredo", 600, 1000]], [["Vincenzo", 600, 500]]],\
[["Frank", 2000, 4000], [["Rocco", 100, 500]]],\
[["John", 2000, 4000], [["Nico", 1000, 300]]]],12600)
