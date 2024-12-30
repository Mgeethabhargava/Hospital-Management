from django

class book(models):
    bookname = model.charfield()
    author_name = model.charfield()
    volume = model.intfield()

class author(models):
    author = model.charfield()
    bookname = model.charfield()


def get_data(request):
    return render_template(request, "intro.html", jsondata=data)

persons x cars list

table persons -> personid,personname, carid , address
table cars -> carid, carname, make, manufacturer

select personname, carname from persons leftjoin cars on cars.carid=person.carid;


a= (){a=1;} => console.log(a); 

with open("text.txt", "r+") as fp:
    data = fp.readlines()
    print(data)
fp.close()
print(data)

