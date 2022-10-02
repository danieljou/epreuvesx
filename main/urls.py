from django.urls import path
from . import views

urlpatterns = [

    path("redirect_user/", views.redirect_user, name="redirect_user"),
     path("", views.redirect_user, name="redirect_user"),
    path("admin_home/", views.admin_home, name="admin_home"),
    path("prof_home/", views.prof_home, name="prof_home"),

    #  Exercice Management 
    path("exercices_homes/", views.exercices_homes, name="exercices_homes"),
    path("add_exercice/", views.add_exercice, name="add_exercice"),
    path("update_exercice/<exercice_id>", views.update_exercice, name="update_exercice"),
    path("delete_exercice/<exercice_id>", views.delete_exercice, name="delete_exercice"),


    #  Matiere Management 
    path("matieres_homes/", views.matieres_homes, name="matieres_homes"),
    path("add_matiere/", views.add_matiere, name="add_matiere"),
    path("update_matiere/<matiere_id>", views.update_matiere, name="update_matiere"),
    path("delete_matiere/<matiere_id>", views.delete_matiere, name="delete_matiere"),


    #  Epreuve Management 
    path("epreuves_homes/", views.epreuves_homes, name="epreuves_homes"),
    path("add_epreuve/", views.add_epreuve, name="add_epreuve"),
    path("update_epreuve/<epreuve_id>", views.update_epreuve, name="update_epreuve"),
    path("delete_epreuve/<epreuve_id>", views.delete_epreuve, name="delete_epreuve"),
    path("details_epreuve/<epreuve_id>", views.details_epreuve, name="details_epreuve"),
    path("douwnload_epreuve_pdf/<epreuve_id>", views.douwnload_epreuve_pdf, name="douwnload_epreuve_pdf")

]
