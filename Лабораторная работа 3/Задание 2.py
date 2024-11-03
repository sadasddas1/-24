#def find_common_participants(participants_first_group, participants_second_group,cut=","):
 #   all = participants_first_group + "|" + participants_second_group
  #  all = all.split(cut)
   ##common = []
    #while i != len(all):
     #   if all.count(all[i]) > 1:
      #      if all[i] not in common:
       ##i += 1
    #common.sort()
    #return common

def find_common_participants(participants_first_group, participants_second_group, cut=','):
    first_group_list = participants_first_group.split(cut)
    second_group_list = participants_second_group.split(cut)
    common_names = set(first_group_list) & set(second_group_list)
    return sorted(common_names)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, ','))

#print(find_common_participants(participants_first_group, participants_second_group, '|'))