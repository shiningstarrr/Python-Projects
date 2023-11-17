# Resources:
- QuerySet API Reference: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#queryset-api
- Making Queries: https://docs.djangoproject.com/en/4.2/topics/db/queries/

# Making Queries:
- Insertion:
    >>> from employee.models import Employee
    >>> emp = Employee(name='John',title='Manager')
    >>> emp.save()
- Update:
    >>> emp = Employee.objects.get(id=1)
    >>> emp.name = 'newName'
    >>> emp.save()
- Retrieve:
    + Retrieve specific objects:
    >>> Employee.objects.all()
    >>> Employee.objects.all().values()
    >>> Employee.objects.all().filter(name='rose')
    + Chaining filter:
    >>> Employee.objects.all().exclude(...).filter(...)
    >>> q = Employee.objects.filter(id=1), print(q.values())
    + Filtered querysets are unique:
    >>> q1 = Employee.objects.filter(...)
    >>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
    >>> q3 = q1.filter(pub_date__gte=datetime.date.today())
    + Retrieve a single object:
    >>> Employee.objects.get(...)
- Limiting QuerySets:
    >>> Employee.objects.all()[:5]
    >>> Employee.objects.all()[:10:2]
    >>> Employee.objects.order_by("headline")[0] 
    which equals to:
    >>> Entry.objects.order_by("headline")[0:1].get()
    + A case-insensitive match, same as 'iexact':
    >>> Blog.objects.get(name__iexact="beatles blog")
    + same as 'exact':
    >>> Entry.objects.get(headline__exact="Cat bites dog")
    + A case-insensitive match, same as 'contains' or 'like':
    >>> Entry.objects.get(headline__icontains="Lennon")
    >>> Employee.objects.filter(name__contains='R').values()
    + same as 'in':
    >>> Entry.objects.filter(id__in=[1, 3, 4])
    + 'gt' greater than, 'gte' greater than or equal to, 'it' less than, 'ite' less than or equal to:
    >>> Entry.objects.filter(id__gt=4)
    + 'startswith' and 'endswith' case-sensitive, 'istartswith' and 'iendswith' case-insensitive:
    >>> Entry.objects.filter(headline__startswith="Lennon")
- Compare between fields:
    >>> from django.db.models import F
    >>> Employee.objects.filter(name=F('title')).values()