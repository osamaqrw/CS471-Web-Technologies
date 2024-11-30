from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links, name="books.links"),
    path('html5/text/formatting', views.formatting, name="books.formatting"),
    path('html5/listing', views.listing, name="books.listing"),
    path('html5/tables', views.tables, name="books.tables"),
    path('search/', views.search, name="books.search"),
    path('createbook/', views.createbook, name="books.createbook"),
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
    path('lab8/task1', views.lab8_task1, name='books.lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='books.lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='books.lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='books.lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='books.lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='books.lab8_task7'),
    path('lab9_part1/listbooks', views.lab9_part1_listbooks, name='books.lab9_part1_listbooks'),
    path('lab9_part1/addbook', views.lab9_part1_addbook, name='books.lab9_part1_addbook'),
    path('lab9_part1/editbook/<int:id>', views.lab9_part1_editbook, name='books.lab9_part1_editbook'),
    path('lab9_part1/deletebook/<int:id>', views.lab9_part1_deletebook, name='books.lab9_part1_deletebook'),
    path('lab9_part2/listbooks', views.lab9_part2_listbooks, name='books.lab9_part2_listbooks'),
    path('lab9_part2/addbook', views.lab9_part2_addbook, name='books.lab9_part2_addbook'),
    path('lab9_part2/editbook/<int:id>', views.lab9_part2_editbook, name='books.lab9_part2_editbook'),
    path('lab9_part2/deletebook/<int:id>', views.lab9_part2_deletebook, name='books.lab9_part2_deletebook'),
    path('lab10/liststudents', views.lab10_liststudents, name='books.lab10_liststudent'),
    path('lab10/addstudent', views.lab10_addstudent, name='books.lab10_addstudent'),
    path('lab10/updatestudent/<int:id>', views.lab10_updatestudent, name='books.lab10_updatestudent'),
    path('lab10/deletestudent/<int:id>', views.lab10_deletestudent, name='books.lab10_deletestudent'),
    
    path('lab10/multilisttudents', views.lab10_multi_liststudents, name='books.lab10_multi_liststudents'),
    path('lab10/multiaddstudent', views.lab10_multi_addstudent, name='books.lab10_multi_addstudent'),
    path('lab10/multiupdatestudent/<int:id>', views.lab10_multi_updatestudent, name='books.lab10_multi_updatestudent'),
    path('lab10/multideletestudent/<int:id>', views.lab10_multi_deletestudent, name='books.lab10_multi_deletestudent'),

    
]   


