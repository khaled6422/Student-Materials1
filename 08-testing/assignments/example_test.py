import pytest
import System


username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

#Tests if the program can handle a wrong username
#def test_login(grading_system):
   # username = 'thtrhg'
    #password =  'fhjhjdhjdfh'
    #grading_system.login(username,password)

#def test_check_password(grading_system):
    #test = grading_system.check_password(username,password)
    #test2 = grading_system.check_password(username,'#yeet')
    #test3 = grading_system.check_password(username,'#YEET')
    #if test == test3 or test2 == test3:
    #    assert False
    #if test != test2:
    #    assert False


#@pytest.fixture
#def grading_system():
   # gradingSystem = System.System()
   #gradingSystem.load_data()
   # return gradingSystem



def test_login(pytestGradingSystem):
    username = "hdjsr7"
    password = "pass1234"
    pytestGradingSystem.login(username, password)
    assert pytestGradingSystem.usr.name == username
    data = pytestGradingSystem.load_user_db()
    assert data[username] 


def test_check_password(pytestGradingSystem):
    user = "hdjsr7"
    pass1 = "pass1234"
    pass2 = "PASS1234"
    pass3 = "Pass1234"
    assert pytestGradingSystem.check_password(user, pass1)
    assert pytestGradingSystem.check_password(user, pass2)
    assert pytestGradingSystem.check_password(user, pass3)


def test_change_grade(pytestGradingSystem):
    user = "cmhbf5"
    passw = "bestTA"
    pytestGradingSystem.login(user, passw)
    pytestGradingSystem.load_data()
    pytestGradingSystem.usr.change_grade("yted91", "software_engineering", "assignment1",69)
    pytestGradingSystem.reload_data()
    data = pytestGradingSystem.load_user_db()
    assert data["yted91"]["courses"]["software_engineering"]["assignment1"]["grade"] == 69


def test_create_assignment(pytestGradingSystem):
    user = "cmhbf5"
    passw = "bestTA"
    pytestGradingSystem.login(user, passw)
    pytestGradingSystem.usr.create_assignment("assignmentX", "11/22/33", "cloud_computing")
    pytestGradingSystem.reload_data()
    data = pytestGradingSystem.load_course_db()
    assert data["cloud_computing"]["assignments"]["assignmentX"]["due_date"] == "11/22/33"


def test_add_student(pytestGradingSystem):
    user = "goggins"
    passw = "augurrox"
    pytestGradingSystem.login(user, passw)
    pytestGradingSystem.usr.add_student('akend3', "cloud_computing")
    pytestGradingSystem.reload_data()
    data = pytestGradingSystem.load_user_db()
    assert data["akend3"]["courses"]["cloud_computing"]


def test_drop_student(pytestGradingSystem):
    user = "goggins"
    passw = "augurrox"
    pytestGradingSystem.login(user, passw)
    pytestGradingSystem.usr.drop_student("akend3", "databases")
    pytestGradingSystem.reload_data()
    data = pytestGradingSystem.load_user_db()
    assert "databases" in data["akend3"]["courses"] == False


def test_submit_assignment(pytestGradingSystem):
    user = "hdjsr7"
    passw = "pass1234"
    pytestGradingSystem.login(user, passw)
    pytestGradingSystem.usr.submit_assignment("cloud_computing", "assignment1", "CheeseMaker5000", "12/12/22")
    pytestGradingSystem.reload_data()
    data = pytestGradingSystem.load_user_db()
    assert data["hdjsr7"]["courses"]["cloud_computing"]["assignment1"]["submission_date"] == "12/12/22" 
    assert data["hdjsr7"]["courses"]["cloud_computing"]["assignment1"]["submission"] == "CheeseMaker5000"


def test_check_ontime(pytestGradingSystem):
    user = "hdjsr7"
    passw = "pass1234"
    pytestGradingSystem.login(user, passw)
    data = pytestGradingSystem.load_user_db()
    ontime = pytestGradingSystem.usr.check_ontime("3/14/22", "2/11/22")
    assert ontime == False


def test_check_grades(pytestGradingSystem):
    user = "hdjsr7"
    passw = "pass1234"
    pytestGradingSystem.login(user, passw)
    grades = pytestGradingSystem.usr.check_grades("software_engineering")
    data = pytestGradingSystem.load_user_db()
    assert data[user]["courses"]["software_engineering"]["assignment1"]["grade"] == grades[0][1]


def test_view_assignments(pytestGradingSystem):
    user = "hdjsr7"
    passw = "pass1234"
    pytestGradingSystem.login(user, passw)
    assignments = pytestGradingSystem.usr.view_assignments("databases")
    data = pytestGradingSystem.load_user_db()
    for x in range(len(assignments)):
        assert list(data[user]["courses"]["databases"].keys())[x] == assignments[x][0]


def test_student_grade(pytestGradingSystem):
    user = "hdjsr7"
    passw = "pass1234"
    pytestGradingSystem.login(user, passw)
    assert pytestGradingSystem.usr.create_assignment("cloud_computing", "assignment1", "WWEFake", "11/11/22") == False


def test_strange_username_1(pytestGradingSystem):
    user = 9899
    passw = "pass1234"
    assert pytestGradingSystem.login(user, passw)


def test_negative_grade(pytestGradingSystem): ######
    user = "goggins"
    passw = "augurrox"
    pytestGradingSystem.login(user, passw)
    assert pytestGradingSystem.usr.change_grade("yted91", "software_engineering", "assignment1", -9)


def test_password(pytestGradingSystem):
    user = "hdjsr7"
    passw = "\t\t\tpassword1234\t"
    assert pytestGradingSystem.login(user, passw)


def test_TA_submit(pytestGradingSystem):
    user = "cmhbf5"
    passw = "bestTA"
    pytestGradingSystem.login(user, passw)
    assert pytestGradingSystem.usr.submit_assignment("cloud_computing", "assignment1", "WWEFaker", "11/11/22") == False


@pytest.fixture
def pytestGradingSystem():
    pytestGradingSystem = System.System()
    pytestGradingSystem.load_data()
    return pytestGradingSystem