import sqlite3

db = sqlite3.connect('app.db')
cr = db.cursor()
uid = 1
cr.execute(
    "create table if not exists skills(title text, progress integer, uid integer)")


def commit_close():
    db.commit()
    db.close()
    print('connection is closed')


input_message = """
Choose from these options
's' ==> show all skills
'a' ==> add skill
'd' ==> delete skill
'u' ==> update skills progress
'q' ==> Quit the app
:"""

user_input = input(input_message).strip().lower()
command_list = ['s', 'a', 'd', 'u', 'q']


def show():
    cr.execute("select * from skills")
    res = cr.fetchall()
    print(f"you have {len(res)} skills")
    if len(res) > 0:
        print("your skills is :")
    for row in res:
        print(f"{row[0]} ==> {row[1]}")
    commit_close()


def add():
    sk = input('add new skill ').strip().capitalize()
    cr.execute(
        f"select title from skills where title = '{sk}' and uid = '{uid}'")
    res = cr.fetchone()
    if res == None:
        prog = input('add your progress ').strip()
        cr.execute(
            f"insert into skills(title, progress, uid) values('{sk}', '{prog}', '{uid}')")
    else:
        press = input("skill exists, want to update(y/n):").lower()
        if press == 'y':
            new_prog = input('add your new progress ').strip()
            cr.execute(
                f"update skills set progress = '{new_prog}' where title = '{sk}' and uid ='{uid}'")
        else:
            print("close")

    commit_close()


def delete():
    sk = input('delete skill ').strip().capitalize()
    cr.execute(f"delete from skills where title = '{sk}' and uid = '{uid}'")
    commit_close()


def update():
    sk = input('add the skill U want to update ').strip().capitalize()
    new_prog = input('add your new progress ').strip()
    cr.execute(
        f"update skills set progress = '{new_prog}' where title = '{sk}' and uid ='{uid}'")
    commit_close()


def quit():
    commit_close()


if user_input in command_list:
    if user_input == 's':
        show()

    elif user_input == 'a':
        add()

    elif user_input == 'd':
        delete()

    elif user_input == 'u':
        update()

    else:
        quit()

else:
    print(f'Command {user_input} Not in the list')
