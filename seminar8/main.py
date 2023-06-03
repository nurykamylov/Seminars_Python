from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_records():
    global last_id

    with open(file_base, "a", encoding='utf-8') as adds:
        for line in range(int(input(" enter the range of data: "))):
            adds.write(str(last_id+line) + ' ' + input('Type the text: ')+'\n')
        adds.close()


def search_records():
    a = input("what are u looking for ?: ")
    with open(file_base, "r") as file:
        
        for lines in file :
            if a in lines:
                print(lines)
        if a not in file:
            return"Not found!"


def change_records():
    search_records()
    delete_recods()
    add_records()
    

def delete_recods():
    global all_data
    with open(file_base, "r") as _:
        del all_data[int(input("enter the row wich one you want delete: "))]
    with open(file_base, 'w') as file:
        for line in all_data:
            file.write(line)
            file.write('\n')
        

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_records()
            case "3":
                search_records()
            case "4":
                change_records()
            case "5":
                delete_recods()
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()