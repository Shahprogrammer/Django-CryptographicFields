from datetime import datetime,date,time
from operator import attrgetter
from typing import Any, Callable, Tuple,Union
from django.db.models.query import QuerySet

def filter(queryset:QuerySet,lookup_function:Callable[[Union[str,int,float,datetime,date,time,Any],str,Any],bool], field_name:str, query:Any)->QuerySet:
    """
    Filters queryset

    Filters queryset as per lookup provided by user &query provided by user

    :param lookup_function: Functions that filters the data
    :type lookup_function: Callable[[Union[str,int,float,datetime,date,time,Any],str,Any],bool]
    :param queryset: Queryset generated by querying data 
    :type queryset: QuerySet
    :param field_name: Name of the field which is to be filtered 
    :type field_name: str
    :param query: Query for filtering the Queryset
    :type query: Any
    :return: QuerySet with Filtered Data
    :rtype: QuerySet
    """
    queryset._result_cache(list(filter(lambda object: lookup_function(
        query, field_name, object), queryset)))
    return queryset


def startswith(query: str, field_name: str, object: Any)->bool:
    """
    Check if a string is Starts With the query(Case Sensitive)
    """
    return str(getattr(object, field_name)).startswith(str(query))


def istartswith(query: str, field_name: str, object: Any)->bool:
    """
    Check if a string is Starts With the query(Not Case Sensitive)
    """
    return str(getattr(object, field_name)).casefold().startswith(str(query).casefold())


def endswith(query: str, field_name: str, object: Any)->bool:
    """
    Check if a string is Ends With the query(Case Sensitive)
    """
    return str(getattr(object, field_name)).endswith(str(query))


def iendswith(query: str, field_name: str, object: Any)->bool:
    """
    Check if a string is Ends With the query(Not Case Sensitive)
    """
    return str(getattr(object, field_name)).casefold().endswith(str(query).casefold())


def contains(query: str, field_name: str, object: Any)->bool:
    """
    Check if query is in value of the object(Case Sensitive)
    """
    return str(query) in str(getattr(object, field_name))


def icontains(query: str, field_name: str, object: Any)->bool:
    """
    Check if query is in value of the object(Not Case Sensitive)
    """
    return str(query).casefold() in str(getattr(object, field_name)).casefold()


def gt(query:Union[int,float], field_name: str, object: Any)->bool:
    """
    Check if value of object is greater than value of query
    """
    return float(getattr(object, field_name)) > float(query)


def gte(query:Union[int,float], field_name: str, object: Any)->bool:
    """
    Check if value of object is greater than or equal to value of query
    """
    return float(getattr(object, field_name)) >= float(query)


def lt(query:Union[int,float], field_name: str, object)->bool:
    """
    Check if value of object is less than value of query
    """
    return float(getattr(object, field_name)) < float(query)


def lte(query:Union[int,float], field_name: str, object)->bool:
    """
    Check if value of object is less than or equal to value of query
    """
    return float(getattr(object, field_name)) <= float(query)


def range(query: Tuple[int, int], field_name: str, object)->bool:
    """
    Check if value of object is in range of query
    """
    return query[0] <= getattr(object, field_name) <= query[1]


def date(query:Union[date,datetime], field_name: str, object)->bool:
    """
    Check if value of object is equal to query
    """
    if isinstance(query, datetime) & isinstance(getattr(object, field_name), datetime):
        return query.date() == getattr(object, field_name).date()
    else:
        return query == getattr(object, field_name)


def year(query: int, field_name, object)->bool:
    """
    Checks if value of object is equal to query
    """
    return query == getattr(object, field_name).year


def month(query: int, field_name, object)->bool:
    """
    Checks if value of object is equal to query
    """
    return query == getattr(object, field_name).month


def day(query: int, field_name, object)->bool:
    """
    Checks if value of object is equal to query
    """
    return query == getattr(object, field_name).day


def time(query:Union[time,datetime], field_name: str, object)->bool:
    """
    Checks if value of object is equal to query
    """
    if isinstance(query, datetime) & isinstance(getattr(object, field_name), datetime):
        return query.time() == getattr(object, field_name).time()
    else:
        return query == getattr(object, field_name)


def hour(query: int, field_name, object)->bool:
    """
    Checks if value of object is equal to query
    """
    return query == getattr(object, field_name).hour


def minute(query: int, field_name, object)->bool:
    """
    Checks if value of object is equal to query
    """
    return query == getattr(object, field_name).minute


def second(query: int, field_name, object)->bool:
    return query == getattr(object, field_name).second

def order_by(queryset:QuerySet, field_name:Tuple(str,...), reverse:bool=False)->QuerySet:
    """
    Order Queryset by the given field

    Order the Queryset as per field_name given.It supports multiple level of sorting

    :param queryset: Queryset generated by querying data
    :type queryset: QuerySet
    :param field_name: Tuple with name of the field from higher priority to lower priority
    :type field_name: Tuple
    :param reverse: Type of ordering (Ascending|Descending), defaults to False
    :type reverse: bool, optional
    :return: QuerySet with Ordered Data
    :rtype: QuerySet
    """
    queryset._result_cache=sorted(queryset, key=attrgetter(*field_name), reverse=reverse)
    return queryset