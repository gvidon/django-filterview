from django.views.generic.list import ListView

class FilterView(ListView):
	mapping = {}
	
	def get_queryset(self):
		
		# Filter queryset, do not filter by None value
		return self.model.objects.filter(**dict(filter(lambda P: P[1], dict(
			
			reduce(lambda items, result: items + result, [
				self.mapping.get(K, lambda K, V: [(K, V)])(K, V) for K, V in self.kwargs.iteritems()
			], [])
		
		).iteritems())))
