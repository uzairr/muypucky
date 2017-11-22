# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from menus.models import Item
from django.views.generic import ( 
	CreateView, UpdateView, 
	ListView, DetailView
	)
from django.shortcuts import render
from menus.forms import ItemForm


class ItemCreateView(CreateView):
	template_name = 'forms.html'
	form_class = ItemForm

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(ItemCreateView, self).form_valid(form)

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Item'
		return context


class ItemUpdateView(UpdateView):
	form_class = ItemForm
	template_name = 'forms.html'

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update View'
		return context


class ItemListView(ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)