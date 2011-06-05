`django-filterview` is a class based view on top of generic ListView with
filtering of the queryset by mapping URL params into filter() arguments.

## Usage

You just define url pattern with named params and `FilterView.as_view()` as url processing view.
The only required `FilterView.as_view()` arguments are `model` and `mapping`. First one plays
the same role as `model` argument of ListView. `mapping` is dictionary for mapping
url params values to filter() arguments. For example:

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

Filter view accepts all ListView arguments and additionally `mapping` argument.
Required arguments are:

* `model` - filtering queryset model object
*	`mapping` - dictionary with keys named like url params and lambda-function returning list of tuples.

Each tuple of list returned by `mapping` dictionary lambda-function has two items - first one is
filter() argument name and the last is its value. So each url param can be mapped into two or more
filter() argument.

Note: if some url param is not presented in `mapping` dictionary it's taken from url and used
in filter() with no changes.

Using above example mapping dictionary and url pattern

	r'^(/(?P<name>[\w\d\s%]+))?(/(?P<gender>(M|F)))?(/(?P<age>[\d]+\-[\d]+))?/?$'

Result filter() arguments are:

	filter(first_name=value, birtdate__range=(
	
		datetime.today() - timedelta( days=366*int(value.split('-')[1]) ),
		datetime.today() - timedelta( days=365*int(value.split('-')[0]) ),
		
	))



	
