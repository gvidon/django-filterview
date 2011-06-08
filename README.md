`django-filterview` is a class based view on top of generic [ListView][0] with
filtering of the queryset by mapping URL params into filter() arguments.

[0]: https://docs.djangoproject.com/en/1.3/ref/class-based-views/#listview

## Installing

Just download source code and extract `filterview` directory to your `PYTHON_PATH`.
No changes in `settings.py` required.

## Usage

In your urls.py insert this line:

	from filterview import FilterView

Then just define url pattern with named params and `FilterView.as_view()` as url processing view.
The only required `FilterView.as_view()` arguments are `model` and `mapping`. First one plays
the same role as `model` argument of ListView. `mapping` is dictionary for mapping
url params values to `filter()` arguments. For example:

	{
		'name': lambda key, value: [('first_name', value)],
		
		'age': lambda key, value: [(
			'birthdate__range', (
				datetime.today() - timedelta( days=366*int(value.split('-')[1]) ),
				datetime.today() - timedelta( days=365*int(value.split('-')[0]) ),
			)
		)],
	}

## Params

`django-filterview` accepts all [ListView arguments][1] and additionally `mapping` argument.

[1]: https://docs.djangoproject.com/en/1.3/ref/class-based-views/#django.views.generic.list.MultipleObjectMixin

Required arguments are:

* `model` - filtering queryset model object
*	`mapping` - dictionary with keys named like url params and function object returning list of tuples.

`mapping` dictionary function object takes url param name and its value as arguments. Each tuple
of returned list has two items - first one is `filter()` argument name and the last
is its value. So each url param can be mapped into two or more `filter()` argument.

Note: if some url param is not presented in `mapping` dictionary it's taken from url and used
in `filter()` with no changes.

Using above example mapping dictionary and url pattern

	r'^(/(?P<name>[\w\d\s%]+))?(/(?P<gender>(M|F)))?(/(?P<age>[\d]+\-[\d]+))?/?$'

Result `filter()` arguments for url `/Jhon/M/30-37` are:

	filter(first_name=<value for name url param>, gender=<value for gender url param>, birtdate__range=(
	
		datetime.today() - timedelta( days=366*int(value.split('-')[1]) ),
		datetime.today() - timedelta( days=365*int(value.split('-')[0]) ),
		
	))



	
